# flask-skeleton

A "hello world" style Flask web server application that (optionally) runs on
Heroku. Some notable parts used in this web application are:

  1. [Flask](http://flask.pocoo.org/)
  2. [Gunicorn](http://gunicorn.org/)
  3. [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/)
  4. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
  5. [Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/)
  6. [Flask-Script](http://flask-script.readthedocs.org/en/latest/)

## development

### setup a virtualenv

Create a virtual environment the web application by running the following
commands in a terminal.

```bash
virtualenv my-venv
source my-venv/bin/activate
python setup.py develop
```
### start the web server

Start the web server on your local machine using Flask-Manager.

```bash
./manage.py runserver
```

Then, in your browser, navigate to http://127.0.0.1:5000/. You should see
something like the following image.

![The flask-heroku application running in a web browser.](https://github.com/sholsapp/flask-heroku/blob/master/data/flask-heroku.png)

## heroku

Before you can get started on Heroku, you'll need to have a Heroku account and
their toolchain setup. To do that, follow the instructions at
https://devcenter.heroku.com/articles/quickstart.
