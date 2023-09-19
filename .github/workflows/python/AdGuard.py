import os
import requests

class AdGuardFilterDownloader:
    def __init__(self, url):
        self.url = url

    def download_filter(self):
        response = requests.get(self.url)
        return response.text.split("\n")

    @staticmethod
    def filter_line(line, prefix, suffix):
        if line.startswith(prefix) and line.rstrip(suffix)[-1].isalpha():
            return line[len(prefix):].rstrip(suffix)
        return None
    def get_filtered_lines(self, lines, prefix, suffix):
        return [self.filter_line(line, prefix, suffix) for line in lines if self.filter_line(line, prefix, suffix) is not None]

    @staticmethod
    def write_payload_to_file(file_path, content, filtered_lines):
        with open(file_path, "w") as f:
            f.write(content)
            for line in filtered_lines:
                f.write(f"  - '+.{line}'\n")

    def generate_payload_file(self, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        lines = self.download_filter()

        file_data = {
            "AdGuard.yaml": {
                "description": "Blocklist of " + self.url,
                "lines": self.get_filtered_lines(lines, "||", '^'),
            },
            "AdGuardWhitelist.yaml": {
                "description": "Whitelist of " + self.url,
                "lines": self.get_filtered_lines(lines, "@@||", '|^'),
            },
        }

        for file_name, data in file_data.items():
            file_path = os.path.join(output_dir, file_name)
            payload_content = f'''payload:
  # {data["description"]}
  # get {len(data["lines"])} domain from AdGuard DNS filter
  # {lines[5][2:]}
'''
            self.write_payload_to_file(file_path, payload_content, data["lines"])

if __name__ == "__main__":
    url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
    output_dir = "autoupdate"

    downloader = AdGuardFilterDownloader(url)
    downloader.generate_payload_file(output_dir)
