Setting up a CsCl gradient for Stable Isotope Probing
=====================================================

## Authorship

Ashley Campbell, Chantal Koechli, and Nick Youngblut (2014)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)


## FAQs

* How much DNA per gradient?
	* Ashley used 5-8 ug per gradient
	* Nick: 5 ug per gradient for the full C-Cycle experiment
* Which ultracentrifuge tubes?
	* Beckman Coulter: Ref# 361621


## Making gradient media

Gradients are run in CsCl (DNA) or CsTFA (RNA) dissolved in gradient buffer.

1. Start by making the gradient buffer solution:

	* Components:
		* 15 mM Tris-HCL (pH 8.0)  => F.W. 157.6
		* 15 mM EDTA  => F.W. 372.24
		* 15 mM KCl  => F.W. 74.56
	* Method for preparing 500 ml:
		* 400 ml milliQ water
		* 7.5 ml of 1 M Tris-HCl (pH 8.0)
		* 0.5592 g KCl
		* 2.7918 g EDTA
		* Disolve solids and bring volume up to 500 ml


2. Decide on the average density you desire for your gradient.
	* Typical DNA run: 1.69 g/ml gradient; 55,000 rpm; 66+ hrs; 20<sup>o</sup>C


3. Prepare Gradient Media solution (ie., gradient buffer + CsCL)
	* When you add your nucleic acid sample, it will dilute your gradient media solution.
	Thus, your gradient media solution should be dense enough to hit your target density
	after adding your nucleic acid sample.
	
	* __Note:__ You can make a stock of Gradient Media Solution (e.g., 200 ml).
	Store it in vials sealed with crimp-capped butyl rubber stoppers to prevent
	evaporation and salt build-up.
		* When needed, use a 20-30 mL syringe to pull out enough volume and transfer
		to reagent well. Also, transfer N_gradients x 100 ul of CsCl solution to a
		micro-cfg tube for balancing the gradient tubes.
	
	* The tubes we use are 4.7 to 4.75 ml volume. Let's say we wanted to leave room
	for 0.45 ml of nucleic acids in TE buffer
	(TE can be used as filler if lesser volumes used)
	while achieving a final gradient density of 1.69 g/ml.
	We would figure the density of our gradient media solution as follows:


>__Total mass of gradient (without tube):__ 1.69 (g/ml) * 4.75 (ml) = 8.0275 (g)

>__Subtract the mass of the DNA/RNA solution:__ 8.0275 (g) - 0.45 (g) = 7.5775 (g)

>__The desired density for CsCl solution:__ 7.5775 (g) / 4.3 (ml) = 1.762 (g/ml)


Thus, dissolve 7.5766 g CsCl in a total volume of 4.3 ml gradient buffer. 

__Note:__ if you add 7.5766 g of CsCL to 4.3 ml buffer, you will end up with a 
total volume > 4.3 ml. It is helpful to use a graduated tube or
cylinder, start with less volume of gradient buffer than you need,
add and dissolve the desired amount of CsCl, and then bring it up to your
final volume.


4. Fine tune the density of your gradient media solution:

    * __NOTE:__ If the CsCl solution is stored in a sealed vial, shake
    the vial vigorously prior reading the RI.
    	* This can help resuspend CsCl that has crystalized in the vial. 
	* Use the digital refractometer to achieve the **EXACT** gradient media density
	that you desire.
	* To use: add 5 ul solution to sample well, making sure it covers
	completely the prism surface (it usually does).
	* Press "read," and it will give you the R<sub>I</sub> and temperature.
	The R<sub>I</sub> of water should be 1.3333.
	* **Wipe well** with kimwipe after each sample.
	* At the end of use, add some water and then wipe clean.
	* We have modified the surface of the prism with a piece of black electrical
	tape cut into the shape of a doughnut (cut with 2 cork borers of different radius). 

	1. First correct for the refractive index of your gradient buffer:
		* All salts will cause refraction, in measuring the CsCl density of our gradient
	media we need to first account for the refraction due to the gradient buffer
	(ie: the Tris, EDTA, and KCl). 
		* We do this by measuring the refractive index of the gradient buffer and
		then using the following equation:
			* R<sub>I corrected</sub> = R<sub>I observed</sub> - (R<sub>I buffer</sub> - 1.3333)

	2. Then to convert refractive index:
		* Density (g/ml) = a * R<sub>I corrected</sub> - b

		1. For CsCl of 1.22 - 1.90 g/ml at 20<sup>o</sup>C: 
			* a = 10.9276, b = 13.593
		2. __Note:__ CsCl gets cold when it goes into solution. The equation above is only
		valid at 20<sup>o</sup>C. Hence, you need to wait until the solution is near
		room temperature before measuring R.
		3. The R<sub>I corrected</sub> of a 1.762 CsCl solution is **1.4052**

	3. Adjust the gradient media solution density:
		* add buffer or CsCl in small increments until R<sub>I</sub> = 
		target density +/- 0.0001 
		
	4. Filter sterilize if needed


