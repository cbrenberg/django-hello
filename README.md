# Django Web Framework Example by Christopher Brenberg

## About

Django is a Python web framework

## Set Up

To get started with Django, you must first install python. Instructions can be found at https://www.python.org/about/gettingstarted/

Once python is installed, type `python -V` into your terminal. If it has been installed successfully, you will see the version listed in the terminal output.

_Optional: To manage different package versions for multiple projects, Django recommends installing and activating a virtual environment for each project. Instructions can be found here under the "Getting a copy of Django's development version": https://docs.djangoproject.com/en/2.1/intro/contributing/_

Python versions 3.4+ come with their own package manager called 'pip', which can be used to install Django using the following commands:

Update pip:

`pip install --upgrade pip`

Django:

`pip install -e django`

From the command line, navigate to the directory in which you want to create your project, and run the following command to create a new Django starter app:

`django-admin startproject YOUR_SITE_NAME`

Verify your project is up and running by starting the development server:

`python3 manage.py runserver`

and navigate your browser to http://localhost:8000. You should see a default view with a rocket and some links to other Django resources.

To create additional apps (or views) within your new site, navigate from the command line to the root level of your app (the folder containing `manage.py`), and run this command:

`python manage.py startapp YOUR_APP_NAME`

You can then map this new app to a relative URL within your project by creating a file called `urls.py` within your new app directory with the following code:

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Then, to point the root project to this new path, navigate to `YOUR_SITE_NAME/urls.py` and make sure it has all of the following code:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('YOUR_APP_NAME/', include('YOUR_APP_NAME.urls')),
    path('admin/', admin.site.urls),
]
```

## Hello World

Here is a link to my [Hello List](https://github.com/LukeSchlangen/simplified-react-axios) example built with React and Axios. This returns an array from a `mockable` http endpoint and displays it on the DOM.

## Next steps

The next steps for learning this is to understand the role of middleware like flux/redux and logging/sagas. These are tools used to manage state, but since this [Hello List](https://github.com/LukeSchlangen/simplified-react-axios) example only has a single state (displaying the list), the next step will likely be adding something to the list with a `POST`.
