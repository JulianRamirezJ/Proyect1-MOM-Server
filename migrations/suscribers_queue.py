
table_name = "suscribers_queue"

columns = [        
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("queue_id", "INT", "NOT NULL"), 
        ("suscriber_id", "VARCHAR(255)", "NOT NULL")]


foreign_keys = [
        ("queue_id", "queues"),
        ("suscriber_id", "users")
]

