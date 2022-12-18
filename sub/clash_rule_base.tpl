mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
dns:
  enable: true
  ipv6: false
  enhanced-mode: fake-ip
  nameserver:
    - 223.5.5.5
  fake-ip-filter:
    # === LAN ===
    - '*.example'
    - '*.home.arpa'
    - '*.invalid'
    - '*.lan'
    - '*.local'
    - '*.localdomain'
    - '*.localhost'
    - '*.test'
    # === Windows 10 Connnect Detection ===
    - '*.ipv6.microsoft.com'
    - '*.msftconnecttest.com'
    - '*.msftncsi.com'
    - 'msftconnecttest.com'
    - 'msftncsi.com'
    # === NTP Service ===
    - 'ntp.*.com'
    - 'ntp1.*.com'
    - 'ntp2.*.com'
    - 'ntp3.*.com'
    - 'ntp4.*.com'
    - 'ntp5.*.com'
    - 'ntp6.*.com'
    - 'ntp7.*.com'
    - 'time.*.apple.com'
    - 'time.*.com'
    - 'time.*.gov'
    - 'time1.*.com'
    - 'time2.*.com'
    - 'time3.*.com'
    - 'time4.*.com'
    - 'time5.*.com'
    - 'time6.*.com'
    - 'time7.*.com'
    - 'time.*.edu.cn'
    - '*.time.edu.cn'
    - '*.ntp.org.cn'
    - '+.pool.ntp.org'
    - 'time1.cloud.tencent.com'
    ## STUN Server
    - '+.stun.*.*.*.*'
    - '+.stun.*.*.*'
    - '+.stun.*.*'
    - 'stun.*.*.*'
    - 'stun.*.*'
    # === Music Service ===
    ## 腾讯音乐
    - 'songsearch.kugou.com'
    - 'trackercdn.kugou.com'
    - '*.kuwo.cn'
    - 'api-jooxtt.sanook.com'
    - 'api.joox.com'
    - 'joox.com'
    - 'y.qq.com'
    - '*.y.qq.com'
    - 'amobile.music.tc.qq.com'
    - 'aqqmusic.tc.qq.com'
    - 'mobileoc.music.tc.qq.com'
    - 'streamoc.music.tc.qq.com'
    - 'dl.stream.qqmusic.qq.com'
    - 'isure.stream.qqmusic.qq.com'
    ## 网易云音乐
    - 'music.163.com'
    - '*.music.163.com'
    - '*.126.net'
    # === Other ===
    ## QQ Quick Login
    - 'localhost.ptlogin2.qq.com'
    - 'localhost.sec.qq.com'
    - '+.qq.com'
    ## WoWs
    - +.wargaming.net
    - '+.worldofwarships.*'
proxies: ~
proxy-groups: ~
rules: ~
