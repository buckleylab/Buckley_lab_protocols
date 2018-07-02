Jupyter Notebooks
=================

## Authorship

Nick Youngblut (2015)


## Printing this protocol

See **Printing protocols** in the [README](../README.md#printing-protocols-conversion-of-protocols-to-pdf)


## Starting up a notebook

### Connect to the using `ssh` and port forwarding

* You need to pick a port to forward on.
  * Pick a 4-5 digit number greater than 6666
  * For this tutorial, let's use `9999`

1. Open Terminal on your Mac 
1. Type: `ssh -L 9999:localhost:9999 USERNAME@doe-sys76.ag.cornell.edu`
  * Change `USERNAME` to your actual username for the server.

### On the server (once connected via ssh)

1. Move to the directory containing the notebook files
  * The notebook files end in `.ipynb`
1. To start the jupyter webserver, type: `screen jupyter notebook --port 9999 --no-browser`
  * You can use `screen -S MyScreenName` to name that screen instance.
    * Example: `screen -S MyScreenName jupyter notebook --port 9999 --no-browser`
      * This screen instance would thus be called `MyScreenName`
1. To detatch from the screen instance, type: `crtl+a` then `d`.
  * The screen instance will now be open until you or someone else kills the process.
  * To list the screens that you have open, type: `screen -ls`
  * To reattach to a screen, type: `screen -r SCREEN_NAME`
     * Where `SCREEN_NAME` is the screen name.
     

## Code to make starting up and connecting to a Jupyter notebook easier

Add this code to you `.profile` or `.bashrc` on your Mac or on the server
(depending on the code)


### Function to start up `jupyter notebook`


~~~
jupyter-n () {
    if [ -z "$1" ] || [ -z "$2" ]
    then
        echo "Usage: jupyter-n notebook_name port_number"
    else
        screen -S "$1.ipynb" -L jupyter notebook --no-browser --port "$2";
    fi
}
~~~


### Function for ssh'ing with port forwarding of many ports

~~~
# expand number range (eg., "8000-8002" = "8000 8001 8002")
exp_range(){
    nums=()
    i=0
    for x in $@
    do
        x=`echo $x | sed 's/-/../'`
        for y in $(eval echo {$x})
        do
            nums[$i]=$y
            i=$((i+=1))
        done
    done
}

# ssh with port forwarding
ssh_doe_ports(){
    # help
    if [ -z "$1" ] || [ $1 == '-h' ]  
    then
        echo "Usage:       ssh_port username port(s)"
        echo "Description: ssh the DOE server with port forwarding (on multiple ports)"
        echo "Example1:    ssh_port nick 7701"
        echo "Example2:    ssh_port nick 7701 7702    #(2 ports)"
        echo "Example3:    ssh_port nick 7701..7704   #(4 ports)"
        return 1
    fi

    # username
    USERNAME=$1
    shift
    SERVER="$USERNAME@doe-sys76.ag.cornell.edu"

    # number expansion
    nums=()
    i=0
    for x in $@
    do
        x=`echo $x | sed 's/-/../'`
        if [[ $x == *..* ]]
        then
            for y in $(eval echo {$x})
            do
                nums[$i]=$y
                i=$((i+=1))
            done
        else
            nums[$i]=$x
            i=$((i+=1))
        fi
    done

    # ssh command
    s1="ssh"
    s2=""
    for port_id in ${nums[*]}
    do
        s2=$s2" -L $port_id:localhost:$port_id"
    done

    echo "$s1$s2 $SERVER"
    eval "$s1 $s2 $SERVER"
} 
~~~   

 
