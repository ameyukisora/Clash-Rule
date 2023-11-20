import requests
import os

def download_and_filter_ips(url, output_file):
    # Download the file from the URL
    response = requests.get(url)
    lines = response.text.split("\n")

    # Filter IP addresses
    ip_list = [ip for ip in lines if ip and ip[0].isdigit()]

    # Write the IP addresses to the output YAML file
    with open(output_file, "w") as f:
        f.write(f'''payload:
  # https://github.com/misakaio/chnroutes2
  {lines[0]}
  {lines[1]}
{"".join(f"  - '{ip}'\n" for ip in ip_list)}
''')

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
    os.makedirs("autoupdate", exist_ok=True)
    output_file = "autoupdate/chnroutes.yaml"
    download_and_filter_ips(url, output_file)
