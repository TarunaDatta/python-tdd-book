Provisioning a new site
=======================

## Required packages
* nginx
* Python 3.6
* virtualenv + pip
* Git
* Tkinter

eg, on Ubuntu
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.6 python3-venv
    sudo apt-get install nginx
    sudo apt-get install git
    sudo apt-get install python3-tk


## Nginx Virtual host config
* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username
```
/home/username
└── sites
 ├── DOMAIN1
 │ ├── .env
 │ ├── db.sqlite3
 │ ├── manage.py etc
 │ ├── static
 │ └── virtualenv
 └── DOMAIN2
 ├── .env
 ├── db.sqlite3
 ├── etc
```