echo 1 > /proc/sys/net/ipv4/ip_forward

source sslstripenv/bin/activate
cd Desktop/project/sslstrip


apt install bc
apt-get install build-essential
apt-get install libelf-dev
sudo apt-get install linux-headers-`uname -r
sudo apt install dkms
sudo rmmod r8188eu.ko
git clone https://github.com/aircrack-ng/rtl8188eus.git
cd rtl8188eus
sudo -i
echo "blacklist r8188eu" to  "/etc/modprobe.d/realtek.conf"
exit
sudo reboot
sudo apt update
cd rtl8188eus
sudo make
sudo make install
sudo modprobe 8188eu

aireplay-ng  --test wlan0







git clone "https://github.com/RinCat/RTL88x2BU-Linux-Driver.git" /usr/src/rtl88x2bu-git
sed -i 's/PACKAGE_VERSION="@PKGVER@"/PACKAGE_VERSION="git"/g' /usr/src/rtl88x2bu-git/dkms.conf
dkms add -m rtl88x2bu -v git
dkms autoinstall




