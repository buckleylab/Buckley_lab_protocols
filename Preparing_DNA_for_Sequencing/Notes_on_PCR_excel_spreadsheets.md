Notes on creating excel spreadsheets for PCR on the Hamilton Robot
====================================

## Author

Steven Higgins (March 2019)

## Notes

## 3/15/2019

In any .xls file for use with the "qPCR_wWorklist_altdispense" method on the Hamilton robot, the "Sample Number" column in the "sample_primer_map" tab must not go above 96 (if preparing a single PCR plate). The method on the robot likely allocates memory only for a single 96 well plate (if indicating only one PCR plate in the setup) and will therefore cause undefined behavior (i.e., accessing random elements in memory) if values increase above 96 (this is tested behavior only for single PCR plate creation). 

In my case, my script for creating .xls files for use with the Hamilton robot PCR method results in iterarting the sample number above 96.  When the Hamilton workstation read and interpreted the .xls file, the robot pipetted all of a single DNA sample well into wells of the PCR plate (when it was supposed to access 24 different samples). It also allocated primer wells incorrectly, exhausting the solution in some wells in some cases. Basically, it performed erratically. Changing only the sample numbers between 1 and 24 resolved this issue and the program ran as it should. The value of the number in the field "Primer Number" in the "sample_primer_map" tab did not affect the operation of the program.

To sum up, make sure to only label "Sample Number" between 1 and 96 in the "sample_primer_map" tab of the .xls file (and possible 1 through 192 if preparing two plates at once). The value in the "Primer Number" field does not matter and can take on values as high as 384 (tested by me).

 
