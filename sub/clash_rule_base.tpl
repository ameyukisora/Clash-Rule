mixed-port: 7890
allow-lan: false
log-level: info
mode: Rule
dns:
  enable: true
  ipv6: false
  listen: '127.0.0.1:8053'
  enhanced-mode: fake-ip
  nameserver: 
    - https://223.5.5.5/dns-query
    - https://223.6.6.6/dns-query
  fake-ip-filter: ['*.lan', '*.localdomain', '*.example', '*.invalid', '*.localhost', '*.test', '*.local', '*.home.arpa', 'time.*.com', 'time.*.gov', 'time.*.edu.cn', 'time.*.apple.com', 'time1.*.com', 'time2.*.com', 'time3.*.com', 'time4.*.com', 'time5.*.com', 'time6.*.com', 'time7.*.com', 'ntp.*.com', 'ntp1.*.com', 'ntp2.*.com', 'ntp3.*.com', 'ntp4.*.com', 'ntp5.*.com', 'ntp6.*.com', 'ntp7.*.com', '*.time.edu.cn', '*.ntp.org.cn', +.pool.ntp.org, time1.cloud.tencent.com, music.163.com, '*.music.163.com', '*.126.net', musicapi.taihe.com, music.taihe.com, songsearch.kugou.com, trackercdn.kugou.com, '*.kuwo.cn', api-jooxtt.sanook.com, api.joox.com, joox.com, y.qq.com, '*.y.qq.com', streamoc.music.tc.qq.com, mobileoc.music.tc.qq.com, isure.stream.qqmusic.qq.com, dl.stream.qqmusic.qq.com, aqqmusic.tc.qq.com, amobile.music.tc.qq.com, '*.xiami.com', '*.music.migu.cn', music.migu.cn, '*.msftconnecttest.com', '*.msftncsi.com', msftconnecttest.com, msftncsi.com, localhost.ptlogin2.qq.com, localhost.sec.qq.com, +.srv.nintendo.net, +.stun.playstation.net, 'xbox.*.microsoft.com', xnotify.xboxlive.com, +.battlenet.com.cn, +.wotgame.cn, +.wggames.cn, +.wowsgame.cn, +.wargaming.net, '+.worldofwarships.*', proxy.golang.org, 'stun.*.*', 'stun.*.*.*', '+.stun.*.*', '+.stun.*.*.*', '+.stun.*.*.*.*', heartbeat.belkin.com, '*.linksys.com', '*.linksyssmartwifi.com', '*.router.asus.com', mesu.apple.com, swscan.apple.com, swquery.apple.com, swdownload.apple.com, swcdn.apple.com, swdist.apple.com, lens.l.google.com, stun.l.google.com, +.nflxvideo.net, '*.square-enix.com', '*.finalfantasyxiv.com', '*.ffxiv.com']
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
  - PROCESS-NAME,aria2c.exe,DIRECT
  - PROCESS-NAME,BitComet.exe,DIRECT
  - PROCESS-NAME,BitComet_x64.exe,DIRECT
  - PROCESS-NAME,wargamingerrormonitor.exe,DIRECT
  - PROCESS-NAME,wgc.exe,DIRECT
  - PROCESS-NAME,wgc_renderer_host.exe,DIRECT
  - PROCESS-NAME,WorldOfWarships64.exe,DIRECT
  - PROCESS-NAME,Netch.exe,DIRECT
  - PROCESS-NAME,Shadowsocks.exe,DIRECT
  - PROCESS-NAME,Trojan.exe,DIRECT