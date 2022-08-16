#!/usr/bin/python3
# this script converts old flf fonts to new aff font

from sys import argv



def glyph_header_flf2aff2(header: str, direction) -> str:

    # remove newline if there is any
    header = header.strip('\n')

    # identifier for variation
    variation_identifier = 'ـ'

    # get string itself without identifiers
    block_string = header.strip(variation_identifier)

    # set direction to 1 for rtl fonts

    # find variation of string

    # legend:
    # 
    # default = 0
    # initial = 1
    # middle = 2
    # final = 3
    # isolated = 4
    

    if header[0] == variation_identifier:
        if header[-1] == variation_identifier:
            variation = 2
        else:
            variation = 3
    elif header[-1] == variation_identifier:
        variation = 1
    else:
        variation = 4
    
    out = block_string + '\n' + str(variation) + ' ' + str(direction)

    return out

def block_strip(block:str) -> str:
    output = ''
    lines = block.split('\n')
    output_lines = [line[:-1] for line in lines[:-1]] + [lines[-1][:-2]]
    output = '\n'.join(output_lines)
    return output



direction = 1

font_filename = argv[1]


# read the font
try:
    fontfile = open(font_filename)
    flf_headers = fontfile.readline().split(' ')
except:
    raise FileNotFoundError

# get font headers
boardh = int(flf_headers[1])
korsi = int(flf_headers[2])
max_block_width = int(flf_headers[3])
comment_lines = int(flf_headers[5])
num_chars = int(flf_headers[8])

comments = ''
for _ in range(comment_lines):
    comments += fontfile.readline()


# get font characters
# font glyphs is character to block
font_glyphs = dict()
i = 0
while True:
    persianchars = fontfile.readline()[:-1]
    if len (persianchars) < 1:
        break
    persianasciichars = '\n'.join(
        [fontfile.readline()[:-2] for _ in range(boardh)])[:-1]
    font_glyphs[persianchars] = persianasciichars

    i += 1

num_chars = i


# generate header
aff2_headers =[
    # document identifier
    'aff2',
    # block height
    str(flf_headers[1]),
    # baseline
    str(int(flf_headers[2]) + 1),
    # number of comment lines
    str(flf_headers[5]),
    # maximum width of blocks
    str(flf_headers[3]),
    # number of blocks
    str(num_chars),
]

# print header
print(' '.join(aff2_headers))
print(comments, end='')

# print glyphs
for character in font_glyphs.keys():
    # max_line_width = max([len(line) for line in font_glyphs[character].split('\n')])

    print(glyph_header_flf2aff2(character, direction))
    print(font_glyphs[character])


