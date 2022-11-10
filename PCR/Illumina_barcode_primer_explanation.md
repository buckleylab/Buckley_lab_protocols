Construction of barcoded primers used for Illumina amplicon sequencing
=================================

## Author

Sam Barnett (January 2017)

## Additionally modified by:

Roli Wilhelm (2017)

Cassi Wattenburger (2019, 2022)

# Primer construction

PCR primers are made up of 5 parts:

    Illumina_adapter    Barcode(8-bases)    Pad(10-bases)   Linker(2-bases) PCR_primer

For example, SA501 from Kozich et al. 2013 is made of:

    AATGATACGGCGACCACCGAGATCTACAC   ATCGTACG    TATGGTAATT  GT  GTGTGCCAGCMGCCGCGGTAA
    
Sequencing primers are only made of the Pad, Linker and PCR_primer:

    Pad(10-bases)   Linker(2-bases) PCR_primer
    
For example the Kozich et al. 2013 forward sequencing primer is:
    
    TATGGTAATT  GT  GTGTGCCAGCMGCCGCGGTAA
    
The indexing primer is the reverse compliment of the reverse sequencing primer.
For examole the Kozich et al. 2013 indexing primer is:

    ATTAGAWACCCBDGTAGTCCGGCTGACTGACT

# Primer sequences for 16S and ITS

See [this spreadsheet](linky).


# Citations:

Kozich JJ, Westcott SL, Baxter NT, Highlander SK, Schloss PD. Development of a Dual-Index Sequencing Strategy and Curation Pipeline for Analyzing Amplicon Sequence Data on the MiSeq Illumina Sequencing Platform. Applied and Environmental Microbiology. 2013;79(17):5112-5120. doi:10.1128/AEM.01043-13.
