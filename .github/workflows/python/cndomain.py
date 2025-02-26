import requests
from datetime import datetime
import pytz
import os

# 定义常量
URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaMax/ChinaMax_Domain.yaml"
OUTPUT_DIR = 'autoupdate'
OUTPUT_FILE = 'cndomain.yaml'
TIMEZONE = 'Asia/Shanghai'
ENCODING = 'utf-8'

# 下载文件内容
response = requests.get(URL)
content = response.text.splitlines()

# 提取域名列表
payload_start_index = content.index("payload:") + 1
payload = [line.strip() for line in content[payload_start_index:] if line.strip() and not line.strip().startswith("#")]
domain_count = len(payload)

# 生成新的文件内容
current_time = datetime.now(pytz.timezone(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")
new_content = [
    "payload:",
    f"  # Updated: {current_time}, Total: {domain_count}",
    *[f"  {domain}" for domain in payload]  # 使用星号解包列表
]

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 保存到文件
output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
with open(output_path, 'w', encoding=ENCODING) as f:
    f.write('\n'.join(new_content))

print(f"域名总数: {domain_count}")
