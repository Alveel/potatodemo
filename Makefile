build:
	s2i build .  registry.access.redhat.com/ubi8/python-38 potatodemo

run:
	docker run -i --rm --name potatodemo -p 8080:8080 potatodemo

stop:
	docker stop potatodemo

shell:
	docker exec -i -t potatodemo bash
