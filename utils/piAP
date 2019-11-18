apt update && apt upgrade -y
apt install hostapd dnsmasq -y
systemctl stop dnsmasq
cat << EOT >>/etc/dhcpcd.conf
interface wlan0
        static ip_address=192.168.0.1/24
        nohook wpa_supplicant
EOT

systemctl restart dhcpcd
mv /etc/dnsmasq.conf /etc/dnsmaq.conf.old
cat << EOT > /etc/dnsmasq.conf
interface=wlan0

dhcp-range=192.168.0.50,192.168.0.150,255.255.255.0,12h
EOT

cat << EOT > /etc/hostapd/hostapd.conf
interface=wlan0
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=theOracle
wpa_passphrase=rfidmechanic
EOT
