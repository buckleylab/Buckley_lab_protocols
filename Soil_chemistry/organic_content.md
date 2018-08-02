Soil organic matter content
===========================

This is basically just a trimmed down version of the method in the
Kellogg Soil Survey Laboratory Methods Manual, Soil Survey Investigations Report No. 42
Version 5.0, pages 495-497. Some details from 
[the SFU Soil Science Lab](https://www.sfu.ca/soils/lab_documents/Estimation_Of_Organic_Matter_By_LOI.pdf)
are also used.

## Authorship

Chantal Koechli, Sam Barnett and Nick Youngblut (2015)

## Updated

Cassi Wattenburger (2018)
* more detail after talking with Akio
* corrected inconsistencies in protocol

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)


## Application

The mineral content consists of the plant ash and soil particles that remain 
after removal of organic matter. The determination of organic matter by loss on ignition
is a taxonomic criterion for organic soil materials (Soil Survey Staff, 2014).


## Method overview

### Preparation

* Dry sample overnight at 110<sup>o</sup>C and cool in dessicator.
* Place samples in clean and dry crucibles.
  * Weigh empty crucible weight
   * This is your **crucible weight (g)** 
  * Record which sample is in which crucible.
* Weigh the sample + crucible.
  * This the the **pre-ignition weight (g)**

Notes (CW):
* Crucibles that are sooty or appear unclean should be rinsed with water and fired at 400<sup>o</sup>C or higher for an hour and allowed to cool in dessicator (not sure if dessicator is necessary for this) before using.
 * This combusts any residue that might skew where final SOM calculation.
* Crucibles can be labelled with grease pens.
* Soil depth in the crucible matters, oxygen may not be able to penetrate all the way to the bottom of the crucible if the soil is too deep and the C will pyrolize instead of combust. Use less soil or a shallow crucible if you think this could be a problem.

### Loss on ignition

* Place sample in a cold muffle furnace and raise the temperature to 400<sup>o</sup>C.
  * Optimum furnace ramp time is 5<sup>o</sup>C/min.
* Heat sample overnight (16 h)
* Once complete, place samples in dessicator to cool
* Weigh the sample + crucible.
  * This the the **post-ignition weight (g)**

### Post 

* %\_organic\_matter = (pre-ignition\_weight - post-ignition\_weight) / 
(pre-ignition\_weight - crucible\_weight) * 100
* %\_mineral\_content = 100 - %\_organic\_matter

## Interferences

**NOTE:** The sample must be placed in a cold muffle furnace to prevent rapid 
combustion and sample splattering


## Safety

Use caution when the muffle furnace is hot.  Wear protective clothing and 
goggles.  Handle the heated material with tongs.


## Equipment

* Labled ceramic crucibles (make sure they are clean and dry)
* Oven, 110<sup>o</sup>C
* Dessicator (may need more than one)
* Muffle furnace, 400<sup>o</sup>C
* Electronic Balance, 0.01-g sensitivity
* A lab notebook for recording values


## Procedure

1. Weigh empty crucible and record crucible weight.
2. Place a 10 to 15 g sample in a crucible.
3. Record which crucible contains each sample.
4. Dry sample at 110<sup>o</sup>C overnight.
5. Remove sample from oven and cool in a desiccator.
6. When cool, record pre-ignition weight to nearest 0.01 g.
7. Place sample in a cold muffle furnace. Turn on furnace and start programmed run (To set program, see section "Muffle furnace program setting").
8. For muffle furnace in Lehmann Lab:
   1. Press left most button till it reads "Run".
   2. Press second button to left untill screen reads "Stat off".
   3. Press right most button once. Screen should read "Stat on".
   4. If program needs to be stopped, press second button to right once. Screen should read "Stat off".
9. Furnace should increase tempereature at a rate of 5<sup>o</sup>C/min. Then hold at 400<sup>o</sup>C for 16 h.
10. Once fernace cools to 105<sup>o</sup>C, remove samples and place in desiccator to cool.
11. When cool, record post-ignition weight to nearest 0.01 g.


# Report

Report mineral content to the nearest whole percent.


# Muffle furnace program setting

1. Press left most button untill screen reads "Prog List".
2. Press second button to run through parameters.  Parameters can be changed by pressing up or down arrow buttons (the two right buttons).
  3. Hb = OFF
  4. Hb U = 0.0
  5. rmPU = min
  6. dwLU = Hour
  7. CYCn = 1
  8. SEGn = 1
  9. type = rmPr
  10. tGt = 400
  11. rate = 5.0
  12. SEGn = 2
  13. type = dwell
  14. dur = 16.0
  15. SEGn = 3
  16. type = Step
  17. tGt = 105
  18. SEGn = 4
  19. type = End
  20. Endt = dwell

# Precision and Accuracy

Precision and accuracy data are available from the KSSL upon request.


# References

Soil Survey Staff. 2014. Keys to soil taxonomy. 12<sup>th</sup> ed. USDA-NRCS

