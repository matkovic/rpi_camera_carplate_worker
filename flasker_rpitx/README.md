## Flasker Rpitx

Simple flask application for listening specific request and triggering RF records through rpitx.

flasker_rpitx.service - this runs app.py as a service on startup.

Commands:
```
vim /etc/systemd/system/flasker_rpitx.service
```

```
systemctl start flasker_rpitx.service
systemctl enable flasker_rpitx.service
```



Obsolete (or when the rpitx stuff can be run on RPi with camera module, currently it does not work properly):

*Sudoers* allow nologin to run rpitx script:
```
sudo visudo
```
Add this inside
```
#custom
www-data ALL=NOPASSWD: /home/pi/rpitx/sendiq
```

and run with
```
sudo /home/pi/rpitx/sendiq -s 250000 -f 433.92e6 -t u8 -i /home/pi/rpitx/record.iq
```