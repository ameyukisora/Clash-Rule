import requests
import re
from pathlib import Path

# 配置常量
URL = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
OUTPUT_FILE = Path("autoupdate/chnroutes.yaml")
IP_PATTERN = re.compile(r'^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$')

def main():
    try:
        print(f"正在下载: {URL}")
        resp = requests.get(URL, timeout=20)
        resp.raise_for_status()
        
        lines = resp.text.splitlines()
        
        # 保留源文件前两行注释，过滤出 IP 行
        header = [f"  {line}" for line in lines[:2]]
        ips = [f"  - '{line}'" for line in lines if IP_PATTERN.match(line)]
        
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