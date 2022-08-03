mixed-port: 7890
allow-lan: false
log-level: info
mode: Rule
dns:
  enable: true
  ipv6: false
  enhanced-mode: fake-ip
  default-nameserver:
    - 223.5.5.5
    - 223.6.6.6
  nameserver:
    - https://dns.alidns.com/dns-query
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
    # === Apple Software Update Service ===
    - 'mesu.apple.com'
    - 'swscan.apple.com'
    # === ASUS Router ===
    - '*.router.asus.com'
    # === Google ===
    - 'lens.l.google.com'
    - 'stun.l.google.com'
    ## Golang
    - 'proxy.golang.org'
    # === Linksys Wireless Router ===
    - '*.linksys.com'
    - '*.linksyssmartwifi.com'
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
    # === Game Service ===
    ## Microsoft Xbox
    - 'speedtest.cros.wr.pvp.net'
    - '*.*.xboxlive.com'
    - 'xbox.*.*.microsoft.com'
    - 'xbox.*.microsoft.com'
    - 'xnotify.xboxlive.com'
    ## Nintendo Switch
    - '*.*.*.srv.nintendo.net'
    - '+.srv.nintendo.net'
    ## Sony PlayStation
    - '*.*.stun.playstation.net'
    - '+.stun.playstation.net'
    ## STUN Server
    - '+.stun.*.*.*.*'
    - '+.stun.*.*.*'
    - '+.stun.*.*'
    - 'stun.*.*.*'
    - 'stun.*.*'
    # === Music Service ===
    ## 咪咕音乐
    - '*.music.migu.cn'
    - 'music.migu.cn'
    ## 太和音乐
    - 'music.taihe.com'
    - 'musicapi.taihe.com'
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
    ## 虾米音乐
    - '*.xiami.com'
    # === Other ===
    ## QQ Quick Login
    - 'localhost.ptlogin2.qq.com'
    - 'localhost.sec.qq.com'
    ## BiliBili P2P
    - '*.mcdn.bilivideo.cn'
proxies: ~
proxy-groups: ~
rules:
  - DOMAIN-SUFFIX,ip6-localhost,DIRECT
  - DOMAIN-SUFFIX,ip6-loopback,DIRECT
  - DOMAIN-SUFFIX,local,DIRECT
  - DOMAIN-SUFFIX,localhost,DIRECT
  - IP-CIDR,10.0.0.0/8,DIRECT,no-resolve
  - IP-CIDR,100.64.0.0/10,DIRECT,no-resolve
  - IP-CIDR,127.0.0.0/8,DIRECT,no-resolve
  - IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
  - IP-CIDR,192.168.0.0/16,DIRECT,no-resolve
  - IP-CIDR,198.18.0.0/16,DIRECT,no-resolve
  - DOMAIN,safebrowsing.googleapis.com,DIRECT
  - DOMAIN-SUFFIX,dl.google.com,DIRECT
  - DOMAIN-SUFFIX,msftconnecttest.com,DIRECT
  - DOMAIN-SUFFIX,msftncsi.com,DIRECT
  - DOMAIN-SUFFIX,windows.com,DIRECT
  - DOMAIN-SUFFIX,windows.net,DIRECT
  - DOMAIN-SUFFIX,windowsupdate.com,DIRECT
  - DOMAIN-SUFFIX,xbox.com,DIRECT
  - DOMAIN-SUFFIX,xboxlive.com,DIRECT
  - DOMAIN-SUFFIX,pool.ntp.org,DIRECT
  - PROCESS-NAME,aria2c.exe,DIRECT
  - PROCESS-NAME,BitComet.exe,DIRECT
  - PROCESS-NAME,wargamingerrormonitor.exe,DIRECT
  - PROCESS-NAME,wgc.exe,DIRECT
  - PROCESS-NAME,wgc_renderer_host.exe,DIRECT
  - PROCESS-NAME,WorldOfWarships64.exe,DIRECT
  - PROCESS-NAME,Netch.exe,DIRECT
  - PROCESS-NAME,Shadowsocks.exe,DIRECT
  - PROCESS-NAME,ShadowsocksR.exe,DIRECT
  - PROCESS-NAME,Trojan.exe,DIRECT
  - PROCESS-NAME,v2ray-sn.exe,DIRECT
