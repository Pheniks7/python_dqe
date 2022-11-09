import re


def check_path(raw_input_text):
    input_text = raw_input_text.strip()
    input_text_format = input_text if re.search('.txt$',
                                                input_text) or re.search('.doc$',
                                                                         input_text) else input_text + '.txt'
    file_path = input_text_format if re.search('^C:', input_text_format) else 'txt_files\\' + input_text_format
    return file_path


def get_full_path():
    input_name_dir = input('Input the file_name (with its path - optional)\n'
                           'Note: to skip this step - press Enter button\n-- ')
    if re.search('[\w]+', input_name_dir):
        full_path = check_path(input_name_dir)
    else:
        full_path = 'txt_files\\No_name_text_file.txt'
    return full_path
