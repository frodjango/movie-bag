was created with pyenv virtualenv 3.6.15 movie-bag-env

pip install flask

click              8.0.4
dataclasses        0.8
Flask              2.0.3
importlib-metadata 4.8.3
itsdangerous       2.0.1
Jinja2             3.0.3
MarkupSafe         2.0.1
pip                21.3.1
setuptools         40.6.2
typing_extensions  4.1.1
Werkzeug           2.0.3
zipp               3.6.0

cd /Users/frodjango/code/movie-bag/app

export ENV_FILE_LOCATION=./.env
export FLASK_APP=app

cd /Users/frodjango/code/movie-bag

python -m app.py

etc...



{
    "email" : "jazzgitan@yahoo.ca",
    "password" : "12345"
}


{
	"name" : "The Dark Knight 6",
	"casts" : [
		"Christian Bale",
		"Heath Ledger",
		"Aaron Eckhart",
		"Michael Caine"
	],
	"genres" : [
		"Action",
		"Crime",
		"Drama"
	]
}
