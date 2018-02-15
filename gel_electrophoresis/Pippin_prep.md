Blue Pippin Protocol
====================

For selecting genomic DNA >4kb for SIP gradients

**NOTE: The Pippin manual is very detailed; if you have any questions, refer to the manual.**

**NOTE: USE ONLY GEL LOADING TIPS (extra long tips).**


## Authorship

Ashley Campbell, Chantal Koechli, and Nick Youngblut (2011-2014)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## Materials

* Blue Pippin
* 0.75% agarose cassette (PN **#:** BLF7510)
* P100 Pipette and tips
* Calibration fixture
* Pippin solutions kit (found in 4<sup>o</sup>C deli cooler in gel room). Contains:
    * Marker S1
    * running buffer
    * loading solution
    * 0.1% Tween

## Method

### Pippen calibration

  1. Pippin should be calibrated to the specific cassette you're using (and should be calibrated daily _or_ if you change the cassette to a diff type)
  1. Follow instruction in manual on pg 9-1
  2. QUICK REF: LED calibration setting should be '0.60' for dye-free cassettes (what we use)

### Prep cassette for run

  1. Check for air bubbles
  2. Check buffer levels (no well should be lass than 50% full, add running buffer if any are too low)
  3. Tilt cassette to remove bubbles from elution wells (__very important__)
  4. Put cassette in Blue Pippin machine
  5. Remove tape
  6. Remove 40uL buffer from each elution well and replace with 40uL fresh buffer
  7. Seal elution wells with adhesive strip
  8. Perform continuity test: click "test"
    1. This checks if all the lanes are electrophoresing correctly
    2. If all good, move on
    3. If not, check for bubbles, they're the most likely culprit.

### Running Protocol

  1. Select "DNASIPgradiet\_size selection" protocol from the drop down list.
  2. Identify which sample are in which lane
  3. Loading Samples
    * __NOTE:__ there are 5 wells, one whole lane is dedicated to the standard marker
    1. In a tube, mix 30uL DNA + 10uL Blue Pippin loading solution (vortex)
    2. Check to make sure all sample wells are full with electrophoresis buffer
    3. For the well that you want to add your sample to, remove 40uL of the buffer
    4. Add the 40uL sample to the well you just removed buffer from
    5. For the Standard, no need to mix with loading solution; just add 40uL std (we use Marker S1 as our standard).
  1. Shut the lid and click "start".
  2. Make sure things are going OK by checking the status bar for each lane in the upper right
  3. Run should take 2 hours & 45 minutes + an addition 45 minute waiting period to increase yield.
    * You should check on the progress occasionally to make sure things are running OK

### Elution
  * Make sure to pre-weigh and label a 2 ml tube for each sample.
  
  1. Pipette 65 uL of sample out of the elution well
  2. Add 40uL 0.1\% Tween (comes with kit) into same well
  3. Incubate for 1 min
  4. Pipette the 40 uL tween back out of elution well and add to first elution of that sample (105 uL total)
  5. Repeat for each sample

### Checking the size-selected DNA

  * The resulting DNA fragment size distribution can be checked with a gel:
    * 1% agarose in TAE buffer 
    * gel dye: Sybr Safe
    * ladder: 2-log
    * voltage: ~1.5 hours
    * volume: 3 ul of ladder, 3 ul of each sample + 6x loading dye
 * The nucleotide concentration is assess with PicoGreen assays:
   * 1 ul post-Pippin sample per PicoGreen rxn
   * PicoGreen quantifications done in duplicate for each sample (as always)

### Storage

   1. Freeze samples at -20<sup>o</sup>C
