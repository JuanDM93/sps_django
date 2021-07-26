# SPS API

Basic Django API Demo for SPSolutions

## Description

This is an api demo built on django's [rest](https://www.django-rest-framework.org/) framework. It serves [sample data](https://docs.atlas.mongodb.com/sample-data/sample-analytics/#std-label-sample-analytics) from a hosted [mongodb](https://www.mongodb.com) database and has [auth](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) capabilites.

### Service Endpoints

```open endpoints
/admin

/docs
/redocs

/api

../auth
../../register
../../login
../../me
../../token/refresh

../customers
../accounts
```

## Run options

Warning: as it uses a hosted DB, it is needed to grant network acces for local testing, more details on [ATLAS](https://www.mongodb.com/es/cloud/atlas)

### Local python virtual environment (127.0.0.1:8090)

Once cloned, create new [python environment](https://docs.python.org/3/tutorial/venv.html) "venv", then activate it

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```bash
py -3 -m venv venv
venv\Scripts\activate
```

Install requirements from file inside sps_demo/ dir

```bash
python -m pip install -U pip setuptools
pip install -r sps_demo/requirements.txt
```

Now, create [.env](https://django-environ.readthedocs.io/en/latest/) file, as in .env.example file inside sps_django/sps_demo/sps_demo dir

Move into project directory, then run server

```bash
cd sps_demo/
python manage.py runserver <PORT>
```

### Docker (0.0.0.0:8090)

#### Dockerized compose

Once cloned, create .env file using .env.example as template inside sps_django/sps_demo/sps_demo dir

Then, just [compose](https://docs.docker.com/compose/)

```bash
docker-compose up
```

#### Container build and run

Move into sps_demo dir and build with Dockerfile [container](https://www.docker.com/resources/what-container)

```bash
cd sps_demo/
docker build -t <CONTAINER_NAME> .
```

Deploy it

```bash
docker run -p <PORT>:<port> <CONTAINER_NAME>
```

### Deployment management

For deployment, services pull a public pre-configured image juandm93/spstest:latest from docker-hub

#### Kubernetes (minikube, docker-desktop)

A deployment.yaml file is at root to orchestrate node asignation and load balancing

```bash
kubectl apply -f deployment.yaml
```

#### Cloud Deployment ([Fly.io](https://fly.io))

A fly.toml file was generated to orchestrate cloud deployment

```Service Public Address
https://sps-django-fly.fly.dev/
```

## Contributing

For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