## Setting up the gradients

1. Add exactly 4.3 ml of the CsCl solution to the cfg tubes.
	* Use weight to measure this volume:
		* 4.3 ml x [density\_CsCl\_solution] = grams of CsCl solution needed.
    	* e.g., 4.3 (ml) x 1.762 (g/ml) = 7.5766 (g)
    * Adding the CsCl solution:
    	* Zero an empty cfg tube on the milligram scale.
    	* Add CsCl solution until desired weight is reached.
	* __Notes:__ The meniscus should be around the "Beckman" label.

1. Add DNA and TE buffer
	* TE is used as filler to in in total add 450 ul of volume to each cfg tube.
	* If adding bisbenzamide, add 8 ul here. (If one has <8 ug DNA)

1. Add TE buffer to fill the tubes to their necks.
	* ~30 ul of TE buffer is needed __IF__ 450 ul of DNA & TE were added.
	* Err on having a bit less volume so you have room to balance.
	* The goal is to have only a very small air bubble when placing lid in the tube
	and applying pressure (the air should go into solution).

1. Weigh and balance tubes by adding TE buffer.
	* When balanced, push the black caps down to seal.
		* The caps probably will not seal well. This is OK.
	* __Note:__ all tubes should be within +/- 0.01 g

1. Mix all tubes by inverting several times (~8-10) until no refraction 
waves can be seen.

1. Run in ultracentrifuge: 55,000 rpm, 20<sup>o</sup>C, 66+ hours.
	* Put stem adapter (brown caps that look like hats) on tubes to keep stem
	from collapsing.
	* Put tubes in rotor.  
		* __Note:__ The rotor should always be set on cloth/paper to prevent
		damage to the magnets underneath. 
	* Turn on ultracentrifuge.
	* Press door button and keep pulling on the handle until the vacuum is off.
	* Put rotor on the spindle and depress the button in the center of the rotor.
		* Make sure it stays depressed.
	* Close door. Set speed, temperature and time. Press start. It will start running
	when the vacuum is fully established.


## CsCl gradient fractioning

### Setting up the fraction recovery system

* Take up MilliQ H<sub>2</sub>O in 20 ml syringe.
* Remove as much air from the syringe as possible.
* Connect the HPLC tubing to the 20 ml syringe.
* Put syringe on the pump and secure. Turn on the syringe pump.
* Attach an 18 G needle to the other end of the HPLC tubing.
	* Place a plastic spacer on the needle (needed for stabing the cfg tube later).
	* Suspend the needle upwards.
* Press "run" on the syringe pump to move the water by 100 ul,
or "run" + "-->" to fast forward the water.
	* Fill the tubing with water until the water is dripping out of the needle.
	* Pump speed: __15 ml / hour__
		* ~30 seconds needed per fraction when using a 18 G needle.
* Make sure to prepare the following (timing is important during the fractionation):
	* 96 well fraction recovery plates
		* Label the recovery plates
	* A stand to suspend the plates
	* The refractometer
	* A P10-pipette and enough tips
	* One 18 G needle per gradient (stabed into the neck)
	* Enough cut 18 G needles (just needle shaft: __~7/8__ inch long)
	* A lab notebook for recording measurements

