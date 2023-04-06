
table_name = "messages_topic"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("message", "TEXT", ""),
        ("status", "BOOLEAN", "NOT NULL", "DEFAULT FALSE"),
        ("topic_queue_id", "INT",  f"REFERENCES topics_queue(id) ON DELETE CASCADE")
]
