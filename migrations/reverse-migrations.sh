USER='root'
PASSWORD=''
DATABASE_NAME='mom_server'

mysql -u {$USER} -p {$PASSWORD} -e "DROP DATABASE {$DATABASE_NAME};"