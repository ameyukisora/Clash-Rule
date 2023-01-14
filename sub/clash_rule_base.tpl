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
    - 119.29.29.29
  nameserver:
    - 'quic://cn-south.ovo.glass'
    - 'quic://cn-east.ovo.glass'
  fake-ip-filter:
    ## STUN Server
    - '+.stun.*.*.*.*'
    - '+.stun.*.*.*'
    - '+.stun.*.*'
    - 'stun.*.*.*'
    - 'stun.*.*'
proxies: ~
proxy-groups: ~
rules: ~
