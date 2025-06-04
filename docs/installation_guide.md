# Final Installation Guide

Hardware Version: Pilot run

Hardware installation of a preassembled or diy assembled Stringman robot.

Tools needed:  

 - Step ladder
 - Handheld drill/driver

Hanging the robot in the room where it will operate involves installing an anchor in each corner, and attaching each of the three support lines to the gantry. support lines refer to the fishing line, while power line refers to the conductor.

## Anchor installation

Start with the three support anchors. You will have received or assembled corner or flat variants appropriate your space.
Installation only differs in how they look and where the screws are. 

Partially install the wood screws into every open screw hole in every anchor until the point just protrudes from the back.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image5.png){ loading=lazy, width=45% }

=== "Corner"
    
    Hold the anchor securely in the corner with about 2cm of clearance to the ceiling, or to the moulding. Don't push it right up against the moulding as you need space for the cover. Drive in every screw.

    ![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image6.png){ loading=lazy, width=45% }
    
	!!! note "Note"
	    The corners of walls in typical "stick framed" american houses will have at least one 2x4 in the corner on one side or the other. However, there are cases when two interior walls meet in a cross where the corner may be hollow. If you believe there is no stud in the corner somehow, you either need to install a backer board connected to the nearest studs, or select a flat anchor variant for that corner and pick a nearby stud.
        
	    If you think you are in a building with steel or aluminum framing, please consult a professional. it is probably possible to bolt the anchor to the stud with the right hardware.
    
	Thread the line through the hole at the bottom of the cover from the inside to the outside.

	![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image7.png){ loading=lazy, width=45% }
    
	Snap on the cover. Secure it at the bottom with an M2.5x6 screw.

	![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image8.png){ loading=lazy, width=45% }

=== "Flat"	
    
    When installing a flat wall anchor, confirm the camera would point towards the center of the work area.  
    Find a stud in the wall near the installation spot. I prefer to use neodymium magnets to locate the drywall scews.
    
    Hold the anchor securely onto the wall with the screw holes aligned to the stud and about 2cm of clearance to the ceiling, or to the moulding. Don't push it right up against the moulding as you need space for the cover. Drive in every screw.

    ![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image1.png){ loading=lazy, width=45% }
    
	Thread the line through the hole at the bottom of the cover from the inside to the outside.
	Sorry about the yellow. I ran out of white.

	![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image2.png){ loading=lazy, width=45% }
    
	Snap on the cover. Secure it at the bottom with an M2.5x6 screw.

	![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image3.png){ loading=lazy, width=45% }
	![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image4.png){ loading=lazy, width=45% }

Plug in the anchor via one of the provided outlet remotes. The outlet remote serves as a low tech kill switch that's immune to software bugs, and serves as your main power on/off switch since the Pilot version has no global sleep mode.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image9.png){ loading=lazy, width=45% }

## Power Anchor

For the power anchor the cover will already have been threaded onto the wire. If it is snapped on already, remove it and slide it down the wire. Gently unspool a few meters of wire so the gantry and gripper can lay on the floor in the center of the room while you install the anchor. Drive in the screws as before, and snap the cover back on and secure it with the M2.5x6 screw.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image10.png){ loading=lazy, width=45% }

## Tie up

Lay the gripper, gantry, and power wire on the floor in the center of the room. with the gantry oriented so the power line goes straight out towards the anchor and isn't wrapped around anything.

Gently pull out enough line from each anchor to reach the gantry. If you feel bumping while pulling out line, this is normal. It is an electrical phenomenon involving the stepper driver.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image11.png){ loading=lazy, width=45% }

Hook each eyelet to the corresponding hook on the gantry.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image12.png){ loading=lazy, width=45% }
![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image13.png){ loading=lazy, width=45% }

Power on all the anchors using the "all on" button on your outlet remote. Open the [control panel](usage_guide.md), and select "Auto tension" from the main menu.

### Learn when to use the kill switch

The "all off" button on the outlet remote serves as a low tech kill switch that turns off all the motorized components.
It is best to keep the outlet remote in the same place at all times, and circle the "all off" button with a red sharpie. You could mount it to the wall or the desk for example. That way you don't have to think too hard in the event that you need to hit that button.

![](https://bucket-neu-2.s3.us-east-1.amazonaws.com/images/install/image14.png){ loading=lazy, width=45% }

"Auto tension" reels in each line until some tension is detected. If a line gets tight but doesn't stop reeling gently tug on it. If that doesn't stop it, hit the "STOP" button in the control panel. The stop button in software commands the motors to keep their current length but doesn't turn anything off. **If for some reason motors are still moving** after this, hit the "all off" button on the outlet remote. You may need to repeat the tension calibration steps for the misbehaving motor.

Hit the kill switch **if the gantry gets too high and the lines are getting too tight**, or if you hear a rising "tink tink" sound. Its a dangerous situation that can quickly lead to something breaking. If this happens it is usually a sign that calibration needs to be improved, but can also becaused by anchor_server.py crashing while reeling in.

Hit the kill switch **if someone becomes entangled in the lines**. But if you can't reach it, You can pull on them till you overpower the motors, which only takes a few kg of force, If any motor is overpowered, the whole system stops.
If this ever happens, please let me know of the circumstances so I can try to prevent it.

Both the hardware and software of this system are released AS IS without warranty. See the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) For more detail.