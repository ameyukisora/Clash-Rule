import requests
import os

url = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
response = requests.get(url)
lines = response.text.split("\n")

# filter out empty elements
lines = list(filter(None, lines))

# create file
os.makedirs("autoupdate", exist_ok=True)
output_file = "autoupdate/chnroutes.yaml"

output_lines = [
    "payload:",
    "  # https://github.com/misakaio/chnroutes2",
    f"  {lines[0]}",
    f"  {lines[1]}"
]
output_lines.extend([f"  - '{line}'" for line in lines[2:]])

with open(output_file, "w") as f:
   f.write("\n".join(output_lines))