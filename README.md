# pizero-epaper-movie
## Display Rotating Movie Images on a Raspberry Pi Zero e-Paper Display
![Sample Image](https://github.com/DennisFaucher/pizero-epaper-movie/blob/master/IMG_20191213_134338.jpg)
So, I was having great fun with a new Raspberry Pi Zero W plus Waveshare e-Paper display acting as a pwnagotchi (www.pwnagotchi.ai) cracking WiFi passwords. Once I realized that WPA passwords can only be cracked if A) people use simple dictionary words or B) You have lots of GPUs for a long time, I decided to repurpose the rPi Zero W. Our work holiday party was coming up, so I figured something to accent my ugly sweater would be a win. These were the steps I took to create a small device that rotates through holiday movie stills:
## Hardware
Raspberry Pi Zero W. WITH PINS as I am terrible at soldering. I purchased mine here: https://www.aliexpress.com/item/32979703845.html

Waveshare 2.13" e-Paper Dsiplay HAT. I purchased mine here: https://www.aliexpress.com/item/32810080308.html
## Software
Install Raspbian OS from here https://www.raspberrypi.org/downloads/raspbian/ and use these instructions: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Connect your Raspberry Pi Zero to keyboard, mouse, HDMI monitor and power to run through the usual Linux setup. I picked up all the necessary cable/power accesories here: https://www.sparkfun.com/products/14298

Install the Waveshare e-Paper drivers using these instructions: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT. Rename the awfully named directory "RaspberryPi\&JetsonNano" to just "Pi".

Copy my christmas.py to the e-Paper/Pi/python/examples directory

Copy my image folders (Unzip Movie-Images.zip), or your own images folders, to the e-Paper/Pi/python/pic directory. You can make your own image folders by extracting images from a movie with VLC using these instrcutions: https://www.isimonbrown.co.uk/vlc-export-frames/

Test by executing "python3 christmas.py" from the e-Paper/Pi/python/examples directory

To autorun on boot, add this line to your /etc/rc.local: "python3 /home/pi/e-Paper/Pi/python/examples/christmas.py > /dev/null 2>&1 &"

Enjoy.
