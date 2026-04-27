import time
from pathlib import Path
from datetime import datetime
from typing import List, Optional
import pytz
import requests

BASE_URL = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists"
TIMEOUT = 15
TIMEZONE = pytz.timezone("Asia/Shanghai")

CONFIGURATIONS = [
    {"remote": "china.txt",  "local": "autoupdate/cn.yaml"},
    {"remote": "china6.txt", "local": "autoupdate/cn_v6.yaml"},
]

def fetch_with_retry(url: str, retries=3, timeout=TIMEOUT) -> requests.Response:
    for i in range(retries):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            if i == retries - 1:
                raise
            print(f"⚠️  Retry {i+1}/{retries} after error: {e}")
            time.sleep(5)

def fetch_ips(url: str) -> Optional[List[str]]:
    """获取并过滤 IP 列表"""
    try:
        print(f"📥 正在获取: {url}")
        resp = fetch_with_retry(url)
        return [
            line.strip() for line in resp.text.splitlines() 
            if line.strip() and not line.strip().startswith("#")
        ]
    except requests.RequestException as e:
        print(f"❌ 请求失败 {url}: {e}")
        return None

def generate_yaml_content(ips: List[str], timestamp: str) -> str:
    entries = "\n".join(f'  - "{ip}"' for ip in ips)
    return (
        "payload:\n"
        f"  # https://github.com/gaoyifan/china-operator-ip\n"
        f"  # {timestamp}\n"
        f"  # Total: {len(ips)}\n"
        f"{entries}\n"
    )

def main():
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
    any_failure = False

    for config in CONFIGURATIONS:
        url = f"{BASE_URL}/{config['remote']}"
        filepath = Path(config["local"])

        ips = fetch_ips(url)
        if ips is None:
            any_failure = True
            continue
        if not ips:                     # 明确检查空列表
            print(f"❌ {config['remote']} returned empty list")
            any_failure = True
            continue

        content = generate_yaml_content(ips, timestamp)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        try:
            filepath.write_text(content, encoding="utf-8")
            print(f"✅ 成功生成: {filepath} (共 {len(ips)} 条)")
        except OSError as e:
            print(f"❌ 写入失败 {filepath}: {e}")
            any_failure = True

    if any_failure:
        exit(1)

if __name__ == "__main__":
    main()