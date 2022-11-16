import os
import re
import file_worker
from task_3_string import parse_text_by_pattern
from task_5_classes_wo_init import News, PrivateAd, Joke
from task_7_CSV import CsvParsing


def choose_option(options, option_number):
    counter = 0
    while True:
        option = input('\nChoose one of the following options to work with NewsFeed:\n'
                       f'{options}\nYour choice: ')
        if option in map(str, range(1, option_number + 1)):
            break
        counter = counter + 1
        if counter < 3:
            print('\nIncorrect input. Try again!\n')
        else:
            print('\nIncorrect input. Stop & Quit!\n')
            break
    return option


class NewsFeed:

    def __init__(self):
        self.news_feed = 'News feed:\n'
        self.new = News()
        self.ad = PrivateAd()
        self.joke = Joke()
        self.csv = CsvParsing()

    def add_content_manually(self):
        while True:
            option = choose_option('1 - Add News\n2 - Add PrivateAd\n3 - Add Joke\n4 - Other', 4)
            if option == '1':
                self.new.make_news()
                content = self.new.create_record()
            elif option == '2':
                self.ad.make_ad()
                content = self.ad.create_record()
            elif option == '3':
                self.joke.make_joke()
                content = self.joke.create_record()
            else:
                self.choose_options()
                break
            self.news_feed = self.news_feed + content
            print(f'\n{content}\nNew content was added\n' if content is not None else 'No new content')

    def add_content_from_text(self, txt):
        raw_list = txt.split('-|-')
        for elem in raw_list:
            if re.search('News:', elem):
                news = parse_text_by_pattern('News:(.+)City:(.*)$', elem)
                if news is None:
                    continue
                raw_city = parse_text_by_pattern('City:(.+)$', elem)
                city = raw_city if raw_city is not None else 'No city'
                self.new.make_news(news, city)
                content = self.new.create_record()
            elif re.search('PrivateAd:', elem):
                ad = parse_text_by_pattern('PrivateAd:(.+)Date:(.+)$', elem)
                if ad is None:
                    continue
                date = parse_text_by_pattern('Date:(.+)$', elem)
                self.ad.make_ad(ad, date)
                content = self.ad.create_record()
            elif re.search('Joke:', elem):
                joke = parse_text_by_pattern('Joke:(.+)$', elem)
                if joke is None:
                    continue
                self.joke.make_joke(joke)
                content = self.joke.create_record()
            else:
                print('Wrong recognition pattern is detected in the file\n')
                content = ''
            self.news_feed = self.news_feed + content

    def show_news_feed(self):
        print(self.news_feed)
        self.csv.re_write_csv(self.news_feed)

    def read_file(self):
        try:
            print('To read file you need to...')
            path = file_worker.get_full_path()
            with open(path, 'r') as file:
                text = file.read()
            print('\nNews feed was read from file\n')
            self.add_content_from_text(text)
            os.remove(path)
            print('The file was deleted\n')
        except FileNotFoundError:
            print('The file was not found\n')
        self.choose_options()

    def save_as_file(self, txt=None):
        news_feed = self.news_feed if txt is None else txt
        print('To save News feed as a file you need to...')
        path = file_worker.get_full_path()
        with open(path, 'w') as file:
            file.write(news_feed)
        print('\nNews feed was saved as a file\n')
        self.csv.re_write_csv(self.news_feed)

    def choose_options(self):
        option = choose_option(
            '1 - Add manually\n2 - Add from file\n3 - Show News feed\n4 - Save in file\n5 - Stop & Quit', 5)
        if option == '1':
            self.add_content_manually()
        elif option == '2':
            self.read_file()
        elif option == '3':
            self.show_news_feed()
        elif option == '4':
            self.save_as_file()
        else:
            pass
