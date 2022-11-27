import os


def get_read_path():
    input_file_name = input('Input the file_name\n'
                            'Note: to skip this step - press Enter button\n-- ')
    input_name_dir = os.path.join('txt_files', input_file_name)
    if os.path.exists(input_name_dir) and os.path.isfile(input_name_dir):
        return input_name_dir
    else:
        raise FileNotFoundError


def get_write_path():
    output_file_name = input('Input the file_name\n'
                             'Note: to skip this step - press Enter button\n-- ')
    output_name_dir = os.path.join('txt_files', output_file_name)
    # if not re.search('[\w]+.txt$', output_name_dir) and not re.search('[\w]+.doc$', output_name_dir):
    if not os.path.isfile(output_name_dir):
        output_name_dir = os.path.join('txt_files', 'No_name_text_file.txt')
    return output_name_dir
