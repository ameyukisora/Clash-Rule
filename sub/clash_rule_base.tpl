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
    - https://223.5.5.5/dns-query
    - https://223.6.6.6/dns-query
sniffer:
  enable: true
  ## 对 redir-host 类型识别的流量进行强制嗅探
  ## 如：Tun、Redir 和 TProxy 并 DNS 为 redir-host 皆属于
  force-dns-mapping: true
  ## 对所有未获取到域名的流量进行强制嗅探
  # parse-pure-ip: false
  # 是否使用嗅探结果作为实际访问，默认 true
  # 全局配置，优先级低于 sniffer.sniff 实际配置
  # override-destination: false
  sniff: # TLS 默认如果不配置 ports 默认嗅探 443
    TLS:
      ports: [443, 8443]
    
    # 默认嗅探 80
    HTTP: # 需要嗅探的端口
      
      ports: [80, 8080-8880]
      # 可覆盖 sniffer.override-destination
      # override-destination: true
  force-domain:
    - 'google.com'
  ## 对嗅探结果进行跳过
  skip-domain:
    - Mijia Cloud
proxies: ~
proxy-groups: ~
rules: ~
