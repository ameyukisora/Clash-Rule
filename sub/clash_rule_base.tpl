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
    - https://dns.alidns.com/dns-query
    - https://doh.pub/dns-query
proxies: ~
proxy-groups: ~
rules: ~
