import sqlite3
import csv


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


def drop_tables():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        s3.execute("DROP TABLE if exists coffees")
        s3.execute("DROP TABLE if exists specials")
        s3.execute("DROP TABLE if exists ratings")
        s3.execute("DROP TABLE if exists stores")


def load_cafe_data():
    drop_tables()
    create_database()
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        with open("coffees.csv", 'r') as coffees_csv:
            done = False
            while not done:
                this_reader = csv.DictReader(coffees_csv, delimiter="\t")
                try:
                    thing = next(this_reader)
                    s3.execute('INSERT INTO coffees (coffee_name, type, cost_lb) VALUES (:coffee_name, :type, :cost_lb)', thing)
                except StopIteration:
                    done = True
        with open("ratings.csv", 'r') as ratings_csv:
            done = False
            while not done:
                this_reader = csv.DictReader(ratings_csv, delimiter="\t")
                try:
                    thing = next(this_reader)
                    s3.execute('INSERT INTO ratings (date, store_name, rating) VALUES (:date, :store_name, :rating)', thing)
                except StopIteration:
                    done = True
        with open("specials.csv", 'r') as specials_csv:
            done = False
            while not done:
                this_reader = csv.DictReader(specials_csv, delimiter="\t")
                try:
                    thing = next(this_reader)
                    s3.execute('INSERT INTO specials (date, store_name, coffee_name, price) VALUES (:date, :store_name, :coffee_name, :price)', thing)
                except StopIteration:
                    done = True
        with open("stores.csv", 'r') as stores_csv:
            done = False
            while not done:
                this_reader = csv.DictReader(stores_csv, delimiter="\t")
                try:
                    thing = next(this_reader)
                    s3.execute('INSERT INTO stores (store_name, type, cost_lb) VALUES (:store_name, :type, :cost_lb)', thing)
                except StopIteration:
                    done = True


def get_stores():
    return "something simple"


if __name__ == "__main__":
    load_cafe_data()
