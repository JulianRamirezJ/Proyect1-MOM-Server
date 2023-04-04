
table_name = "suscribers_topic"

columns = [
        ("id", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
        ("topic_id", "INT", f"REFERENCES topics(id)"),
        ("user_id", "INT", f"REFERENCES users(id)"),
]



