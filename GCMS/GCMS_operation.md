Protocol for operating Shimadzu GCMS-QP2010
===============================================================================

## Authorship

Ashley Campbell, Chantal Koechli, Nick Youngblut and Sam Barnett (2016)

Updated 2021, 2022 by Cassi Wattenburger (more detail, maintenance notes)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

***

# Equipment/materials

* GCMS: Shimadzu GCMS-QP2010
* Autosampler: Shimadzu AOC-5000 Auto Injector
* Septa: Thermolite Shimadzu Plug (Restek, Cat# 27154)
* Split liner: 3.5mm x 5.0 x 95 (Restek, Cat# 22284)
* Deactivated fused silica

***

# GCMS start up

## WARNINGS:

* You should not need to start the floor vacuum pump (rotory pump) manually.
This can be done using the GCMS software.  

## Procedure:

### Prior to start up:
1. Change carrier gas tank if low (~500 PSI, easier to do when GCMS is off)
	* See protocol to change carrier gas tank below but skip turning off the flow control step

1. Change oil if low or old
	* With the GCMS off, open the front-most "oil" cap and poor fresh oil in to about 3/4 full
	* If the oil is not clear in color, drain by disconnecting the rotary pump from the vacuum line, elevating, and draining the oil from the opening at the bottom-front
	
3. Change the glass insert if it has exceeded 1000 uses
	* Best done when GCMS is off
	* See protocol to change the glass insert below

4. Change the septum if it has exceeded 100 uses
	* See protocol for changing the septum below

### Turn equipment on

1. Turn on carrier gas (should be Helium)
	* The PSI on the left gauge should be ~100
1. Turn on Shimadzu AOC-5000 Auto Injector (switch on power unit in back)
1. Turn on computer
1. Turn on  the GC (switch in front)
1. Turn on the MS (switch in back)
1. Start the __GCMS Real Time Analysis software__
	* If hardware connection error, on GC press FUNC button > GC Configuration > Configuration Parameters > Protocol = Level 3 & Baud Rate = 57600 > Apply

### The next steps are done in GCMS Real Time Analysis software

1. From top screen, select __Instrument > Vacuum Control > Advanced__ 
1. Manual startup
	* Manual startup provides more control, option for safety checks, and may produce less wear and tear.
	* Manual startup procedure:
		1. Turn on flow controller
		1. Turn on GC system
    	1. Close vent valve (may already be closed)
	    1. Turn on rotory pump
			* Let the pressure drop to <3.1 pascals (in reality it only reaches about 5.8 pascals)
			* This takes over 30 minutes 
	    1. AFTER pressure is <3.1 pascals (or <5.8) and stabilizes: turn on the turbo molecular pump
			* __Note:__ A sound resembling a jet engine is normal, 
			as long as it only lasts < a minute
			* Wait for vacuum to return and stabilize before moving on
	    1. Turn on ion source heater
			* GC and MS indicators in top right of screen should soon say 'ready'
	    1. Wait at least 24 hours before running samples on GCMS
			* This allows for any contaminating air in system to be purged
1. Run leak check procedure (pg. 19 operation guide)
1. Run GCMS tuning proceedure (see below)
1. Load a method or create a new method
	* Make sure that GC and MS are heating up to the method's specified temps
	* A batch file can then be created if needed

 OR 
 
 1. Auto-startup
	 2. Click Auto-startup and wait for the progress bar to read "Complete".

***

# GCMS tuning

## WARNINGS:

* If the GCMS has not been used in a long time (e.g., a year), wait ~1 day prior to tuning.
	* This wait provides time for the column to be purged of contaminants.

## Procedure:

Follow procedure starting on Page 21 of the GCMS-QP2010 Operation Guide. Perform a leak check 


1. Open GCMS Real Time Analysis software 
1. On left hand side bar, click Tuning icon
1. Click Auto Tuning Condition icon
1. Under Target Conditions tab, select:
	* Adjust Resolution 
	* Adjust Sensitivity
	* Calibrate Mass Number
1. Click Start Auto Tuning
1. Once auto tuning is complete select File > Save Tuning File As
	* Save tuning file in GCMSsoltuons/system/Tune1
	* Save tuning file as yymmdd_UID (ex: 160920_seb369)
1. Compare tuning results to expected

***

# GCMS sample processing

## Procedure:

* Follow procedure for Continuous Analysis outlined on on pages 169-187 of GCMS-QP2010 System User's Guide

1. Create batch file
	* Reuse/alter a previous batch file especially if standards will be the same or use Batch Table Wizard to create new file
	* Make sure to use methods file specific for your test
	* Make sure to use the most recent tuning file (see GCMS Tuning above)
1. Save batch file to new folder specific for this run
	* Must have a new file for each subsequent runs, even if you are running a time series
1. Copy and paste methods file specified in you batch file into your new run folder
	* If methods file is not in the same folder as the batch file, your samples will not be run
1. Once you double check your batch file click start to start the run
1. If you need to stop the run for any reason, click pause or stop
1. During run, check carrier gas levels (on He tank) to make sure it does not run out due to any leaks
1. Once run is complete, save data to your run folder

***

### Changing the septum on the injection port while GCMS is on
1. For each run (or after 100 punctures) replace septa on injection port
	* This must be done quickly as carrier gas flow must be stopped
	* It may be easier to remove grill from top of GCMS in case you drop one of the small parts
	* Use work gloves while replacing septa as the injection port is VERY HOT and skin oils will interfere with the GCMS!!!
	* Septa replacement
		1. Open Instrument > Vacuum Control > advanced
		1. Turn off flow controller to stop flow of carrier gas
		1. With work gloves unscrew metal sealing cover
		1. Remove T-shaped adapter (easiest to do with tweezers so you don't drop it)
		1. With tweezers remove old septa and place in "Used Septa" jar
		1. With tweezers place new septa in hole being careful not to deform or puncture septa
		1. Carefully place T-shaped adaptor on top of septa
		1. Screw metal sealing cover back on
			* Be sure not to tighten too hard as this may deform septa and result in leaks or easy coring
		1. Restart flow controller
		1. Reset septa consumables by double clicking septa icon on right hand toolbar, clicking "Reset Consumables" and clearing value for septa
***

# Changing the carrier gas tank while GCMS is on

If the carrier gas tank approaches 500 PSI during an experiment, it should be switched out for a new tank.

Note: Work quickly and with a partner if possible so that the flow controller is off for as little time as possible.

1. Instrument > Vacuum Control > Advanced > Turn off Flow Controller
2. Close carrier tank valve
3. Loosen the regulator using a wrench and turning counter-clockwise
4. Hold the regulator and column carefully while you switch out tanks, trying not to jostle or bump the column
5. Tighten the regulator back on to the new tank by turning clockwise with a wrench as tightly as you can
6. Open the carrier gas tank and use soapy water to check for any leaks
	* Slowly squirt onto the connection between the regulator and tank, if bubbles appear and then expand, there is a leak and the connection must be tightened
7. Turn the Flow Controller back on

***

# Changing the glass insert split liner while the GCMS is on (WIP)

The injection port glass liner should be switched out every 1000 runs.

1. See pg. XXX of the GCMS-QP2010 Operation Guide
2. using tweezers and gloves, place 10 mg of deactivated fused silica (glass wool) into a new glass liner according to instructions in guide
3. In software, Instrument > Vacuum Control > Advanced > turn off Flow Controller
4. Remove hood of GCMS
5. xxxxx
6. Profit

***

# GCMS shut down

* GCMS shut down is almost the reverse of the startup.

## Procedure:

### The first steps are done in GCMS Real Time Analysis software
* Use manual shutdown, Instrument > Vacuum Control > Advanced
	* Auto shutdown does not give enough time between the turbo molecular pump shutdown
	and the vacuum pump shutdown. 
	* Manual shutdown procedure:
		1. Turn off ion source heater
			* wait till heater is <80˚C before moving on
		1. Turn off turbo molecular pump
			* wait at least 10 minutes
    	1. Turn off rotary pump
    	2. Turn off GC system
    	3. Wait for the GC to cool to close to room temperature <35˚C then turn off flow controller.

### Once GC system is cool you proceed with manual shutdown of equipment
1. Turn off the MS (switch in back)
1. Turn off the GC (switch in front)
1. Turn off Shimadzu AOC-5000 Auto Injector (switch on power unit in back)
1. Shut down computer
1. Close main valve on carrier gas (helium)
	* No need to close the other valves

***

# General notes

* The blue septa may provide a better seal than the green septa (for higher temps).
* The rotory vacuum oil should be changed every 6 months.
* Replace the injection port glass liner (contains glass wool) after ~1000 injections.
	* This helps prevent the liner from fusing to the injection port.

## GCMS maintenance log

* 3/16/22 Shimadzu service maintenance performed by Michael H. Obelsky (mhobelsky@shimadzu.com)
	* Cleaned parts
	* Replaced Helium filter and copper tubing
	* Replaced bungee cord on auto-injector with used one (may need to be replaced soon)
	* Installed mist filter on rotary pump
	* Replaced oil in rotary pump
	* Overall said GCMS doing well for its age

## Autosampler

* Service is needed every ~2 years.
* Do not lubricate anything besides the guide rails in the horizontal portion. 
	* Lubricating other components will likely break them.
* You can find videos on how to perform maintenance by googling 'leap autosampler'.


## Carboxen 1010 PLOT column

* Bake at 200<sup>o</sup>C for 1-2 hours if column disconnected for < 1 day.
* If it is diconnected for >1 day, bake overnight at 200<sup>o</sup>C.
