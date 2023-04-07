
table_name = "messages_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("message", "TEXT", ""),
        ("status", "BOOLEAN", "NOT NULL", "DEFAULT FALSE"),
        ("queue_id", "INT", "NOT NULL")
]

foreign_keys = [
        ("queue_id", "queues")
]