build:
	docker build . --tag custom-python-ubi
	s2i build . custom-python-ubi potatodemo
	docker tag potatodemo tstocp1.azurecr.io/alwyn/potatodemo:latest

push:
	docker push tstocp1.azurecr.io/alwyn/potatodemo

run:
	docker run -i --rm --name potatodemo -p 8080:8080 potatodemo

stop:
	docker stop potatodemo

shell:
	docker exec -i -t potatodemo bash
