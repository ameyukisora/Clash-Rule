import os
import requests

url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
response = requests.get(url)
lines = response.text.split("\n")

# 过滤
def filter_line(line, prefix, suffix):
    if line.startswith(prefix) and line.rstrip(suffix)[-1].isalpha():
        return line[len(prefix):].rstrip(suffix)
    return None

filtered_lines = [filter_line(line, "||", '^') for line in lines if filter_line(line, "||", '^') is not None]
filtered_lines_whitelist = [filter_line(line, "@@||", '|^') for line in lines if filter_line(line, "@@||", '|^') is not None]

# 创建文件
def write_payload_to_file(file_path, content, filtered_lines):
    with open(file_path, "w") as f:
        f.write(content)
        for line in filtered_lines:
            f.write(f"  - '+.{line}'\n")

output_dir = "autoupdate"
os.makedirs(output_dir, exist_ok=True)

file_data = {
    "AdGuard.yaml": {
        "description": "Blocklist of https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
        "lines": filtered_lines,
    },
    "AdGuardWhitelist.yaml": {
        "description": "Whitelist of https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
        "lines": filtered_lines_whitelist,
    },
}

for file_name, data in file_data.items():
    file_path = os.path.join(output_dir, file_name)
    payload_content = f'''payload:
  # {data["description"]}
  # get {len(data["lines"])} domain from AdGuard DNS filter
  # {lines[5][2:]}
'''
    write_payload_to_file(file_path, payload_content, data["lines"])