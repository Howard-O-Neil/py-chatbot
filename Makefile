bootstrap:
	pip install virtualenv
	pip install --upgrade virtualenv
	virtualenv env
	. env/bin/activate
	pip install -r requirement.txt

setup-dns:
	docker-compose -f docker-proxy-dns.yaml up -d

reset-dns:
	docker-compose -f docker-proxy-dns.yaml restart

turnoff-dns:
	docker-compose -f docker-proxy-dns.yaml down

db-rm-revision:
	rm migrations/versions/${id}_.py

db-gen-migrate:
	./script/db-gen-migrate.sh

db-revert:
	./script/db-downgrade.sh

db-migrate:
	./script/db-gen-migrate.sh
	flask db upgrade

auth-script:
	chmod 777 script/*

dump-data:
	./script/dump-data.sh

dump-schema:
	./script/dump-schema.sh

dump-db:
	./script/dump-db.sh

# backup-data:
