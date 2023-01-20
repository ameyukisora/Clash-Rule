mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
ipv6: false
enable-process: true
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  default-nameserver:
    - 223.5.5.5
    - 223.6.6.6
  nameserver:
    - https://223.5.5.5/dns-query
    - https://223.6.6.6/dns-query
    - https://doh.pub/dns-query
proxies: ~
proxy-groups: ~
rules: ~
