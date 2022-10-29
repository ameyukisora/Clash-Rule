mixed-port: 8889
allow-lan: false
log-level: info
mode: Rule
proxies: ~
proxy-groups: ~
script:
  shortcuts: 
    Game: network == "udp" and match_provider("game_udp")
rules:
  - SCRIPT,Game,⚓ Game
rule-providers:
  game_udp:
    type: http
    behavior: classical
    url: https://raw.iqiq.io/ameyukisora/Clash-Rule/master/provider/game_udp.yaml
    path: ./providers/rule-provider_game_udp.yaml
    interval: 86400