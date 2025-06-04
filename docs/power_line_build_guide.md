# Powerline/Gantry Build Guide

Hardware Version: Pilot run

Coveres the connetion of the power line between the power anchor and gripper, gantry assembly, and tie up of the fishing lines.
This is meant to be done **before** [final installation](installation_guide.md).

Tools needed:  

 - Scissors
 - Tape measure
 - Wire strippers for 30awg
 - Lighter or heat gun for heat shrink tubing
 - Soldering station with helping hands


!!! tip "Warning"

    PLA will soften and is flammable. Direct any heat source used to shrink tubing away from it.

## Gantry

The gantry refers to a passive component that hangs where all the anchor lines meet. A fudicial marker is displayed on four sides of a hollow box. The markers have to be fairly large (10cm on a side) for the cameras several meters away to determine their position and orientation in the room.

Print the components of the gantry in a white or light colored filament with two walls and 12% cubic infill. Attach them together with four M3x4 screws. 

![](images/gantry/image10.png){ loading=lazy, width=45% }
![](images/gantry/image11.png){ loading=lazy, width=45% }

# Stickers

You should have received four copies of the “gantry_front” aruco marker on sticker paper. Cut out the stickers with a ruler and an exacto knife along the thin dotted line, which leaves a 1cm border around the marker. If you need to print the stickers again, You can find the [document here](https://docs.google.com/document/d/1uWInzjaWLs-bZ3f5-mjPZeAdHX51PbgfzJ0FCqzDZFw/edit?usp=sharing) and the [paper on amazon](https://www.amazon.com/dp/B092444Z49)

![](images/gantry/image3.png){ loading=lazy, width=45% }
![](images/gantry/image4.png){ loading=lazy, width=45% }

To more easily remove the backing, make a gentle cross cut into the corner of the backing with the knife with only enough pressure to cut the backing, but not the sticker.
Put one sticker on each face of the gantry. They must be oriented correctly. The word “gantry_front” is printed at the bottom of each. Note that the top of the gantry is the part where the second part was screwed on. Refer to this image for the correct orientation

![](images/gantry/image2.png){ loading=lazy, width=45% }

## Fishing Lines

Remove the swivels from each of the fishing speed clips and set them aside.
Put the three clips onto the keyring.

![](images/gantry/image12.png){ loading=lazy, width=45% }

Cut three 10m lengths of braided fishing line from your supply. Tie a swivel on the end of each one with a [palomar knot](https://www.animatedknots.com/palomar-knot).

![](images/gantry/image5.png){ loading=lazy, width=45% }

Tie the other end of the line to the spool on an anchor until all three of the regular anchors have lines.

TODO: add image.

## Power line

You were supplied with a custom made counter-twisted wire consisting of two 30awg conductors and some 40lb test braided fishing line.
Lay it out flat on the floor and gently shake loose any twists or kinks.

Measure 2 meters from one end and mark the point. Pull apart the fishing line from the wires at this point to make about 10cm of slack.
Tie an [alpine butterfly](https://www.animatedknots.com/alpine-butterfly-loop-knot) in the fishing line at this location. You can use the plastic screwdriver as an aid when tying the knot. This is a difficult knot, I suggest practicing first on some scrap fishing line. If you haven't bought the cross locking tweezers yet, surely this will change your mind.

![](images/gantry/image6.png){ loading=lazy, width=45% }

After you pull the knot tight, You should have a small immobile loop in the fishing line and slightly slack wires. Attach the keyring to this loop. This way, the fishing line can bear all the weight, and the wires not be stressed.

![](images/gantry/image7.png){ loading=lazy, width=45% }

Thread the 2m end of power line down through the center hole of the gantry. Pull it through till the keyring gets stopped in the cone, and then thread the 8m end out through one of the side holes.

![](images/gantry/image8.png){ loading=lazy, width=45% }
![](images/gantry/image9.png){ loading=lazy, width=45% }


### Anchor Spool Connection

Thread the long (8m) end of the power line through the back of a cover matching the configuration of anchor you installed the slip ring on.

![](images/gantry/image19.png){ loading=lazy, width=45% }

The Fishing line must take any tension in the event that the spool becomes completely unwound, so it must be tied off to the spool.
untwist back about 10 cm of fishing line. Insert the end into the small hole in the spool, such that it comes back out of the adjacent larger hole. Tie off the fishing line with a triple square knot. You may need multiple pairs of tweezers if not a $100M surgery robot.

![](images/gantry/image20.png){ loading=lazy, width=45% }
![](images/gantry/image21.png){ loading=lazy, width=45% }

Trim back the black and white wires of the powerline so that they end where the wires of the slip ring end, with just a little slack. the length should be such that the fishing line bears any tension.

![](images/gantry/image22.png){ loading=lazy, width=45% }

Prepare one narrow heat shrink tube cut in two, and one whole larger heatshrink tube. Put them onto the wires before beginning the splice.

![](images/gantry/image15.png){ loading=lazy, width=45% }

Splice both conductors. black to black, and red to whatever the other one is.

![](images/gantry/image23.png){ loading=lazy, width=45% }

Shrink the small tubes for each conductor first, then the large heat shink tube around them both.

!!! tip "Warning"

    Keep flame or heat well away from the fishing line. If you damage it with flame, even if it appears intact, cut the splice out and start over.

After completing the splice, manually wind a few turns of the powerline onto the spool in the pictured direction. 

![](images/gantry/image24.png){ loading=lazy, width=45% }

### Gripper Spool Connection

Thread the short end of the power line that comes out of the bottom of the gantry into the hole in the top of the gripper. Pushing it so it comes around the bottom of the spool and out the window. Pull out enough to work with (30cm)

![](images/gantry/image13.png){ loading=lazy, width=45% }
![](images/gantry/image14.png){ loading=lazy, width=45% }

!!! tip "Note"

    Though this step is not pictured at this time, the correct process is documented above where the power line is joined to the anchor spool.

Untwist back about 10 cm of fishing line. Insert the end into the small hole in the spool, such that it comes back out of the adjacent larger hole. Tie off the fishing line with a triple square knot. Trim back the conductors of the powerline so that they end where the wires of the slip ring end.

TODO: ADD PHOTO.

Prepare one narrow heat shrink tube cut in two, and one whole larger heatshrink tube. Put them onto the wires before beginning the splice.

![](images/gantry/image15.png){ loading=lazy, width=45% }

Splice both conductors. black to black, and red to whatever the other one is.

![](images/gantry/image16.png){ loading=lazy, width=45% }

Shrink the small tubes for each conductor first, then the large heat shink tube around them both. Image incorrectly pictures the fishing line not tied off the spool.

![](images/gantry/image17.png){ loading=lazy, width=45% }

Pull the excess line out of the top of the gripper, but not so much that you pull the splice through. we will take up the slack later, when we can turn the gripper on.

![](images/gantry/image18.png){ loading=lazy, width=45% }

Plug in the power anchor. This should now deliver power to the gripper as well. Confirm the green light on the raspberry pi comes on. If not, check for 24v on the input terminals of the larger buck converter on the gripper.

You should already have installed the software on it in the [Raspberry Pi Setup](raspi_setup.md) Guide, but if you have not, do that now. If it is installed, it starts at boot. Start the control panel on your PC and wait for the gripper to connect.

Click on the gripper, and select `Manual Spool Control`.
Reel the spool in with the `up arrow` key and take up enough slack that you only have about 0.5m of line remaining between the gripper and gantry.

![](images/gantry/image25.png){ loading=lazy, width=45% }
![](images/gantry/image26.png){ loading=lazy, width=45% }
![](images/gantry/image27.png){ loading=lazy, width=45% }


Install the gripper's shell. The half with the slanted line inside goes on the side of the gripper with the slanted motor.
The bottom edge of each shell half fits along the features of the gripper frame. press it down firmly.
Secure the shells at the top with four M3x4 screws.

![](images/gantry/image28.png){ loading=lazy, width=45% }
![](images/gantry/image29.png){ loading=lazy, width=45% }
![](images/gantry/image30.png){ loading=lazy, width=45% }

Assembly is complete! Congratulations! Move on to the Installation Guide when you're ready to hang it up.

### [Insallation guide](installation_guide.md)