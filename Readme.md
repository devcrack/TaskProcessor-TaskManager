# Task Process for Process Manager
## Requirements :
* Rabittmq
* celery
* flask
* python3-venv
* python 3.5 or higher

## RabbitMQ install & configuration
First of all you need to have install the broker. For this we going use RabbitQM server.

For install this: ```sudo apt install rabbitmq-server``` :+1:

You can also install the management plugin for make more easy to peek into a running RabbitQM instance. Let's install the management plugin as follows: 
```bash
   sudo rabbitmq-plugins enable rabbitmq_management
    [OUTPUT]:
    .
    .
    .
    .
    The following plugins have been enabled:  
    mochiweb  
    webmachine  
    rabbitmq_web_dispatch  
    amqp_client  
    rabbitmq_management_agent  
    rabbitmq_managementPlugin configuration has changed. 
    Restart RabbitMQ for changes to take effect.
```
As invited by the installer, we need to restart rabbitMQ as follows:
```bash
sudo service rabbitmq-server restart
*Restarting message broker rabbitmq-server         [OK]
```
Now using the web browser we can now reach the home page of the management console by navigating to *http://\<host-address\>:15672*

### Configuring users 
We need to configure an administrator user in the Broker as follows:
```bash
sudo rabbitmqctl add_user <YOU_USERNAME> <YOUR_PASSWORD>
[Output]:
Creating user "ccm-admin" ......done.

sudo rabbitmqctl set_user_tags <YOUR_USERNAME> administrator
[Output]:
Setting tags for user "ccm-admin" to [administrator] ......done.

rabbitmqctl set_permissions -p / <YOUR_USERNAME> ".*" ".*" ".*"

```

## Creating virtual environment
First of all you need to have install the **python3-venv**.

For install this: ```sudo apt install python3-venv``` :+1:

After of that we  create the virtual environment for as follows:
```bash
python3 -m venv <path_&_name_directory_VENV>
```

For activate it:
```bash
source <path_&_name_directory_VENV>/bin/activate
```

For deactivate it :
```bash
deactivate
```

## Installing packages for project 
For this you have to have activate the virtual environment, once you have done it
```bash
pip install flask celery 
```

## Celery broker configuration
In your Celery base configuration in configure.py file you have to add the parameters that we have configured in **RabbitMQ install & configuration**  section
```bash
Task_Procesor_for_ManageProcess
├── main
│   ├── configure.py
```

```python
CELERY_BROKER_URL = 'amqp://<YOUR_USERNAME>:<YOUR_USERPASSWORD>@<BROKER_SERVER_ADDRESS>:5672'
```
A Result Backend if you have
```python
CELERY_RESULT_BACKEND = 'mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'
```
## Executing Celery Tasks 
```bash
celery worker -A main.main.celery_instance --loglevel=info
```

## Project Execution
In root of project directory type: 
```bash
python run.py
```
**Note** You have to have the virtual environment activate it for execute the project.

## Test using INSOMNIA
[Download ISNOMNIA](https://insomnia.rest/download/#linux)

Once you have installed insomnia run the test on it.

### Note
Is important that you have created this directorires:
- core_programs
- hipcc_data

in the root of home user directory jus like this: 
```bash
home/
└── yeyo    
    ├── core_programs
    ├── hipcc_data
```

### Executing Process
Request type **POST**

URL for request: **http://<server_address>:5000/start_work**


JSON Structure for hard sphere program execution

- **user_mail:** Mail user of the logged user.
- **id_process:** Id_for identify the program to run.
- **frac_vol:** Fraction volumen to do calculation.

```json
{
    "user_mail":"pedro@gmail.com",
    "id_process":0,
    "frac_vol":0.5
}
```

Response message: 
> Executed 

With Code:
>200

JSON Structure for soft sphere and yukawa hard_sphere programs execution id_process for Soft Sphere is 1, id_process for Yukawa is 2

- **user_mail:** Mail user of the logged user.
- **id_process:** Id_for identify the program to run.
- **frac_vol:** Fraction volumen to do calculation.
- **ini_temp:** Initial Temperature to do calculation.

```json
{
    "user_mail":"pedro@gmail.com",
	"id_process":2,
	"frac_vol":0.5,
	"ini_temp":-2	
}
```

Response message: 
> Executed 

With Code:
> 200


JSON Structure for Dynamic Module

- **user_mail:** Mail user of the logged user.
- **id_process:** Id_for identify the program to run.
- **frac_vol:** Fraction volumen to do calculation.

```json
{        
        "user_mail":"pedro@gmail.com",
        "id_process": 1,
        "frac_vol": 0.5 
}
```
Response message: 
> Executed 

With Code:
> 200


### Creating user directories

Request Type: **POST**

URL:http://<SERVER_ADDRESS>:5000/mkdir_usr

JSON Structure for create user directories

- **user_mail:** Mail user of the logged user.

```json
{        
        "user_mail":"pedro@gmail.com"
}
```
Response message: 
> User-directory-created

With Code:
> 200

### Get directories content
Request Type: **POST**

URL: http://<SERVER_ADRRESS>:5000/ls_dir

JSON Structure for get directories content. 

- **user_mail:** Mail user is the root directory name.

- **psedo_pth:** Is a list with all the directories of path in other words  all the nested directories from root directory to the directory to list its contents.
```json
{        
        "user_mail":"pedro@gmail.com",
        "psedo_pth:["child_dir1", "child_child_dir",.....]
}
```
Return JSON with a structure like this:

```json
{
  "Date:2019-3-25-Time:17": [
    "coefficient-Date:2019-3-25-Time:17:59:45.dat",
    "f_self-Date:2019-3-25-Time:17:59:45.dat",
    "sk-Date:2019-3-25-Time:17:59:45.dat"
  ]
}
```

### Download Files

Request Type: **POST**

URL: http://<SERVER_ADDRESS>:5000/**get_file**


Example JSON Structure

- **user_mail:** Mail user is the root directory name.

- **psedo_pth:** Is a list with all the directories of path in other words  all the nested directories from root directory to directory that contains the file.

- **fle_name:** Name of the file to download 

```json
{
	"user_mail":"alejandro@gmail.com",
	"psedo_pth":["Dynamic", "corrida1"],
	"fle_name": "nudes.jpg"
	
}
```
Return the requested file.


#  :camel: Todos :rocket:
- [x] Enable Lite Task for Task Process
    - [X] Codify the executiong of Hard Sphere
    - [X] Codify the executiong of Soft Sphere
    - [X] Codify the executiong of Yukawa
    - [X] Codify the executiong of Dynamic Module V0.1
- [x] Configure Broker  for connect microservice 
    - [x] Configure User for connect to broker externally
- [X] Execute with API and Celery
- [X] Execute procces through api and celery
- [X] Create documentation up to the current progress
- [X] Create user directories as we were doing  in previous versions
- [X] Enable the file Download as we were doing  in previous versions