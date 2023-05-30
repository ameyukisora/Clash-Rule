mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
ipv6: false
global-client-fingerprint: chrome
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  nameserver:
    - https://doh-pure.onedns.net/dns-query
  proxy-server-nameserver:
    - 117.50.11.11
    - 117.50.10.10
proxies: ~
proxy-groups: ~
rules: ~
