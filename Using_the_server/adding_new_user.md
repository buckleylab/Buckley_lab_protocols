Adding a new user to the server
========================================

### Authorship:
Cassi Wattenburger (2022)

#### Updated by: 

### Description:
Add a new user to a server *properly*.

### Current user with sudo priviledges:
1. To create new user account: `sudo useradd -m username`
    * Set the password to something temporary and give it to the new user
    * Note: the -m command creates a user directory
1. Set the default user shell to bash: `sudo usermod --shell /bin/bash username`
    * This step is important or .bashrc will not work!
1. Add the user to the appropriate groups: `usermod -a -G buckley username` & `usermod -a -G ssh_with_pw username`
  

### New user:
1. Change password: `passwd` and follow prompts
2. Follow steps in xxx to set up server for use.
