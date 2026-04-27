import re
import time
from pathlib import Path
import requests

URL = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
OUTPUT_FILE = Path("autoupdate/chnroutes.yaml")
IP_PATTERN = re.compile(r'^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$')

def fetch_with_retry(url, retries=3, timeout=20):
    """带重试的 HTTP GET 请求"""
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

        # 保留所有以 # 开头的注释行（若格式有变也能自适应）
        header = [f"  {line}" for line in lines if line.strip().startswith("#")]
        ips = [f"  - '{line}'" for line in lines if IP_PATTERN.match(line)]

        if not ips:
            raise ValueError("No valid IPs found – upstream format may have changed")

        content = [
            "payload:",
            "  # https://github.com/misakaio/chnroutes2",
            *header,
            *ips
        ]

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text('\n'.join(content), encoding='utf-8')
        print(f"✅ 成功生成: {OUTPUT_FILE} (共 {len(ips)} 条)")

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()