mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
ipv6: false
dns:
  enable: true
  ipv6: false
  enhanced-mode: redir-host
  nameserver:
    - 8.8.8.8
    - 8.8.4.4
  fallback:
    - https://doh.pub/dns-query
    - https://223.6.6.6/dns-query
  fallback-filter:
    geoip: false
    ipcidr:
      - 0.0.0.0/32
      - 100.64.0.0/10
      - 127.0.0.0/8
      - 240.0.0.0/4
      - 255.255.255.255/32
proxies: ~
proxy-groups: ~
rules: ~
