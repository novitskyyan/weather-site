import sqlite3


class DataBase:
    def __init__(self, db_name, table_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_name = table_name
        self.create_table()

    def create_table(self):
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name}" \
                             f"(" \
                             f"id INTEGER PRIMARY KEY AUTOINCREMENT," \
                             f"city TEXT," \
                             f"temp TEXT," \
                             f"min_temp TEXT," \
                             f"max_temp TEXT," \
                             f"description TEXT," \
                             f"wind TEXT," \
                             f"sunset TEXT," \
                             f"sunrise TEXT);"
        self.cursor.execute(create_table_query)

        self.conn.commit()

    def add_city(self, city_, temp_, min_temp_, max_temp_, description_,
                 wind_,
                 sunrise_, sunset_):
        city_info_query = f"INSERT INTO {self.table_name} (city, temp, " \
                          f"min_temp, max_temp, description, wind, " \
                          f"sunset, sunrise) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        data_tuple = (city_, temp_, min_temp_, max_temp_, description_,
                      wind_,
                      sunrise_, sunset_)
        self.cursor.execute(city_info_query, data_tuple)
        self.conn.commit()

    def get_cities(self):
        city_info_query = f"SELECT * FROM {self.table_name} ORDER BY id DESC LIMIT 4"
        self.cursor.execute(city_info_query)
        rows = [city[1:] for city in self.cursor.fetchall()]
        return rows
