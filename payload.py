import scapy.all.Ether
import scapy.all.IP
import scapy.all.TCP

frame = Ether(dst="00:0c:29:A0:A7:5B") / IP(dst="192.168.128.132") / TCP() / "This is my payload"
