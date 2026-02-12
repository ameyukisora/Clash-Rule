import requests
from datetime import datetime
import pytz
from pathlib import Path

# 配置常量
URL = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt"
OUTPUT_FILE = Path("autoupdate/gfw.yaml")
TIMEZONE = 'Asia/Shanghai'

def main():
    try:
        print(f"正在下载: {URL}")
        response = requests.get(URL, timeout=15)
        response.raise_for_status()
        
        lines = response.text.splitlines()
        # 跳过第一行（通常是注释或标题）
        urls = lines[1:] if len(lines) > 1 else []
        
        timestamp = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")
        
        # 构建内容
        content = f"""payload:
  # {timestamp}
  # TOTAL: {len(urls)} urls
{chr(10).join(urls)}
"""
        # 写入文件
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(content, encoding='utf-8')
        print(f"✅ 成功生成: {OUTPUT_FILE} (共 {len(urls)} 条)")
        
    except requests.RequestException as e:
        print(f"❌ 下载失败: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        exit(1)

if __name__ == "__main__":
    main()