
table_name = "suscribers_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("queue_id", "INT", f"REFERENCES queues(id)"),
        ("user_id", "VARCHAR(255)", f"REFERENCES users(id)")
]



