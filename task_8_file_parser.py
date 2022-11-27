import re
from task_3_string import parse_text_by_pattern
from task_5_classes_wo_init import News, PrivateAd, Joke


class FileParser:
    def __init__(self):
        self.new = News()
        self.ad = PrivateAd()
        self.joke = Joke()

    def choose_option(self, options, option_number):
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

    def add_content_manually(self):
        manual_content = ''
        while True:
            option = self.choose_option('1 - Add News\n2 - Add PrivateAd\n3 - Add Joke\n4 - Other', 4)
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
                break
            print(f'\n{content}\nNew content was added\n' if content is not None else 'No new content')
            manual_content = manual_content + content
        return manual_content

    def add_content_from_text(self, data):
        text_content = ''
        for elem in data.split('-|-'):
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
            text_content = text_content + content
        return text_content

    def add_content_from_json(self, data):
        json_content = ''
        for elem in data.values():
            if elem['type'] == 'News':
                news = elem['body']
                if news is None:
                    continue
                city = elem['city'] if elem['city'] is not None else 'No city'
                self.new.make_news(news, city)
                content = self.new.create_record()
            elif elem['type'] == 'PrivateAd':
                ad = elem['body']
                if ad is None:
                    continue
                date = elem['date']
                self.ad.make_ad(ad, date)
                content = self.ad.create_record()
            elif elem['type'] == 'Joke':
                joke = elem['body']
                if joke is None:
                    continue
                self.joke.make_joke(joke)
                content = self.joke.create_record()
            else:
                print('Wrong recognition pattern is detected in the file\n')
                content = ''
            json_content = json_content + content
        return json_content

    def add_content_from_xml(self, data):
        xml_content = ''
        root = data.getroot()
        for elem in root.iter('content'):
            if elem.attrib['type'] == 'News':
                news = elem.find('body').text
                if news is None:
                    continue
                city = elem.find('city').text if elem.find('city') is not None else 'No city'
                self.new.make_news(news, city)
                content = self.new.create_record()
            elif elem.attrib['type'] == 'PrivateAd':
                ad = elem.find('body').text
                if ad is None:
                    continue
                date = elem.find('date').text
                self.ad.make_ad(ad, date)
                content = self.ad.create_record()
            elif elem.attrib['type'] == 'Joke':
                joke = elem.find('body').text
                if joke is None:
                    continue
                self.joke.make_joke(joke)
                content = self.joke.create_record()
            else:
                print('Wrong recognition pattern is detected in the file\n')
                content = ''
            xml_content = xml_content + content
        return xml_content
