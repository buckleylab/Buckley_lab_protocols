Dissolved Organic Carbon
========================

These are instructions to measure DOC/TN on the Shimadzu TOC-VCPN and attached TNM-1 in the Goodale lab (Corson E212). Make sure to ask permission from Christine Goodale before using the TOC analyzer.

## Authorship
Cassi Wattenburger (Feb 2020)

## Updated

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## Materials
 
* TOC analyzer
* Ultra Zero Air (Airgas AI UZ300)
* 10 mL test tubes (acid-washed/fired)
* 40 mL vials, flat bottomed (acid-washed/fired)
* parafilm
* DOC samples
* Standards (see below)
* ddH2O
 
## Standards

**Note:** All glassware used to prepare/store standards must be acid-washed (dishwasher) and/or fired at 425°C for at least 1 hr. The Lehmann lab (Bradfield 916) has a muffle furnace that can be used. Do not fire volumetric glassware. 

**Note:** Stock solutions must be made fresh weekly and stored at 4°C, do not autoclave

**Note:** the NPOC and TON standards should be made together in the same solution

* Blank: 0.05 M HCl (1 full 40 mL vial needed per full run)
 * 4.13 mL 12.1 M HCl (concentrated) into 995.87 mL ddH2O
* NPOC std: 100 and 10 ppm KHP in 0.05 M HCl (3 full 40 mL vials needed per full run)
  * 1000 ppm = 1 g in 1000 mL 0.05 M HCl
  * 100 ppm = 15 mL of 1000 ppm stock into 135 mL 0.05 M HCl
  * 10 ppm = 15 mL of 100 ppm solution into 135 mL 0.05 M HCl
* TON std: 100 and 10 ppm KNO3 in 0.05 M HCl (with KHP)
 * see above
* External stds: 1 mM alanine, glucose, glycine in 0.05 M HCl (1 half-full 40 mL vial each per run)
  * 10 mM Alanine stock: 0.0891 g in 100 mL 0.05 M HCl
  * 10 mM Glycine stock: 0.0751 g in 100 mL 0.05 M HCl
  * 10 mM Glucose stock: 0.180 g in 100 mL 0.05 M HCl
  * 1 mM: 2 mL in 18 mL 0.05 M HCl

## Preparing standards and samples
**Note:** Glassware must be acid washed and/or fired (see above note).

**Note:** Before you can run your samples, you need to know what % 2M HCl must be added to bring the sample to pH 2 so you can program the TOC analyzer to acidify the samples appropriately. Acidification removes non-organic C from the sample, such as carbonates.

1.	Prepare standards from stock solutions (ie 1000 ppm KHP/KNO3 and 10-100 mM external stds), diluted in 0.05 M HCl
2.	Before the run, thaw samples if frozen
3.	Samples can be manually diluted beforehand or auto-diluted during the run. If sample is limited, manually dilute and reserve extra at 4°C. The extra can be used the next day if the run fails
 a.	**Note:** Do not freeze/thaw DOC samples more than once because it causes flocculation. Ideally, DOC samples are never frozen but this is not always possible.
4.	Place 7-8 mL of each sample into test tubes, position the test tube in the center of a 40 mL vial and parafilm the top to keep it in position.
5.	Transfer 40 mL of each blank or standard into the needed number of vials, parafilm the top

## Turning on the TOC analyzer
1.	Turn on E-Pure water system and wait until it reaches 18 mV before using any water from it
a.	Remember to turn it off before you leave after starting the run
2.	Open the software, TOC-Control V > Sample Table Editor, press OK (no password)
3.	Make new run file, File > New > Sample Run > OK > (place in your folder) > Save
4.	Turn on the gas tank (turn left) next to the machines, pressure should be set to ~50 PSI
5.	Turn on the TOC-VCPN (bottom-right button) and TNM-I (switch on side) machines
6.	Click the lightning bolt button in the software and allow the instrument to warm up ~1 hr
 a.	Instrument > Background Monitor to check progress, all monitored systems should have a green check mark when ready
