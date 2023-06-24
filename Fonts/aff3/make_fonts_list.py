#!/usr/bin/python3

# make a file containing details about fonts available in this repo.
# the file is made to be used by araste-get

import os

fonts_dir = './'

files_list = os.listdir(fonts_dir)

list_file_dir = './list.md'

list_file = open(list_file_dir, 'w')

HEADER_DOCTYPE = 'aff3'


# open each font file in directory
for font_file_name in filter(lambda x : x.endswith('.aff'), files_list):
        with open(fonts_dir + font_file_name) as font_file:

            # check if file is really a font
            font_header = font_file.readline().split(' ')
            if font_header[0] == HEADER_DOCTYPE:

                # print font name (this is the name that araste-get uses)
                print('# ' + font_file_name[:-len(HEADER_DOCTYPE)], file=list_file)

                # print font comments below
                for _ in range(int(font_header[3])):
                    print(font_file.readline().replace('\n', '  \n'), end='', file=list_file)

                # newline between each header
                print(file=list_file)