Submitting prepared library for sequencing at the Cornell BRC
=================================

## Authorship

Cassandra Wattenburger (June 2021)

## Updated by

# Description

We do our sequencing at Cornell Biotechnology Resource Center. These instructions list details of how to fill out the submission form and submit a prepared library for sequencing.

### Illumina MiSeq sequencing submission

NOTE: This guide assumes you are submitting a 16S V4 or ITS1 amplicon library using the Kozich barcodes.

1. Place order [here](https://www.biotech.cornell.edu/core-facilities-brc/services/miseq-illumina-sequencing) using the "Submit Samples" link.
1. Scroll to Genomics and select Illumina Sequencing
2. Either select a stored payment method or enter a new one
3. On the next page, choose
    * Instrument: MiSeq
    * Sequencing kit: v2 500 bp
    * Read Length: 2x250 bp Paired End
    * Sample Preparation: Library Submission (customer prep)
    * Illumina Sequencing Adaptor Type: Custom
    * Which Custom Sequencing Primer are you submitting? Read1, Read2, and Index1
    * Custom sequencing primer mixing: Mix with Illumina's primers
      * NOTE: If you plan to spike phiX into the run (which you should definitely do for low complexity libraries), phiX will not amplify if the Illumina primers aren't also included!
    * Barcode Type: Dual barcode
    * Custom DNA Barcode Index Length: 8
    * Multiplexed: No
    * Were any of these samples made using a PCR free library prep type? No
    * Are these libraries low complexity? Yes
      * 16S V4 and ITS1 are low complexity (ITS1 less so), a genome library would be considered high complexity because you are not sequencing a single conserved region
    * Organism (optional): Prokaryotic
4. On the next page, enter the following information into the General Comments:

   > We have generated our dual-indexed custom barcoded library as described in Kozich et al., (2013). Along with the submitted library, we have provided 10 ul of 100 uM custom sequencing primers: Read1, Read2, and Index1. We request the following MiSeq run specifications: a PhiX spike-in of 5% and a cluster density of 650-750k/mm^2 (under-shooting the cluster density is better than over-shooting). These MiSeq run specifications are described in Kozich et al., (2013); see 'Run Monitoring' in the Supplemental Materials. Please let us know if you have any questions. Thank you! [Citation: Kozich JJ, Westcott SL, Baxter NT, Highlander SK, Schloss PD. (2013). Development of a Dual-Index Sequencing Strategy and Curation Pipeline for Analyzing Amplicon Sequence Data on the MiSeq Illumina Sequencing Platform. Appl Environ Microbiol 79:5112-5120.]

   * 5-10% phiX is usually adequate, 5% is generally OK for ITS1, 10% is better for 16S V4.

5. Below the comments, name your library samples, choose the number of lanes to be used for each library (ussually 1), enter 20 uL as the volume, enter the DNA concentration (at least 5 ng/ul), and enter 8 random ATGCs for Index1 and Index2 (form requires it but it isn't necessary for our libraries).
6. Proceed to verification and submit.
7. Prepare 20 uL of each sample, 10 uL of Sequencing primers Read1, Read2, and Index1 at 100uM. Make sure each tube is labelled well including the concentrations. Put these in a bag labelled with the order number.
8. Take the samples over to 130 Biotechnology Building on ice

Sequencing takes 1-2 weeks. See our (pipeline for processing raw sequence data)[] once you recieve data back.