7.	Check the water containers inside the TOC-VCPN, fill with ddH2O using a squirt bottle if necessary
8.	Check the halogen scrubber for green corrosion, if it is nearing the top of the column ask for assistance to replace the column
9.	Check gas flow, the TOC-VCPN should be at ~130 and the TNM-I should be at ~0.5
 a.	**Note:** Software must be linked via step 6 before gas flow will begin
10.	Check the liquid containers next to the TOC-VCPN, behind the carousel, and on the floor
 a.	The large container behind the carousel should be full of ddH2O before starting a run
 b.	The container on the floor should be empty if it looks full (wash discharge)
 c.	The ddH2O and HCl containers empty slowly, but should still be checked before each run and refilled if needed
11.	Run maintenance, Instrument > Regeneration of the TC Catalyst and … > Residue Removal after warmup is complete
12.	Sign into the logbook, make sure to note the PSI of the gas tank

## Making calibration curve files
**Note:** This only needs to be done once and then you can use the method files for all future runs

1.	Make one calibration curve each for NPOC and TN measurements
2.	Make a method file, File > New > Calibration Curve > ✓ Edit Manually > ✓ Dilution from standard > Analysis (choose NPOC or TN) > (Name whatever you want) > ✓ Multiple injections > Calculation method: Linear, do not check Zero Shift > (Name the file and place in your folder)
3.	Options to select:
  a.	No. injections: 3/5
  b.	Lower the number of washes if sample is limited
  c.	Enter each standard concentration (as a dilution factor of the 100 or 10 ppm std)
  i.	Typical curve: 100, 50, 25, 10, 5, 0
  d.	Injection volume: 80 uL
  e.	No acidification (already in 0.05 M HCl)
4.	Finish making the calibration curve

## Making sampling method files
**Note:** “Dilution” refers to pre-diluted sample dilution that the software will correct for, while “auto-dilute” refers to the amount the machine should dilute the sample before running it. Don’t mix them up!

**Note:** I recommend making an external std method (no auto-dilution, no acidification), an internal check method (auto-dilute the 100 ppm std by 4 [25 ppm], no acidification), and a sample method (no auto-dilution, acidify to predetermined %).

1.	File > New > Method > OK > Next > Analysis: NPOC/TN
2.	Choose appropriate calibration curves (see above)
3.	Name the method file appropriately
4.	3/5 injections, 80 uL injections
5.	Set auto-dilution and acidification as appropriate for the analysis type

## Setting up/starting the run
1.	Place your blank, standards, and samples in the carousel
2.	Put both of your calibration curves as the first two entries into the sample editor, Insert > Calibration Curve > (appropriate .cal file), enter the appropriate vial positions on the carousel according to the dilution scheme
  a.	Note: use the first 100 ppm std vial for one calibration curve, and the second for the other calibration curve to ensure you have
  enough std for each
3.	Insert your external checks into the next three entries, using the external std method, enter appropriate vial positions from the carousel
4.	Insert a blank using the internal check method file, use the 0.05 M HCl blank vial
5.	Insert an internal standard (25 ppm) using the internal check method, use the 3rd 100 ppm vial
6.	Insert your first sample using the sample method that you made, copy/paste (Paste > Paste Samples) this row to populate the spreadsheet, intersperse an internal std check every 10 or so samples (this will allow you to calculate and correct for instrument drift)
7.	To delete a row, use cut
8.	Got to View > ASI/8Port Sampler Vials… to enter missing vial position information from copy/paste, double check everything before starting the run
9.	To start the run, Press the green stoplight button, choose whether the instrument stays on or shuts down after the run is complete (keep it on if you will be running back to back), ✓ External acid addition
10.	To watch progress, View > Sample Window

## Ending the run
1.	When the run is complete, remove your samples from the carousel and turn the gas tank off.
2.	To export your data, File > ASCII Export… > Export Sample Table and Each Injection
