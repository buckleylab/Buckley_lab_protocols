GitHub Basics
===

## Authorship

Nick Youngblut, Sam Barnett (2017)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)


## Online resources

* [Pro Git book](http://git-scm.com/book/en/v2)
* [top10 git tutorials](http://sixrevisions.com/resources/git-tutorials-beginners/)
* [Vogella](http://www.vogella.com/articles/Git/article.html#git)



## git basics

### Scheme 

* git is used for collaborating on the same set of files (eg., Jupyter notebooks).
  * It allows >= 1 user to edit the same files, combine changes, and revert
  back to old file versions if needed.
* The central location of the Git repos on the server is `/home/git/`.
* With git, you will make a clone (copy) of the repo, then you can edit files in the
repo, commit (save) those changes, and push (upload) them back to the central repo
(`/home/git/`).
  * Other users can pull (download) those changes to their own copy of the repo.
  * ALSO, you can easily revert back to an old version of >=1 file in the repo.


### Cloning a repo

* This will make a local copy of the repo.

1. Type: `git clone /path/to/repo/`
  * A new directory should have been created in your current working directory.


### Pulling from origin 

* This assumes that you are in a git repo.

1. Type: `git pull origin master`
  * This pulls any changes


### Commiting and pushing changes

* This assumes that you are in a git repo.
* This also assumes that you've edited >=1 file in the repo.

1. To see the changes you've made to files in the repo, type:
  * `git status` 
1. To make sure git is tracking all files in the repo, type:
  * `git add .`
1. To commit (save) all of those changes, type:
  * `git commit -a -m "I added more documentation to file X"`
    * The `-m` is used to attach a message to the commit, so you and others have some idea
    on what changed for this commit.
1. To push changes to the central repo, type:
  * `git push origin master`
    * This is assuming that you are in the `master` branch.


### Reverting back to an old version of a file

Let's assume you want to revert a file named `TEST.txt`

* If the changes have NOT been committed yet:
  * `git checkout TEST.txt`
* If you want to revert back to a version from a previous commit:
  * Get the commit ID:
    * `git log`
    * copy the string of numbers & letters following `commit`
	  * eg., `9558be93892393fa661392fb55686016f0dfb5f5`
  * View the old file: 
    * `git show 9558be93892393fa661392fb55686016f0dfb5f5:TEST.txt`
      * Use tab-completion after to colon to list files in the old commit.
  * Save the old file over the new file:
    * `git show 9558be93892393fa661392fb55686016f0dfb5f5:TEST.txt > TEST.txt`  


## Dealing with merge conflicts

* **Merge with accepting `their` edits**
  * `git checkout --theirs path/of/file`    
* **Force pull (overwrite local files)**
  * Method 1
    * Resetting your changes prior to pulling
    * steps
	  * `git reset --hard HEAD`
        * resetting your changes
	  * `git clean -f -d`		
        * [optiontal] - deletes all untracked files/directories
	  * `git pull`
  * Method 2
    * Force merging
	* steps
      * `git fetch origin master`
      * `git merge -s recursive -X theirs origin/master`
* **Abort a merge (e.g., if in conflict resolution mode)**
  * `git merge --abort`
* **Undo merge**
  * `git reset --hard HEAD`


## Branching

* listing branches (-a = remote)
  * `git branch -a`
* make new branch
  * `git branch testing`
* changing to a branch
  * `git checkout testing`
* merging (to master)
  * `git checkout master`
  * `git merge testing`
* merging 'somebranch' to master (overwrite master)
  * `git checkout master`
  * `git merge -X theirs somebranch`
* deleting a branch
  * `git branch -d testing`
* push branch to remote repo
  * `git push origin testing`
* see branch merging
  * `git branch --merged`
* see remote branches
  * `git branch -r`
* rename branch
  * `git branch -m old_branch new_branch`
* view file in another branch
  * `git show feature/CLdb_v2:bin/script.pl`
* pull a new branch from origin
  * NOTE: may have to run `git remote update` and possibly `git fetch`
  * `git checkout -b develop origin/develop`
* show files added in current branch (relative to master)
  * `git diff --name-only MYBRANCH master`


## Remote

* showing remotes
  * `git remote -v`
* pushing (updating repo)
  * `git push ./path2dir/remote_repo.git`
* fetching new changes from server
  * `git fetch origin`
* pulling (fetching and merging)
  * `git pull`
* showing origin branch
  * `git remote show origin`
* delete|remote remote (eg. origin)
  * `git remote rm origin`
* new origin
  * `git remote add origin /home/git/my_repo`
* fetching (adding) a branch from remote
  * `git checkout --track origin/feature/CLdb_v2m`
  * OR:
  * `git fetch <remote> <rbranch>:<lbranch>`
  * `git checkout <lbranch>`
  

## Undo/rollback/revert changes

* amend commit
  * `git commit --amend`
* revert un-stage file
  * `git checkout FILE`
* discard last commit (and keep working before actually commiting)
  * `git reset HEAD~`
* unstaging
  * `git reset HEAD FILE`
* revert an added file
  * `git reset FILE`
* rollback to an older commit
  * `git log`						
    * getting commit version ('commit_name')
  * `git checkout commit_name`
    * checking out old version
  * `git reset --hard HEAD^`
    * reset to last commit
* reverting to old commit
  * `git revert commit_id`
  * undo changes made during old commit but keep history (may have merge conflicts)
* find detached head changes
  * `git reflog show HEAD@{now} -10`
* revert to tag
  * `git reset --hard v0.1`
* show/view old version of file
  `git show REVISION:path/to/file`		
    * last revision: `git show HEAD~1:
    * 4th last revision: git show HEAD~4:src/main.c
* replace current copy w/ old version
  * `git show c2ab3a32900caa3f07558ddcd0a4402d7b9841c4:./bin/FILE.txt > bin/FILE.txt`
* view file in another branch
  * `git show feature/CLdb_v2:bin/script.pl`
* show all files in a commit
  * `git ls-tree --name-only -r 3d12dad913806d279c73875a52a3c0f4220dd57b`
* show files committed in old commit
  * `git show --pretty="format:" --name-only 3d12dad913806d279c73875a52a3c0f4220dd57b`
* diff (compare) file with last commit
  * `git diff HEAD@{1} filename`
* show old version of file
  * `git show HEAD^:path/to/file`


### Creating a new master remote repo on the server from already made project.

* This will make a new master remote repo from a directory that you have already made in your home directory.

1. Go into your project directory `cd /home/USER/my_project`
2. Type: `git init`
 	* Inititates project as a git repo.
3. Type: `git add .`
  	* Adds all files to tracking
  	* This would be the point where you should think about which files you don't want tracked (gitignore)
4. Type: `git commit -a -m "Initial commit"`
  	* This is your initial commit
5. Type" `git clone --bare /home/USER/my_project /home/git/my_project.git`
  	* Clones the project repo into the git directory but keeps in bare to save server space. This means it doesn't keep an image of the repo in the git directory.
6. Go into the new project directory `cd /home/git/my_project.git`
7. Type: `git init --bare --shared`
  	* This reinitializes the new master git repo such that it can be shared with everyone in the git group.
8. You may need to change the path to master in your local version of this project repo. To do this, go into your local project directory and type: `git remote add origin /home/git/my_project.git`.  You can check to see if your local repo is connecting to the correct master by running: `git remote show origin`.
9. Just to be safe, push any changes that you might have made: `git push origin master`


## Code to make using git a bit easier
  
~~~  
# alias for a pretty git log
alias git-lg="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"  
~~~
