# SPS API

Basic Django API Demo for SPSolutions

## Description

This is an api demo built on django's [rest](https://www.django-rest-framework.org/) framework. It serves [sample data](https://docs.atlas.mongodb.com/sample-data/sample-analytics/#std-label-sample-analytics) from a hosted [mongodb](https://www.mongodb.com) database and has [auth](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) capabilites.

### Service Endpoints

```open endpoints
/admin

/api
../users
../../auth/register
../../auth/login
../../auth/me
../../auth/token/refresh
```

## Run options

Warning: as it uses a hosted DB, it is needed to grant network acces for local testing, more details on [ATLAS](https://www.mongodb.com/es/cloud/atlas)

### Local python virtual environment (127.0.0.1:PORT)

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

Install requirements

```bash
python -m pip install --upgrade pip
python -m pip install -U setuptools wheel
pip install -r requirements.txt
```

Now, create [.env](https://django-environ.readthedocs.io/en/latest/) file, as in .env.example file inside sps_demo/sps_demo dir

Move into project directory

```bash
cd sps_demo/
```

Then run server

```bash
python manage.py runserver <PORT>
```

## Contributing

For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
