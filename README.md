# Smile Frame

Nice project to display encouragement pic file (png format) when you smile

Raspberry PI - PiTFT install guide:
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi

This folder should contain:
~/.config/autostart/newshell.sh.desktop 

```bash
 [Desktop Entry]
 Type=Application
 Exec=/home/pi/new_shell.sh
 Name=newshell
 Comment=Run Smile App
```

new_shell.sh can be found home folder of this repo.

Raspbian Ver:
VERSION="9 (stretch)"

Smile detector reference:
https://www.electromaker.io/project/view/open-cv--face-eyes--smile-detection-with-raspberry-pi