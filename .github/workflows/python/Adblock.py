import requests
import os
from datetime import datetime
import pytz


def download_and_filter_lists(urls):
    rules = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.splitlines()
            rules.extend([line.strip() for line in lines if line.strip().startswith(("DOMAIN", "IP-CIDR"))])
        else:
            print(f"无法下载文件：{url}")

    return rules


def write_to_yaml_file(rules, output_file):
    line_counts = {}
    for line in rules:
        line_type = line.split(",")[0]
        line_counts[line_type] = line_counts.get(line_type, 0) + 1

    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, "w") as output:
        output.write(f'''payload:
  # Merged BanAD, BanProgramAD, BanEasyListChina from https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash
  # {current_time}
  # {", ".join(f'{k}: {v}' for k, v in line_counts.items())}
  # TOTAL: {sum(line_counts.values())}
''')
        for line in rules:
            output.write(f"  - {line}\n")


if __name__ == "__main__":
    list_urls = [
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list",
    ]

    os.makedirs("autoupdate", exist_ok=True)
    output_yaml_file = "autoupdate/Adblock.yaml"

    lines_to_extract = download_and_filter_lists(list_urls)
    write_to_yaml_file(lines_to_extract, output_yaml_file)
