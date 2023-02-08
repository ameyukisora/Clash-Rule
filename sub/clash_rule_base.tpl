mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
ipv6: false
geodata-mode: true
enable-process: true
geox-url:
  geoip: "https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geoip.dat"
  geosite: "https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geosite.dat"
  mmdb: "https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/Country.mmdb"
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  nameserver:
    - https://doh.pub/dns-query
proxies: ~
proxy-groups: ~
rules: ~
