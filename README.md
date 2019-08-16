# A simple API with FLASK - part II (for begginers) 

This API uses Python 3.7 ...<br>
The purpose of this API is just to demonstrate the most "basic" level possible of an API using FLASK.<br>
This API is the same as the one previously published, except with its separate classes / methods (MVC style).<br><br>

LINK to part I:<br>
https://github.com/RicardoTurco/apiWithFlaskBASIC

# ROADMAP:

1) Create and activate a VIRTUALENV<br>
(Verify the appropriate form for your S.O.)

2) Install packages and dependencies:<br>
(pip install -r requirements.txt)

3) Generate SQLite database:<br>
python run.py db init<br>
python run.py db migrate<br>
python run.py db upgrade<br><br>


After that, just run your application.<br>
(python crud.py)

# Available Endpoints:

Add New User:<br>
(POST: localhost:5000/user)

https://github.com/RicardoTurco/apiWithFlaskBASIC/blob/master/images/000_addNewUser.jpg <br>
(The image shows the JSON template to be sent.)


Get All Users:<br>
(GET: localhost:5000/user)

https://github.com/RicardoTurco/apiWithFlaskBASIC/blob/master/images/001_getAllUsers.jpg


Get Users bu ID:<br>
(GET: localhost:5000/user/1)

https://github.com/RicardoTurco/apiWithFlaskBASIC/blob/master/images/002_getUserByID.jpg


Update User:<br>
(PUT: localhost:5000/user/1)

https://github.com/RicardoTurco/apiWithFlaskBASIC/blob/master/images/003_updateUser.jpg <br>
(The image shows the JSON template to be sent.)

Delete User:<br>
(DELETE: localhost:5000/user/1)

https://github.com/RicardoTurco/apiWithFlaskBASIC/blob/master/images/004_deleteUser.jpg
