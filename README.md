# Store-Manager-API

![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Coverage Status](https://coveralls.io/repos/github/bryan-munene/Store-Manager-API/badge.svg)](https://coveralls.io/github/bryan-munene/Store-Manager-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/67a0efd8529d6bcc1c6e/maintainability)](https://codeclimate.com/github/bryan-munene/Store-Manager-API/maintainability)
[![Build Status](https://travis-ci.org/bryan-munene/Store-Manager-API.svg?branch=development)](https://travis-ci.org/bryan-munene/Store-Manager-API)
[![codecov](https://codecov.io/gh/bryan-munene/Store-Manager-API/branch/development/graph/badge.svg)](https://codecov.io/gh/bryan-munene/Store-Manager-API)



Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. These are API endpoints for this app


## Getting Started

These instructions will guid you on how to deploy this system locally. For live systems, you will need to consult deployment notes of flask systems for that.

To get started first you need a machine that can run on Python3 and handle postgres database.

### Prerequisites

You will need these installed first before we go any further.

- [Python3.6](https://www.python.org/downloads/release/python-365/)

- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)


For Virtual Environment, you can install like this after Installing Python3:

```
pip install virtualenv
```
```
pip install virtualenvwrapper
```


## Installation and Running


### Installing

Clone the repository below

```
git clone -b development https://github.com/bryan-munene/Store-Manager-API.git
```

Create a virtual environment

```
    virtualenv venv --python=python3.6
```

Activate virtual environment

```
    source venv/bin/activate
```

Install required Dependencies

```
    pip install -r requirements.txt
```



### Running

Start the flask server on your command prompt:

    First you need to ``` cd ``` to your project root directory

Then:

```
    python run.py
```

With the server running, paste this in your browser's address bar:

```
    localhost:5000/api/v1/
```

This is the welcome page.



## Running the tests

This repository contains tests to test the functionality of the API.

To run these tests, run the following command:

### Running all tests.

These tests test the ``` Items Class, Sales Class, and the Users Class```

In the project's root directory, with the virtual environment running, run this command:

```
pytest
```


### Running specific test scripts

It is possible to run test scripts individually. 

``` cd ``` to your tests directory.

```
pytest test_users.py
```
to test the class Users only.


# Versioning

This app contains multiple versions.

**Version 1** is made up of the following endpoints and uses python data structures (non-persistent storage), to store the data.

**Version 2** uses postgresql database to store data.

# Endpoints

## Version 1 Endpoints Available

|    #   | Method | Endpoint                        | Description                           |
|--------| ------ | ------------------------------- | ------------------------------------- |
|    1   | GET    | /                               | Index/Welcome page                    |
|    2   | POST   | /api/v1/register                | Create new user                       |
|    3   | POST   | /api/v1/login                   | Login a registered user               |
|    4   | GET    | /api/v1/logout                  | Logout a logged in user               |
|    5   | POST   | /api/v1/add_item                | Create a new item                     |
|    6   | GET    | /api/v1/items                   | Retrieve all items                    |
|    7   | GET    | /api/v1/items/<int:item_id>     | Retrieve a specific item by item id   |
|    8   | DELETE | /api/v1/items/<int:item_id>     | Delete a specific item by item id     |
|    9   | PUT    | /api/v1/items/<int:item_id>     | Update a specific item by item id     |
|    10  | POST   | /api/v1/make_sale               | Make a sale                           |
|    11  | GET    | /api/v1/sales                   | Retrieve all sales                    |
|    12  | GET    | /api/v1/sales/<int:sale_id>     | Retrieve a specific sale              |




#Documentation

Coming soon...

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [pip](https://pypi.org/project/pip/) - Dependency Management


## Authors

* **Muthuri Munene Bryan** -  - [bryan-munene](https://github.com/bryan-munene)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

