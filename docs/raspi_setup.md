# Raspberry Pi Setup

To be performed for each robot component (four anchors and one gripper)
If you purchased a fully assembled robot you do not need to do this.

## For pre-imaged cards

When the component boots it will look for wifi credentials using it's camera. Hold up a wifi share QR code to it and it should appear on your network and be detected by the control panel in under a minute.

You can generate a valid wifi share code with [qifi.org](http://qifi.org)

## Image SD card

Download the [Raspiberry Pi Imager](https://www.raspberrypi.com/software/)

Insert a MicroSD card and open the imager.  

For device, select `Raspberry Pi Zero 2 W`  
![](images/raspi/image1.png){ loading=lazy, width=45% }

Download the [Stringman Raspberry Pi Image](https://storage.googleapis.com/stringman-models/stringman-zero2w.img) (1.6 GB)
For operating system, select custom image and use the downloaded file.
![](images/raspi/image2.png){ loading=lazy, width=45% }
![](images/raspi/image3.png){ loading=lazy, width=45% }

Click `Next` and then select the SD card you would like to flash.

![](images/raspi/image4.png){ loading=lazy, width=45% }

Click `Write` and confirm. When the image is finished, insert it into the raspberry pi of the stringman component and boot.

Configure the wifi with a share code according to the structions in the section above.

### Updates

At this time it is only possible to update by logging into each component

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