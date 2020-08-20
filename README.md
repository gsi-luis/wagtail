
## Watgail Learning

### Installation for development using Docker and Docker-compose

#### Install Docker:

1. Install dependencies

    ````
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    ````

2. Add Docker’s GPG Key

    ````
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add –
    ````

3. Install the Docker Repository

    ````
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
    ````

4. Update Repositories

    ````
    sudo apt-get update
    ````

5. Install Latest Version of Docker

    ````
    sudo apt-get install docker-ce
    ````

#### Install Docker-compose

1. Download the Docker Compose binary

    ````
    sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ````

2. Apply executable permissions to the Compose binary

    ````
    sudo chmod +x /usr/local/bin/docker-compose
    ````


#### Clone repository

````
git clone https://github.com/gsi-luis/wagtail.git
````

#### Structure of project

````
/path/to/root/of/project
    |-config          (configurations files used into containers)
    |-Dockerfiles     (docker files and docker composes)
    |-src             (root of project django)
    |-.env.example    (env file example by keys used by environment)
    |-deploy-dev      (bash file commands for deployment environment develop)
    |-LICENSE
    |-README.md
````


#### Languages and frameworks of project
````
* Python 3.8.3
* Wagtail 2.10
* Postgis 9.6+
* Nginx

Note: view requirements.txt for all dependencies used.
````

#### Set config values on .env.dev file with configurations for environment

````
cd /path/to/root/of/project
cp .env.example src/.env
nano src/.env
````

#### Edit your host configuration file to add the app domains

172.70.0.3  wagtaillearning.api.dev.local.com

#### Start the application

1. Move to root of project and run script to initiate application

    ````
    cd /path/to/root/of/project
    bash deploy-dev
    ````
2. Create admin user for default:
    ````
    docker exec -it container.wagtaillearning.api.dev.local.com sh
    python manage.py createsuperuser
    ````

3. Access to app from browser:
    ````
   http://wagtaillearning.api.dev.local.com/admin/
   ````
#### Monitor task and schedules task

1. Access to app from browser:
    ````
   http://wagtaillearning.api.dev.local.com/flower/
   ````
2. Authentication to app from browser:
    ````
   username: celery
   password: celerymonitor
   ````

#### Run Unit tests

Run from project root directory inside of django.learning.app.dev.local.com container:

````
python manage.py test
````

### General ENV variables
````
DEBUG=1
SECRET_KEY='bwj+--xg41((^+rqcvi!ueabmd6bbgl_vqs@5fho05ygdj!tx='
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 wagtaillearning.api.dev.local.com [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=dev
SQL_USER=apilocal
SQL_PASSWORD=apilocal
SQL_HOST=wagtaillearning_api_postgres
SQL_PORT=5432
````
