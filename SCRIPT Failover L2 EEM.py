SCRIPT Failover L2 EEM


Links de Fibras Opticas 

###SWNDIST1C
Link TVCABO → Ethernet1/1

###SWDIST1V
Link CONNECTIS → Ethernet1/16
#######################################################
LÓGICA FUNCIONAL (RESUMO)
Se TVCABO cair
 Remove VLANs 21,28,75,244 do SW1A-DIST
 Adiciona VLANs 21,28,75,244 no SW1B-DIST
!
Se TVCABO subir
 Adiciona VLANs 21,28,75,244 no SW1A-DIST
 Remove VLANs 21,28,75,244 do SWDIS
 !
 !
 Se CONNECTIS cair
Remove VLANs 20,113,136,203 do SW1B-DIST
Adiciona VLANs 20,113,136,203 no SW1A-DIST
!
Se CONNECTIS subir
Adiciona VLANs 20,113,136,203 no SW1B-DIST
Remove VLANs 20,113,136,203 do SW1A-DIST
####################################Configuração do SW1A-DIST and SW1B-DIST Down and Up Fibra_TvCabo
conf t
event manager applet TVCABO_DOWN_SW1A-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down"
 action 1.0 syslog msg "TVCABO DOWN - removendo VLANs 21,28,75,244 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 21,28,75,244"
 action 6.0 cli command "end"
end
!
conf t
event manager applet TVCABO_DOWN_SW1B-DIST
 event syslog pattern "TVCABO DOWN"
 action 1.0 syslog msg "TVCABO DOWN - adicionando VLANs 21,28,75,244 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
#####################TvCabo Subir 
conf t
event manager applet TVCABO_UP_SW1B-DIST
 event syslog pattern "TVCABO UP"
 action 1.0 syslog msg "TVCABO UP - removendo VLANs 21,28,75,244 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 21,28,75,244"
 action 6.0 cli command "end"
end
!
conf t
event manager applet TVCABO_UP_SW1A-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to up"
 action 1.0 syslog msg "TVCABO UP - restaurando VLANs 21,28,75,244 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
####################################Configuração do SW1B-DIST and SW1A-DIST Down and Up Fibra_Connectis
conf t
event manager applet CONNECTIS_DOWN_SW1B-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to down"
 action 1.0 syslog msg "CONNECTIS DOWN - removendo VLANs 20,113,136,203 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_DOWN_SW1A-DIST
 event syslog pattern "CONNECTIS DOWN"
 action 1.0 syslog msg "CONNECTIS DOWN - adicionando VLANs 20,113,136,203 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
#####################Connectis Subir
conf t
event manager applet CONNECTIS_UP_SW1A-DIST
 event syslog pattern "CONNECTIS UP"
 action 1.0 syslog msg "CONNECTIS UP - removendo VLANs 20,113,136,203 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SW1B-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to up"
 action 1.0 syslog msg "CONNECTIS UP - restaurando VLANs 20,113,136,203 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
##############################################SYSLOG entre os Switches 

logging host 10.22.103.27
logging host 10.23.103.27
logging trap notifications














conf t
event manager applet TVCABO_UP_SW1A-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to up"
 action 1.0 syslog msg "TVCABO UP - restaurando VLANs 21,28,75,244 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
############################################Configuração do SW1B-DIST
conf t
event manager applet CONNECTIS_DOWN_SW1B-DIST
 event syslog pattern "CONNECTIS DOWN"
 action 1.0 syslog msg "CONNECTIS DOWN - adicionando VLANs 20,113,136,203 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SW1B-DIST
 event syslog pattern "CONNECTIS UP"
 action 1.0 syslog msg "CONNECTIS UP - removendo VLANs 20,113,136,203 no SW1A-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_DOWN_SW1B-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to down"
 action 1.0 syslog msg "CONNECTIS DOWN - removendo VLANs 20,113,136,203 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SW1B-DIST
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to up"
 action 1.0 syslog msg "CONNECTIS UP - restaurando VLANs 20,113,136,203 no SW1B-DIST"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
logging host 10.22.103.27
logging host 10.23.103.27
logging trap notifications


