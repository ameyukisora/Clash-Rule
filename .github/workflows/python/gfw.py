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

        # 保留非空、非注释的行，但排除以 "payload:" 开头的行（防止二次输出）
        rule_lines = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            if stripped.startswith("payload:"):  # 关键处理：跳过原始文件的 payload 头部
                continue
            rule_lines.append(line)    # 保留原始缩进，通常为 "  - 'domain'"

        if not rule_lines:
            raise ValueError("No rules extracted – upstream format may have changed")

        timestamp = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")

        # 构造完整的文件内容：头部 + 保留的规则行
        head = f"payload:\n  # {timestamp}\n  # TOTAL: {len(rule_lines)} urls\n"
        content = head + "\n".join(rule_lines) + "\n"

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(content, encoding='utf-8')
        print(f"✅ 成功生成: {OUTPUT_FILE} (共 {len(rule_lines)} 条)")

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()