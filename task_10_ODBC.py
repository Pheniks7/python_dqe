import sqlite3


class DBConnection:
    database = 'news_feed.db'

    script = 'CREATE TABLE IF NOT EXISTS news (news_text TEXT NOT NULL, city TEXT NOT NULL, PRIMARY KEY(news_text, city));' \
             'CREATE TABLE IF NOT EXISTS private_ad (ad_text TEXT NOT NULL, date TEXT NOT NULL, PRIMARY KEY(ad_text, date));' \
             'CREATE TABLE IF NOT EXISTS joke (joke_text TEXT NOT NULL, rate TEXT NOT NULL, PRIMARY KEY(joke_text, rate));'

    def __init__(self):
        with sqlite3.connect(DBConnection.database) as self.connection:
            self.cursor = self.connection.cursor()
            self.cursor.executescript(DBConnection.script)
            self.connection.commit()

    def add_record(self, table_name, col1, col2):
        try:
            self.cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?);', (col1, col2))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('\nThis record already exists in the table\n')
        except sqlite3.Error:
            print('\nSome error happened while adding values into the table\n')
        finally:
            self.cursor.close()

    def show_tables(self):
        query_list = ['SELECT * FROM news', 'SELECT * FROM private_ad', 'SELECT * FROM joke']
        print('Printing DataBase...')
        for item in query_list:
            print('The result for query:', item)
            for row in self.cursor.execute(item).fetchall():
                print(row)
