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

Cassi Wattenburger (2018, more detail)

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## Application

The mineral content consists of the plant ash and soil particles that remain 
after removal of organic matter. The determination of organic matter by loss on ignition
is a taxonomic criterion for organic soil materials (Soil Survey Staff, 2014).

## Materials

* soil (sieved to 2mm or finer)
* crucibles or metal tin (labeled)
* drying oven (Lehman lab, room 916)
* muffle furnace (Lehmann lab, room 916)
* heat-resistant gloves
* tongs
* dessicator with dessicant
* scale (0.001 g sensitivity)
* lab notebook and pen for recording values

## Interferences

**NOTE:** The sample must be placed in a cold muffle furnace to prevent rapid 
combustion and sample splattering

## Safety

Use caution when the muffle furnace is hot.  Wear protective clothing and 
goggles. Handle the heated material with tongs.  
  
Indicating dessicant (blue/pink) contains cobaltous chloride which is a potential carcinogen. Wear gloves when handling and avoid inhaling by handling in a fume hood (drierite can produce a lot of dust when poured).

## Procedure

1. Heat clean and empty crucibles in muffle furnace at 400<sup>o</sup>C for 1 hr then cool to 105<sup>o</sup>C.
2. Move empty crucibles to dessicator and allow to cool to room temp (~30 min to 1 hr).
3. Weigh empty crucible and record **crucible weight** to nearest 0.001 g.
4. Place a 10 to 15 g soil sample in each crucible.
   * A minimum of 5 g of sample can be used to take the measurement
5. Record which crucible contains each sample.
6. Dry sample at 105<sup>o</sup>C overnight.
7. Remove sample from oven and cool in a desiccator to room temp (~30 min to 1 hr).
6. When cool, record **pre-ignition weight** of dried sample and crucible to nearest 0.001 g.
7. Place sample in a cold muffle furnace. Turn on furnace and start programmed run (To set program, see section "Muffle furnace program setting").
   * Samples should be heated at 400<sup>o</sup>C for 16 hrs
8. For muffle furnace in Lehmann Lab:
   * Make sure PID and program is correct before running.
   1. Press left most button till it reads "Run".
   2. Press second button to left untill screen reads "Stat off".
   3. Press right most button once. Screen should read "Stat run".
   4. If program needs to be stopped, press second button to right once. Screen should read "Stat off".
9. Furnace should increase tempereature at a rate of 5<sup>o</sup>C/min. Then hold at 400<sup>o</sup>C for 16 h.
10. Once fernace cools to 105<sup>o</sup>C, remove samples and place in desiccator to cool.
11. When cool, record **post-ignition weight** to nearest 0.001 g.

### SOM and mineral content calculation

* %\_organic\_matter = (pre-ignition\_weight - post-ignition\_weight) / 
(pre-ignition\_weight - crucible\_weight) * 100
* %\_mineral\_content = 100 - %\_organic\_matter

## Notes
* Even if the soils were previously dried, they still need to be dried overnight to evaporate hygroscopic water.
* Soil depth in the crucible matters, oxygen may not be able to penetrate all the way to the bottom of the crucible if the soil is too deep and the C will pyrolize instead of combust. Use less soil or a shallow crucible if you think this could be a problem. Do not use crucible lids.
* Samples are cooled in a dessicator to prevent moisture from hygroscopically attaching to the crucible/soil.

# Muffle furnace PID setting

The PID is a set of algorithms that ensures the furnace does not over or undershoot the target temperatures while running. The algorithms differ based on the maximum temperature. There is a laminated scrap of paper in the drawer below the furnace with various PID settings recorded. The settings below are for 450<sup>o</sup>C (close enough to our max temp).

1. Press left most button until screen reads "Pid List"
2. Press the second button to run through parameters. Parameters can be changed by pressing up or down arrow buttons (the two right buttons).
  1. G.SP = 800
  2. Pb = 9 
  3. t1 = 194
  4. td = 32

# Muffle furnace program setting

1. Press left most button until screen reads "Prog List".
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


# References

Soil Survey Staff. 2014. Keys to soil taxonomy. 12<sup>th</sup> ed. USDA-NRCS

