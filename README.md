### Mihomo providers and remote config (mihomo core)
|| Descriptions |
| - | - |
| autoupdate | Automatically update every 24 hours using GitHub Actions. |
| provider | Manual maintenance. |
| sub | Used for subconverter. See [pref_com.ini](https://github.com/ameyukisora/Clash-Rule/blob/master/pref_com.ini).|
| mixin_dns_tun.yaml | CFW mixin TUN settings. |
| pref_com.ini | Subconverter external config. |

#### How to use Mihomo Core in CFW 0.20.39

1. Download the latest Mihomo Core (mihomo-windows-amd64-xx.xx.xx.zip)

2. Rename .exe file to "clash-win64.exe" and replace the file at:
   [CFW installation directory]\resources\static\files\win\x64\clash-win64.exe

3. Download the resources.7z file from this repository
   - Extract the "resources" folder
   - Drag and drop it into the CFW installation root directory
   - Choose to merge folders and replace files when prompted
