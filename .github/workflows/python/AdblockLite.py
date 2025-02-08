import os
import requests
from datetime import datetime
import pytz
from collections import Counter

class AdblockListProcessor:
    def __init__(self, urls, output_file):
        self.urls = urls
        self.output = output_file
        self.rules = set()

    def _fetch_rules(self):
        for url in self.urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                self.rules.update(
                    line.strip()
                    for line in response.text.splitlines()
                    if line.startswith(("DOMAIN", "IP-CIDR"))
                )
            except requests.RequestException as e:
                print(f"下载失败 {url}: {e}")

    def _existing_rules(self):
        if not os.path.exists(self.output):
            return None
        with open(self.output, encoding='utf-8') as f:
            return [line.strip(" -\n") for line in f.readlines()[5:]]

    def _need_update(self):
        existing = self._existing_rules()
        return existing != sorted(self.rules) if existing else True

    def _generate_header(self):
        counts = Counter(rule.split(',')[0] for rule in self.rules)
        return (
            f"payload:\n"
            f"  # Merged ACL4SSR: BanAD, BanProgramAD\n"
            f"  # {datetime.now(pytz.timezone('Asia/Shanghai')):%Y-%m-%d %H:%M:%S}\n"
            f"  # {', '.join(f'{k}:{v}' for k, v in counts.items())}\n"
            f"  # TOTAL: {sum(counts.values())}\n"
        )

    def process(self):
        self._fetch_rules()
        if not self._need_update():
            print("规则未变更")
            return

        with open(self.output, 'w', encoding='utf-8') as f:
            f.write(self._generate_header())
            f.writelines(f"  - {rule}\n" for rule in sorted(self.rules))
        print(f"文件已更新: {self.output}")

if __name__ == "__main__":
    AdblockListProcessor(
        urls=[
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
            "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list"
        ],
        output_file=os.path.join("autoupdate", "AdblockLite.yaml")
    ).process()
