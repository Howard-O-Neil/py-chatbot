POSTGRES_HOST=py-chatbot-database
POSTGRES_PORT=5432
time_stamp=$(date +%s%N | cut -b1-13)
prefix=backup

pg_dump -h py-chatbot-database -U admin -d chatbot -s > ${prefix}/${time_stamp}-schema.sql