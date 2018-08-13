## About

This application is designed to manage the jenkins tasks. It provides create, update, delete and retrieve API to handle the tasks.
Also it provide shell scripts to manager the tasks by tasks.sh.

## How to use it
To configure jenkins serve and logs, please modify the conf/App.ini file. the default is locahost.

If in Linux system, make sure python is right installed.

    $ ssh joe@206.189.129.179 -p 6621
    $ sudo pip install flask, python-jenkins
    $ cd /path/to/app
    $ export FLASK_APP=App.py
    $ python -m flask run
 * Running on http://localhost:5000/

if in Windows system, on Command Prompt:

    C:\path\to\app> pip install flask, python-jenkins
    C:\path\to\app> set FLASK_APP=App.py
    C:\path\to\app> python -m flask run
 * Running on http://localhost:5000/

## API description

### Get the task
Get http://localhost:5000/v1/<task_name>

<br/> response (json)  </br>
<br/> {  </br>
<br/>   "Task": "Get the task"  </br>
<br/>    "Job Name": "Job Name" or ""  </br>
<br/>   "Result": "Successed" or "Failed"  </br>
}

### Create Task
Post http://localhost:5000/v1/<task_name>

<br/> response (json)  </br>
<br/> {  </br>
<br/>    "Task": "Get the task"  </br>
<br/>     "Job Name": "Job Name" or ""  </br>
<br/>    "Result": "Successed" or "Failed"  </br>
}

### Build Task
Put http://localhost:5000/v1/<task_name>

<br/> Header:   application/json  </br>
<br/> Body:  </br>
<br/>   {"action","build"}  </br>

<br/> response (json)  </br>
<br/> {  </br>
<br/>    "Task": "Build the task"  </br>
<br/>     "Job Name": "Job Name" or "  </br>
<br/>    "Result": "Successed" or "Failed"  </br>
}

### Delete Task
Delete http://localhost:5000/v1/<task_name>

<br/> response (json)  </br>
<br/> {  </br>
<br/>    "Task": "Delete the task"  </br>
<br/>     "Job Name": "Job Name" or ""  </br>
<br/>    "Result": "Successed" or "Failed"  </br>
}


### Enable Task
Put http://localhost:5000/v1/<task_name>

<br/> Header: application/json
<br/> body:
<br/>   {"action","enable"}
<br/> response (json)
<br/> {
<br/>    "Task": "Enable the task"
<br/>     "Job Name": "Job Name" or ""
<br/>     "Result": "Successed" or "Failed"
<br/> }