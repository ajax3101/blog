init:
	cd blog && sqlite3 blog.sqlite < init.sql

dev:
	cd blog && FLASK_APP=app FLASK_ENV=development python -m flask run
	
run:
	cd blog && FLASK_APP=app FLASK_ENV=production python -m flask run
