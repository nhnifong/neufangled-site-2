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

Once in, perform an update and install necessary dependencies

    sudo apt update -y && sudo apt full-upgrade -y -o Dpkg::Options::="--force-confold" && sudo apt install -y git python3-dev python3-virtualenv rpicam-apps

Clone the [cranebot-firmware](https://github.com/nhnifong/cranebot3-firmware) repo

    git clone https://github.com/nhnifong/cranebot3-firmware.git && cd cranebot3-firmware    

You do not need to follow the instructions in the readme of that repo, as those instructions are for development. Continue with these instructions.
Follow **either** the anchor section or gripper section below

### Anchors

For the power anchor, uncomment th `power anchor` line in the `server.conf` file and comment out the `anchor` line.

    nano server.conf

`ctrl-s` to save and `ctrl-x` to exit.

Open the interactive raspi config and go to "Interface Options" and "serial interface"
Disable the login shell and enable the hardware uart (no, then yes)

    sudo raspi-config

Execute the following command to add a line at the end of `/boot/firmware/config.txt` that disables bluetooth, which would otherwise occupy the uart hardware.

    echo "dtoverlay=disable-bt" | sudo tee -a /boot/firmware/config.txt

### Gripper

Setup for the raspberry pi in the gripper with the Inventor Hat Mini.  

Uncomment the `gripper` or line in the `server.conf`.

    nano server.conf

`ctrl-s` to save and `ctrl-x` to exit.

Disable the hardware i2c while replacing it with a software I2C at a 100khz. This is for compatibility with the BNO085.

    sudo raspi-config nonint do_i2c 1 && echo "dtoverlay=i2c-gpio,bus=1,i2c_gpio_sda=2,i2c_gpio_scl=3,i2c_gpio_delay_us=2" | sudo tee -a /boot/firmware/config.txt


### Common instructions

Install server

    chmod +x install.sh
    sudo ./install.sh


#### QA scripts

Note that if you are proceeding to QA scripts you must reboot and then stop the service before running those scrips.

    sudo reboot now

log back in

    sudo systemctl stop cranebot.service

### Updates

At this time there are no packaged releases, only github

    git switch pilot
    git pull
    source venv/bin/activate
    pip install -r requirements_raspi.txt
    sudo systemctl restart cranebot.service

### Setting a different wifi network

Insert the Micro SD card from a robot component in your PC. Confirm it is mounted at /media/$USER/rootfs
run the following command from the cranebot3-firmware repo

    sudo ./add_wifi_config.sh "SSID" "password"

repeat this for the SD card from every component.