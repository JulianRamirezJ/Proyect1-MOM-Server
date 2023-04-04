table_name = "topics"

columns = [
    ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
    ("name", "VARCHAR(255)", ""),
    ("user_id", "INT", f"REFERENCES users(id)")
]