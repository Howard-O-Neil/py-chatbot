python manage.py db migrate --rev-id $(date +%s%N | cut -b1-13)