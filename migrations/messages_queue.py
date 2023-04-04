
table_name = "messages_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("message", "TEXT", ""),
        ("queue_id", "INT", f"REFERENCES queues(id)")
]
