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
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith("DOMAIN") or stripped_line.startswith("IP-CIDR"):
                lines_to_extract.append(f"{stripped_line}")
    else:
        print(f"无法下载文件：{url}")

# 统计
count_domain = sum(1 for line in lines_to_extract if line.startswith("DOMAIN,"))
count_keyword = sum(1 for line in lines_to_extract if line.startswith("DOMAIN-KEYWORD"))
count_suffix = sum(1 for line in lines_to_extract if line.startswith("DOMAIN-SUFFIX"))
count_ipcidr = sum(1 for line in lines_to_extract if line.startswith("IP-CIDR"))

# 当前时间
tz = pytz.timezone('Asia/Shanghai')  # 设置时区为UTC+8
current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# 写入文件内容
content = f'''payload:
  # Adblock rules from https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash
  # Merged BanAD, BanProgramAD, BanEasyListChina
  # {current_time}
  # DOMAIN: {count_domain}, DOMAIN-KEYWORD: {count_keyword}, DOMAIN-SUFFIX: {count_suffix}, IP-CIDR: {count_ipcidr}
'''

# 将提取的行写入.yaml文件
with open(output_yaml_file, "w") as output_file:
    output_file.write(content)
    for line in lines_to_extract:
        output_file.write(f"  - {line}\n")