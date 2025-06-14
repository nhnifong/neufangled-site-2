# Anchor Build Guide

Hardware Version: Pilot run

Build time: about 45 minutes per anchor.

A complete robot consists of fours anchors, a gantry, and a gripper.
First you should have printed the parts according to the [print guide](print_guide.md)

## Tool list

 - [Mini screwdriver with a bit set](https://www.amazon.com/dp/B01KB02F9C)  
 - Soldering station
 - [Cross locking tweezers](https://www.amazon.com/dp/B001BU9MLG) *Mandatory* you'll jump off a bridge without them.  
 - [Mini side cutters](https://www.amazon.com/dp/B00FZPDG1K)  
 - Super glue ([loctite super glue “professional liquid”](https://www.amazon.com/dp/B07VL6MP94?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1) recommended)


Print the long hexagonal screwdriver bit holder. You will need a brim when printing it. Most precision screwdrivers come with a set of bits with 4mm hex shanks. This is designed to fit those but be long enough to be held in a drill from the outside of this frame.

![](images/ag/image4.png){ loading=lazy, width=45% }

Glue the two sides of the spool together with the grooved wheel on the outside. Use small dabs of superglue around the ‘shelf’ on the spool where the solvent would be able to evaporate more easily.

![](images/ag/image16.png){ loading=lazy, width=45% }
![](images/ag/image33.png){ loading=lazy, width=45% }

Once the glue is dry enough to handle, press a 4x14mm steel tube into one of the 4x13x5 bearings so one end is flush.
Place two M4 washers onto the tube and press this into the hole on the grooved wheel side of the spool.

![](images/ag/image21.png){ loading=lazy, width=45% }
![](images/ag/image10.png){ loading=lazy, width=45% }

Cut away the sacreficial bridge from this U-shaped region in the frame.  

![](images/ag/image15.png){ loading=lazy, width=45% }

### Noise Dampening

Insert four rubber noise dampeners into the four motor screw holes as show, so that the thicker end is pointed outwards.

![](images/ag/image25.png){ loading=lazy, width=45% }

Cut out a square piece of adhesive foam grip tape and an 8mm wide strip of tape and stick them in the pictured locations.
These serve to prevent the motor from making rigid contact with the frame. If it makes rigid contact the robot gets loud because the frame and wall act like a speaker.

![](images/ag/image32.png){ loading=lazy, width=45% }


## Spool installation

Press a bearing into the pictured hole in the narrow rib. Make it flush with both sides.

![](images/ag/image24.png){ loading=lazy, width=45% }

Insert all four M3x10 motors screws in their holes. It’s a bit harder to insert them later, but still possible.

![](images/ag/image36.png){ loading=lazy, width=45% }

Insert an M4x12 screw into the bearing that is pressed into the frame. Place two M4 washers onto it on the inside of the rib.
Now you have to get through the fiddly step of installing the spool without these two washers falling off. they are important. without that spacing, the spool can touch the frame, and that makes noise. you will need to pull the screw back as pictured.

![](images/ag/image8.png){ loading=lazy, width=45% }
![](images/ag/image12.png){ loading=lazy, width=45% }

Place the belt onto the spoo, then slide the spool into place on the frame. The spool’s grooves side faces the thick rib. Slide the bearing down the slot, while pressing the M4x12 screw on the other side in so the washers don't fall off. when the bearing is fully seated and the spool is straight, the M4 screw will fit into the hole on the flat side of the spool. Screw it in using the printed screwdriver and an appropriately size hex driver.


![](images/ag/image37.png){ loading=lazy, width=45% }
![](images/ag/image38.png){ loading=lazy, width=45% }
![](images/ag/image39.png){ loading=lazy, width=45% }
![](images/ag/image40.png){ loading=lazy, width=45% }

That was the hardest step, it’s downhill from here.  
Press the bearing retainer into the void that remains in the tick rib, and secure it with the flat head M3x6 screw.

![](images/ag/image41.png){ loading=lazy, width=45% }

##  Motor installation

!!! note "Extra motor setup if you did not buy the hardware kit"
    If you purchased your motors elsewhere you may need to perform some additional steps.

    1. Install the short 4-wire jumper of the MKS\_SERVO42C between the board and stepper. There is only one way it will fit.
    2. Connect the motor to 24v power
    3. Perform motor self calibration with a bare shaft
    4. Set the mode to UART
    5. Set the uart baud to 38400

If you bought the hardware kit from us, those steps were performed before the motor was packed, though it can't hurt to confirm the settings.

When handling the motor be careful not to ever place it on the PCB. the three buttons can break off.  
Install a 20 tooth aluminum pully wheel on the shaft. tighten both set screws. Make it flush with the end of the shaft for now.

![](images/ag/image28.png){ loading=lazy, width=45% }

Work the belt over the pully wheel with a tool and install the motor with the larger connector facing downwards. (down is the narrower end of the frame.) Tighten the screws by using the printed screwdriver and the holes in the frame and spool to access the screws.

![](images/ag/image3.png){ loading=lazy, width=45% }
![](images/ag/image14.png){ loading=lazy, width=45% }

There is a cutaway on the top face from which you can more easily access the pully wheel set screw with an allen wrench.
Loosen the set screws on the aluminum wheel and adjust it's depth until the wheel runs as quietly as possible. Retighten. 

![](images/ag/image19.png){ loading=lazy, width=45% }

Spin your spool slowly and confirm it makes a full rotation without excessive friction. If you feel bumps only when moving fast, ignore that, it’s an electrical effect.

![](images/ag/image17.png){ loading=lazy, width=45% }

## For power anchors only

**One** of the anchors in your robot needs to supply power to the gripper. It doesn’t matter which one, but you need to install slip ring at this point before too many other things get in the way.
Power is supplied to the gripper via a wire that takes the place of the fishing line, and is transferred via a slip ring at each end.  
Take a slip ring and identify the wires that come out of the rotor. Insert these two wires into the metal tube that leads into the center of the spool.

![](images/ag/image46.png){ loading=lazy, width=45% }

Wiggle and push the wires until they come out of the outlet in the spool’s center. Pull them the rest of the way through. Seat the slip ring in its place and secure it with three M3x4 screws.  
Leave the wires that come out of the spool center hanging for now.

![](images/ag/image47.png){ loading=lazy, width=45% }
![](images/ag/image48.png){ loading=lazy, width=45% }

## Power supply circuit

Screw a nut onto the DC barrel Jack. (it should come pre-installed, but may fall off in shipping. It’s important this is done before the wiring.

![](images/ag/image22.png){ loading=lazy, width=45% }

Get one small DC step down converter from your kit (the green one).
Cut two 2.5cm pieces of 28 guage wire or similar and solder them to GND and IN+

![](images/ag/image27.png){ loading=lazy, width=45% }
![](images/ag/image42.png){ loading=lazy, width=45% }

Locate the long cable that came with the MKS\_SERVO42C. It has two different ends that are mirrors of each other. If you use the end that matches this photo, VIN and GND will be red and black. Cut short all but the power and ground wires. We will not be using the others.  

![](images/ag/image43.png){ loading=lazy, width=45% }

Solder the black and red leads also to the barrel jack. (it’s long leg is negative) The motor will receive 24v from this connector.  
At the same time, connect the step down regulator’s inputs to the 24v of the jack.

![](images/ag/image44.png){ loading=lazy, width=45% }

Find one of the pre-made anchor connectors.. The only two hanging wires on these should be the red and the black coming from the 4-pin connector. Solder these to the **output** of the DC step down converter. The converter has only on ground terminal to be used for both input and output, so you may have to solder one of the ground wires by just sticking it to the side of the other.

![](images/ag/image50.png){ loading=lazy, width=45% }
![](images/ag/image26.png){ loading=lazy, width=45% }

Place this wiring harness into the frame as shown. Feed the 4-pin connector into the oval shaped hole. Push the barrel jack into the U shaped recess and tighten the nut.

![](images/ag/image35.png){ loading=lazy, width=45% }
![](images/ag/image9.png){ loading=lazy, width=45% }

Plug the wide connector into the motor.
Plug the small connector into the pins just next to the wide connector, with the orange wire on the pin at the edge of the board.

![](images/ag/image45.png){ loading=lazy, width=45% }

### Power Anchor

If this is the power anchor, (the one with a slip ring installed) connect the input side of the slip ring to 24v power.
Be sure to use a stripper suitable for such a small guage of wire

![](images/ag/image49.png){ loading=lazy, width=45% }

## Raspberry Pi installation

Use the [raspberry pi sd card imager tool](https://www.raspberrypi.com/software/) to create a card that is pre configured with your wifi password, ssh turned on, and a username you can login with. See [Raspberry Pi Setup](raspi_setup.md) for more detail. You can also do this later.  
Setting “pi” as the username and password is standard practice for people who know that real security is only possible if you throw all the electronics in the lake

Insert the SD card into the Raspberry Pi Zero 2 W. Install an aluminum heatsink on the SOC.  
Solder a 4 pin straight header on the pins shown in the image, protruding from the back.

![](images/ag/image23.png){ loading=lazy, width=45% }

!!! tip "Note"

    The 4-pin header's long end should come out of the *back* of the Raspberry Pi Zero 2W

Screw the raspberry pi down to the frame with four m 2.5 x 4 screws. Note the direction in the photo

![](images/ag/image5.png){ loading=lazy, width=45% }

From the back, feed the 4 pin plug to the straight header and connect it with the V+ (red) wire closest to the SD card.

![](images/ag/image7.png){ loading=lazy, width=45% }

Open the Raspberry Pi camera Module 3\. Take care to ground yourself before handling the camera.   
Take out the “mini” ribbon and connect its wide end to the camera. The black painted side of the ribbon goes towards the back side of the PCB and the gold plated side goes towards the camera lens.  
To attach a ribbon cable, gently pull out both sides of the plastic retaining clip, insert the ribbon end, and push the retainer back into place.  
Discard any other ribbons that shipped with the camera.

![](images/ag/image13.png){ loading=lazy, width=45% }
![](images/ag/image34.png){ loading=lazy, width=45% }

Mount the camera with two M2x4 screws with the ribbon facing upwards.

Fold the ribbon back and forth to fit it entirely inside the frame and connect it to the raspberry pi with the black face up.  
Be careful with the raspberry pi’s ribbon cable retention clip, it is extremely delicate.

![](images/ag/image20.png){ loading=lazy, width=45% }
![](images/ag/imag11.png){ loading=lazy, width=45% }

Assembly is complete\!  
Plug in your unit to 24v power and confirm both the motor control screen and raspi green light are on.  
(Do not run motor calibration, it has been done already and can only be done with a bare shaft)  
Proceed with all the raspberry pi software setup now before continuing with the rest of the physical installation.
