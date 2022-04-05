# DatabaseCS162

Instructions on how to run the app. 

- Download the app from this repo. 
- Extract it and open the whole folder in VSCode
- There you can see the two main folders as the Frontend and Backend
- The frontend folder contains react files while the backend is mainly python(flask)
- Before you are able to run the app, you need to have a virtual environment to be created, so please create a terminal in VSCode (keyboard hosrtcut is Command + ~). And type 'pipenv shell' in the VSCode terminal. Im using mac, so the shortcut might be different for windows users. 
- Now you need to install the following packages:
   -  pip install -U Flask
   -  pip install python-dotenv
   -  pip install -U Flask-SQLAlchemy
   - pipenv install flask
   - pip install -U flask-cors

NB, to create the database, you need to go to the Backend directory in the VSCode Terminal and run the the following commands - 

 - pipenv shell   -> this will start the virtual environment
 - export FLASK_APP=app.py
 - python
 - from app import db
 - db.create_all()

Before running this command, download Postgres if you don't have in in your device, and also download PgAdmin4. Inside PgAdmin4, create an empty database with the name cs162. Once that empty database is created(simply right click and create), then the db.create_all() comes in -  and code will use that directory to create tables that I have inside app.py file with it's complete CRUD functionality. 

For the frontend to run, we need to install the following - 

 - pip install react-bootstrap
 - pip install react-router-dom
 - pip install react-hook-form


I have created an api end point for all of the 6 Tables I have created, and you can use postman to CREATE, DELETE, POST, and GET data to the DB. 

The data of each table is also displayed in the react frontend as table for each of the 6 tables I have created.




   

