# DjangoRestAPI_ProgresRepo

DjangoAPI to make CRUD request to PosgreSQL


### Prerequisites
1.	Azure Vitual Machine
2.	Installations of Python, VScode(any IDE), pgadmin(to connect to Progres db)
3.	ProgreSQL PAAS Database instance on Azure.
4.	Required port, 8000 opened on firewall

## Installations
1. First install the Django module
   ```sh
   pip install django
   ```
2. To create rest APIs it is needed to install Django rest framework
   ```sh
   pip install djangorestframework
   ```
3. By default, the Django project comes with a security that blocks requests coming from different domains. To disable this, install Django CORS headers module
   ```sh
   pip install django-cors-headers
   ```

## Now create the Django project
Open the command prompt in the desired folder and type the command to create a projected named CustomerApp
   ```sh
   django-admin startproject DjangoAPI
   ```
To confirm the Project is working, start the server by running the command, 
   ```sh
   python manage.py runserver
   ```
The app is now running in the port 8000.

## Django Appb Setup

Lets create one app to implement our api methods.
To create an app, need to type this command in the Project folder.

   ```sh
   python manage.py startapp CustomerApp
   ```

In the installed apps section, lets add Rest framework, cors header, and the newly created app.
We need to add the cors headers in middle ware section as well.
We will also add instruction to enable all domains to access the APIs.
This is not recommended in production. Instead, just add only those domains that needs to be whitelisted.

   ```sh
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'CustomerApp.apps.CustomerappConfig'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

   ```

## Models Creation
Then create the model needed for our app.to store Customer details.
Employee model will have  fields : Customer ID, Customer name
   ```sh
   from django.db import models

# Create your models here.

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=500)

   ```
## Database final SetUp

As PostgreSQL is used for the database.
To connect to PostgreSQL  from the Django app, it is needed to install the database adapter.
   ```sh
   pip install psycopg2
   ```


Add the database details in settings.py file


Then needed to write the command to make migrations file for the models.
   ```sh
   python manage.py makemigrations CustomerApp
   ```
After executing this, we can see a migration file which tells us what changes to the database will be done

once it looks fine, we can execute the command to push these changes to the database.

```sh
   python manage.py migrate CustomerApp
   ```
## Serializers creation

Create serializers for the models.
Serializers basically help to convert the complex types or model instances into native python data types that can then be easily rendered into json or xml or other content types.
They also help in deserialization which is nothing but converting the passed data back to complex types.

Created  serializers.py in the App Folder for the below code 

```sh
   from rest_framework import serializers
from CustomerApp.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers 
        fields=('CustomerId','CustomerName')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers 
        fields=('CustomerId','CustomerName')
   ```

## Final Setup

Then started writing the API methods in views.py, configure settings in Settings.py and also the urls files.  All included in the repository.

After all is configured, include the required Host Ips in the  “ALLOWED_HOSTS = []”     in the settings.py file. Then run the below command to start the API.

```sh
python manage.py runserver 0.0.0.0:8000
   ```
You can use Postman to verify the CRUD request to http://serverip/customer
for example:  post request for the below Json to the DB

```sh
   {
        "CustomerId": 1,
        "CustomerName": "Mary"
    }
   ```
    


