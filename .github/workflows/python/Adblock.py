import os
import requests
from datetime import datetime
import pytz


class AdblockListProcessor:
    def __init__(self, urls, output_file):
        self.list_urls = urls
        self.output_yaml_file = output_file
        self.unique_rules = set()

    def download_and_extract_rules(self):
        for url in self.list_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                for line in response.text.splitlines():
                    line = line.strip()
                    if line.startswith(("DOMAIN", "IP-CIDR")) and line not in self.unique_rules:
                        self.unique_rules.add(line)
            except requests.RequestException:
                print(f"无法下载文件：{url}")
        print(f'合并规则数量：{len(self.unique_rules)}')

    def load_existing_rules(self):
        if not os.path.exists(self.output_yaml_file):
            return None
        with open(self.output_yaml_file, "r", encoding="utf-8") as file:
            lines = file.readlines()[5:]
            return [line.strip(" -\n") for line in lines]

    def has_changes(self):
        existing_rules = self.load_existing_rules()
        return existing_rules != list(self.unique_rules)

    def count_rule_types(self):
        counts = {}
        for rule in self.unique_rules:
            rule_type = rule.split(",")[0]
            counts[rule_type] = counts.get(rule_type, 0) + 1
        return counts

    def write_yaml(self):
        if not self.has_changes():
            print("规则没有发生更改")
            return

        counts = self.count_rule_types()
        total = sum(counts.values())
        current_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")
        counts_str = ", ".join(f'{k}: {v}' for k, v in counts.items())

        header = (
            "payload:\n"
            f"  # Merged ACL4SSR: BanAD, BanProgramAD, BanEasyListChina and dler-io: Surge Reject.list\n"
            f"  # {current_time}\n"
            f"  # {counts_str}\n"
            f"  # TOTAL: {total}\n"
        )

        with open(self.output_yaml_file, "w", encoding="utf-8") as file:
            file.write(header)
            for rule in sorted(self.unique_rules):
                file.write(f"  - {rule}\n")
        print(f"已更新 {self.output_yaml_file}")

    def process(self):
        self.download_and_extract_rules()
        self.write_yaml()


if __name__ == "__main__":
    list_urls = [
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list",
        "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list",
        "https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/AdBlock.list"
    ]

    output_dir = "autoupdate"
    os.makedirs(output_dir, exist_ok=True)
    output_yaml = os.path.join(output_dir, "Adblock.yaml")

    processor = AdblockListProcessor(list_urls, output_yaml)
    processor.process()