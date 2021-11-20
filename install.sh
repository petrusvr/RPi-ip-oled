#!/bin/bash

echo ip-oled service intaller

IS_ROOT=`id -u`


if [[ $IS_ROOT -ne 0 ]]; then
    echo "Please run as root"
    exit
fi

mkdir -p /usr/lib/ip-oled

yes | cp -rf ./bin/* /usr/lib/ip-oled/

yes | cp -rf ./ip-oled.service /lib/systemd/system/ip-oled.service
chmod 644 /lib/systemd/system/ip-oled.service

systemctl daemon-reload
echo "Enabling service ip-oled"
systemctl enable ip-oled.service
echo
echo
systemctl start ip-oled.service
echo
systemctl status ip-oled.service

echo "Yupi, reboot system to check ip-oled starts at system boot"