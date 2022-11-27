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
    control_phrase = 'add it to the end of this paragraph.'
    last_words_lst = re.findall('\s(\w+)[.|!|?|…]', txt)
    last_words_sentence = control_phrase + ' ' + ' '.join(last_words_lst).capitalize() + '.'
    full_txt = re.sub(control_phrase, last_words_sentence, txt)
    return full_txt


def start_paragraph(txt):
    m = re.search('^\s*(\w)', txt)
    start = m.span()[0]
    end = m.span()[1]
    txt = re.sub(txt[start:end], txt[start:end].upper(), txt, 1)
    return txt


def check_one_match(txt):
    pattern = '[.|!|?|\n]\s*[a-z]'
    if re.search(pattern, txt):
        m = re.search(pattern, txt)
        start = m.span()[0]
        end = m.span()[1]
        fisrt_word_upper = txt[start:end].upper()
        txt = txt[:start] + fisrt_word_upper + txt[end:]
        while len(re.findall(pattern, txt)) > 0:
            txt = check_one_match(txt)
    return txt


def capitalize_first_words(txt):
    if txt is None or txt == '':
        txt = 'No text'
    txt = start_paragraph(txt)
    txt = check_one_match(txt)
    return txt


def parse_text_by_pattern(pattern, txt):
    try:
        found = re.search(pattern, txt.strip()).group(1)
        return found.strip()
    except AttributeError:
        return None

# print('Number of whitespace characters:', count_whitespaces(initial_text))
# print('Number of whitespace characters:', count_whitespaces_2(initial_text), '\n')

# text_update_1 = fix_iz_get_lower(initial_text)
# print('With fixed IZ\n', text_update_1, '\n')

# text_update_2 = extract_append_last_words(text_update_1)
# print('With appended string\n', text_update_2, '\n')

# text_update_3 = capitalize_first_words(text_update_2)
# print('With capitalized 1st words V_1\n', text_update_3, '\n')

# text_update_4 = capitalize_first_words_2(text_update_2)
# print('With capitalized 1st words V_2\n', text_update_4, '\n')
