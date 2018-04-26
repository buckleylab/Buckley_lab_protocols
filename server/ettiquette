General server ettiquette
=========================

The server only has so much processors, memory, hard drive space, and read/write speed. 
These guidelines will help us all effectively manage these finite resources. 


* Before running a substantial job (ie., a job that's going to use many processors or a lot of memory):
  * Check to see what jobs are currently running on the server with `htop` or `top`
  * If the job will be running for a while, contact the other users and let them know.
  * You can use the `nice` command to give your job a lower priority. 
  See [this](http://www.thegeekstuff.com/2013/08/nice-renice-command-examples/) for more information.
* Compress or delete old files. 
  * This frees up hard drive space.
  * To get file sizes: `ls -thlc`
  * To get size of directories: `du -d 1 -h`
  * To compress a file (eg., "myfile.txt"): `pigz myfile.txt`
  * To compress all files in a directory (eg., "./mydir/"): `pigz -r ./mydir/`
  * To uncompress: `pigz -d myfile.gz`
* Shutdown old Jupyter Notebook kernels.
  * This frees up memory. 
  * The variables in each kernel take up memory, and large objects (like a big dataframe) can take up a lot of memory.
  * Variables that are no longer needed can be reassigned to 0 or `NA` to free up memory. 


## Helpful commands

* Killing jobs
  * `kill [PID]`
    * PID = the job's process ID, which you can get from `htop` or `top`
  * `pgrep` and `pkill` can be used to find and kill many jobs at the same time
* Scheduling jobs to run later (eg., the middle of the night)
  * A simple way:
    * Use `sleep` to set a pause of X seconds prior to running your job.
    * For example, to run a job (eg., `raxml`) 4 hours from now:
      * `sleep 14400; raxml mytree.nwk`
  * A more complex way (but more adaptive):
    * Use `cron` to schecule a job
    * See [here](http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/) for a general introduction
