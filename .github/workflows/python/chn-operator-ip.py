import requests
from pathlib import Path
from datetime import datetime
import pytz
from typing import List, Optional

# 配置常量
BASE_URL = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists"
TIMEOUT = 15
TIMEZONE = pytz.timezone("Asia/Shanghai")

CONFIGURATIONS = [
    {"remote": "china.txt", "local": "autoupdate/cn.yaml"},
    {"remote": "china6.txt", "local": "autoupdate/cn_v6.yaml"},
]

def fetch_ips(url: str) -> Optional[List[str]]:
    """获取并过滤 IP 列表"""
    try:
        print(f"📥 正在获取: {url}")
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        
        # 过滤空行和注释
        return [
            line.strip() for line in resp.text.splitlines() 
            if line.strip() and not line.strip().startswith("#")
        ]
    except requests.RequestException as e:
        print(f"❌ 请求失败 {url}: {e}")
        return None

def generate_yaml_content(ips: List[str], timestamp: str) -> str:
    """生成 YAML 内容"""
    entries = "\n".join(f'  - "{ip}"' for ip in ips)
    return f"""payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # Total: {len(ips)}
{entries}
"""

def main():
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
    
    for config in CONFIGURATIONS:
        url = f"{BASE_URL}/{config['remote']}"
        filepath = Path(config["local"])
        
        ips = fetch_ips(url)
        if ips is None:
            continue
            
        filepath.parent.mkdir(parents=True, exist_ok=True)
        content = generate_yaml_content(ips, timestamp)
        
        try:
            filepath.write_text(content, encoding="utf-8")
            print(f"✅ 成功生成: {filepath} (共 {len(ips)} 条)")
        except OSError as e:
            print(f"❌ 写入失败 {filepath}: {e}")

if __name__ == "__main__":
    main()