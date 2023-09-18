import requests
import os

url = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
response = requests.get(url)
lines = response.text.split("\n")

# filter ip
ip_list = [ip for ip in lines if ip and ip[0].isdigit()]

# create file
os.makedirs("autoupdate", exist_ok=True)
output_file = "autoupdate/chnroutes.yaml"

output_content = f'''payload:
  # https://github.com/misakaio/chnroutes2
  {lines[0]}
  {lines[1]}
'''

with open(output_file, "w") as f:
    f.write(output_content)
    f.writelines(f"  - '{ip}'\n" for ip in ip_list)