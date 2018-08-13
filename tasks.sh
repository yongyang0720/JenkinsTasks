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
    echo Date: $1 >> $LOG_FILE
}

# Get the task
# Get http://localhost:5000/v1/<task_name>
get_task(){

    if [! $1] then
        return
    else
        log() "Get the task $1"
        response = curl -X Get http://localhost:5000/v1/$1
        log() response
        printf response
    if
}

# Create Task
# Post http://localhost:5000/v1/<task_name>
create_task(){

    if [! $1] then
        return
    else
        log() "Create the task $1"
        response = curl -X Post http://localhost:5000/v1/$1
        log() response
        printf response
    if

}

# Build Task
# Put http://localhost:5000/v1/<task_name>
# Header: application/json
# body:
# {"action","build"}
build_task() {

    if [! $1] then
        return
    else
        log() "Build the task $1"
        response = curl -X PUT http://localhost:5000/v1/$1 -d -d {"action" : "buile"}
        log() response
        printf response
    if

}


# Delete Task
# Delete http://localhost:5000/v1/<task_name>
delete_task() {

    if [! $1] then
        return
    else
        log() "Delete the task $1"
        response = curl -X DELETE http://localhost:5000/v1/$1
        log() response
        printf response
    if

}

# Enable Task
# Put http://localhost:5000/v1/<task_name>
# Header: application/json
# body:
# {"action","enable"}
enable_task() {

    if [! $1] then
        return
    else
        log() "Delete the task $1"
        response = curl -X PUT http://localhost:5000/v1/$1 -d {"action" : "enable"}
        log() response
        printf response
    if

}

echo "############################"
echo "     Task managerment       "
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

case $task in
1) # get the task
    task_name = ""
    while [! "task_name"]
    do
        echo "please type the task name"
        read task_name
    done
        get_task() $task_name

2)  # create the task
    task_name = ""
    while [! "task_name"]
    do
        echo "please type the task name"
        read task_name
    done
        create_task() $task_name

3)  # enable the task
    task_name = ""
    while [! "task_name"]
    do
        echo "please type the task name"
        read task_name
    done
        enable_task() $task_name

4)  # build the task
    task_name = ""
    while [! "task_name"]
    do
        echo "please type the task name"
        read task_name
    done
        build_task() $task_name

5)  # delete the task
    task_name = ""
    while [! "task_name"]
    do
        echo "please type the task name"
        read task_name
    done
        delete_task() $task_name

6) # Exit
    exit()