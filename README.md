# RPi-ip-oled
PWr Raspberry Pi ip print on OLED display.

## Install steps
Install required packages:
```console
/home/pi# sudo apt install unzip

/home/pi# sudo apt install wget
```

Download released installer
```console
wget https://github.com/petrusvr/RPi-ip-oled/releases/download/v1.0.0/ip-oled.zip
```

Unzip installer
```console
unzip ip-oled.zip
```

Enter to unzipped installer folder
```console
cd ip-oled
```

Add execute permissions to installer
```console
chmod +x install.sh
```

Run installer. Required root priviledges to register ip-oled to systemd.
```console
sudo ./install.sh
```

after install is done you will see on console:
```console
ip-oled service intaller
Enabling service ip-oled



● ip-oled.service - Service that displays IPs on OLED
     Loaded: loaded (/lib/systemd/system/ip-oled.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2021-11-20 19:51:46 CET; 41ms ago
   Main PID: 2499 (python3)
      Tasks: 1 (limit: 4915)
        CPU: 28ms
     CGroup: /system.slice/ip-oled.service
             └─2499 /usr/bin/python3 /usr/lib/ip-oled/main.py

Nov 20 19:51:46 raspberrypi systemd[1]: Started Service that displays IPs on OLED.
Yupi, reboot system to check ip-oled starts at system boot

```