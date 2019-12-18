#cool one liner, gives you the path to the script dir, unless the script itself is a symlink
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


apt update && apt upgrade -y
apt install python3 python3-pip git hostapd dnsmasq -y
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
hw_mode=g #refers to 802.11 standard
channel=7
wmm_enabled=0 #disables QOS
macaddr_acl=0 #mac addr filtering
auth_algs=1 # auth algs, 1 for open auth algo with WPA
ignore_broadcast_ssid=0
wpa=2 #enables wpa2
wpa_key_mgmt=WPA-PSK #key management algorithms 
wpa_pairwise=TKIP #wpa encryption standard
rsn_pairwise=CCMP #wpa2 encryption
ssid=theOracle #ssid
wpa_passphrase=rfidmechanic 
# https://wireless.wiki.kernel.org/en/users/documentation/hostapd
EOT

echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' >> /etc/default/hostapd
systemctl unmask hostapd
systemctl enable hostapd
systemctl start hostapd

systemctl enable dnsmasq
systemctl start dnsmasq

cd $DIR

pip3 install -r requirements.txt

cd ..
DIR2=$(pwd)

crontab -l > mycron
#echo new cron into cron file
echo "@reboot python3 $DIR2/Main.py" >> mycron
#install new cron file
crontab mycron
rm mycron
