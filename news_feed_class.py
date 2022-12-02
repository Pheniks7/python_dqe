import os
import re
import json
import sys
import xml.etree.ElementTree as ET
import file_worker
from task_7_CSV import CsvParsing
from task_8_file_parser import FileParser
from task_10_ODBC import DBConnection


class NewsFeed:

    def __init__(self):
        self.news_feed = 'News feed:\n'
        self.csv = CsvParsing()
        self.parser = FileParser()
        self.db_conn = DBConnection()

    def read_file(self):
        try:
            print('\nTo read file you need to...')
            path = file_worker.get_read_path()
            file_type = re.search('.[a-z]+$', path).group(0).strip('.')
            prev_len = len(self.news_feed)
            with open(path, 'r', encoding='utf8') as file:
                print('\nNews feed was read from file\n')
                if file_type == 'txt' or file_type == 'doc':
                    data = file.read()
                    self.news_feed = self.news_feed + self.parser.add_content_from_text(data)
                elif file_type == 'json':
                    data = json.load(file)
                    self.news_feed = self.news_feed + self.parser.add_content_from_json(data)
                elif file_type == 'xml':
                    data = ET.parse(file)
                    self.news_feed = self.news_feed + self.parser.add_content_from_xml(data)
                else:
                    raise FileNotFoundError
            if len(self.news_feed) > prev_len:
                os.remove(path)
                print('The file was deleted\n')
        except FileNotFoundError:
            print('The file was not found\n')
        self.choose_options()

    def show_news_feed(self):
        print(self.news_feed)
        self.csv.re_write_csv(self.news_feed)
        self.db_conn.show_tables()

    def save_as_file(self, txt=None):
        news_feed = self.news_feed if txt is None else txt
        print('\nTo save News feed as a file you need to...')
        path = file_worker.get_write_path()
        with open(path, 'w', encoding='utf8') as file:
            file.write(news_feed)
        print('\nNews feed was saved as a file\n')
        self.csv.re_write_csv(self.news_feed)
        self.db_conn.show_tables()

    def choose_options(self):
        option = self.parser.choose_option(
            '1 - Add manually\n2 - Add from file\n3 - Show News feed\n4 - Save in file\n5 - Stop & Quit', 5)
        if option == '1':
            self.news_feed = self.news_feed + self.parser.add_content_manually()
            self.choose_options()
        elif option == '2':
            self.read_file()
        elif option == '3':
            self.show_news_feed()
        elif option == '4':
            self.save_as_file()
        else:
            sys.exit()
