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
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback:
    - https://cn-east.iqiqzz.com/dns-query
    - https://cn-south.iqiqzz.com/dns-query
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
