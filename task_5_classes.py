from datetime import datetime, timedelta
from random import randrange


class News:
    def __init__(self):
        self.cur_time = datetime.now()
        self.txt = input('\nType the news: ').capitalize()
        self.city = input('Enter the city: ').title()

    def publish(self):
        return (f'News ------------------------------\n'
                f'{self.txt}\n{self.city}, {self.cur_time.strftime("%d/%m/%Y %H.%m")}'
                f'\n-----------------------------------\n')


class PrivateAd:
    def __init__(self):
        self.txt = input('\nType the advertisement: ').capitalize()
        self.date = self.__check_input_date()

    def __check_input_date(self):
        for i in range(3):
            try:
                input_date = datetime.strptime(input('Enter the ad expiration date in this formate "dd/mm/yy": '),
                                               '%d/%m/%y')
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

    def publish(self):
        date_diff = self.date - datetime.now()
        return (f'Private Ad ------------------------\n'
                f'{self.txt}\nActual until: {self.date.strftime("%d/%m/%Y")}, {date_diff.days} days left'
                f'\n-----------------------------------\n')


class Joke:
    __JOKE_METER_LIST = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    def __init__(self):
        self.txt = input('\nType the joke: ').capitalize()
        self.rate = self.__rate_joke()

    def __rate_joke(self):
        return f'{Joke.__JOKE_METER_LIST[randrange(10)]} of ten'

    def publish(self):
        return (f'Joke of the day -------------------\n'
                f'{self.txt}\nFunny meter - {self.rate}'
                f'\n-----------------------------------\n')


class NewsFeed:
    __OPTION = {'1': 'News()', '2': 'PrivateAd()', '3': 'Joke()'}

    def __init__(self):
        self.news_feed = ['News feed:\n']

    def add_content(self):
        while True:
            option = input('Choose one of the following options You want to add in NewsFeed:\n'
                           '1 - News\n2 - PrivateAd\n3 - Joke\nYour choice: ')
            if option in ['1', '2', '3']:
                break
            print('\nIncorrect input. Try again!\n')
        content = eval(NewsFeed.__OPTION[option]).publish()
        self.news_feed.append(content)
        print('\nNew content was added\n')

    def show_news_feed(self):
        for elem in self.news_feed:
            print(elem)


my_news_feed = NewsFeed()
my_news_feed.add_content()
my_news_feed.add_content()
my_news_feed.add_content()
my_news_feed.show_news_feed()
