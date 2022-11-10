Thermocycler Program for Illumina Miseq Barcoding
=================================================

## Authorship

Cassandra Wattenburger (2018)

## Description
This protocol lists the thermocycle conditions used for barcoding samples for eventual Illumina Miseq Sequencing.

## Printing this protocol
See Printing protocols in the README

## 16S V4 region (515F and 816R)

* 95C for 2 minutes (denaturation)
* 29 cycles of...
1. 95C for 20 seconds
2. 55C for 15 seconds
3. 72C for 10 seconds
* 55 to 95C, in 0.5C increments (melting curve)
* 72C for 5 minutes (elongation)
* 4C forever

## ITS1 region (short version)

* 98C for 30 seconds (denaturation)
* 29 cycles of...
1. 95C for 5 seconds
2. 50C for 20 seconds
3. 72C for 10 seconds
* 75 to 95C, in 0.5C increments (melting curve)
* 72C for 2 minutes (elongation)
* 4C forever

If these conditions don't give good results, try the longer protocol below.

## ITS1 region (long version)

* 98C for 2 minutes (denaturation)
* 29 cycles of...
1. 95C for 30 seconds
2. 55C for 30 seconds
3. 72C for 30 seconds
* 55 to 95C, in 0.5C increments (melting curve)
* 72C for 5 minutes (elongation)
* 4C forever

ITS is tricky and you may need to fiddle with the cycle conditions to work with your samples.
