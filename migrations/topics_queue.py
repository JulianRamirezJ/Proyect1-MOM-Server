
table_name = "topics_queue"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("name", "VARCHAR(255)", ""),
        ("topic_id", "INT","NOT NULL"), 
        ("suscriber_id", "VARCHAR(255)", "NOT NULL")
]

foreign_keys = [
        ("topic_id", "topics"),
        ("suscriber_id", "users")
]




