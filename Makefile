build:
	s2i build .  registry.access.redhat.com/ubi8/python-38 potatodemo

run:
	docker run -i -d --rm --name potatodemo -p 5000:5000 potatodemo

stop:
	docker stop potatodemo

log:
	docker logs -f potatodemo

shell:
	docker exec -i -t potatodemo bash
