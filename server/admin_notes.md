Notes for Server Admins
=================

## Authorship

Sam Barnett (2018)


## Introduction

This file contains notes and functions relevant for administration of the Buckley lab server.
This list of functions is a work in progress so if something is missing please feel free to add to it.

## Creating a new user
As new people join the lab and more collaborations occur you may need to add more users to the server. 
To do so follow the following steps.

1. Log in on your account. You must have sudo privileges for this.
2. run `sudo adduser <newusername>`
    * make sure the new username is not the same as any current user.
3. When prompted type in new password.
4. Retype password when prompted again.
5. Fill out information when prompted. This is not actually required.
6. For them to log in from their own machine you must add the new user to the group ssh:
    * `sudo usermod -a -G ssh <newusername>`
7. Add new user to any other groups required:
    * `sudo usermod -a -G <groupname> <newusername>`

The new user is all set for using the server.
