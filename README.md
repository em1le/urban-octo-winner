# urban-octo-winner

![Heroku Deploy](https://github.com/em1le/urban-octo-winner/actions/workflows/heroku_deploy.yml/badge.svg)

## Introduction

To be honest, I started wednesday night around 9pm and I did not have a clue what application to show you.

![What should i think ?](https://media.giphy.com/media/HflJzrKnz8RglnC86J/giphy.gif)

So this modest project is a platform where a media content creator can catalog and take inventory of its work.

### Global user case
As a media content creator :
- I want to add articles to my account
- I want to add references to my articles
- I want to have a global view of my catalog
- I want to make CRUD operation on my articles

### UML

![UML Diagram](http://www.plantuml.com/plantuml/png/bPBFJiCm3CRlVOemBanYqfYeD7RQUo2elCHT3VbJEUuGGhmxYKffsNfPUcZwY_NvwnVlem1Bvsnn8mqwL0u4cQ2Gq2e9wX14WbE66BLGy4Ly9zy2WrEMFCfdYogmDA4ej8KOLL8ZRJ5MlnlrLIYbD6FIDJjbqal8OOOk6AhfdBPC6XD2JGvi9j0PGfyXUS4ZSeQCDNAc5IM10ntJMUPTHCveMZlz_1vyTj9KkRWts2Rs4JWLde1r0tptiDakyqcgbig6fF_V9yKgTYroraW6Gh13UmyE9phbUjIPFq87P4UyAH-NGmU1kXxL4m4jTC8HPKlLMo1_dcDDFD_m8f0-aJ7HM0tRws_FmW4dlxBj-wMPCICibxq_EtMsddLsCKsJzRfwlYsVydFVMY3_ibAJMxrOExKOPeFCubhbsNH6vJyqoE_HcyxP7m00)


### Pre-requisites
Ask me the environment variables files else you would not be able to have a correct experience on the app.

### Docker installation

#### Docker

First you have to make sure that docker is installed on your local environment.

Try the following command :
```shell
$ docker --version
```
If it show something such as `Docker version 20.10.12, build e91ed57` it should be fine.

Otherwise [follow tutorial on docker](https://docs.docker.com/get-started/)

#### Docker Compose

We need docker compose installed in order to make it work.
As written on docker part, you should try the following command to check if docker is installed :
```shell
$ docker-compose --version
```
If something like `docker-compose version 1.29.2, build 5becea4c` pops up it's fine in the other hand you would have to take a look
on [how to install docker-compose](https://docs.docker.com/compose/install/)

#### Let's do it

The basic stuff is installed to make it work.
Thus launch followings :

```shell
$ docker-compose up --build
```

Afterwise, you should access localhost:8000 or 127.0.0.0:8000

### From scratch

You might also want to install without docker, just a few steps more to have a project running :
##### Clone the repo

Choose the right place to store you project and do as follow :
```shell
$ git clone git@github.com:em1le/urban-octo-winner.git
```
Go inside the clone folder
```shell
$ cd urban-octo-winner
```

##### Create a venv
As your at your folder's root you may launch the following command :
```shell
$ python3 -m venv catalog-env
```

A fresh folder has just been created under the catalog-env name.
Then you must source the env :
```shell
$ source catalog-env/bin/activate
```

Fine enough, let's install the requirements :
```shell
$ pip install -r requirements.txt
```

#### Migrate
Run the command ``./manage.py migrate``

#### Fire it up
Run the comman `./manage.py runserver`

You should now be able to see the application

## Todo
 - Add locust
 - Add more useful data to dashboard
 - Add more pertinent tests

