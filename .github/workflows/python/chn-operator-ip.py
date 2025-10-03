import requests
from pathlib import Path
from datetime import datetime
import pytz
from typing import List, Optional, Callable

BASE_URL = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists"
TIMEOUT = 10
TIMEZONE = pytz.timezone("Asia/Shanghai")

CONFIGURATIONS = [
    {"url_suffix": "china.txt",   "filename": "autoupdate/cn.yaml",   "is_v6": False},
    {"url_suffix": "china6.txt",  "filename": "autoupdate/cn_v6.yaml", "is_v6": True},
]

def is_valid_ip_line(line: str, is_v6: bool = False) -> bool:
    """判断是否为有效IP行（跳过空行、注释）"""
    line = line.strip()
    return bool(line) and not line.startswith("#")

def fetch_ips(url: str, is_v6: bool) -> Optional[List[str]]:
    """获取并过滤IP列表"""
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        return [line.strip() for line in resp.text.splitlines() if is_valid_ip_line(line, is_v6)]
    except requests.RequestException as e:
        print(f"❌ 请求失败 {url}: {e}")
        return None

def generate_yaml_content(ips: List[str], timestamp: str) -> str:
    """生成YAML内容"""
    ip_entries = "\n".join(f'  - "{ip}"' for ip in ips)
    return f"""payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # Total: {len(ips)}
{ip_entries}
"""

def main():
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
    
    for config in CONFIGURATIONS:
        url = f"{BASE_URL}/{config['url_suffix']}"
        filepath = Path(config["filename"])
        
        print(f"📥 正在获取: {url}")
        
        ips = fetch_ips(url, config["is_v6"])
        if ips is None:
            continue
            
        filepath.parent.mkdir(parents=True, exist_ok=True)
        content = generate_yaml_content(ips, timestamp)
        
        try:
            filepath.write_text(content, encoding="utf-8")
            print(f"✅ 成功生成 {filepath}，包含 {len(ips)} 个IP条目")
        except OSError as e:
            print(f"❌ 写入失败 {filepath}: {e}")

if __name__ == "__main__":
    main()

