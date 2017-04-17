# pi-tools
Useful tools for a Raspberry Pi

## Mailer

Sends the current IP addresses assigned to the PI to a defined mail address.
This helps you connecting to a Pi it is connected to a network with dynamically assigned IP addresses.

This scrip can be run automatically after the boot.
For that, you can create a launcher script that is called by cron after every startup.
Within that script, everything that must be called after startup can be added.

```bash
#!/bin/sh
# launcher.sh
# is executed with every boot 
sleep 30
python /home/pi/Documents/mailer/mailmyip.py
```

To make this run after a startup, we add this to the cron config

```
sudo crontab -e
```
and add the entry
```
@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1
````
this will execute the script after each restart and log the ouput into the cronlog file.