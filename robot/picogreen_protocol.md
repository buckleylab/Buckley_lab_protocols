Picogreen Protocol 
==================

## Authorship

Chantal Koechli and Nick Youngblut (2011-2014)

Updated by Cassi Wattenburger (2022)

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

# Automated Picogreen protocol (using the Hamilton robot)

### Basic method

* Select the XXX.med file in the robot software
* The method will prompt you for all of the materials needed
  (e.g., picogreen & DNA standard)
* Run the method in simulation mode to get an idea of what to expect.

Notes:
* You will need to transfer some 200x picogreen and the lambda standard into green microcentrifuge tubes that are robot compatible
* Recommend using 2 uL of DNA per reaction
* Prepare more 1x TE than the robot method prompts or you will get liquid handling errors
* Keep the light off in the robot (picogreen is light sensitive)

### Notes on CsCl gradient fractionation quantification

* Using 2 ul of each fraction per Picogreen rxn should be adequate, 
even at the ends of the gradient.
* Use 5 ul of each fraction if you want higher precision. 

# Manual Picogreen protocol

### Notes

* The protocol assumes one 96-well plate.

### Materials

* \(1\) Costar black 96-well plate
	* VWR: cat# 62402-983
* \(8\) 1.5ml micro-cfg tubes
* \(2\) 15 or 50 ml falcon tubes (depends on volume 1x TE buffer neded)
* \(1\) Quant-iT™ PicoGreen® dsDNA Assay Kit
	* ThermoFisher: cat# P7589
	* Warm up the picogreen reagent before use


### Make 1x TE buffer

* __NOTE:__ Sketching out a plate layout is highly encouraged before beginning analysis. 
	* The plate will contain:
		* Standards
			* Dilution series of DNA standard
		* Unknowns
			* Provided nucleotide samples with unknown concentrations
		* Blanks
			* Accounts for background noise in unknowns
			(from humics and other contaminants)

* __NOTE:__ This protocol assumes all standards, unknowns, and blanks are run
in duplicate.

* To make 1x TE buffer from the 20x stock supplied in the kit:
	* 1:20 dilution
		* e.g., 2 ml of 20x TE buffer in 38 ml of nuclease-free water

* Calculate the total volume of TE buffer needed:

	* raw_total_volume = TE for standards + TE for sample dilutions + TE for picogreen
reagent dilution
		* volume for all standards (ul):
			* 14 * 99 + 1832.5 = 3218.5 ul
		* volume for all blanks (ul):
			* Number\_of\_blanks * 199
		* volume for all unknowns (ul):
			* Number\_of\_unknowns * 198 
			
	* final_total_volume = raw\_total\_volume * 1.1
		* __Note:__ Produces 10\% extra 1x TE buffer

	* For example:
		* 10 unknowns in duplicate + 1 blank in duplicate + 14 total standards
		would need 5.59 mL of raw_total_volume and 6.15 mL final_total_volume
		(with extra TE buffer).

* use a 50 mL falcon tube for making the 1x TE buffer


### Make standards 

* Stock standard conc.: 100 ug/mL
* Working standard conc. needed: 2 ug/mL
	* 1:50 dilution in TE buffer
* Volume working standard needed (ul): 500
* Volume TE buffer needed (ul): 500 * 49/50 = __490__
* Volume stock standard needed (ul): 500 * 1/50 = __10__


* Make up standards, as specified in table below, in 1.5 mL Eppendorf
    tubes
    * __Note:__ This will make 2 replicates of each standard (enough for 1 plate).

  **Final Conc. post-pico (ng/mL)** ___ **TE to add (uL)**   ___ **2ug/mL working std to add (uL)**
  --------------------------------- --- -------------------- --- ----------------------------------
  750                                   62.5                     187.5
  500                                   125                      125
  250                                   187.5                    62.5
  100                                   225                      25
  50                                    237.5                    12.5
  20                                    245                      5
  0                                     250                      0

	* 'post-pico' means the final conc. after adding the Picogreen reagent.

* Add 100 uL of each standard to unique wells of a Costar black 96-well
plate. The standard curve should be duplicated.


### Unknown & blank well reagent additions

*   Add 99 uL of TE buffer to all wells on the Costar plate assigned as
	unknowns or blanks.
	* Multichannel pipettors and reagent resevoirs can be used for this step if many
    unknowns/blanks are in the layout.

*   Add 100 uL of TE buffer to all blank wells.
	* The blanks will not have Picogreen reagent added.

*   Add 1uL of the corresponding unknown to the assigned unknown well.


### Making and adding Picogreen Reagent

* Based on the number of unknowns to be run, calculate the volume of 1x
Picogreen reagent that should be made (volume in ul):

	* total\_volume (uL): 110 * (number\_of\_unknowns + number\_of\_standards)
		* __NOTE:__ Remember the duplicates!

* Once that the total volume is determined, calculate dilution of the 200x
Picogreen reagent:

	* Volume of 200x Picogreen needed (uL): total\_volume * 1/200
	* Volume of TE buffer needed (uL): total\_volume * 199/200

* For example:
	* If running 10 unknowns in duplicate (& 14 total standards), 
	3740 uL of 1x Picogreen should be made ((20+14)*110=3740), using 18.7 uL of 200x Picogreen
	reagent diluted with 3721.3 uL of 1x TE buffer.

*   Make up Picogreen reagent in a falcon tube (15 mL or 50 mL, depending
    on the amount needed) that is wrapped in aluminum foil (to prevent
    degradation of reagent).

*   Once reagent is made up, transfer 100 uL of reagent to each well of
    the Costar plate to be analyzed, EXCEPT the wells to be used as
    blanks. 
	* Again, the multichannel pipettor and reagent resevoirs can
    be useful in this step.    
    * Make sure to pipet up and down to mix reagent with well contents.

*	Place the Costar plate in the plate reader and incubate for 5 minutes
	* Alternatively, just stick the plate in a drawer.


# Plate reader

While unknowns are incubating, set up analysis program on plate
    reader software:

1.  Open Softmax Pro 6.3 software.

1.  Then, click on: 'Protocols' tab => 'Protocol Manager' => 'Protocol library' 
	=> 'Nucleic Acids' => 'Picogreen assay'.
	This will open up an already created Pico protocol.

1.  To make sure the plate reader is set-up to run a fluorescence assay,
    click on the 'Settings Icon', choose the 'FL' option, and make sure
    that excitement is set to 485nm and emission is set to 535 nm.

1.  Modify plate set-up by scrolling to the page with the plate layout,
    and clicking on the small plate icon ('Template editor'). This will
    open up a screen that will allow you to add standards, unknowns, and
    blanks to the plate to be read.
    * __Note:__ The dilution factor for the unknowns should be set to 100 if 2 uL of template was used, 200 if 1 uL of template was used.
    * __Note:__ The robot sets up each measurement in duplicate in adjacent columns
    * Recommend using a pre-made template (picogreen_template.prcl) so you don't have to set up the standards every time

1.  To read plate, open the plate reader using the open/close button and
    place the plate into the reader. Note the orientation of the plate!
    Then press the read button.
    * You may be prompted to switch out the XXX first if it was changed out for another assay.

1.  Once read is done, save the file and export data as .txt file. Exclude all but the unknowns.

1. You can quickly tidy the .txt files for easy downstream analysis using the picogreen_tidy.py script.
