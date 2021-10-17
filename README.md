**Flask with math**

This project exposes an API to solve a few mathematical operations like: power, factorial and fibonacci.

### Docker

Please take note that you need to have Docker installed on your system.

Although the application can be run as a standalone python module.

### Database

The default, sqlite3, database was used for storing the data.

### Postman

Requests were made with Postman during development but for usage also.

### Run app

This is the order of steps that need to be taken.

* Change directory to flask_math.
* Run the app with docker, all the necessary files are in flask_math directory:
* The application will run on port 5000.

```flask
sudo docker-compose up -d --build
```

* Alternatively, you can run the app as a standard python module:

```flask
python app.py
```

* Now you need to acquire the JWT first for authorisation.
* The username and password are set to test, you need to add them in the body and set Content-Type to application/json.

```flask
http://127.0.0.1:5000/login
{"username":"test","password":"test"}
Content-Type: application/json
```

* Now pass the JWT for each API request you intend to make, but only for the first time.
* Take note that the JWT expires after a few minutes (WIP).

```flask
Authorization: Bearer <access token>
```

We will use as an example of usage the /v1/power API. The other APIs are : http://127.0.0.1:5000/v1/fibonacci
and http://127.0.0.1:5000/v1/factorial .

* To create a new resource:

```flask
POST http://127.0.0.1:5000/v1/powers
```

* To read a resource for a specific ID(where 1 is out desired ID):
```flask
GET http://127.0.0.1:5000/v1/powers/1
```

* To read all resources:
```flask
GET http://127.0.0.1:5000/v1/powers
```

* To update an existing resource:
```flask
PUT http://127.0.0.1:5000/v1/powers/1
Body {"base":2, "exponent":3, "power":8}
```

* To delete an existing resource:
```flask
DELETE http://127.0.0.1:5000/v1/powers/1
```