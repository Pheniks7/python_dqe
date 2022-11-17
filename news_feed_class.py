import os
import re
import json
import file_worker
from task_7_CSV import CsvParsing
from task_8_file_parser import FileParser


class NewsFeed:

    def __init__(self):
        self.news_feed = 'News feed:\n'
        self.csv = CsvParsing()
        self.parser = FileParser()

    def read_file(self):
        try:
            print('To read file you need to...')
            path = file_worker.get_full_path()
            file_type = re.search('.[a-z]+$', path).group(0).strip('.')
            with open(path, 'r') as file:
                print('\nNews feed was read from file\n')
                if file_type == 'txt' or file_type == 'doc':
                    data = file.read()
                    self.news_feed = self.news_feed + self.parser.add_content_from_text(data)
                elif file_type == 'json':
                    data = json.load(file)
                    self.news_feed = self.news_feed + self.parser.add_content_from_json(data)
                else:
                    raise FileNotFoundError
            os.remove(path)
            print('The file was deleted\n')
        except FileNotFoundError:
            print('The file was not found\n')
        self.choose_options()

    def show_news_feed(self):
        print(self.news_feed)
        self.csv.re_write_csv(self.news_feed)

    def save_as_file(self, txt=None):
        news_feed = self.news_feed if txt is None else txt
        print('To save News feed as a file you need to...')
        path = file_worker.get_full_path()
        with open(path, 'w') as file:
            file.write(news_feed)
        print('\nNews feed was saved as a file\n')
        self.csv.re_write_csv(self.news_feed)

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
            pass
