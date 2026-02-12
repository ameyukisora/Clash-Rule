import requests
from datetime import datetime
import pytz
from pathlib import Path

# 配置常量
URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaMax/ChinaMax_Domain.yaml"
OUTPUT_FILE = Path("autoupdate/cndomain.yaml")
TIMEZONE = 'Asia/Shanghai'

def main():
    try:
        print(f"正在下载: {URL}")
        resp = requests.get(URL, timeout=20)
        resp.raise_for_status()
        
        lines = resp.text.splitlines()
        payload = []
        in_payload = False
        
        for line in lines:
            # 查找 payload: 标记
            if line.strip() == "payload:":
                in_payload = True
                continue
            
            if in_payload:
                stripped = line.strip()
                # 过滤空行和注释
                if stripped and not stripped.startswith("#"):
                    payload.append(stripped)
        
        timestamp = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")
        
        # 构建新内容
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