from datetime import datetime, timedelta
from random import randrange
from task_3_string import capitalize_first_words
from file_worker import TextFile
import re


def create_record_lines(class_name, text_to_publish):
    return (f'{class_name.ljust(35, "-")}\n'
            f'{text_to_publish}'
            f'\n-----------------------------------\n')


class News:
    txt = 'No text'
    city = 'No city'

    def create_record(self, txt=None, city=None):
        raw_txt = input('\nType the news: ') if txt is None else txt
        News().txt = capitalize_first_words(raw_txt)
        raw_city = input('Enter the city: ').title() if city is None else city
        News().city = raw_city.title()
        self.text_to_publish = f'{News().txt}\n{News().city}, {datetime.now().strftime("%d/%m/%Y %H.%m")}'
        return create_record_lines(__class__.__name__, self.text_to_publish)


class PrivateAd:
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
                print('We can offer you 15 days publishing')
                input_date = datetime.now() + timedelta(days=15)
                return input_date

    def create_record(self, txt=None, date=None):
        raw_txt = input('\nType the advertisement: ') if txt is None else txt
        txt = capitalize_first_words(raw_txt)
        date = self.__check_input_date(date)
        date_diff = date - datetime.now()
        text_to_publish = f'{txt}\nActual until: {date.strftime("%d/%m/%Y")}, {date_diff.days} days left'
        return create_record_lines(__class__.__name__, text_to_publish)


class Joke:
    def __rate_joke(self):
        joke_meter_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        return f'{joke_meter_list[randrange(10)]} of ten'

    def create_record(self, txt=None):
        raw_txt = input('\nType the joke: ') if txt is None else txt
        txt = capitalize_first_words(raw_txt)
        rate = self.__rate_joke()
        text_to_publish = f'{txt}\nFunny meter - {rate}'
        return create_record_lines(__class__.__name__, text_to_publish)


# print(Joke().create_record())


class NewsFeed:

    def __init__(self):
        self.news_feed = 'News feed:\n'
        self.new = News()
        self.ad = PrivateAd()
        self.joke = Joke()

    def add_content_manually(self):
        while True:
            option = input('Choose one of the following options You want to add in NewsFeed:\n'
                           '1 - News\n2 - PrivateAd\n3 - Joke\nYour choice: ')
            if option in ['1', '2', '3']:
                break
            print('\nIncorrect input. Try again!\n')
        if option == '1':
            content = self.new.create_record()
        elif option == '2':
            content = self.ad.create_record()
        else:
            content = self.joke.create_record()
        self.news_feed = self.news_feed + content
        print('\nNew content was added\n')

    def parse_text_file(self):
        pass

    def show_news_feed(self):
        for elem in self.news_feed:
            print(elem)

    def read_file(self):
        path = TextFile().get_full_path()
        with open(path, 'r') as file:
            text = file.read()
        print('\nNews feed was read from file\n')
        print(text)
        return text

    def save_as_file(self, news_feed):
        path = TextFile().get_full_path()
        with open(path, 'w') as file:
            file.write(news_feed)
        print('\nNews feed was saved as a file\n')


NewsFeed().read_file()
# my_news_feed.save_as_file()
# my_news_feed.add_content_manually()
