import sqlite3


def create_database():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        s3.execute("""CREATE TABLE IF NOT EXISTS coffees (
                    id INTEGER PRIMARY KEY,
                    coffee_name  TEXT NOT NULL,
                    type TEXT,
                    cost_lb REAL
                   )
                """)
        s3.execute("""CREATE TABLE IF NOT EXISTS ratings (
                    id INTEGER PRIMARY KEY,
                    date  TEXT NOT NULL,
                    store_name TEXT,
                    rating REAL
                   )
                """)
        s3.execute("""CREATE TABLE IF NOT EXISTS specials (
                    id INTEGER PRIMARY KEY,
                    date  TEXT NOT NULL,
                    store_name TEXT,
                    coffee_name TEXT,
                    price REAL
                   )
                """)
        s3.execute("""CREATE TABLE IF NOT EXISTS stores (
                    id INTEGER PRIMARY KEY,
                    store_name  TEXT NOT NULL,
                    type TEXT,
                    cost_lb REAL
                   )
                """)
        s3.execute("CREATE  INDEX coffees_coffee_name_index ON coffees(coffee_name)")
        s3.execute("CREATE  INDEX ratings_store_name_index ON ratings(store_name)")
        s3.execute("CREATE  INDEX specials_coffee_name_index ON specials(coffee_name)")
        s3.execute("CREATE  INDEX specials_store_name_index ON specials(store_name)")
        s3.execute("CREATE  INDEX stores_store_name_index ON stores(store_name)")
        s3.execute("CREATE  INDEX ratings_date_index ON ratings(date)")
        s3.execute("CREATE  INDEX specials_date_index ON specials(date)")
