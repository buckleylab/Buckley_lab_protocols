Overview of steps to prepare DNA for Sequencing
=======================

## Authorship

Cassi Wattenburger (2019)

## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## Notes

* See linked, detailed protocols for more information about each step

## Method

1. Dilute each DNA sample to same concentration
    * 2 ng/uL recommended
    * can use robot method "plate_pooling.med" to automate

2. [Amplify each sample using appropriate barcoded primers (Kozich et al 2013 AEM)](./PCR/PCR_with_barcoded_primers.md)
    * use robot method "qPCR_wWorklist_altdispense.med"
    * use [this spreadsheet](./PCR/template%20PCR%20robot%20sheet.xls)
    * doing reactions in triplicate recommended, aim for at least duplicate succesful reactions for each sample

3. Pool triplicate PCR reactions
    * use robot method "plate_pooling.med"

4. Normalize DNA concentration
    * SequalPrep™ Normalization Plate Kit, cat no. A1051001, Thermo Fisher Scientific

5. Concentrate library to 100 uL per 96 samples using speed vac

6. [Run library on 1.5% low melt agarose gel and select band of appropriate length](https://github.com/buckleylab/Buckley_lab_protocols/blob/master/gel_electrophoresis/gel_extraction.md)

7. Clean up DNA from gel
    * Wizard® SV Gel and PCR Clean-Up System, cat no. A9281, Promega
	
8. [Pico quantitate and concentrate sample to ~5 ng/uL](https://github.com/buckleylab/Buckley_lab_protocols/blob/master/robot/picogreen_protocol.md)

9. Send library to Cornell BRC for sequencing
