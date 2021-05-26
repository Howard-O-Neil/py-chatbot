bootstrap:
	pip install virtualenv
	pip install --upgrade virtualenv
	virtualenv env
	. env/bin/activate
	pip install -r requirement.txt

setup-dns:
	docker-compose -f docker-proxy-dns.yaml up

auth-script:
	chmod 777 script/*

dump-data:
	./script/dump-data.sh

dump-schema:
	./script/dump-schema.sh

dump-db:
	./script/dump-db.sh

# backup-data:
