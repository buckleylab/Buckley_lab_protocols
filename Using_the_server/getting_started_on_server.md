Server setup for new users (on Windows)
========================================

### Authorship:
Cassi Wattenburger (July 2018)

#### Updated by: 
Cassi (Sept 2019)

### Description:
This guide is to help new users get started on the server on a Windows computer. It assumes little knowledge of command line, linux, etc.

## Connect to the server
1. Have someone already on the server make you an account.
2. Download and install PuTTY (https://www.chiark.greenend.org.uk/~sgtatham/putty/)
   - PuTTY is how you login and interact wtih the server.
3. Connect to the server by entering in the following info:
   - Host name: doe-sys76.ag.cornell.edu
   - Connection type: SSH
   - Click 'Save' so that you don't have to retype every time
   - Click 'Open' to log in
  
Tips: 
* Auto-username: To save yourself a little time when you login, load your saved session, go to Connection > Data, then type your username into the auto-login username box, then save the session again.
* Double click a saved session and it will automatically start.

## Install Anaconda
Anaconda is used to create environments on the server. An environment is an independent instance of whatever programs and package versions you need for a given project. This way you can have two or more versions of the same software installed in different environments but they won't interfere with one-another.

1. Download the Linux Anaconda installer:\
   `wget "https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh"`
    - This link may be out of date. Check https://www.anaconda.com/distribution/ for the latest download link.
2. Install:\
   '`bash Anaconda3-2019.07-Linux-x86_64.sh`
   - Follow the prompts.
   - If the above link was out of date, you'll need to replace the .sh file name in the command with the name of the file you downloaded instead.
3. To make sure Anaconda installed correctly:\
 `conda list`
   - All of the packages available through Anaconda should be listed. If not, something went wrong.
   
Useful Anaconda commands:
   - List existing environments\
   `conda info --envs`
   - Create new environment\
   `conda create -n NAME_ENV python=VERSION_NUMBER`
   - Delete environment\
   `conda remove -NAME_ENV --all`
   - Activate environment\
   `source activate NAME_ENV`
   - Deactivate an environment
   `source deactivate`

## Install Qiime2
Qiime2 is a software that you can use to process sequence data. It is a wrapper for many different tools and makes them all easier to use together.
   - Use the instructions found here:\
   https://docs.qiime2.org/2019.7/install/native/
     - Use the Linux instructions. This link may be out of date, in that case use whatever installation instructions are most recent.
  
## Make Jupyter Notebook screens command
Jupyter Notebook is a scripting tool that you can use to run code from various languages. This step will create a command to allow you to easily create screens of Jupyter Notebook.
1. Edit the .bashrc\
   `nano .bashrc`
   - **Don't delete or change any of the other code here.** Use the down arrow to move to the bottom of the file.
2. Enter the following:
   ```
   # jupyter notebook command
   jupyter-n () {
     if [-z "$1"]|[-z "$2"]
     then
       echo "Usage: jupyter-n notebook_name port_number"
      else
       screen -S "$1.ipynb" -L jupyter notebook --no-browser --port "$2"
      fi
     }
   ```
3. **Cntrl+X** to save and exit. The console will ask you if you want to overwrite (Y) and what to name the file (don't change).
4. Log out and then back in to the server.

* See [these instructions](https://github.com/buckleylab/Buckley_lab_protocols/blob/master/Using_the_server/jupyter_notebooks.md) for more code to expand the number of jupyter-n screens you can have open at once.
 
## About screens
Screens allow you to continue long-running processes even when you aren't logged-in or connected to the server (thus protecting your work while it's still running). You can also use screens to run multiple processes on the server at once. An attached screen can be intereacted with through the PuTTY terminal. A detached screen cannot be interacted with in this way, but will run independently and will not stop running if you disconnect. Screens retain whichever directory location and conda environment you opened them in.

   - See which screens are currently active\
   `screen -ls`
   - Create a named screen\
   `screen -S NAME_SCREEN`
   - Detach a screen from the server with **CTRL+A+D**
   - Reattach the screen\
   `screen -r`
   - Kill an attached screen with **CTRL+C** then **Y**
   - Kill detached screen\
   `screen -X -S NAME_SCREEN quit`

## Port forwarding Jupyter Notebooks
Port forwarding creates a user-interface of a Jupyter Notebooks screen on your web browser.
1. Configure PuTTY for port forwarding
   - In PuTTY, select the session that the port will be attributed to
   - Navigate to "SSH" > "Tunnels" in the left-hand list of directories.
   - Source port: any number of your choosing that is 4 digits and ends in 0. This needs to be a number someone else isn't already using.
   - Destination: localhost:PORT_NUMBER (the same port number as chosen above)
   - Click "Add"
   - Navigate back to "Session" and click "Save"
2. Start a screen\
   `jupyter-n NOTEBOOK_NAME PORT_NUMBER`
   - If this doesn't work, something went wrong with the Jupyter Notebook setup and you'll need to doublecheck and edit the .bashrc
3. Interact with your screen using port-forwarding
   - Copy/paste the token given when the screen is started into your web browser.
   - See tokens for active juputer notebook screens with `jupyter notebook list`
  
## Port forwarding R Studio
1. Configure PuTTY
   - In PuTTY navigate to "SSH" > "Tunnels" in the left-hand list of directories.
   - Source port: 8787
   - Destination: localhost:8787
   - Click "Add"
   - Navigate back to "Session" and click "Save"
2. In web browser go to localhost:8787 and log in using your server credentials.

There are many packages already installed for R on the server, but you should reinstall the ones you plan to use. Reinstallation will put the packages in a local directory specific to you, and R will look there first to call the packages. These packages won't update or change if the server packages are updated.

You could make individual library paths for each project if you want to use different package versions. In that case you'll need to make a directory for each R library and specify the path to the directory when installing and loading the packages. However, this gets complicated quickly and should probably be avoided.

Unfortunately, you can't create a screen of R Studio. However, you can create a screen of R in the terminal. Just type:\

`screen -S SCREEN_NAME /usr/bin/R`

## Other helpful tools
1. FileZilla
   - Allows you to easily transfer files from the server to your computer and vice-versa.
2. Xming
   - Alternative to PuTTY with graphical displays.
