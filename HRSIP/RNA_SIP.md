RNA Stable Isotope Probing Test Protocol
========================================

## Authorship

Chantal Koechli (2012)

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## Extract nucleic acids

> Extract nucleic acids using modified Griffith's et al. nucleic acid extraction method. 
DNase extract to remove DNA using RTS DNase™ kit by MoBio (Catalog # 15200-50)

## Gel electrophoresis to check that RNA is present

> Run aliquot of extract on gel to ensure RNA is present, using RNA sample loading buffer (Sigma Aldrich R4268). 
Can use 1% agarose get in 0.5X TAE buffer. 
Use dilutions of RiboRuler High Range RNA Ladder (Thermo Scientific #SM1821) run alongside RNA on gel to quantify RNA. 
For good band definition, run gel at 40V for 1-1.5 hours. 
Use Image J to measure pixels of standard ladder to create standard curve. 500-1000ng of RNA is needed for gradient centrifugation. 

## Gradient centrifugation: 

### Setting up a CsTFA gradient for Stable Isotope Probing

#### Gradient Media

Gradients are run in CsTFA (RNA) dissolved in gradient buffer.

1. Start by making the gradient buffer solution:
	* 15mM Tris-HCL, pH 8.0
	* 15mM EDTA
	* 15mM KCl
	
2. Decide on the average density you desire for your gradient.
	* Typical RNA run: 1.8 g/ml gradient; 62,000 rpm; 69 hrs; 20 deg. C (adapted from Whitley et al Nature Protocols RNA SIP paper)
	
3. Prepare Gradient Media solution (ie: gradient buffer + CsTFA)

	* When you add your nucleic acid it will dilute your gradient media solution, thus your gradient media solution should be dense enough to hit your target density after adding your nucleic acid sample.

	* The tubes we use are 4.7 to 4.75 ml volume. Let's say we wanted to leave room for 0.4 – 0.45 ml of nucleic acids in TE while achieving a final gradient density of 1.8 g/ml. We would figure the density of our gradient media solution as follows:

>__Total mass of gradient (without tube):__ 1.8 (g/ml) * 4.75 (ml) = 8.5500 (g)

>__Subtract the mass of the RNA solution:__ 8.5 (g) - 0.45 (g) = 8.1000 (g)

>__The desired density for solution:__ 8.1000 (g) / 4.3 (ml) = 1.8837 (g/ml)

>Thus, dissolve 8.1000g CsTFA in a total volume of 4.3 ml gradient buffer. 
	Note, if you add 8.1000g of CsTFA to 4.3 ml buffer you will end up with a total volume of more than 4.3 ml. 
	It is helpful to use a graduated tube or cylinder, start with less volume of gradient buffer than you need, 
	add and dissolve the desired amount of CsCl, and then bring it up to your final volume.


4. Fine tune the density of your gradient media solution

>Use the digital refractometer to achieve the __EXACT__ gradient media density that you desire. To use: add 5 ul solution to sample well, making sure it covers completely the prism surface (it usually does).  
Press "read" and it will give you the RI and temperature. The RI of water should be 1.3333.  
Wipe well with kimwipe after each sample. At the end of use add some water and then wipe clean. 
We have modified the surface of the prism with a piece of black electrical tape cut into the shape of a doughnut (cut with 2 cork borers of different radius). 


>First correct for the refractive index of your gradient buffer:
All salts will cause refraction, in measuring the CsTFA density of our gradient media 
we need to first account for the refraction due to the gradient buffer (ie: the Tris, EDTA, and KCl). 
We do this by measuring the refractive index of the gradient buffer and then using the following equation:

>R<sub>I corrected</sub> = R<sub>I observed</sub> - (R<sub>I buffer</sub> - 1.3333)

>__R<sub>I observed</sub>:__ Either the gradient buffer +CsTFA OR fractions (one correction before running gradient and one after)

>__R<sub>I buffer</sub>:__ Gradient buffer with formamide and NOT CsTFA


>Then to convert refractive index (R<sub>I</sub>) to CsTFA density: 

>rho = 163.559 - 262.271 (R<sub>I</sub>) + 105.281 (R<sub>I</sub>)<sup>2</sup> [at 25<sup>o</sup>C]


>Note CsTFA gets cold when it goes into solution. The equation above is only valid at 20C. Hence, you need to wait until the solution is near room temperature before measuring R<sub>I</sub>.

>The [R<sub>I corrected</sub> ] of a 1.8000 CsTFA solution is 1.3713

>The above equation may not be universal for all batches of CsTFA and gradient buffer, due to differences in chemical batches and buffer concentration (correspondence between Chantal Koechli and Tillmann Lueders). Therefore, a single point standardization must also be done when preparing each batch of CsTFA solution This is done by weighing a fixed volume of solution as accurately as possible to determine the density. The best method is to use a small volumetric flask (1-5mL). Weigh a flask, fill, and cover with stopper to prevent evaporation (weigh stopper first). Then weigh the CsTFA as accurately as possible to determine density. Then measure the refractive index and calculate density from the equation. The difference between the two density values can be used as our correction factor (when converting from RI to density). 



## Setting up the gradients

1. Dissolve CsTFA in gradient buffer to make CsTFA solution of density 1.8000g/ml, 
which has a [RI corrected] of 1.3713 (will need to solve the RI corrected/RI observed equation to know the value of RI observed you will measure with the refractrometer).
	1. The solution gets cold, so you need to wait until it is near room temperature before measuring RI. 
	2. Filter sterilize if needed
	3. Add buffer or CsTFA in small increments until RI = R<sub>I corrected</sub>

1. Add 4.3ml exactly of the CsTFA solution to the tubes.
	1. The meniscus should be around the "Beckman" label

1. Weigh and balance tubes with the CsTFA solution
	1. Note, 10ul CsTFA solution = 0.018g
	2. All tubes should be within 0.01g

1. Add RNA and TE AND 150ul Formamide (37% sln)
	1. Amount of RNA to add is 500 ng
	2. Total volume of RNA, TE, and formamide together should be 400ul

1. Add gradient buffer to fill the tubes to their necks
	1. Err on having a bit less volume so you have room to balance

1. Weigh and balance tubes by adding gradient buffer
	1. Add the black caps, and repeat weighing and balancing. When balanced, push the black caps down to seal.

1. Mix all tubes by inverting several times until no refraction waves can be seen

1. Run in ultracentrifuge 62,500 rpm, 20C, 69 hours.
	1. Put stem adapter (brown caps that look like hats) on tubes to keep stem from collapsing.
	2. Put tubes in rotor. Rotor should always be set on cloth/paper to prevent damage to the magnets underneath. 
	3. Turn on ultracentrifuge.
	4. Press door button and keep pulling on the handle until the vacuum is off.
	5. Put rotor on the spindle and depress the button in the center of the rotor. Make sure it stays depressed.
	6. Close door. Set speed, temperature and time. Press start. It will start running when the vacuum is fully established.


## CsCl gradient fractioning (5/2012)

### Setting up:

- Fill 25mL syringe with water, turn tip up and push out as much air as possible
- Hook syringe up to autopump and press run several times until there are no air bubbles in tubing
- Set up ring stand with cored stopper in it (this holds the tube for fractionation)
- Using a 21G 1&1/2 needle, cut off the plastic base of the needle\*
	- Do not cut into the medal shaft of the needle, cut the plastic as close as you can to the base of the needle. 
	  This minimizes sample loss from it getting stuck inside the shaft of the plastic part during fractionation
- With modified needle, puncture modified silicone (clear) stopper through the middle on its longest side. 

### Fractionation:

- Remove two tubes from the ultracentrifuge at a time using the forceps in the box. Keep the other tubes spinning. 
- Remove cap with forceps; avoid shaking the tube as much as possible.
- Place tube in cored stopper
- Puncture bottom of tube with needle (21G 1&1/2)that is attached to silicone stopper
- Puncture needle into the top in the curvature zone between the neck of the tube and the lip. Careful not to puncture through the back side of the tube after you push it through on the front side
- Place 96 well plate under bottom syringe. \*Should fractionate in column form for robot
- Press "run" on autopump and collect fraction in well
- Move plate so that next well is underneath the needle
- Measure RI of each fraction upon fractionation
- Repeat until all desired fractions are collected

1. Clean up fractions, using Ampure MagBead Clean-up, following manufacturer's (and robot) instructions/protocol. 

1. Ribogreen quantification of fractions. 

1. Reverse Transcribe RNA to cDNA via Invitrogen SuperScript III First-Strand Synthesis SuperMix ($391.30 for 50 rxns,)

1. PCR (16s rRNA) of cDNA products and gel to ensure product from RT reactions.


