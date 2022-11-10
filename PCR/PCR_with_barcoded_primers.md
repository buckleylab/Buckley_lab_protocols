PCR with Illumina Miseq Barcoded Primers
=================================

## Authorship:

Ashley Campbell, Chuck Pepe-Ranney, Chantal Koechli, and Nick Youngblut (2014)

## Updated by:
Sam Barnett (2018)

# Description
This protocol is for running real time PCR using barcoded primers for Illumina Miseq sequencing.
 

# Method

__Important notes to read before starting:__ 
* If using the robot for PCR setup, all template DNA must come from the same 96-well plate.  
If you have samples from more than one plate, you must transfer them to the same plate. If your current template
plate is completely full (no room for additional positive or negative control) you must transfer
samples to a new plate with enough room for your positive and negative controls. This is common
for DNA from 96-well extraction kits.
* If you are running your PCR reactions in triplicate, you can only run 30 samples at once. This means
that if you have 94 samples on your template plate, you need to run 4 separate PCR reactions
(3 with 30 samples each and 1 with 4 samples). One way to avoid that last small PCR run is to only add
90 samples to each 96-well template DNA plate.

1. Add positive and negative controls to your template DNA plate.
	* Positive control: Mock community, bacterial colony DNA extract, anything you know contains your primer target.
	* Negative control: empty well, molecular grade water, extraction buffer.

2. Calculate sample volume necessary for addition of __5 ng__ of template DNA to PCR
reactions. This is just a guideline for how much DNA to use per rxn. You may need to
use more or less depending on PCR inhibitors and rxn efficiency.

3. If dilutions beyond the capacity within a single 25 ul PCR reaction are necessary
you will need to make a separate dilution plate containing all 

4. PCR composition for 1 rxn:

	* 12.5 uL Mastermix (NEB Q5 High Fidelity, Hot Start PCR Mastermix - M0494)
		* 50% of total volume
		
	* 2.5 uL combined forward and reverse barcoded primers (10 uM)
		* 10% of total volume		
		* Primer plates can be created with the robot method: "make\_primer\_plate"

	* 0.625 uL Picogreen reagent
		* 2% of total volume
		* 4x concentration, dilute the 200x stock that comes in the Picogreen kit with 1X TE
	
	* [optional] 1.25 uL BSA (20 mg/mL, NEB B9000S)
		* 5% of total volume

	* X uL template (we usually shoot for 5 ng/reaction)

	* PCR water up to 25 uL

* NOTE: Mastermix and Picogreen can be mixed prior to PCR (31.25 ul picogreen in 1.25 ml Mastermix) and then 13.1 µl mix added per PCR reaction.

5. Use robot method "qPCR\_wWorklist\_altdispense" for setting up PCRs, 
running triplicate reactions for each sample to be sequenced. 

6. Run thermocycler protocol for gene of interest

* NOTE: we usually run a melt curve after the 30 amplification cycles to distiguish amplification from primer-dimer formations.

7. Combine amplified replicate PCRs for each samples, transferring samples to a new 96-well plate. 
	* This can be done with the robot method: "plate_pooling"
