MoBio Nucleotide Extraction Kit Protocol
========================================

## Authorship

Spencer Debenport & Sam Barnett (2016)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)


## General description

This protocol describes all of the necessary steps to go from soil samples to
nucleotides with the MoBio Nucleotide Extraction Kit (96-well method). 

Kit: **PowerMag Microbiome RNA/DNA Isolation Kit** (cat# 27500-4-EP)


***

# Loading deep well plates for extraction

If sharing (splitting) a 96-well plate, see [this protocol](./shared_DNA_extraction_plate_protocol.md)

## Purpose

This protocol explains how to load the deep well 96-well plates (Glass Bead Plates) with
soil samples prior to bead beating and DNA extraction. The plates used should come from
DNA MoBio 96-well nucleotide extraction kit already containing silica beads. 
Soils can be loaded into the plate in batches, with the plate stored at -20<sup>o</sup>C
until the extraction.


## Materials/Equipment

* Scale (.01g sensitivity)
* Weighing paper and/or small weighing boats
* Spatulas
* Glass stiring rods
* Well protectors (tip box top with drilled hole and microcentrifuge tube with end cut off
  inserted into hole.)
  * Initial cleaning: see [Cleaning](./MoBio_96-well_kit_protocol.md##Cleaning)
* Deep well 96-well plate (silica beads should already be inside wells)
  * "Glass Bead Plate"


## Protocol

1. Centrifuge plate before filling to make sure silica beads are at bottom (as per kit
   instructions).
1. Cut rubber plate cover into column strips.
  * This will allow you to load 1 column at a time, with the other columns still sealed.
1. Remove cover from first column and place well protector on top such that "funnel" is in
   first well.
  * **MAKE SURE:** thoroughly clean the well protoctor between soil sample
    * see [Cleaning](./MoBio_96-well_kit_protocol.md##Cleaning)
  * **MAKE SURE:** most other wells are covered by lid or well protector.
1. Weigh out **0.25 g** of soil.
1. Pour soil into well through funnel.
  * If soil is wet/muddy, it can be scraped into well with or without well protector.
  * If soil is sticky, it can be pushed through the funnel with glass stirring rod.
1. Carefully remove well protector.
1. Repeat for all soil samples.
  * Use a new, clean well protector for each soil.
1. When column is done, put cover strip back and remove strip from next column.
1. Once all wells are done or if long break is required, put plate (covered) in -20˚C
   freezer until conducting the nucleotide extraction.


## Tips
1. Be very careful about static charge of plate.  It can cause dry soil particles to
   spread out to other wells or stick to covers.
1. For wet and sticky soils, weigh out 0.27-0.30 g instead to account for loss stuck to
   weighing paper and well protector.
1. For very wet soils, use weighing boats instead of paper.
1. For moist soil that clumps well, soil can be rolled up into cylinder shape in weighing
   paper and it falls neatly into well.
1. Place clean tip box cover over open wells during short breaks such as cleaning well
   protectors.
1. Keep soils on (dry) ice.
1. Only take out soils from freezer for 2-3 columns at a time to reduce effects from
   thawing.
1. Use many spatulas to save time of cleaning.


## Cleaning
* Between soils, thoroughly wipe out well protectors with 70% ethanol to remove any
  residual soils.
* Between soils, thoroughly wipe off spatulas and glass rods with 70% ethanol to remove
  residual soils.
* Before starting new plate, soak well protectors in 10% bleach solution for 20 min to
  remove residual DNA.
* Before starting new plate, flame sterilize spatulas.


***

# Nucleotide extraction 

Most of the protocol is performed by the robot, but there are a couple of steps prior
to using the robot. Also, some steps are conducted off the robot.

## Before Starting:
1. Make sure the 96-well plate of samples is ready to go (see above for loading instructions).
  * Thaw out 96-well plate of samples if stored previously at -20<sup>o</sup>C.
1. Add beta-mercaptoethanol (B-ME) to PowerMag Microbiome lysis solution.
  *	25 ul B-ME per 1 ml lysis solution
  * 64 ml total lysis solution needed per 96 well plate
  * Warm the Lysis Solytion at 60<sup>o</sup>C 
1. Run the MoBio_Kit.med method in simulation mode to calculate total volumes needed for all solutions.
2. Set up the robot platform according to directions from MoBio_kit.med method.
  * Add 300 ul filter tips.
  * Arrange reagent reservoirs.
  * Ensure that deep well plate adapters are installed in the rear two positions of the rightmost carrier. 
1. Make sure the balance plates for the three centrifugation steps are readily available.

## Robot Method:

1.	Add 650 ul warmed PowerMag Microbiome Lysis Solution/B-ME to each well of the Glass Bead Plate.
2.	Secure a Bead Plate Sealing Mat to the Glass Bead Plate. 
3.	Place Glass Bead Plate in BioSpec BeadBeater. Beat for 1 min at maximum speed.
4.	Centrifuge Glass Bead Plate for 15 min at 3000 x g.
   * **NOTE:** Make sure to have a balance plate with adjusted weight to match your bead plate in the centrifuge. Weigh your plate and either add or remove water from the balance plate until it matches the weight of your plate. Reseal balance plate.
5.	Remove and discard Bead Plate Sealing Mat.
6.	Transfer supernatant to new 2 ml Deep Well Plate (DWP). 
7.	Add 150 ul PowerMag Inhibitor Removal Solution to each well and apply Sealing Tape to the DWP. 
8.	Vortex DWP for 5 seconds.
9.	Incubate DWP at 4<sup>o</sup>C for 5 minutes.
10.	Centrifuge DWP for 15 min at 3000 x g.
   * **NOTE:** Make sure to have a balance plate with adjusted weight to match your bead plate in the centrifuge. Weigh your plate and either add or remove water from the balance plate until it matches the weight of your plate. Reseal balance plate.
11.	Remove and discard Sealing Tape.
12.	Avoiding the pellet, transfer the entire volume of supernatant to new DWP. 
13.	Apply Sealing Tape to DWP.
14.	Centrifuge for 15 min at 3000 x g.
   * **NOTE:** Make sure to have a balance plate with adjusted weight to match your bead plate in the centrifuge. Weigh your plate and either add or remove water from the balance plate until it matches the weight of your plate. Reseal balance plate.
15.	Transfer no more than 850 ul supernatant to a new DWP, avoiding the pellet.
   * **NOTE:** DWP can be stored at 4<sup>o</sup>C for several hours at this stage.
16.	Add 875 ul of Bead/Bind Solution to DWP.
17.	Shake for 10 min at 500 rpm. 
18.	Place DWP on Magnet.
19.	Incubate for 10 min on Magnet.
20.	Pipette 580 ul from DWP to waste.
21.	Move plate to empty platform.
22.	Add 500 ul Wash Solution to each well of DWP.
23.	Move plate back to Magnet. 
24.	Incubate for 10 min on Magnet. 
25.	Pipette 600 ul from DWP to waste.
26.	Repeat steps 21-25 two more times.
27.	Move plate to empty platform.
28.	Add 100 ul Elution Buffer to each well of DWP.
29.	Shake for 25 min at 500 rpm.
30.	Place DWP back on Magnet.
31.	Incubate for 10 min.
32.	Pipette 100 ul from DWP to microplate.
