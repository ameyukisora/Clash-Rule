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
  default-nameserver:
    - 117.50.11.11
    - tls://1.12.12.12:853
    - tls://223.5.5.5:853
  nameserver:
    - https://doh-pure.onedns.net/dns-query
    - https://dns.alidns.com/dns-query
    - https://doh.pub/dns-query
proxies: ~
proxy-groups: ~
rules: ~
