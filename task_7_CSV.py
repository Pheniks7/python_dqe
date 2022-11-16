import csv
import re
import string


class CsvParsing:
    pattern = f'[{string.punctuation.replace("_", "")}|\s]'

    def extract_words(self, text):
        word_set = set()
        for word in re.split(CsvParsing().pattern, text):
            word_set.add(re.sub('[^\w]', '', word))
        return sorted(list(word_set - {''}))

    def count_word(self, text):
        word_list = self.extract_words(text)
        count_word_list = []
        for word in word_list:
            count = len(re.findall(f'({CsvParsing().pattern}|^){word}({CsvParsing().pattern}|$)', text))
            count_word_list.append([word, count])
        return count_word_list

    def count_letter(self, raw_text):
        text = raw_text.lower()
        alphabet = list(string.ascii_lowercase)
        total_count = len(re.findall('[a-z]{1}', text))
        count_letter_list = []
        try:
            for letter in alphabet:
                count_letter_list.append([letter, text.count(letter), raw_text.count(letter.upper()),
                                          round(text.count(letter) * 100 / total_count, 2)])
        except ZeroDivisionError:
            print('Game over')
        return count_letter_list

    def save_as_csv(self, file_name, count_list):
        if len(count_list) > 0:
            with open(f'txt_files/{file_name}', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                for item in count_list:
                    writer.writerow(item)
            print(f'File {file_name} is updated\n')

    def re_write_csv(self, raw_text):
        count_word_list = self.count_word(raw_text.lower())
        self.save_as_csv('count_word.csv', count_word_list)
        count_letter_list = self.count_letter(raw_text)
        self.save_as_csv('count_letter.csv', count_letter_list)

#
# with open('txt_files/No_name_text_file.txt', 'r') as file:
#     txt = file.read()
#     CsvParsing().re_write_csv(txt)
