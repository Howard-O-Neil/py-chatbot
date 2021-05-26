
# Python ChatBot

A project of building chatbot support for software business

A setup made with Flask, Gunicorn, Alchemy, Alembic

- A LAMP Stack done right
  - MySql replaced by PostgreSql
  - PHP (come on dude 🙂) replaced by Python

- Some key feature
  - No Sql
    - Sync PostgreSql table schema with python data models
    - Auto generate database migration code whenever models is updated
  - Cli setup with ease
  - Faster development
    - Hex Architecture
    - Docker Proxy DNS
  - JWT Secure (Cli supported)
  - Webhooks (Cli supported)
  - Integrate with [DialogFlow](https://cloud.google.com/dialogflow/docs)
  - Integrate with [Facebook API](https://developers.facebook.com/)
  - Deploy with [AWS](https://aws.amazon.com/?nc2=h_lg)

- Some helpful document
  - [APScheduler](https://apscheduler.readthedocs.io/en/latest/index.html)
  - [Authlib](https://docs.authlib.org/en/latest/index.html)
  - [Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/)
  - [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/)
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - [Flask-Script](https://flask-script.readthedocs.org/en/latest/)
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
  - [Flask-Security](https://pythonhosted.org/Flask-Security/)
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  - [Gunicorn](https://gunicorn.org/)

# Documentation

- [Developing](./docs/developing.md)
- [Cli](./docs/bootstrapping-alembic.md)
- [Configuration](./docs/configuration.md)

# Quickstart

```bash
  # development only

  make bootstrap

  source env/bin/activate.fish  # if u use fish shell
  source env/bin/activate       # if u use bash shell
  # search google               # is u use other shell

  make set-dns
  make auth-script
  docker-compose up
```

# Related Works

  1. [sean-/flask-skeleton](https://github.com/sean-/flask-skeleton)
  2. [sholsapp/flask-skeleton](https://github.com/sholsapp/flask-skeleton)
  3. [graup/flask-restless-security](https://github.com/graup/flask-restless-security)
  4. [imwilsonxu/fbone](https://github.com/imwilsonxu/fbone)
  5. [xen/flask-project-template](https://github.com/xen/flask-project-template)
  6. [jelmerdejong/flask-app-blueprint](https://github.com/jelmerdejong/flask-app-blueprint)
  7. [sdetautomation/flask-api](https://github.com/sdetautomation/flask-api)
  8. [cburmeister/flask-bones](https://github.com/cburmeister/flask-bones)
