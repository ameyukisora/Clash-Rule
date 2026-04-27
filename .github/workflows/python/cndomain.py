import time
from pathlib import Path
from datetime import datetime
import pytz
import requests

URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaMax/ChinaMax_Domain.yaml"
OUTPUT_FILE = Path("autoupdate/cndomain.yaml")
TIMEZONE = 'Asia/Shanghai'

def fetch_with_retry(url, retries=3, timeout=20):
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

def main():
    try:
        print(f"正在下载: {URL}")
        resp = fetch_with_retry(URL)
        lines = resp.text.splitlines()

        payload = []
        in_payload = False

        for line in lines:
            if line.strip() == "payload:":
                in_payload = True
                continue

            if in_payload:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    payload.append(stripped)

        if not payload:
            raise ValueError("Parsed empty domain list – upstream format may have changed")

        timestamp = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")
        new_lines = [
            "payload:",
            f"  # Updated: {timestamp}, Total: {len(payload)}",
            *[f"  {domain}" for domain in payload]
        ]

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text('\n'.join(new_lines), encoding='utf-8')
        print(f"✅ 成功生成: {OUTPUT_FILE} (共 {len(payload)} 条)")

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()