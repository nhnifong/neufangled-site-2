# Gripper Build Guide

Hardware Version: Arpeggio

Print time: about 12 hours
Build time: about 2 hours

First you should have printed the parts according to the [print guide](print_guide.md)

## Tool list

 - [Mini screwdriver with a bit set](https://www.amazon.com/dp/B01KB02F9C)
 - Soldering iron with helping hands and a magnifier
 - [Cross locking tweezers](https://www.amazon.com/dp/B001BU9MLG)
 - Super glue ([loctite super glue “professional liquid”](https://www.amazon.com/dp/B07VL6MP94?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1&th=1) recommended)

## Fingers

Attach a fork to the back of a finger pad. Forks and finger pads are both symmetrical. There is no left and right finger. Insert an M3x30 bolt with M3 washers in the following four locations: after the bolt head, one on each side of the fork, and one at the end of the bolt, followed by an m3 nylock nut. Tighten the nylock nut until no slack remains, then back off until the rod can swing with no out of plane motion. Repeat for the other finger.

Slide in a geared lever into the finger assembly with it's flat face coplanar with the finger's flat flace.
Insert an M4x25 bolt through the assembly and a M4 lock nut on the other side.

If you are able to, try to get two M4 washers into the gaps as the bolt comes through. (its not necessary but reduces noise. I have found that you can use a pocket knife to push the washer in while holding it centered with an allen wrench in the hole)

Tighten and then back off just until the mechanism moves freely. Repeat with the other finger.

Locate the pressure sense connector. It is a two pin 2.54 pitch female molex plug with about 20cm of wire ends.

Select the finger with the wire channel. Feed the wires through the small hole starting at the gear and leading down towards the finger joint. Push them down the channel, till they pop out of the face near the joint, thenput them all they way through.

Place a very small piece of heat shrink on each wire.
Strip the ends of the wires, solder the pressure sense resistor to the wires in such a way that they are not twisted. there is no polarity, but there is not enough room for a twist.
Remove the adhesive backing and stick the sensor in the center of the finger pad, feeding any excess wire back through the channel.

Cover the face of the finger in adhesive backed foam and trim it to size.
When trimming the foam, you don’t have to be very precise, and it doesn't have to go exactly to the edge.

## Motors

Attach the aluminum servo horns to both motors with the included M3x6 center screw.

Snap two m3x6 screws into the finger drive gear from the sides. For this you cannot use the phillips head screws that come with the STS3215 you need to use the black hex screws that have a thinner head.

## Body Assembly

After printing, tear the ears off the mechanism lid print. Clean up the area the bridge was supporting with a sharp tool.

Attach the finger motor to the inside of mechanism_lid with four of the smallest screws included with the motors.

Insert two M4x25 bolts into the back plate from the bottom, hold them in as you place it on the table. Followed by two M4 washers.

Mesh the two geared levers together in the closed position, making sure they are aligned correctly. They must remain meshed the entire time. Use a rubber band to hold them together if necessary.  

Feed the plug of the pressure sense wire through the smile shaped slot in back_plate, and place the fingers on the bolts simultaneously, keeping them meshed, and keeping the sens wire from being pinched anywhere.

Place M4 washers over the bolts after they protrude from the fingers.

Place the mechanism lid and finger motor assembly onto the back plate, gently wiggle everything in order to get it to fit. The two M4x25 bolts should go through the holes in mechanism_lid and the drive gear should mesh with the finger gears. The alignment tabs on the sides should line up.

Insert two M4 nuts into the hexagonal holes. Tighten the bolts from behind and then back off enough that the geared levers move freely. 
Secure the lid around the edges with four M3x10 bolts

## Electronics

Unpack one Camera Module and install the 8cm mini cable. (golden one) the wide end of the mini ribbon cable plugs in the camera, with its black face on the camera’s back side. The plastic retaining clip is pulled out to loosen a ribbon cable, and pushed in to secure one.  
screw the camera to the camera mount with two M2x4 bolts in opposite corners. Make sure the ribbon is in the pictured direction.

Stick a heat sink onto a Raspberry Pi Zero 2W (with header). It goes on the black chip.

![](images/grip/image11.png){ loading=lazy, width=45% }

Press the Strinman Gripper Hat onto the raspberry pi.

Insert spacers between the two boards, and insert M3x14 through the boards and spacers. Only three corners are used since the ribbon cable is in the path of one of them.

Attach the PCBs to the camera mount in the three corners that have screw holes.

Fold the ribbon cable over as shown and insert it into the raspberry pi zero 2w's connector. Be careful it is very delicate.

Very carefully and gently pull out both sides of the black retaining clip in the Raspberry Pis ribbon cable connector. (Zoom in on the photo above to get a good look at it.) Insert the ribbon cable, black side up, under the retention clip. Push the clip back in to secure it. If the clip falls out, you can put it back in with tweezers by inserting one side at a time.

Attach the camera mount assembly to the back plate with an M3x6 countersunk screw.

Image an SD card according to the instructions in [Raspi Setup](raspi_setup.md) and insert it into the SD card slot.

Fold the two fork shaped linkages into place so their remaining holes align with the holes in the gripper body.  
Attach these with four M3x14 screws.
After connecting them all, test the movement of the gripper. If they do not move freely enough, loosen the screws a little.

Attach the rangefinder to the frame with two M2x4 screws.  
Attach the IMU to the frame with two M3x4 screws.  
Plug in the 4-pin dupont connector that has doubles coming out of it into the IMU. VCC ond the end  
Plug the 4-pin dupond connector with singles into the rangefinder. VCC on the end.  
Feed the white connector through the hole to the other side and connect it to the stemma port on the Inventor Hat Mini

## Wrist motor

Attach a bracket to the remaining motor in the pictured orientation. Secure with four of the included small tapping screws from the motor box.

Attach the three-holed helical wrist drive gear to the motor horn with two M3x6 screws.
 
Plug the pressure sense plug into the Gripper Hat at port A0. This plug does not have polarity.

Plug a three wire SPOX cable into each motor.

Plug the wrist motor into the motor port on he Gripper Hat. Leave the other motor unconnected for now.

Plug the stemma cable from the rangefinder into the Gripper hat.

## Marker Display Box

Put a 10x15x4 bearing onto the ABS tube followed by a 3/8" x 7/8" steel washer. 

Put a drop of cyanoacrylate glue onto the inside of the center hole of the remaining helical gear, and quickly press it onto the end of the ABS rod so that 6.5 mm of tube protrude. It's a very tight fit you must have a good grip on it and twist it.

Stick marker codes onto all four sizes of the marker box.
If you are printing them, This is the [sticker paper on amazon](https://www.amazon.com/dp/B092444Z49) and the [document with the marker images is here](https://docs.google.com/document/d/1B41dnssHsm1Db0LiHVgLatEv6H1jt0amIagw2v5_7dU/edit?usp=sharing). It must be printed without margins.

Put a drop of cyanoacrylate glue onto the inside of the hole in the display box and quickly jam the other end (with no bearing) of the ABS rod into it until it bottoms out. Again, it's intentionally a very tight fit and you need a good grip and a twist.

Put another steel washer on the bottom of the tube under the bearing, and holding it in place, slide the gear end of the tube into the slot in the top of the gripper until firmly seated. Press the wrist block into the opening firmly and secure with three m2.5x6 screws.

Find (or create yourself) the 75cm cable with male JST ZH plugs at both ends. Thread it into the top of the display box, down the tube, into the gripper, and out the hole on the side of the gripper. Plug the cable into the gripper hat.

## Check out tests and calibration

Find (or create yourself) the barrel jack to Female JST ZH adapter. Plug this into the wire at the top of the display box, and use one of the anchor power supplies (24V) to power on the gripper.

When the component boots it will look for wifi credentials using it's camera. Hold up a wifi share QR code to it and it should appear on your network and be detected by the control panel in under a minute.

You can generate a valid wifi share code with [qifi.org](http://qifi.org)


Find the IP or hostname of the device using your router and SSH into the pi with user `pi` and password `Fo0bar!!`

    ssh pi@<address>

Once in, stop the cranebot service and run the checkout script

    sudo systemctl stop cranebot.service
    /opt/robot/env/bin/qa-gripper-arp

This will prompt you to plug in the other motor.

At the end it prompts you to run ffplay on your host machine to verify the camera looks ok. closing the window on your host machine ends the script.
you can then run on the pi

    sudo shutdown now

and pull power when the green light goes out.

Complete! you are now in possession of one complete gripper - the most complex part of Stringman.

Proceed to the [Raspberry Pi Setup](raspi_setup.md) instructions and after that's done, there is a script in qa/gripper_eval.py that can help you confirm the gripper has been assembled correctly and you have good continuity on all conenctors. There's also a manual QA checklist in [Quality Assurance](quality_assurance.md)

![](images/grip/image82.png){ loading=lazy, width=45% }