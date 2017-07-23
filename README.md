# PyBird

PyBird is an twitter like made with django. An web framework of python language.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

We work with Vagrant to be sure we've all have the same environment.

You can follow this link and this setup to have the exact and same environment than us.
https://github.com/aminehaddad/django-environment-in-vagrant

### Installing

Install the following applications in your host operating system:

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)

The following Vagrant plugin is recommended to keep the VirtualBox guest additions automatically updated:

* [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)

This is how you install vagrant-vbguest:

	vagrant plugin install vagrant-vbguest

## Getting the source code

Retrieve the source code:

	git clone https://github.com/aminehaddad/django-environment-in-vagrant.git PyBird
	cd PyBird

## (Optional) Setting it up for Windows

You need to modify the Vagrantfile if you are running Windows by replacing:

	config.vm.network "private_network", ip: "10.10.10.10"

with:

	config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"

## Starting the virtual machine development environment

The following command will start the environment:

	vagrant up

The installation script will run within the virtual machine if it is the first time it is started (in order to install the required packages).

## Setting up the virtual machine development environment

SSH into the virtual machine:

	vagrant ssh

The source code is shared with the virtual machine in this directory:

	cd site

Always run the following command to use the proper python virtual environment:

	workon site

## Get PyBirdApp as a Django project

Get PyBirdApp Django project :

	git clone https://github.com/DiegoWaz/PyBird

    cd PyBird

Install the required python packages:

	pip install -r requirements.txt

You can now start the development web server:

	./manage.py runserver 0.0.0.0:8080

For Windows, replace `./manage.py` with `python manage.py`:

	python manage.py runserver 0.0.0.0:8080

Access this URL :

* [http://10.10.10.10:8080/PyBirdApp](http://10.10.10.10:8080/PyBirdApp)

To turn off the virtual machine, run the following from your host terminal:

	vagrant halt -f

To turn on the virtual machine, run the following:

	vagrant up

## Access to database

We are using an sqlite3 database. Follow this command to explore database :

    sqlite3

    .open /home/ubuntu/site/PB_Prod/db.sqlite3

    .header on

    select * from PyBirdApp_post;

    .quit


