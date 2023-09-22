import requests
import os
from datetime import datetime
import pytz


class AdblockListProcessor:
    def __init__(self, urls, output_file):
        self.list_urls = urls
        self.output_yaml_file = output_file
        self.lines_to_extract = []

    def download_lists(self):
        for url in self.list_urls:
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.splitlines()
                self.lines_to_extract.extend(
                    [line.strip() for line in lines if line.strip().startswith(("DOMAIN", "IP-CIDR"))])
            else:
                print(f"无法下载文件：{url}")

    def compare_with_old_file(self):
        try:
            with open(self.output_yaml_file, "r") as old_file:
                old_contents = old_file.readlines()[5:]
                old_rules = [old_rule.strip(' -\n') for old_rule in old_contents]
                if self.lines_to_extract == old_rules:
                    return True  # The content is the same
            return False
        except FileNotFoundError:
            return False

    def write_to_yaml_file(self):
        if self.compare_with_old_file():
            print("规则没有发生更改")
            return

        line_counts = {}
        for line in self.lines_to_extract:
            line_type = line.split(",")[0]
            line_counts[line_type] = line_counts.get(line_type, 0) + 1

        tz = pytz.timezone('Asia/Shanghai')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

        with open(self.output_yaml_file, "w") as output:
            output.write(f'''payload:
  # Merged BanAD, BanProgramAD, BanEasyListChina from https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash
  # {current_time}
  # {", ".join(f'{k}: {v}' for k, v in line_counts.items())}
  # TOTAL: {sum(line_counts.values())}
''')
            for line in self.lines_to_extract:
                output.write(f"  - {line}\n")


if __name__ == "__main__":
    list_urls = [
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list",
    ]

    os.makedirs("autoupdate", exist_ok=True)
    output_yaml_file = "autoupdate/Adblock.yaml"

    adblock_processor = AdblockListProcessor(list_urls, output_yaml_file)
    adblock_processor.download_lists()
    adblock_processor.write_to_yaml_file()
