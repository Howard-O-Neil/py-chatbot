bootstrap:
	./script/bootstrap.sh

setup-dns:
	docker rm -f docker-proxy-dns
	docker-compose -f docker-proxy-dns.yaml up -d

restart:
	./script/restart.sh

monitor-app:
	grc tail -f gunicorn.error.log

reset-dns:
	docker-compose -f docker-proxy-dns.yaml restart | true
	docker restart docker-proxy-dns | true

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
