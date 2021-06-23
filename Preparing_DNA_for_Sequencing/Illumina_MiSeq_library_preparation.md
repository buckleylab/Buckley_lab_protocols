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
	* [speed-vac](../lab_equipment/speed-vac.md)
	 
6. [Gel extraction](../gel_electrophoresis/gel_extraction.md) of bands with the expected fragment size 
	* This is recommended to increase sequence quality

7. Quantify the library sample using PicoGreen or Qubit
	* Sample requirements for a MiSeq run:
		* >=20 uL with a concentration of 5 ng/uL
	* Vacuum evaporate if needed
		* [speed-vac](../lab_equipment/speed_vac.md)

8. Submission to Cornell Sequencing Facility:
	* Place 20 uL of sample with a concentration of 5 ng/uL into sequencing tube
	* Additionally, submit 10 uL of 100 uM _sequencing primers_:
		* forward sequencing primer
		* reverse sequencing primer
		* reverse index read primer

## Usual comments provided with the sequencing order

### 515f-806r 16S sequencing:

We have generated our dual-indexed custom barcoded library
as described in Kozich et al., (2013). Along with the submitted library,
we have provided 10 ul of 100 uM custom sequencing primers: 
Primer 1, Index Primer, Primer 2.

We request the following MiSeq run specifications: a __cluster density of 650-750k/mm^2__
(under-shooting the cluster density is better than over-shooting),
a __PhiX spike-in of 5%__. These MiSeq run specifications are described 
in Kozich et al., (2013); see 'Run Monitoring' in the Supplemental Materials.

In addition, we have been in contact with Peter Schweitzer on using dPCR to for library
quantification in hopes of obtaining more accurate cluster densities. 
The dPCR assay entails using the ABI QuantStudio3D instrument with SYBR Green and 
primers that target the Illumina adaptor sequences. 
The data that Peter has shared with us looks promising, but taking the quantifications
at face value would likely cause __over-clustering__, and thus the raw values likely
need to be corrected in order to achieve the target cluster density. 
Please let us know if dPCR cannot be used to quantify our libraries or if
you have any other questions about the assay.

Also, please let us know if you have any questions about the primers or requested
run parameters. Thank you!

[Citation: Kozich JJ, Westcott SL, Baxter NT, Highlander SK, Schloss PD. (2013).
Development of a Dual-Index Sequencing Strategy and Curation Pipeline
for Analyzing Amplicon Sequence Data on the MiSeq Illumina Sequencing
Platform. Appl Environ Microbiol 79:5112-5120.]

### ITS1 sequencing:
