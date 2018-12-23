# Restaurant SQL Server App

A Python web app to demonstrate the following:

* Creating server and handling GET and POST requests
* Using Python Database API and ORM through [SQLAlchemy](https://www.sqlalchemy.org/)
* Managing CRUD (Create, Read, Update, Delete) operation on database tables
* Setting-up database in [SQLite](https://www.sqlite.org/index.html) and in [PostgreSQL](https://www.postgresql.org/) using Python only

## Running the app

First datbase must be initialize and entried added to relevant tables. This can be done by running the `database_setup.py` which will set the database and create empty table. Then by running `lots_of_menus.py`, the tables will be populated with data. Run these script using command as shown below

```bash
$> python database_setup.py
$> python lots_of_menus.py
```

After this, all is needed to run the Python server as below:

```bash
$> python restaurant-web-server.py
```

## Dependencies

Following are required to run the app

* Python 3.6
* SQLAlchemy 1.2
* SQLite 3.23

### TODO

* Update the app with CSS.
* Add more featueres.