### Fractionation 

* Remove two tubes from the ultracentrifuge at a time using the forceps in the box.
	* If more tubes are still in the ultracentrifuge: keep the other tubes spinning. 
	* __WARNING: Avoid shaking/disturbing any of the tubes!!! This will disrupt the
	established gradient!!!__
* Slide one tube into place in the fraction recovery system.
	* Store the other tube on a rack until this fractionation is complete.
* Secure the tube in the fraction recovery system (tighten all clamps).
* Place a cut 18 G needle in the Tube Penetration Device (TPD)
	* The TPD is the repurposed dissecting microscope.
* Puncture the bottom of the tube with the needle by raising the needle slowly
with the Tube Penetration Device (TPD).
	* __Note:__ If there is an air leak somewhere, then the contents of the tube
	will start to drip out.
* Lower the TPD, and the cut 18 G needle should remain in the tube.
* Set the TPD aside and replace it with a stand holding a 96 well plate.
	* The plate should be very close to the cut 18 G needle.
* With the 18 G needle attached to HPLC tubing that is attached to the syringe, 
stab the tube at the lower end of the neck.
	* __Note:__ Make sure that the needle and tubing does not contain any air!
	* This should be the only part of the top of the tube that is visible.
	* The rubber tube holders are marked for where to stab the tube.
* Press "run" on the syringe pump.
	* __Note:__ The first fraction will be likely less than 100 ul.
	* __Note:__ The presence of an air leak may also not be evident until the
	first fraction, so be careful; check for drips.
* Measure density with the refractometer for each fraction by pipetting 5 ul from the
  well and onto the refectometer.
	* Record the RI in your lab notebook
* Collect fractions until you reach the minimum RI<sub>corrected</sub> needed:
	* min(RI<sub>corrected</sub>) = __1.3967__
		* This corresponds to a buoyant density that would contain 10% G+C DNA
		(assuming equilibrium).
		* This will probably require 25-30 fractions.


### Cleaning up between tubes

* Remove the cfg tube and discard the rest of the liquid.
* Remove and replace the needles.
* Seal the 96-well plate until used for downstream applications.

### Final Clean-up 

* Shut off syringe pump.
* Make sure all used consumables are discarded.
* Wash CsCl solution off of equipment with water. 


## Removing CsCl from DNA samples (de-salting)

Magnetic bead-based clean-up is used.

### Using the robot:

* Robot protocol: __MagBead_Extraction.med__

### Manual option 1: isopropanol ppt

1. Add 3 volumes of DNA free water to the CsCl solution and mix
2. Add 0.6 volumes (calculated from new volume) of isopropanol 
	* (ie: 100 ul fraction + 300 ul water + 240 ul isopropanol)
3. Spin 14,000 g 30 min
4. Pour off supernatant. 
	* __BE CAREFUL NOT TO POUR OFF YOUR DNA PELLET!!!__
5. Wash 2 x with 70% Etoh
	1. Add 1mL of 70% ETOH to each tube
	2. Vortex 
	3. Centrifuge at 14,000 g for 15min 
6. Resuspend in 50 uL TE

### Manual option 2: filtration

1. Use Pall 96 well filter plates
2. Add 100ul CsCl fraction + 200 ul 50 mM Tris pH 8 (or TE if desired) to wells
3. Balance plates
4. Spin ~500 g 10 min, RT
5. Remove flow through and add 300 ul buffer to wells
6. Repeat 4 and 5 for a total of 4 times
7. During the last spin, run for 20 minutes instead of 10
8. Add 25ul - 50ul to the center of each membrane
9. Allow 5 minutes to dissolve DNA
10. Pipette up and down to remove from membrane
11. Measure volume removed if the volume exceeds the amount added in step 8
and if the wells were not dry.


#### Notes:

* balance plates to within 0.5 g
* Max g force for plate is ~3500g
* Hold up volme of plates is 0-30ul
* Large amounts of DNA will slow filtration and may require longer spin times
* expect <1.5 mM CsCl remaining after 4th spin,
  for higher purity increase number of washes or use isopropanol ppt.

