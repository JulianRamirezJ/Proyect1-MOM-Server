
table_name = "suscribers_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("queue_id", "INT",  f"REFERENCES queues(id) ON DELETE CASCADE"),
        ("user_id", "VARCHAR(255)",  f"REFERENCES users(id) ON DELETE CASCADE")
]



