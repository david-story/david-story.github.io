---
layout: pages
title:  "Stackable Embedded System"
minimal_mistakes_skin    : "dark"
---

This is a small board format that I created to make learning programming microcontrollers a little easier on myself.
Mainly, I incorporated circuits and hardware modules that I already know work well, created a standardized pin-out,
and then created a master microcontroller board that could communicate with any attached boards. This way I could
ensure that the hardware was functional, and could then focus on programming the microcontroller to interact with 
the hardware. 

### Specifications ###

#### Microcontroller Board Hardware ####
<ul style="list-style-type:square">
   <li> PIC18F45K40 (Can choose SMD or thru-hole) </li>
   <li> Sets standardized board size and pin-out format </li>
   <li> Onboard power regulation and power indication </li>
   <li> ICSP programming pinouts </li>
   <li> USB Port for power and communication (communication in development) </li>
   <li> Mounting posts for connecting multiple boards or mounting to chassis</li>
   </ul>
   
#### Microcontroller Board Hardware ####
<ul style="list-style-type:square">
   <li> 8 Programmable LEDS </li>
   <li> 1 Programmable RGB LED with PWM connection </li>
   <li> 1 DIP switch module with 6 SPST switches</li>
   <li> 1 Analog photoresistor </li>
   <li> 1 Analog potentiometer </li>
   <li> 1 Analog humidity sensor </li>
   <li> 2 Analog temperature sensors </li>
   <li> 1 Analog current sensor (up to 10A) with 2.54mm and lug outputs </li>
   </ul>
   
### Where to find ###

Eagle schematics and board files are stored in a repository.
Folders in the repository will each hold two files:

<ul style="list-style-type:square">
<li>somefile.sch - <i>this is the schematic file</i></li>
<li>somefile.brd - <i>this is the board file</i></li>
</ul>
	
Each folder will hold a different system; the main microcontroller board is under a folder aptly named 'microcontroller-board'

The files are avaliable at the following link:

<a href="https://github.com/david-story/modular-embedded-stack">Modular Embedded Stack Repository </a>

### Schematic ###

The following are the schematic images for the microcontroller board:

<figure class="one">
	<figcaption>First schematic for modular embedded stack</figcaption>
    <a href="/assets/images/project-microcontroller-schem1.png"><img src="/assets/images/project-microcontroller-schem1.png"></a>
</figure>

<figure class="one">
	<figcaption>Second schematic for modular embedded stack</figcaption>
    <a href="/assets/images/project-microcontroller-schem2.png"><img src="/assets/images/project-microcontroller-schem2.png"></a>
</figure>

### Board ###

The following is the board file with all layers for the modular embedded stack:

<figure class="one">
	<figcaption>Modular Embedded Stack Board</figcaption>
    <a href="/assets/images/project-microcontroller-board.png"><img src="/assets/images/project-microcontroller-board.png"></a>
</figure>
