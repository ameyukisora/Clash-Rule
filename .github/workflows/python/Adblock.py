import requests
import os
from datetime import datetime
import pytz

list_urls = [
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list",
]

# 输出文件
os.makedirs("autoupdate", exist_ok=True)
output_yaml_file = "autoupdate/Adblock.yaml"

# 用于存储以DOMAIN或者IPCIDR开头的行的列表
lines_to_extract = []

# 下载并处理每个.list文件
for url in list_urls:
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.splitlines()
        lines_to_extract.extend([line.strip() for line in lines if line.strip().startswith(("DOMAIN", "IP-CIDR"))])
    else:
        print(f"无法下载文件：{url}")

# 统计
line_counts = {}
for line in lines_to_extract:
    line_type = line.split(",")[0]
    line_counts[line_type] = line_counts.get(line_type, 0) + 1

# 当前时间
tz = pytz.timezone('Asia/Shanghai')  # 设置时区为UTC+8
current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# 写入文件内容
content = f'''payload:
  # Adblock rules from https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash
  # Merged BanAD, BanProgramAD, BanEasyListChina
  # {current_time}
  # {", ".join(f'{k}: {v}' for k, v in line_counts.items())}
  # TOTAL: {sum(line_counts.values())}
'''

# 将提取的行写入.yaml文件
with open(output_yaml_file, "w") as output_file:
    output_file.write(content)
    for line in lines_to_extract:
        output_file.write(f"  - {line}\n")
