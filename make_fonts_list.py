#!/usr/bin/python3

# make a file containing details about fonts available in this repo.
# the file is made to be used by araste-get

import os

fonts_dir = './Fonts/'

files_list = os.listdir(fonts_dir)

list_file_dir = './Fonts/list.md'

list_file = open(list_file_dir, 'w')

HEADER_DOCTYPE = 'flf2a$'



for font_file_name in filter(lambda x : x.endswith('.flf'), files_list):
        with open(fonts_dir + font_file_name) as font_file:
            font_header = font_file.readline().split(' ')
            if font_header[0] == HEADER_DOCTYPE:
                print('# ' + font_file_name.rstrip('.flf'), file=list_file)
                for _ in range(int(font_header[5])):
                    print(font_file.readline().replace('\n', '  \n'), end='', file=list_file)
                print(file=list_file)