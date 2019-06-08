function gt(){
    target=$(goto)

    # Return when fzf exit
    if test -z $target
    then
        return
    fi

    if test -d $target
    then
        cd $target
    else
        cd $(dirname $target)
    fi
}
