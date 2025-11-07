# Final Installation Guide

Hardware Version: Pilot run

Hardware installation of a preassembled or diy assembled Stringman robot.

Tools needed:  

 - Step ladder
 - Handheld drill/driver

Hanging the robot in the room where it will operate involves installing an anchor in each corner, and attaching each of the four support lines to the gantry. Power is delivered to the gripper by plugging in the jst connector at the end of the power anchor's line.

## Anchor installation

You will have received or assembled corner or flat anchor variants appropriate your space.
Installation only differs in how they look and where the screws are.

Partially install the wood screws into every open screw hole in every anchor until the point just protrudes from the back.

![](images/install/image5.png){ loading=lazy, width=45% }

Remove the anchor's white cover by unscrewing the silver screw on the bottom if it is present, you can back it halfway out. The pull up on the large flat face to release the tabs, then pull it straight off the front. Another way if it feels stuck is, after getting the tabs loose, hold the cover and give the whole thing one large shake so the anchor falls in your lap and you're holding the empty cover.

The cover should be prevented from falling because the line or wire is threaded through the face hole with a fishing swivel tied on the other side. Gently pull this out so you have enough space and let it dangle a foot or so below the anchor as your mount it.

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

## Tie up

Lay the gripper and gantry on the floor in the center of the room. Ensure all anchors are powred off. Pull all four lines slowly out of the anchors until their ends reach the gantry. If you feel bumping while pulling out line, this is normal. It is an electrical phenomenon involving the stepper driver, and it is harmless.

![](images/install/image11.png){ loading=lazy, width=45% }

Thread each eyelet into the closest hole in the side of the gantry and clip it onto one of the speed clips. Do not cross lines.

![](images/install/image12.png){ loading=lazy, width=45% }
![](images/install/image13.png){ loading=lazy, width=45% }

Plug the gripper's JST connector into the one on the power wire. the conductors can either pass over the top of the gantry or through the hole with the fishing line, it does not matter as long as they are slack. the fishing lines should bear all the weight.

Power on all the anchors using the "all on" button on your outlet remote. Open the [control panel](usage_guide.md). Wait for all components to be discovered, connected, and for video to come online. Select "Auto tension" from the main menu.

Lay the full page "origin" marker in the center of the room, aligned with your walls.

Select the "Full Auto Calibration" option from the main menu.

After calibration, you can move the robot around with a gamepad or the keyboard.

### Learn when to use the kill switch

The "all off" button on the outlet remote serves as a low tech kill switch that turns off all the motorized components.
Usually, without power the gripper slowly falls until it touches the floor.
It is best to keep the outlet remote in the same place at all times, and circle the "all off" button with red sharpie or nail polish. You could mount it to the wall or the desk for example. That way you don't have to think too hard in the event that you need to hit that button.

![](images/install/image14.png){ loading=lazy, width=45% }

"Auto tension" reels in each line until some tension is detected. If a line gets tight but doesn't stop reeling gently tug on it. If that doesn't stop it, hit the "STOP" button in the control panel. The stop button in software commands the motors to keep their current length but doesn't turn anything off. **If for some reason motors are still moving** after this, hit the "all off" button on the outlet remote. You may need to repeat the tension calibration steps for the misbehaving motor.

Hit the kill switch **if the gantry gets too high and the lines are getting too tight**, or if you hear a rising "tink tink" sound. Its a dangerous situation that can quickly lead to something breaking. If this happens it is usually a sign that calibration needs to be improved, but can also becaused by anchor_server.py crashing while reeling in.

Hit the kill switch **if someone becomes entangled in the lines**. But if you can't reach it, You can pull on them till you overpower the motors, which only takes a few kg of force, If any motor is overpowered, the whole system stops.
If this ever happens, please let me know of the circumstances so I can try to prevent it.

Both the hardware and software of this system are released AS IS without warranty. See the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) For more detail.