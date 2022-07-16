from sys import argv
fname = argv[1]
exec(open(fname).read())
    
maxwidth = 0
for block in font_glyphs.values():
    lines = block.split('\n')
    height = len(lines) + 1
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

codetag_count = len(font_glyphs.keys())

print('flf2a$', height, korsi, maxwidth, old_layout, comment_lines, rtl, new_layout, codetag_count)
print(comment)

for k in font_glyphs.keys():
    print(k)
    print(font_glyphs[k].replace('@', '#').replace('\n', '@\n')[:-1]+'@')