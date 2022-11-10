#! usr/bin/env python

import sys, os

Usage = """Tidy picogreen assay output from SoftMax Pro.
This script will:
1. Remove duplicate and empty rows
2. Remove header and footer lines
3. Save the output in a new file called tidy_filename

Arguments:
Arg1: Name of file to tidy
Arg2: Number of header lines
Arg3: Number of footer lines

PROTIP: To process many .txt files at once run the following in terminal:
for FILE in *.txt; do python ~/scripts/picogreen_tidy.py $FILE X Y; done
Replace X and Y with header and footer numbers.

By Cassi Wattenburger 04/09/21"""

# Check for arguments
if len(sys.argv) < 4:
   print(Usage)

else:
   # Define arguments
   infilename = sys.argv[1]
   header = int(sys.argv[2])
   footer = int(sys.argv[3])
   # Read picogreen file
   with open(infilename, encoding="utf8", errors='ignore') as i:
      infilelines = i.readlines()
   # Skip duplicate and empty rows
   linenum = 0
   for line in infilelines:
      if len(line) < 1:
         pass
      elif len(line) > 1:
         first = line[1]
         if first.isspace() == True:
            pass
         else:
         # Remove header and write to temporary file
            linenum += 1
            if linenum > header:
               cleanline = line.replace('\00', '') # removes NULL characters
               with open("temp.txt", "a") as o:
                  o.write(cleanline)
            else:
               pass
   # Remove footer
   with open("temp.txt") as t:
      outfilelines = t.readlines()
   outfilelines = outfilelines[:(len(outfilelines)-footer)]
   # Create final file name
   outfilename = "tidy_"+infilename
   # Write final file
   for outline in outfilelines:
      with open(outfilename, "a") as x:
         x.write(outline)
   # Delete temp file
   os.remove("temp.txt")

# End of script
