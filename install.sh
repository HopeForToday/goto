#!/bin/bash

CONFIG_DIR=~/.config/goto
DATA_DIR=~/.local/share/goto
FILE_LIST_PATH=$DATA_DIR/files
IGNORE_FILE_PATH=$CONFIG_DIR/ignore
CONFIG_FILE_PATH=$CONFIG_DIR/config.json


#######################################
# Arguments:
#   $1 dir
#   $2 description
#######################################
_check_dir() {
    if [ -d $1 ]
    then
        echo "Find existing $2 dir: $1"
    else
        mkdir $1
        echo "Not find $2 dir: $1, created it"
    fi
}


#######################################
# Arguments:
#   $1 file path
#   $2 description
#######################################
_check_file() {
    if [ -f $1 ]
    then
        echo "Find existing $2 file: $1"
    else
        touch $1
        echo "Not find $2 file: $1, created a empty one"
    fi
}

_check_dir $CONFIG_DIR config
_check_dir $DATA_DIR data
_check_file $CONFIG_FILE_PATH config
_check_file $FILE_LIST_PATH 'file list'
_check_file $IGNORE_FILE_PATH ignore


echo
echo "Installing goto..."
pip install --user .
echo

printf "Installation complete!\n"
