# AirBnB_clone

![AirBnB clone logo.](https://github.com/rmarcais/AirBnB_clone_v2/raw/main/img/logo_airbnb.png)

##Introduction

This project is the first step of a big one witch is to clone the AirBnB full web application.
 * This first step is in python. We will start by implement the parent class called BaseModel.
 * This class do the initialization, serialization and deserialization of the future instances : Instance <-> Dictionary <-> JSON string <-> file
 * During this project, we created some classes that inherit from BaseModel such as : User, State, City, Place, review, state, amenity...
 * Create the first abstracted storage engine of the project: File storage.
 * And to finish create the unittest to validate all the classes and storage processes

![image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220523T112936Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b22e5a5e597a1e98835f74cf7b8c31493467cbd556867daf6a85989345949f63)

## Definitions

First lets have some few definitions to help understand the project :

* __What is a Python package ?__

A Python package is a folder containing modules and maybe other folders that themselves may contain more folders and modules. A package folder usually contains one file named __init__.py that basically tells Python: “Hey, this directory is a package!” The init file may be empty, or it may contain code to be executed upon package initialization.

* __Why use the command interpreter in Python ?__

The Cmd instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate Cmd itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit Cmd’s methods and encapsulate action methods.

* __How to manage `datetime` ?__

To manage datetime in python, you have to import the module named datetime. This module allow you to deal with the hours or the dates

* __What is a `UUID` what can it be used for?__

UUIDs are generally used for identifying information that needs to be unique within a system or a network.

* __What is `*args` and how to use it ?__

The special syntax `*args` in function definitions in python is used to pass a variable number of arguments to a function. But we won't use `*args` in this project.

* __What is `**kwargs` and how to use it ?__

Kwargs allow you to pass keyword arguments to a function. They are used when you are not sure of the number of keyword arguments that will be passed in the function. Kwargs can be used for unpacking dictionary key, value pairs. This is done using the double asterisk notation ( ** ).

* __How to handle named arguments in a function ?__

Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific parameter names. A keyword argument is preceded by a parameter and the assignment operator `=` . Keyword arguments can be likened to dictionaries in that they map a value to a keyword.

## Use the console

The `(hbnb)` Airbnb Clone can be run both in interactive and non-interactive mode.
To run the console in non-interactive mode, you can use the following command :

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
You can use the interactive mode with the following command :

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## Main commands

| COMMAND after the (hbnb)                               |                 DESCRIPTION                  |
|--------------------------------------------------------|:--------------------------------------------:|
| quit                                                   |             To quit the console              |
| EOF                                                    |          To quit the console by EOF          |
| help + command                                         |     Display the help for the command ask     |
| create + class                                         |      Creates an object and print the ID      |
| show + class + id                                      |    To show the informations of the object    |
| destroy + class + id                                   |             To remove an object              |
| all + class                                            |     To show all the instances of a class     |
 | update + class + id + attribute name + "attribute value" | To create or update the attribute of a class |
| count + class                                          | To count the number of instance by class     |

## New feature

In this new version of the HBNB, we improve two of our command to make them work with multiple argument, the first one that we update is the `do_create`, now we can create new instance with given paramater and In our dictionnary the information will look clearer.

We also updated our [basemodel](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/base_model.py). We mainly updated already created class to make them work with sql, for this we had to use `sqlalchemy`, a python module to make python interact with sql.

[Filestorage](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/engine/file_storage.py) was updated too, we create a new public instance `delete` that delete an `obj` from `__objects` only if the obj exist inside.
In this filestorage file we update the `all` instance that permit to the user to show all instance of a class.

We updated all other class file to make them work with sql.

## [BaseModel](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/base_model.py)

The BaseModel class is the parent of all the classes : 

* The `init method` defines the common attributes for all the class that inrherite from that one. We call that the constructor method.

* The `str method` is the method that defines the good output format as a string.

* The `save method` is useful to updates the public instance attribute 'updated_at' with
        the current datetime.

* The `to_dict method` returns a dictionary containing all the keys and values of the instance.

## [Other classes](https://github.com/rmarcais/AirBnB_clone_v2/tree/main/models)
All the classes listed bellow inherits from BaseModel :

| class       | Attributes | Description |
|-------------|:----------:|:-----------:|
| [User](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/user.py)       |email + password + first_name + last_name| This class is about user information, it retrieve main information about the future user  |
| [State](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/state.py)     |name                                     | This  class retrieve information about for the future state of the future location |
|[City](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/city.py)       |state_id + name                          |  This class retrieve more precise information about the geographic position of future location |
| [Place](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/place.py)     | city_id + user_id + name + description </br> number_rooms + number_bathrooms + max_guest </br> price_by_night + latitude + longitude + amenity_ids | This class retrieve all information about the future location, all important information like the number of room and the equipment inside the location  |
| [Review](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/review.py)   |place_id + user_id + text                | This class retrieve a review of the future place with information of the user that post the review  |
| [Amenity](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/amenity.py) |name                                     | This class retrieve information about the future amenity  |

# The storage system

Our Air BnB clone has two storage system, a DataBase storage and a File Storage.
We store our different type of storage in the [Engine](https://github.com/rmarcais/AirBnB_clone_v2/tree/main/models/engine) folder.

To have a better representation of how we store the data, here is a schema:

![image](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png)

## [Filestorage](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/engine/file_storage.py)

This file is composed of methods that are used by the console :
* The `all method` display the dictionary view of objects.

* The `new method` sets a new instance with the class name and a new id for the object.

* The `save method` serialize the object in dictionary format to the JSON file.

* The `reload method` deserialize the JSON file to object. In other words, bring the data in the `file.json` and change it to object.

## [DataBase Storage](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/models/engine/db_storage.py)

This file is composed of method that are used by the console :
* The `all method` display all the object of a class stored in the database.

* The `new method` add a new object to a session.

* The `save method` save everything in the current session in use.

* The `delete method`  delete an object inside the current session.

* The `reload method` create all table and session.

* The `close method` close the session in use.

## [Console](https://github.com/rmarcais/AirBnB_clone_v2/blob/main/console.py)

The HBNBCommand class is created to implement the prompt. The option `do` at the beginning of the method define the action. So `do_quit` defined the command to quit the prompt, the `EOF` command does the same with the signal.

* The `command do_create` is to create a new instance and tell the user if there is a missing argument or if the class called doesn't exist. If the argument are passed on the good way, the instance is created and saved. We update this command to make it work with multiple parameter and with a specific syntax. If your information after the parameter is a string, you should write it like that `name="NAME"`. But if it's an integer or a float, you should write like this `age=5` or `height=175.3`
```commandline
Usage: create <Class name> <param 1> <param 2> <param 3>... OR <class name>.create(<param 1> <param 2> <param 3>...)
```
* The `command do_show` is to show a string representation of an instance. This mean that when you type : "show User id" on the good way it will display the information of this user. If a argument is missing it will display an error message.
```commandline
Usage: show <class name> <id> OR <class name>.show(<id>)
```
* The `command do_destroy` works on the same way as "show" but the objective is to remove an instance.
```commandline
Usage: destroy <class name> OR <class name>.destroy(<id>)
```
* The `command do_all` displays in the prompt the string representation of all the instance saved.
```commandline
Usage: all OR all <class name> OR <class name>.all()
```
* The `command do_update` is useful to update an instance. If the instance already exist, it updates the instance and the datetime. If the instance doesn't exist, it creates it.
```commandline
Usage: update <class name> <id> <attribute name> "<attribute value>" 
Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
```
* The `command do_count` counts the number of instance for each class.
```commandline
Usage: count <class name> OR <class name>.count()
```
* The `method default` is called when the command is not recognized. If the input line cannot be overrided, an error message is printed and returns. 
```commandline
$ input
(hbnb) User.count()
$ method default switch by
(hbnb) count User
```

## [Python Unit Tests](https://github.com/rmarcais/AirBnB_clone_v2/tree/main/tests)

We have done some tests for our classes and methods. Tests are made to make sure our code display the result and the outputs expected.

The command to display the results of the tests in interactive mode is :
```
$ python3 -m unittest discover tests
```
And the command in non-interactive mode is :
```
echo "python3 -m unittest discover tests" | bash
```

## [RESTful API](https://github.com/elodieriou/AirBnB_clone_v3/tree/main/api)

For this part of the project AirBnB clone v3, we have to start our REST API. For doing this, we use Flask.
The API is used to exchange data between the server and the database doing request.

![image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/02078cd7f0573885c85a225c7436584a5afea1f9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220523T095359Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3caa4fe94e844264e6dcd2eed977c79096a42eaa5d91f1f1bc69e0f96a2d672b)

## AUTHORS

Rémi Marçais [Github](https://github.com/rmarcais) \
Elodie Riou [Github](https://github.com/elodieriou)
