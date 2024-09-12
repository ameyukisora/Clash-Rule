import requests
from datetime import datetime
import pytz
import os

# 下载文件
url = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaMax/ChinaMax_Domain.yaml"
response = requests.get(url)
content = response.text.splitlines()

# 处理文件内容
payload_start = content.index("payload:") + 1
payload = [line.strip() for line in content[payload_start:] if line.strip() and not line.strip().startswith("#")]

# 计算域名数量
domain_count = len(payload)

# 获取当前时间
tz = pytz.timezone('Asia/Shanghai')
current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# 创建新的文件内容
new_content = ["payload:"]
new_content.append(f"  # Updated: {current_time}, Total: {domain_count}")
new_content.extend([f"  {domain}" for domain in payload])

# 确保autoupdate文件夹存在
os.makedirs('autoupdate', exist_ok=True)

# 保存到文件
with open('autoupdate/cndomain.yaml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_content))

print(f"File updated and saved. Total domains: {domain_count}")
