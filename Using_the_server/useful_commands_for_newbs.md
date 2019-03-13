Useful commands for people who don't understand command line
============================================================

## Authorship

Cassi Wattenburger (2019)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)

**NOTE:** 
* all-caps mean you enter your own info into the command

## Navigating

* `cd DIRECTORY_NAME`
  * use this command to move to a directory new directory
  
* `cd ..`
  * move backwards one directory

* `cd $HOME`
  * move to your home directory
  
* `ls DIRECTORY_NAME`
  * see the contents of a directory

## Organization

* `mkdir DIRECTORY_NAME`
  * make a named directory

* `cp FILE_PATH NEW_FILE_PATH`
  * copy a file from one location to another
  
* `rm FILE_NAME`
  * delete a file (be careful...)
  
## Manipulating files
  
* `wget -q -c -O FILE_PATH`
  * for downloading files from websites, useful for getting sequencing data from the BRC

* `grep -A 1 SEARCH FILE_NAME`
  * search a file for a string or what have you

* `sed -FILE_NAME s/SEARCH/REPLACE/g`
  * to search and replace strings in a file

* `head FILE_NAME`
  * look at the top section of a file (useful for big files)
  
## Other

* `htop`
  * check processor and memory usage on the server, useful to check before you start a big job so that the server isn't overwhelmed
