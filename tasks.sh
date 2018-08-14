#/bin/bash

#
###########################################################################################
# Tasks Manage Scripts
# Author: Yong
###########################################################################################

# Get current working directory

if [ -z "$LOGDIR" ]; then
    BASEDIR = `dirname $0`
    LOGDIR = $BASEDIR/log
    export LOGDIR

fi

LOG_FILE = $LOGDIR/task_shell.log

log() {
    Date = `date "+%Y%m%d%H%M%S"`
    echo Date: $1 >> $LOG_FILE $LOG_FILE
}

# Get the task
# Get http://localhost:5000/v1/<task_name>
get_task(){

    if [! $1]
    then
        echo "Task name should not be null"
        return
    else
        log() "Get the task"
        response = curl -X Get http://localhost:5000/v1/$1
        log() $response
        echo $response
    fi
}

# Create Task
# Post http://localhost:5000/v1/<task_name>
create_task(){

    if [! $1]
    then
        echo "Task name should not be null"
        return
    else
        log() "Create the task"
        response = curl -X Post http://localhost:5000/v1/$1
        log() $response
        echo $response
    fi
}

# Build Task
# Put http://localhost:5000/v1/<task_name>
# Header: application/json
# body:
# {"action","build"}
build_task() {

    if [! $1]
    then
        echo "Task name should not be null"
        return
    else
        log() "Build the task"
        response = curl -X PUT http://localhost:5000/v1/$1 -d -d {"action" : "buile"}
        log() $response
        echo $response
    fi
}


# Delete Task
# Delete http://localhost:5000/v1/<task_name>
delete_task() {

    if [! $1]
    then
        echo "Task name should not be null"
        return
    else
        log() "Delete the task"
        response = curl -X DELETE http://localhost:5000/v1/$1
        log() $response
        echo $response
    fi

}

# Enable Task
# Put http://localhost:5000/v1/<task_name>
# Header: application/json
# body:
# {"action","enable"}
enable_task() {

    if [! $1]
    then
        echo "Task name should not be null"
        return
    else
        log() "Delete the task"
        response = curl -X PUT http://localhost:5000/v1/$1 -d {"action" : "enable"}
        log() $response
        echo $response
    fi

}

while true
do
    echo "############################"
    echo "     Tasks managerment       "
    echo "############################"
    echo "please enter your choise"
    echo "1: Get the task"
    echo "2: Create the task"
    echo "3: Enable the task"
    echo "4: Build the task"
    echo "5: Delete the task"
    echo "6: Exit"
    echo "-----------------------------"
    read task
    task_name = ""

    case $task in
    1) # get the task
        while [! $task_name]
        do
            read -p  "please type the task name" task_name
        done
        get_task() $task_name
        return
        ;;

    2)  # create the task
        while [! $task_name]
        do
            read -p  "please type the task name" task_name
        done
        create_task() $task_name
        return
        ;;

    3)  # enable the task
        while [! "task_name"]
        do
            read -p "please type the task name" task_name
        done
        enable_task() $task_name
        return
        ;;

    4)  # build the task
        while [! $task_name]
        do
            read -p "please type the task name" task_name
        done
        build_task() $task_name
        return
        ;;

    5)  # delete the task
        while [! $task_name]
        do
            read -p "please type the task name"  task_name
        done
        delete_task() $task_name
        return
        ;;

    6) # Exit
        exit()
        ;;

    *) # whrong input, try it agian
        echo "wrong input, please choose it again"
        continue

    esac
done