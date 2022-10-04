import re

initial_text = '''homework:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''


def count_whitespaces(txt):
    counter = 0
    for symbol in range(len(txt)):
        if txt[symbol].isspace():
            counter += 1
    return counter


def count_whitespaces_2(txt):
    counter = re.findall('\s', txt)
    return len(counter)


def fix_iz_get_lower(txt):
    new_txt = txt.lower().replace(' iz ', ' is ')
    return new_txt


def extract_append_last_words(txt):
    last_words_lst = re.findall('\s(\w+)[.|!|?|…]', txt)
    last_words_sentence = ' '.join(last_words_lst).capitalize() + '.'
    full_txt = txt.capitalize() + ' ' + last_words_sentence
    return full_txt


def capitalize_first_words(txt):
    lines = []
    for line in txt.split('\n'):
        sentences = []
        for sentence in line.split('.'):
            m = re.match('[ \n|\t]*(.*)', sentence)
            sentences.append(re.sub(m.group(1), m.group(1).capitalize(), sentence))
        lines.append('.'.join(sentences))
    return '\n'.join(lines)


print('Number of whitespace characters:', count_whitespaces(initial_text))
print('Number of whitespace characters:', count_whitespaces_2(initial_text), '\n')

text_update_1 = fix_iz_get_lower(initial_text)
print('With fixed IZ\n', text_update_1, '\n')

text_update_2 = extract_append_last_words(text_update_1)
print('With appended string\n', text_update_2, '\n')

text_update_3 = capitalize_first_words(text_update_2)
print('With capitalized 1st words\n', text_update_3, '\n')
