# rfidMechanic
An app that gets a read from rfid marked cards and then, depending on the type of the card game selected predicts results.

It also displays approximated chances of winning for each player in hold em (it does so by simulating a 1000 hands, so the margin of error is not benign - it seems to be at least 5 percentage points).

Here's a demonstration video of the hold em mode:
https://youtu.be/O1KWP25Fn3Y

This is a personal project and it's definietely nowhere close to finished (although most of the code is here, there's still some stuff to figure out with making this fit into a practical size, getting a better reader that can read through a table, improving how tags fit into cards and so on).

Thus there is no support promised whatsoever and the notes here are as much for me some time from now as for anybody who would want to try this, but do feel free to contact me if you run into any problems - however do know that this project is going to move very slowly and because of that I'd advise against setting it up unless you're really interested in such a thing and it may be of use to you.

Minimum requirements for running the app:

  - Arduino nano

  - MiFare RFID-RC522 reader/writer module for arduino connected same as in the example in arduino/schematic.png
  
  - A computer with python3 and pyserial (for Windows you need to manually change the serial port, it's not being auto-detected yet).

Arduino usage:
If you're using NTAG213 (Mifare Ultralight) use the theAppRead.ino program found in arduino/ntag213, otherwise use the one found in arduino/classic dir - it should work with the most commonely sold nfc tags. Same goes for writing, set the value to be written by changing the buffer[0] (ntag213), or dataBlock[0] (classic) - it's marked with a comment. I reccommend watching arduino IDE's serial monitor while writing a tag - the proccess can sometimes fail if the tag is placed incorrectly. Currently I'm not making enough cards to justify making the process easier.

Connect the arduino using the USB cable to your device before launching Main.py .

You need to change the ip address in webMechanic/mechanic.js to your computer's address, otherwise you'll get an error (you don't need to if you're using the AP setup with a pi). 

There's also a script for deploying on a raspberry pi that also configures hostapd to allow the pi to be used as an access point (since you're not going to carry a laptop in your jacket):


Installation on a raspberry pi:
1) do a clean install of raspbian

2) clone the repo and put it somewhere like /opt/rfidMechanic

3) run utils/raspDeploy.sh

After that just reboot your pi and use your phone to connect to the wifi network (default ssid: "theOracle", default password: "rfidmechanic"). Then open up your browser and enter 192.168.0.1:8080 to access the app. 
