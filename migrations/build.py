import os
import mysql.connector
import config

mydb = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD
)

tables = ["users", "topics", "queues",
        "suscribers_queue","suscribers_topic",
        "messages_queue","messages_topic"]

table_files = ["users.py", "topics.py", "queues.py",
            "suscribers_queue.py","suscribers_topic.py",
            "messages_queue.py","messages_topic.py"]

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(config.DATABASE_NAME))
cursor.execute(f"USE {config.DATABASE_NAME};")
for i, table in enumerate(tables):
    with open(f"{table}_migration.sql", "w") as f:
        exec(open(table_files[i]).read())
        create_table = f"CREATE TABLE {table_name} (\n"

        for col in columns:
            if len(col) == 1:
                create_table += f"  {col[0]},\n"
            elif len(col) == 2:
                create_table += f"  {col[0]} {col[1]},\n"
            elif len(col) == 3:
                create_table += f"  {col[0]} {col[1]} {col[2]},\n"
            elif len(col) == 4:
                create_table += f"  {col[0]} {col[1]} {col[2]} {col[3]},\n"

        create_table = create_table[:-2] + "\n)"
        cursor.execute(create_table)
        mydb.commit()
