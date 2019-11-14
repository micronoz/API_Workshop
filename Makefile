build:
	docker build --tag flask_demo .

run: build
	docker run -p 3500:8000 flask_demo