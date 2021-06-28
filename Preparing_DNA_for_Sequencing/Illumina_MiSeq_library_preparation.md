Preparing a Library for Illumina MiSeq Sequencing
=================================

## Authorship

Ashley Campbell, Chuck Pepe-Ranney, Chantal Koechli, and Nick Youngblut (2014)

## Updated by:
Sam Barnett (2018)

Cassi Wattenburger (2021)

# Description
This is the pipeline for preparing a library for sequencing with the Illumina MiSeq after running PCR

# Method

1. Amplify your DNA using the [PCR protocol](../PCR/PCR_with_barcoded_primers.md)

2. Combine replicate PCRs for each sample, transferring samples to a new 96-well plate
	* This can be done with the robot method: "plate_pooling"
	* [plate_pooling spreadsheet template](../robot/template_robot_platepooling.xls)

3. Perform SequalPrep PCR purification and normalization
	* SequalPrep Normalization Plates, Life Technologies, A10510-01
	* Follow the [manufacturer's instructions](https://www.lifetechnologies.com/order/catalog/product/A1051001),
	using 25 uL of PCR product for each sample
	* Multiple plates can be done in parallel by hand using a multichannel pipette, but be extra precautious if 
	preping 2 different libraries with overlapping barcodes

4. Combine all SequalPrep samples together (~4 ml for a full 192 sample library)
	* This may require pooling in multiple tubes so its best to mix all samples together in a 15ml Falcon tube
	or reagent reservior
	* Pre-weigh the tube(s) to help with the next step (speed-vac)
		* This will help you determine the volume after Vacuum evaporation

5. Vacuum evaporate samples to concentrate down to volume needed for a gel excision
	* 50 uL per well
	* [speed-vac](../lab_equipment/speed_vac.md)
	 
6. [Gel extraction](../gel_electrophoresis/gel_extraction.md) of bands with the expected fragment size 
	* This is recommended to increase sequence quality

7. Quantify the library sample using PicoGreen or Qubit
	* Sample requirements for a MiSeq run:
		* at least 20 uL with a concentration of 5 ng/uL
	* Vacuum evaporate if needed
		* [speed-vac](../lab_equipment/speed_vac.md)

8. Submit to [Cornell Sequencing Facility]()

