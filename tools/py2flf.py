from sys import argv
fname = argv[1]
exec(open(fname).read())
    
maxwidth = 0
for block in font_glyphs.values():
    lines = block.split('\n')
    height = len(lines)
    for line in lines:
        maxwidth = max(maxwidth, len(line))

my_name = 'name <email>'
comment = f'''{fname}
    this is a font file for araste
    designed by {my_name}
'''

comment_lines = len(comment.split('\n'))

old_layout = 0
new_layout = 0

rtl = 1

# count chars
codetag_count = 0
checked_chars = []
for char in font_glyphs.keys():
    only_char = char.strip('ـ')
    if only_char not in checked_chars:
        # print_cg('ـ' + only_char)
        # print_cg('ـ' + only_char + 'ـ')
        # print_cg(only_char + 'ـ')
        # print_cg(only_char)
        checked_chars.append(only_char)
        codetag_count += 4


# print headers
print('flf2a$', height, korsi, maxwidth, old_layout, comment_lines, rtl, new_layout, codetag_count)
print(comment)

def print_cg(k):

    if k in font_glyphs:
        glyph = font_glyphs[k]
    elif k[1:] in font_glyphs:
        glyph = font_glyphs[k[1:]]
    elif k[:-1] in font_glyphs:
        glyph = font_glyphs[k[:-1]]

    elif k[1:-1] in font_glyphs:
        glyph = font_glyphs[k[1:-1]]
    else:
        glyph = font_glyphs[' ']
    print(k)
    print(glyph.replace('\n', '@\n')+'@@')

z = []
for k in font_glyphs.keys():
    q = k.strip('ـ')
    if q not in z:
        print_cg('ـ' + q)
        print_cg('ـ' + q + 'ـ')
        print_cg(q + 'ـ')
        print_cg(q)
        z.append(q)

# print(j)
