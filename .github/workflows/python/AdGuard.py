import os
import requests

url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
response = requests.get(url)
lines = response.text.split("\n")

# 过滤
filtered_lines = []
filtered_lines_whitelist = []

for line in lines:
    if line.startswith("||") and line.rstrip('^')[-1].isalpha():
        filtered_lines.append(line[2:].rstrip('^'))
    elif line.startswith("@@||") and line.rstrip('|^')[-1].isalpha():
        filtered_lines_whitelist.append(line[4:].rstrip('|^'))

# 创建文件
output_dir = "autoupdate"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "AdGuard.yaml")
output_file_whitelist = os.path.join(output_dir, "AdGuardWhitelist.yaml")

payload_content = f'''payload:
  # Blocklist of https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
  # get {len(filtered_lines)} domain from AdGuard DNS filter
  # {lines[5][2:]}
'''
payload_content_whitelist = f'''payload:
  # Whitelist of https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt
  # get {len(filtered_lines_whitelist)} domain from AdGuard DNS filter
  # {lines[5][2:]}
'''

with open(output_file, "w") as f, open(output_file_whitelist, "w") as f_whitelist:
    f.write(payload_content)
    f_whitelist.write(payload_content_whitelist)

    for line in filtered_lines:
        f.write(f"  - '+.{line}'\n")

    for line in filtered_lines_whitelist:
        f_whitelist.write(f"  - '+.{line}'\n")