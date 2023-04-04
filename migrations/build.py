import os
import mysql.connector
import config

mydb = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(config.DATABASE_NAME))

tables = ["users", "topics", "queues",
        "suscribers_queue","suscribers_topic",
        "messages_queue","messages_topic"]

table_files = ["users.py", "topics.py", "queues.py",
            "suscribers_queue.py","suscribers_topic.py",
            "messages_queue.py","messages_topic.py"]

for i, table in enumerate(tables):
    with open(f"{table}_migration.sql", "w") as f:
        exec(open(table_files[i]).read())
        create_table = f"CREATE TABLE {table_name} (\n"
        for col in columns:
            create_table += f"  {col[0]} {col[1]} {col[2]},\n"
        create_table = create_table[:-2] + "\n)"
        
        f.write(f"USE mydatabase;\n\n{create_table};\n")