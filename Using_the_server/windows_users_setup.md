Getting set up on the server if you're a Windows user
========================================

### Authorship:
Cassi Wattenburger (July 2018)

### Updated by:

### Description:
This guide is to help new server users get started on a Windows device. It assumes little knowledge of command line or how servers work.

## Connect to the server
1. Have someone already on the server make you an account.
2. Download and install PuTTY (https://www.chiark.greenend.org.uk/~sgtatham/putty/)
   - PuTTY is how you log in to the server.
3. Connect to the server by entering in the following info:
   - Host name: doe-sys76.ag.cornell.edu
   - Connection type: SSH
   - Click 'Save' so that you don't have to retype every time
   - Click 'Open' to log in
  
Tip: To save yourself a little time when you log in, load your saved session, go to Connection > Data, then type your username into the auto-login username box, then save the session again.

## Install Anaconda
Anaconda is used to create environments on the server. An environment is an independent instance of whatever programs and packages you like.
This way you can have two versions of the same software installed at the same time for different projects, 
but they won't interfere with one-another.

1. In command line:\
 `bash Anaconda-latest-Linux-x86.sh`   
 or\
 `wget "https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe"`
   - **Note:** The second link may be outdated, you should use the latest Anaconda version link.
2. To make sure Anaconda installed correctly:
 `conda list`
   - All of the packages available through Anaconda should be listed
Useful Anaconda commands:
   - Create new environment
   `conda create -n NAME_ENV python=VERSION_NUMBER`
   - Delete environment
   `conda remove -NAME_ENV --all`
   - Activate environment
   `source activate NAME_ENV`

## Install Qiime2
Qiime2 is a software that you can use to analyze sequence data. 
   - Use the instructions found here: https://docs.qiime2.org/2018.2/install/native/#install-qiime-2-within-a-conda-environment
     - Use the Linux instructions
  
## Setup Jupyter Notebooks Screens
Jupyter is a scripting tool that you can use to run code from various languages. This code will allow you to more easily create screens of Jupyter notebook.
1. Edit the .bashrc
   `nano .bashrc`
   - **Don't delete or change any of the other code here.** Use the down arrow to move to the bottom of the file.
2. Write code for starting screens of Jypyter
   `# jupyter notebook command`
   `jupyter-n () {`
     `if [-z "$1"]|[-z "$2"]`
     `then`
       `echo "Usage: jupyter-n notebook_name port_number"`
      `else`
       `screen -S "$1.ipynb" -L jupyer notebook --no-browser --port "$2"`
      `fi`
     `}`
3. **Cntrl+X** to save and exit. The console will ask you if you want to overwrite and/or what to name the file.
4. Log out and then back in to the server and this should be functional.
 
## Port forwarding Jupyter Notebooks
Port forwarding creates a user-interface of Jupyter on your web browser.
1. Configure PuTTY for port forwarding
   - In PuTTY navigate to "SSH" > "Tunnels" in the left-hand list of directories.
   - Source port: any number of your choosing that is 4 digits and ends in 0. This needs to be a number someone else isn't already using.
   - Destination: localhost:PORT_NUMBER (the same port number as chosen above)
   - Click "Add"
   - Navigate back to "Session" and click "Save"
2. Start a screen
   - `jupyter-n NOTEBOOK_NAME PORT_NUMBER`
   - If this doesn't work, something went wrong with the Jupyter Notebook setup and you'll need to doublecheck and edit the .bashrc
   - Write down the token given.
   - The screen exists whichever directory you intitiated it in.
3. Interact with your screen using port-forwarding
   - In web browser type locahost:PORT_NUMBER
   - Log in, you'll need that token.

About screens:
   - Detach a screen from the server with **CTRL+A+D**
   - Reattach the screen with `screen -r`
   - Kill an attached screen with **CTRL+C**
   - See which screens are currently active `screen -ls`
  
## Port forwarding R Studio
1. Configure PuTTY for port forwarding
   - In PuTTY navigate to "SSH" > "Tunnels" in the left-hand list of directories.
   - Source port: 8787
   - Destination: localhost:8787
   - Click "Add"
   - Navigate back to "Session" and click "Save"
2. In web browser go to localhost:8787 and log in using your server credentials.
 - There are many packages already installed for R on the server globally, but you should reinstall the ones you plan to use. Reinstallation will put the packages in a local directory, and R will look there first to call the package. These packages won't update or change if the server packages are updated.
 - You could make individual library paths for each project if you want to use different versions of each package. In that case you need to make a directory for those packages and specify the path when installing and loading. This gets complicated quickly though and should probably be avoided.

## Other helpful tools
1. FileZilla
   - Allows you to easily transfer files from the server to your computer and vice-versa.
2. Xming
 
  
 
