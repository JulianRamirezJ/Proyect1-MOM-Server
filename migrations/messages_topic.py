
table_name = "messages_topic"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("message", "TEXT", ""),
        ("topic_id", "INT",  f"REFERENCES topics(id) ON DELETE CASCADE")
]
