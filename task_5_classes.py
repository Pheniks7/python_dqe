import os
import re
from datetime import datetime, timedelta
from random import randrange
import file_worker

from task_3_string import capitalize_first_words, parse_text_by_pattern


def create_record_lines(class_name, text_to_publish):
    return (f'\n{class_name.ljust(35, "-")}\n'
            f'{text_to_publish}\n'
            f'-----------------------------------\n')


class News:
    def __init__(self, txt=None, city=None):
        self.cur_time = datetime.now()
        self.txt = capitalize_first_words(input('\nType the news: ') if txt is None else txt)
        self.city = (input('Enter the city: ').title() if city is None else city).title()

    def create_record(self):
        text_to_publish = f'{self.txt}\n{self.city}, {self.cur_time.strftime("%d/%m/%Y %H.%m")}'
        return create_record_lines(__class__.__name__, text_to_publish)


class PrivateAd:
    def __init__(self, txt=None, date=None):
        self.txt = capitalize_first_words(input('\nType the advertisement: ') if txt is None else txt)
        self.date = self.__check_input_date(date)

    def __check_input_date(self, date=None):
        for i in range(3):
            try:
                input_date_raw = input(
                    'Enter the ad expiration date in this formate "dd/mm/yy": ') if date is None else date
                input_date = datetime.strptime(input_date_raw, '%d/%m/%y')
                date_diff = int((input_date - datetime.now()).days)
                if date_diff < 0 or date_diff > 365:
                    raise ValueError('\nPlease, enter valid date')
                return input_date
            except ValueError:
                print('\nPlease, enter the expiration date with VALID value AND in CORRECT formate "dd/mm/yy"')
            if i == 2:
                print('\nWe can offer you 15 days publishing\n')
                input_date = datetime.now() + timedelta(days=15)
                return input_date

    def create_record(self):
        date_diff = self.date - datetime.now()
        text_to_publish = f'{self.txt}\nActual until: {self.date.strftime("%d/%m/%Y")}, {date_diff.days} days left'
        return create_record_lines(__class__.__name__, text_to_publish)


class Joke:

    def __init__(self, txt=None):
        self.txt = capitalize_first_words(input('\nType the joke: ') if txt is None else txt)
        self.rate = self.__rate_joke()

    def __rate_joke(self):
        joke_meter_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        return f'{joke_meter_list[randrange(10)]} of ten'

    def create_record(self):
        text_to_publish = f'{self.txt}\nFunny meter - {self.rate}'
        return create_record_lines(__class__.__name__, text_to_publish)


class NewsFeed:

    def __init__(self):
        # self.news_feed = ['News feed:\n']
        self.news_feed = 'News feed:\n'

    def add_content_manually(self):
        while True:
            option = input('Choose one of the following options You want to add in NewsFeed:\n'
                           '1 - News\n2 - PrivateAd\n3 - Joke\nYour choice: ')
            if option in ['1', '2', '3']:
                break
            print('\nIncorrect input. Try again!\n')
        if option == '1':
            content = News().create_record()
        elif option == '2':
            content = PrivateAd().create_record()
        else:
            content = Joke().create_record()
        self.news_feed = self.news_feed + content
        print('\nNew content was added\n')

    def add_content_from_text(self, txt):
        raw_list = txt.split('-|-')
        for elem in raw_list:
            if re.search('News:', elem):
                news = parse_text_by_pattern('News:(.+)City:(.*)$', elem)
                if news is None:
                    continue
                raw_city = parse_text_by_pattern('City:(.+)$', elem)
                city = raw_city if raw_city is not None else 'No city'
                content = News(news, city).create_record()
            elif re.search('PrivateAd:', elem):
                ad = parse_text_by_pattern('PrivateAd:(.+)Date:(.+)$', elem)
                if ad is None:
                    continue
                date = parse_text_by_pattern('Date:(.+)$', elem)
                content = PrivateAd(ad, date).create_record()
            elif re.search('Joke:', elem):
                joke = parse_text_by_pattern('Joke:(.+)$', elem)
                if joke is None:
                    continue
                content = Joke(joke).create_record()
            else:
                print('Wrong recognition pattern is detected in the file\n')
                content = ''
            self.news_feed = self.news_feed + content

    def show_news_feed(self):
        print(self.news_feed)

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
            return text
        except FileNotFoundError:
            print('The file was not found\n')

    def save_as_file(self, txt=None):
        news_feed = self.news_feed if txt is None else txt
        print('To save News feed as a file you need to...')
        path = file_worker.get_full_path()
        with open(path, 'w') as file:
            file.write(news_feed)
        print('\nNews feed was saved as a file\n')
