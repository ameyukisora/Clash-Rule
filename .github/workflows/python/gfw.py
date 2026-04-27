import time
from pathlib import Path
from datetime import datetime
import pytz
import requests

URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt"
OUTPUT_FILE = Path("autoupdate/gfw.yaml")
TIMEZONE = 'Asia/Shanghai'

def fetch_with_retry(url, retries=3, timeout=15):
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

        # 过滤掉空行和注释行，其余全部视为 URL/规则
        urls = [line for line in lines if line.strip() and not line.strip().startswith("#")]

        if not urls:
            raise ValueError("No URLs extracted – upstream format may have changed")

        timestamp = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")
        content = (
            "payload:\n"
            f"  # {timestamp}\n"
            f"  # TOTAL: {len(urls)} urls\n"
        )
        content += "\n".join(urls) + "\n"

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(content, encoding='utf-8')
        print(f"✅ 成功生成: {OUTPUT_FILE} (共 {len(urls)} 条)")

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()