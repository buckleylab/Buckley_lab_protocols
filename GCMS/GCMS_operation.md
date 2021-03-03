Protocol for quantifying CO2 in headspace samples with the Shimadzu GCMS-QP2010
===============================================================================

## Authorship

Ashley Campbell, Chantal Koechli, Nick Youngblut and Sam Barnett (2016)

Updated 2021 by Cassi Wattenburger (more details)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

***

# Equipment 

* GCMS 
	* Shimadzu GCMS-QP2010

* Autosampler
	* Shimadzu AOC-5000 Auto Injector

***

# GCMS start up

## WARNINGS:

* You should not need to start the floor vacuum pump (rotory pump) manually.
This can be done using the GCMS software.

* If the GCMS has not been used in a while:
	* Check the oil level in the rotory vacuum pump (on the floor).
	* Check the amount of carrier gas still in the tank.  

## Procedure:

### Prior to start up:
1. Change carrier gas tank if low
	1. Make sure He tank is closed
	2. Use large wrench and turn the regulator connection counter-clockwise to loosen
	3. Hold the column in one hand while you use the other to move the new tank in place
		* The column is delicate and should not be bumped or placed down
	4. Tighten the regulator connection clock-wise until you can no longer tighten it
	5. Check for leaks using soapy water
		* Open the tank to allow gas flow and slowly pour soapy water on
		* If a bubble appears and gets larger, there is a leak and the regulator connection must be tightened more.

1. Fill oil if low
	1. xxx

### Turn everything on

1. Turn on carrier gas (should be Helium)
	* The PSI should be ~100
1. Turn on Shimadzu AOC-5000 Auto Injector (switch on power unit in back)
1. Turn on computer
1. Turn on  the GC (switch in front)
1. Turn on the MS (switch in back)
1. Start the __GCMS Real Time Analysis software__

### The next steps are done in GCMS Real Time Analysis software

1. From top screen, select __Instrument > Vacuum Control > Advanced__ 
1. Use the manual startup
	* Manual startup provides more control, 
	option for safety checks, 
	and may produce less wear and tear.
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
			* If the sound continues, reverse the steps to shut down the GC and troubleshoot
			* Wait for vacuum to return and stabilize before moving on
	    1. Turn on ion source heater
			* GC and MS indicators in top right of screen should soon say 'ready'
	    1. Wait at least 24 hours before running samples on GCMS.
			* This allows for any contaminating air in system to be purged
1. Run GCMS tuning proceedure
1. Load a method or create a new method
	* Make sure that GC and MS are heating up to the method's specified temps
	* A batch file can then be created if needed

***

# GCMS tuning

## WARNINGS:

* If the GCMS has not been used in a long time (e.g., a year),
wait ~1 day prior to tuning.
	* This wait provides time for the column to be purged of contaminants.

## Procedure:

Follow procedure starting on Page 21 of the GCMS-QP2010 Operation Guide.

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
 
### Leak check:

* Follow procedure outlined on Page 19 of the GCMS-QP2010 Operation Guide.

***

# GCMS sample processing

## Notes:

* The septum can be changed while the GC is on.
The carrier gas flow will just need to be turned
off very briefly prior to changing the septum.

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
1. For each run replace septa on injection port
	* This must be done quickly as carrier gas flow must be stopped
	* It may be easier to remove grill from top of GCMS in case you drop one of the small parts
	* Use work gloves while replacing septa as the injection port is VERY HOT!!!
	* Septa replacement
		1. Open vacuum control and click "advanced"
		1. Turn off flow controller to stop flow of carrier gas
		1. With work gloves unscrew red sealing cover
		1. Remove T-shaped adapter
		1. With tweezers remove old septa and place in "Used Septa" jar
		1. With tweezers place new septa in hole being careful not to deform or puncture septa
		1. Place T-shaped adaptor on top of septa
		1. Screw red sealing cover back on
			* Be sure not to tighten too hard as this may deform septa and result in leaks or easy coring
		1. Restart flow controller
1. Reset septa consumables by double clicking septa icon on right hand toolbar, clicking "Reset Consumables" and clearing value for septa
1. Once you double check your batch file click start to start the run
1. If you need to stop the run for any reason, click pause or stop
1. During run, check carrier gas levels (on He tank) to make sure it does not run out due to any leaks
1. Once run is complete, save data to your run folder

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
	
*** 

# Maintenance

## Autosampler

* Service is needed every ~2 years.
* Do not lubricate anything besides the guide rails in the horizontal portion. 
	* Lubricating other components will likely break them.
* You can find videos on how to perform maintenance by googling 'leap autosampler'.

***

# Notes on Carboxen 1010 PLOT column

* Bake at 200<sup>o</sup>C for 1-2 hours if column disconnected for < 1 day.
* If it is diconnected for >1 day, bake overnight at 200<sup>o</sup>C.
