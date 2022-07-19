import cv2
import numpy as np

# things to set
image_name = '../pixelart.png'
raw_height = 13
num_of_raws = 3
image_width = 512
korsi = 7
maxwidth = 11
characters = ['ا', '‍ا', 'آ', '‍آ', 'ب‍', 'ب', 'پ‍', 'پ', 'ت‍', 'ت', 'ث‍', 'ث', 'ج‍', 'ج', 'چ‍', 'چ',
              'ح‍', 'ح', 'خ‍', 'خ', 'د', '‍د', 'ذ', '‍ذ', 'ر', '‍ر', 'ز', '‍ز', 'ژ', '‍ژ', 'س‍', '‍س‍',
              '‍س', 'س', 'ش‍', '‍ش‍', '‍ش', 'ش', 'ص‍',
              '‍ص‍', '‍ص', 'ص', 'ض‍', '‍ض‍', 'ض', '‍ض', 'ط‍', 'ط', 'ظ‍', 'ظ',
              'ع‍', '‍ع‍', '‍ع', 'ع', 'غ‍', '‍غ‍', '‍غ',
              'غ', 'ف‍', 'ف', 'ق‍', 'ق', 'ک‍', '‍ک‍', '‍ک', 'ک', 'گ‍', '‍گ‍', '‍گ', 'گ', 'ل‍', 'ل', 'م‍', '‍م‍',
              'م', 'ن‍', 'ن', 'و', 'ه‍', '‍ه‍', '‍ه', 'ه', 'ی‍', '‍ی', 'ی', ' ',
              '(', ')', '.', '،', '!', '؟', '؛',  '«', '»', 
              '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', ]

comment = """your font
designed to be used in araste app
name <email>"""
char_for_zero = "██"
char_for_one = "  "


chars = [' ', '▘', '▝', '▀', '▖', '▍', '▞', '▛', '▗', '▚', '▐', '▜', '▃', '▙', '▟', '▉']

# read image raws and concatenate them
image = cv2.imread(image_name)
z = [0 for _ in range(num_of_raws)]
for i in range(num_of_raws):
    z[i] = image[i * (raw_height + 1) + 1: (i + 1) * (raw_height + 1) + 1]

z.reverse()
z = np.concatenate(z, axis=1)


q = []


# print a glyph block
def flf_print(g):
    i = 0
    for r in g:
        if i == 0:
            i = 1
        else:
            print()
        for z in r:
            if z == 1:
                print(char_for_one, end='')
            else:
                print(char_for_zero, end='')
        print('@', end='')
    print('@')


def kprint(a):
    # print(len(a), len(a[0]))
    for i in range(0, len(a)-2, 2):
        for j in range(0, len(a[i]) - 2, 2):
            # print(i, j)
            g = 0
            if a[i, j] == 0:
                g += 1
            if a[i, j+1] == 0:
                g += 2
            if a[i+1, j] == 0:
                g += 4
            if a[i+1, j+1] == 0:
                g += 8
            # print(a[i:i+2, j:j+2], end='')
            print(chars[g], end='')
        print()


def py_print(char, g):
    print(f'"{char}": """', end='')

    s = np.shape(g)
    nnf = np.ones((s[0]+2, s[1] + 2))
    nnf[:-2, :-2] = g
    if char[0] == 'ـ':
        nnf[korsi-1, -2] = 0
        # nnf[korsi-1, -3] = 0

    kprint(nnf)
    print('""",')
# print headers
old_layout = 0
comment_lines = len(comment.split('\n'))
rtl = 1
new_layout = 0
codetag_count = len(characters)
# print('flf2a$', raw_height, korsi, maxwidth, old_layout, comment_lines, rtl, new_layout, codetag_count)
# print(comment)


print("korsi =", korsi // 2)
print("font_glyphs = {")

# read glyphs


glyphs = []
previous_pointer = 0
for pointer in range(z.shape[1]-1, -1, -1):
    if z[korsi, pointer, 0] == 80:
        if pointer < previous_pointer - 1:
            gl = z[:-1, pointer+1:previous_pointer]
            gl[gl[:, :, 0] != 0] = [255, 255, 255]
            gl = cv2.split(gl)[0]
            gll = gl * 1/255
            q = []
            for k in gll:
                qq = int(0)
                for kk in k:
                    qq *= 2
                    qq += int(kk)
                q.append(qq)
            glyphs.append(q)
            py_print(characters[len(glyphs) - 1].replace('‍', 'ـ'), gll)
        previous_pointer = pointer

# for i in range(len(glyphs)):
#     print(f'    "{characters[i]}" : {glyphs[i]},')
print("}")