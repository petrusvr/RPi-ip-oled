# RPi ip-oled.service
To make working with the Raspberry Pi lab kit easier, a service has been prepared which shows the current configuration of the network interfaces on a connected display. Once installed, the application starts automatically so there is no need to connect a monitor and keyboard to the RPi kit. To work with the kit, you can use the VNC Client, which will connect to the IP address displayed on the OLED display.
![OLED display on kit](https://github.com/petrusvr/RPi-ip-oled/blob/main/git_resources/oled.jpg?raw=true)

## Install steps
Install required packages:
```console
sudo apt install unzip

sudo apt install wget
```

Download released installer
```console
wget https://github.com/petrusvr/RPi-ip-oled/releases/download/v1.0.1/ip-oled.zip
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

## Usage instructions
Once correctly installed, the application launches itself together with the start of the operating system. After a while, the display will show the current IP addresses for both network interfaces (eth0 and wlan0). The application checks every 5 seconds whether the address has not changed.  If the IP address changes during the application run, the display shows the new configuration.

To stop the application, press any of the buttons on the RPi kit (red or green).

Restarting the application manually is possible by executing the command:
```console
sudo systemctl start ip-oled
```

Checking the application operation status is possible by command:
```console
sudo systemctl status ip-oled
```

