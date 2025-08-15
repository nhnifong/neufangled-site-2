# Raspberry Pi Setup

To be performed for each robot component (four anchors and one gripper)
If you purchased a fully assembled robot and provided the wifi credentials, you do not need to do this.

## Image SD card

Download the [Raspiberry Pi Imager](https://www.raspberrypi.com/software/)

Insert a MicroSD card and open the imager  

For device, select `Raspberry Pi Zero 2 W`  
![](images/raspi/image2.png){ loading=lazy, width=45% }


For operating system, select `RASPBERRY PI OS LITE (64-BIT)`.  
it can be found in the `Raspberry Pi OS (other)` section.

![](images/raspi/image6.png){ loading=lazy, width=45% }
![](images/raspi/image5.png){ loading=lazy, width=45% }

Select the SD card you inserted as the media to be flashed.  
Click `Next`  
Click `Edit Settings`  

![](images/raspi/image3.png){ loading=lazy, width=45% }

Set the user and password. `pi` and `pi` are normally fine defaults.
Confirm the wifi credentials are correct.

![](images/raspi/image4.png){ loading=lazy, width=45% }

On the Services tab, enable SSH

![](images/raspi/image7.png){ loading=lazy, width=45% }

Click `Save` and then `Yes`

## Log Into the Pi

### Match IP addresses to devices

After installation, power on each component one at a time. It is an oversight on my part, but there isn't an LED on them to help you figure out which IP address corresponds to each component.  

When powered on, they should show up on your network. In order to discover their IP addresses, you may have to look at the configuration page of your router. On an ATT router/gateway for example, that would be http://192.168.1.254/ and it's in a section at the bottom labeled home network devices.

From a terminal or powershell, connect to the pi, substituting the address.

    ssh pi@192.168.1.111

With only one turned on at a time you should be able to know which one you are logged into. Although when you turn on the anchor with the power line to the gripper, both come on at the same time. Those two can be disambiguated with

    i2cdetect -y 1

If it's the gripper, you'll see a few addresses, If it's an achor, nothing.

Draw a diagram of the room on a piece of paper labelling the address of each device, with which one is the power anchor.

### Configure and Install

Once in, perform an update

    sudo apt update
    sudo apt full-upgrade

you may have to hit enter a few times during full-upgrade.

When starting with the lite raspi image, you will be missing the following packages, so install those.

    sudo apt install git python3-dev python3-virtualenv

Clone the [cranebot-firmware](https://github.com/nhnifong/cranebot3-firmware) repo

    git clone https://github.com/nhnifong/cranebot3-firmware.git
    cd cranebot3-firmware

You do not need to follow the instructions in the readme of that repo, as those instructions are for development. Continue with these instructions.
Follow either the anchor section or gripper section below

### Anchors

For any raspberry pi that will be part of an anchor, uncomment the `anchor` or `power anchor` line in the `server.conf` file depending on whether this anchor is the one having the power line to the gripper.

    nano server.conf

`ctrl-s` to save and `ctrl-x` to exit.

Install server

    chmod +x install.sh
    sudo ./install.sh

Open the interactive raspi config and go to "Interface Options" and "serial interface"
Disable the login shell and enable the hardware uart (no, then yes)

    sudo raspi-config

add the following line at the end of the boot config with `sudo nano /boot/firmware/config.txt`. This disables bluetooth, which would otherwise occupy the uart hardware.
Then reboot after this change

    dtoverlay=disable-bt

### Gripper

Setup for the raspberry pi in the gripper with the Inventor Hat Mini.  

Uncomment the `gripper` or line in the `server.conf`.

    nano server.conf

`ctrl-s` to save and `ctrl-x` to exit.

Install server

    chmod +x install.sh
    sudo ./install.sh

Enable i2c

    sudo raspi-config nonint do_i2c 0

Add this line to `/boot/firmware/config.txt` just under `dtparam=i2c_arm=on` and reboot

    dtparam=i2c_baudrate=400000
