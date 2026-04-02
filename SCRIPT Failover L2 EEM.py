SCRIPT Failover L2 EEM


Links de Fibras Opticas 

###SWNDIST1C
Link TVCABO → Ethernet1/1

###SWDIST1V
Link CONNECTIS → Ethernet1/16
#######################################################
LÓGICA FUNCIONAL (RESUMO)
Se TVCABO cair
 Remove VLANs 21,28,75,244 do SWNDIST1C
 Adiciona VLANs 21,28,75,244 no SWDIST1V
!
Se TVCABO subir
 Adiciona VLANs 21,28,75,244 no SWNDIST1C
 Remove VLANs 21,28,75,244 do SWDIS
 !
 !
 Se CONNECTIS cair
Remove VLANs 20,113,136,203 do SWDIST1V
Adiciona VLANs 20,113,136,203 no SWNDIST1C
!
Se CONNECTIS subir
Adiciona VLANs 20,113,136,203 no SWDIST1V
Remove VLANs 20,113,136,203 do SWNDIST1C
####################################Configuração do SWNDIST1C and SWNDIST1V Down and Up Fibra_TvCabo
conf t
event manager applet TVCABO_DOWN_SWNDIST1C
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down"
 action 1.0 syslog msg "TVCABO DOWN - removendo VLANs 21,28,75,244 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 21,28,75,244"
 action 6.0 cli command "end"
end
!
conf t
event manager applet TVCABO_DOWN_SWNDIST1V
 event syslog pattern "TVCABO DOWN"
 action 1.0 syslog msg "TVCABO DOWN - adicionando VLANs 21,28,75,244 no SWDIST1V"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
#####################TvCabo Subir 
conf t
event manager applet TVCABO_UP_SWDIST1V
 event syslog pattern "TVCABO UP"
 action 1.0 syslog msg "TVCABO UP - removendo VLANs 21,28,75,244 no SWDIST1V"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 21,28,75,244"
 action 6.0 cli command "end"
end
!
conf t
event manager applet TVCABO_UP_SWNDIST1C
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to up"
 action 1.0 syslog msg "TVCABO UP - restaurando VLANs 21,28,75,244 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
####################################Configuração do SWNDIST1V and SWNDIST1C Down and Up Fibra_Connectis
conf t
event manager applet CONNECTIS_DOWN_SWDIST1V
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to down"
 action 1.0 syslog msg "CONNECTIS DOWN - removendo VLANs 20,113,136,203 no SWDIST1V"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_DOWN_SWNDIST1C
 event syslog pattern "CONNECTIS DOWN"
 action 1.0 syslog msg "CONNECTIS DOWN - adicionando VLANs 20,113,136,203 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
#####################Connectis Subir
conf t
event manager applet CONNECTIS_UP_SWNDIST1C
 event syslog pattern "CONNECTIS UP"
 action 1.0 syslog msg "CONNECTIS UP - removendo VLANs 20,113,136,203 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SWDIST1V
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to up"
 action 1.0 syslog msg "CONNECTIS UP - restaurando VLANs 20,113,136,203 no SWDIST1V"
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
event manager applet TVCABO_UP_SWNDIST1C
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to up"
 action 1.0 syslog msg "TVCABO UP - restaurando VLANs 21,28,75,244 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 21,28,75,244"
 action 6.0 cli command "end"
end
!
############################################Configuração do SWNDIST1V
conf t
event manager applet CONNECTIS_DOWN_SWNDIST1V
 event syslog pattern "CONNECTIS DOWN"
 action 1.0 syslog msg "CONNECTIS DOWN - adicionando VLANs 20,113,136,203 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SWNDIST1V
 event syslog pattern "CONNECTIS UP"
 action 1.0 syslog msg "CONNECTIS UP - removendo VLANs 20,113,136,203 no SWNDIST1C"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/1"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_DOWN_SWDIST1V
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to down"
 action 1.0 syslog msg "CONNECTIS DOWN - removendo VLANs 20,113,136,203 no SWDIST1V"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan remove 20,113,136,203"
 action 6.0 cli command "end"
end
!
conf t
event manager applet CONNECTIS_UP_SWDIST1V
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/16, changed state to up"
 action 1.0 syslog msg "CONNECTIS UP - restaurando VLANs 20,113,136,203 no SWDIST1V"
 action 2.0 cli command "enable"
 action 3.0 cli command "configure terminal"
 action 4.0 cli command "interface Ethernet1/16"
 action 5.0 cli command "switchport trunk allowed vlan add 20,113,136,203"
 action 6.0 cli command "end"
end
!
logging host 10.222.103.27
logging host 10.223.103.27
logging trap notifications


