b = '''
 ⠀
⠁ ⠂ ⠃ ⠄ ⠅ ⠆ ⠇ ⠈ ⠉ ⠊ ⠋ ⠌ ⠍ ⠎ ⠏ ⠐ ⠑ ⠒ ⠓ ⠔ ⠕ ⠖ ⠗ ⠘ ⠙ ⠚ ⠛
 ⠜ ⠝ ⠞ ⠟ ⠠ ⠡ ⠢ ⠣ ⠤ ⠥ ⠦ ⠧ ⠨ ⠩ ⠪ ⠫ ⠬ ⠭ ⠮ ⠯ ⠰ ⠱ ⠲ ⠳ ⠴ ⠵ ⠶ ⠷ ⠸ ⠹ ⠺ ⠻ ⠼ ⠽ ⠾ ⠿ 
 ⡀ ⡁ ⡂ ⡃ ⡄ ⡅ ⡆ ⡇ ⡈ ⡉ ⡊ ⡋ ⡌ ⡍ ⡎ ⡏ ⡐
 ⡑ ⡒ ⡓ ⡔ ⡕ ⡖ ⡗ ⡘ ⡙ ⡚ ⡛ ⡜ ⡝ ⡞ ⡟ ⡠ ⡡ ⡢ ⡣ ⡤
  ⡥ ⡦ ⡧ ⡨ ⡩ ⡪ ⡫ ⡬ ⡭ ⡮ ⡯ ⡰ ⡱ ⡲ ⡳ ⡴ ⡵ ⡶ ⡷ 
  ⡸ ⡹ ⡺ ⡻ ⡼ ⡽ ⡾ ⡿
⢀ ⢁ ⢂ ⢃ ⢄ ⢅ ⢆ ⢇ ⢈ ⢉ ⢊ ⢋ ⢌ ⢍ ⢎ ⢏ ⢐ ⢑ ⢒ ⢓ ⢔ ⢕
 ⢖ ⢗ ⢘ ⢙ ⢚ ⢛ ⢜ ⢝ ⢞ ⢟ ⢠ ⢡ ⢢ ⢣ ⢤ ⢥ ⢦ ⢧ ⢨ ⢩ ⢪ ⢫ ⢬
  ⢭ ⢮ ⢯ ⢰ ⢱ ⢲ ⢳ ⢴ ⢵ ⢶ ⢷ ⢸ ⢹ ⢺ ⢻ ⢼ ⢽ ⢾ ⢿⣀ ⣁ ⣂ ⣃ ⣄ 
  ⣅ ⣆ ⣇ ⣈ ⣉ ⣊ ⣋ ⣌ ⣍ ⣎ ⣏ ⣐ ⣑ ⣒ ⣓ ⣔ ⣕ ⣖ ⣗ ⣘ ⣙ ⣚ ⣛ ⣜ ⣝ 
  ⣞ ⣟ ⣠ ⣡ ⣢ ⣣ ⣤ ⣥ ⣦ ⣧ ⣨ ⣩ ⣪ ⣫ ⣬ ⣭ ⣮ ⣯ ⣰ ⣱ ⣲ ⣳
   ⣴ ⣵ ⣶ ⣷ ⣸ ⣹ ⣺ ⣻ ⣼ ⣽ ⣾ ⣿ '''.replace('\n', '').replace(' ', '')

braille_chars = list(b)
# print(b)

braille_map = [
    [1, 8],
    [2, 16],
    [4, 32],
    [64, 128],
]




import cv2
import numpy as np

# things to set
image_name = './pixelart.png'
raw_height = 13
num_of_raws = 3
image_width = 512
korsi = 1
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


# read image raws and concatenate them
image = cv2.imread(image_name)
z = [0 for _ in range(num_of_raws)]
for i in range(num_of_raws):
    z[i] = image[i * (raw_height + 1) + 1: (i + 1) * (raw_height + 1) + 1]

z.reverse()
z = np.concatenate(z, axis=1)


q = []



def kprint(a):
    # print(len(a), len(a[0]))
    for i in range(0, len(a)-4, 4):
        for j in range(0, len(a[i]) - 2, 2):
            # print(i, j)
            g = 0
            for x in range(4):
                for y in range(2):
                    if a[i + x][j + y] == 0:
                        g += braille_map[x][y]

            print(braille_chars[g], end='')
            # print(braille_chars[g])
            # cv2.imshow('block', a[i:i+4, j:j+2]); cv2.waitKey(0)
        print()


def py_print(char, g):
    print(f'"{char}": """', end='')

    # if char[0] == 'ـ':
    #     g[korsi*4+2][0] = 0
    # g[korsi *4 +2][:] = 0
    # if char[-1] == 'ـ':
    #     g[korsi*4+2][-1] = 0

    s = np.shape(g)
    nnf = np.ones((s[0]+4, s[1] + 2))
    nnf[:-4, :-2] = g
    # print(char)
    # if char[0] == 'ـ':
    #     nnf[korsi*4+2, -4:] = 0
    # if char[-1] == 'ـ':
    #     nnf[korsi*4+2, :2] = 0

    kprint(nnf)
    print('""",')


# print headers
old_layout = 0
comment_lines = len(comment.split('\n'))
rtl = 1
new_layout = 0
codetag_count = len(characters)


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

print("}")