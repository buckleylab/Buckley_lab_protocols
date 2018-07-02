Quantifying isotopic enrichment
===============================

## Authorship

Chantal Koechli, and Nick Youngblut (2014)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

## UC Davis Stable Isotope Facility 

* [link](http://stableisotopefacility.ucdavis.edu/)

* 5 atom-% is the upper limit of isotopic enrichment

* total carbon in sample must be in range: 200-2000 ug C

* Analytical accuracy:  0.2 permil for 13C


## DNA

### Notes

* Using glucose for a natural abundance carbon source

* 200-2000 ug C of glucose requires 500-5000 ug total weight

* MW of dsDNA nucleotides: (# nucleotides x 607.4) + 157.9

* average % C in dsDNA: ~46% (see DNA carbon % notes)

* (5 + 224.7) / (95 + 19775) 

* (X / 0.0112372 - 1) * 1000 = 40 permil

* 1 ug DNA-C in 200 ug total C
	* dilution = 1:200
	* Accuracy: 0.2 permil * 200 = +/-40 permil 
	* If using Vienna Pee Dee Belemnite (V-PDB) as standard:
		* (Rsample / Rstandard - 1) * 1000 
		* Rstandard = 0.0112372
		* (X / 0.0112372 - 1) * 1000 = 40 permil
		* X = (40/1000 + 1) * 0.0112372 = 0.0112372 
			* Rsample must be > ~0.0112 to exceed noise
	* 
	
	
## References

>El Zahar Haichar F, Achouak W, Christen R, Heulin T, Marol C, Marais M-F, et al. (2007).
Identification of cellulolytic bacteria in soil by stable isotope probing.
Environmental Microbiology 9:625–634.

	* 2 ug of gradient fraction added to tin capsule and dried for 2 hr at 60<sup>o</sup>C
	

## DNA carbon % notes

Adenine: C5H5N5
	* 44.4% C

Guanine: C5H5N5O
	* 39.7% C

Cytosine: C4H5N3O
	* 43.2% C

Thymine: C5H5N2O2
	* 48.0% C

Phosphate: PO4
	* 0% C

2-deoxyribose: C5H9O4
	* 45.1% 

deoxyribose + phosphate + base: 

	* C5H9O + PO4 + base

	* 180 + base
		* 60 C

	Adenine: 
		* 135
		* 60 C
		* Total: 215, 120 C, 55.8% C
		
	Guanine:
		* 151
		* 60 C
		* Total: 231, 120 C, 51.9% C
	
	Cytosine:
		* 111
		* 48 C
		* Total: 291, 108, 37.1% C
	
	Thymine: 
		* 125
		* 60 C
		* Total:  305, 120, 39.3% C
