
table_name = "topics_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("name", "VARCHAR(255)", ""),
        ("topic_id", "INT",  f"REFERENCES topics(id) ON DELETE CASCADE"),
        ("suscriber_id", "VARCHAR(255)",  f"REFERENCES users(id) ON DELETE CASCADE"),
]



