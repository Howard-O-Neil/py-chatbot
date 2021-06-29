time_stamp=$(date +%s%N | cut -b1-13)
prefix=backup

pg_dump -h py-chatbot-database -U admin -d chatbot -a > ${prefix}/${time_stamp}-data.sql