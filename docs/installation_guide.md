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

![](images/install/image5.png){ loading=lazy, width=45% }

Remove the anchor's white cover by pulling up on the large flat face to release the tabs, then pull it straight off the front. Another way if it feels stuck is, after getting the tabs loose, hold the cover and give the whole thing one large shake so the anchor falls in your lap and you're holding the empty cover.

The cover should be prevented from falling because the line or wire is threaded through the face hole with a fishing swivel tied on the other side. Let it dangle a foot or so below the anchor as your mount it.

=== "Corner"

    Hold the anchor securely in the corner with about 2cm of clearance to the ceiling, or to the moulding. Don't push it right up against the moulding as you need space above the top for the cover. Drive in every screw.
    
    ![](images/install/image6.png){ loading=lazy, width=45% }
    
	!!! note "Note"
	    The corners of walls in typical "stick framed" american houses will have at least one 2x4 in the corner on one side or the other. However, there are cases when two interior walls meet in a cross where the corner may be hollow. If you believe there is no stud in the corner, you either need to install a backer board connected to the nearest studs, or select a flat anchor variant for that corner and pick a nearby stud.
        
	    If you think you are in a building with steel or aluminum framing, please consult a professional. it is probably possible to bolt the anchor to the stud with the right hardware.
    
    
	![](images/install/image7.png){ loading=lazy, width=45% }
    
	While holding the line tight so it can't get pinched in the body somewhere, Snap on the cover. Push it straight on hard so both tabs at the top click into place. Secure it at the bottom with an M2.5x6 screw.
    
	![](images/install/image8.png){ loading=lazy, width=45% }

=== "Flat"	
    
    When installing a flat wall anchor, confirm the camera would point towards the center of the work area.  
    Find a stud in the wall near the installation spot. I prefer to use neodymium magnets to locate the drywall scews.
    
    Hold the anchor securely onto the wall with the screw holes aligned to the stud and about 2cm of clearance to the ceiling, or to the moulding. Don't push it right up against the moulding as you need space for the cover. Drive in every screw.
    
    ![](images/install/image1.png){ loading=lazy, width=45% }
	![](images/install/image2.png){ loading=lazy, width=45% }
    
	While holding the line tight so it can't get pinched in the body somewhere, Snap on the cover. Push it straight on hard so both tabs at the top click into place. Secure it at the bottom with an M2.5x6 screw.
    
	![](images/install/image3.png){ loading=lazy, width=45% }
	![](images/install/image4.png){ loading=lazy, width=45% }

Plug in the anchor via one of the provided outlet remotes. The outlet remote serves as a low tech kill switch that's immune to software bugs, and serves as your main power on/off switch since the Pilot version has no global sleep mode.

![](images/install/image9.png){ loading=lazy, width=45% }

## Power Anchor

For the power anchor the cover will already have been threaded onto the wire. If it is snapped on already, remove it and slide it down the wire. Gently unspool a few meters of wire so the gantry and gripper can lay on the floor in the center of the room while you install the anchor. Drive in the screws as before, and snap the cover back on and secure it with the M2.5x6 screw.

![](images/install/image10.png){ loading=lazy, width=45% }

## Attach the gripper and gantry

(when buying an assembled robot, the gantry should come pre-attached to the gripper)

Your gripper needs a wire tail coming out of the hole in the center at the top with about 50cm of slack.

!!! note "Note"

    If you don't have enough slack, don't just yank out more wire. the winch servo has too much resistance and you could damage the wire. the only safe way to do it is to command the spool motor to move, but since the gripper is unpowered, you'd have to either use a servo tester to control only that servo, or power the gripper with aligator clips from a 9-24v supply. (a 9v battery may even be just enough for this)

Thread all three components of this wire tail (GND, V++, and fishing line) up through the center hole in the gantry. pull up by the fishing line so that 20 cm of tail is above the hole.

Tie a fishing swivel onto this fishing line with a palomar knot. this swivel should not be able to pass back through the hole.

## Tie up

Lay the gripper and gantry on the floor in the center of the room. Ensure all anchors are powred off. Pull all four lines slowly out of the anchors until their ends reach the gantry. If you feel bumping while pulling out line, this is normal. It is an electrical phenomenon involving the stepper driver, and it is harmless.

![](images/install/image11.png){ loading=lazy, width=45% }

Hook each eyelet to the corresponding hook on the gantry.

![](images/install/image12.png){ loading=lazy, width=45% }
![](images/install/image13.png){ loading=lazy, width=45% }

Connect the conductors from the gripper to the conductors from the power wire. the conductors can either pass over the top of the gantry or through the hole with the fishing line, it does not matter as long as they are slack. the fishing lines should bear all the weight.

Power on all the anchors using the "all on" button on your outlet remote. Open the [control panel](usage_guide.md). Wait for all components to be discovered, connected, and for video to come online. Select "Auto tension" from the main menu.

Select the "Full Auto Calibration" option from the main menu.

After calibration, you can move the robot around with a gamepad or the keyboard.

### Learn when to use the kill switch

The "all off" button on the outlet remote serves as a low tech kill switch that turns off all the motorized components.
It is best to keep the outlet remote in the same place at all times, and circle the "all off" button with a red sharpie. You could mount it to the wall or the desk for example. That way you don't have to think too hard in the event that you need to hit that button.

![](images/install/image14.png){ loading=lazy, width=45% }

"Auto tension" reels in each line until some tension is detected. If a line gets tight but doesn't stop reeling gently tug on it. If that doesn't stop it, hit the "STOP" button in the control panel. The stop button in software commands the motors to keep their current length but doesn't turn anything off. **If for some reason motors are still moving** after this, hit the "all off" button on the outlet remote. You may need to repeat the tension calibration steps for the misbehaving motor.

Hit the kill switch **if the gantry gets too high and the lines are getting too tight**, or if you hear a rising "tink tink" sound. Its a dangerous situation that can quickly lead to something breaking. If this happens it is usually a sign that calibration needs to be improved, but can also becaused by anchor_server.py crashing while reeling in.

Hit the kill switch **if someone becomes entangled in the lines**. But if you can't reach it, You can pull on them till you overpower the motors, which only takes a few kg of force, If any motor is overpowered, the whole system stops.
If this ever happens, please let me know of the circumstances so I can try to prevent it.

Both the hardware and software of this system are released AS IS without warranty. See the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) For more detail.