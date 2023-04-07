table_name = "topics"

columns = [    
    ("id", "INT", "AUTO_INCREMENT UNIQUE", "PRIMARY KEY"), 
    ("name", "VARCHAR(255)", ""),    
    ("user_id", "VARCHAR(255)", "NOT NULL")
]

foreign_keys = [
        ("user_id", "users")
]