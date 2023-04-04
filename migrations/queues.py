table_name = "queues"

columns = [
    ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
    ("name", "VARCHAR(255)", ""),
    ("user_id", "VARCHAR(255)", f"REFERENCES users(id)"),
]