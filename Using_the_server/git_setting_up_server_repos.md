Setting up master git repositories on the server
========================================

## Authorship:
Sam Barnett (February 2018)

## Updated by:

=============
# Description
This file explains how to set up local master git repositories on the
Buckley lab server. This should work on your local machine too, but you'll 
have to change the file paths.
============

### Creating a new master remote from scratch
This will create a new master remote directory from scratch. This should be done
at the begining of a project, before the project directories have been made.
You must be part of the group "git" in order to do this on the server.

1. Make a bare directory in our server git repo directory (`/home/git/`)
   - i.`cd /home/git`
   - ii. `mkdir PROJECT_NAME.git`
	iii. `cd PROJECT_NAME.git`
	iv. `git --bare init --shared`
2. Clone this repo into your local directory
	i. `cd /home/USERNAME/git_repos`
	ii. `git clone /home/git/PROJECT_NAME.git`
		*You may get a message saying you just cloned an empty repo*
3. You now have a master and local repo for your project. Before moving on, you should make your first commit and push that to the master.
	i. `cd /home/USERNAME/git_repos/PROJECT_NAME`
	ii. `touch README`
	iii. `git add README`	*Adds the file `README` to tracking*
	iv. `git commit -a -m "Inital commit"`
	v. `git push origin master`

You are now all set!

### Creating a new master remote repo on the server from started project directory.
This will make a new master remote repo from a directory that you have 
already made in your home directory. This is good if you want to begin keeping
track of changes to a directory of an already started project.

1. Initiate your project directory as a git repo
	i. `cd /home/USERNAME/PROJECT_NAME`
	ii. `git init`	*initiates git repo*
	iii. `git add .`	*adds all current files to tracking*
		* Note: this would be the time to think about which files you want to track and which you dont (`gitignore`).
	iv. `git commit -a -m "Initial commit"`
2. Clone and reinitalize this local repo into the master repo directory on the server
	i. `cd /home/git`	
	ii. `git clone --bare /home/USERNAME/PROJECT_NAME /home/git/PROJECT_NAME.git`	*Clones the project into `/home/git/` but bare so no files are actually cloned*
	iii. `cd PROJECT_NAME.git`
	iv. `git init --bare --shared`	*Reinitializes the repo*
3. Change the origin path of your local repo to the new master repo
	i. `cd /home/USERNAME/PROJECT_NAME`
	ii. `git remote add origin /home/git/PROJECT_NAME.git` *Changes the origin path to the new master*
4. Check that it works
	i. `git remote show origin`	*Displays the path to the repo origin, should be /home/git/PROJECT_NAME.git*
	ii. `git push origin master`	*Make sure you can push to the master*

You are now all set!
