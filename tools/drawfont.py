import subprocess

characters = 'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
korsi = 13


def ocount(t):
    for i, c in (enumerate(t)):
        if c != ' ':
            return i
    return i

def ocounto(f):
    kk = []
    for ff in f:
        for i in range(len(ff) - 1, 0, -1):
            if ff[i] != ' ':
                break
        kk.append(ff[:i])
    return kk

# make a font
def print_glyph_block(character):
    print("'"+character+"'", ": '''")

    # glyph variation
    character = character.replace('ـ', '\u200d')

    # get ascii-art of the character
    shell_command = f'python3 ttf_character_to_png.py {character}; jp2a output.png --width=33'
    out = subprocess.check_output(shell_command , shell=True)

    # trim spaces from the ascii block
    # dirty code, but it works!
    out = out.decode('utf-8')
    out = out.replace('\\n', '\n')
    osize = min(map(ocount, out.split('\n')[1:-1]))
    out_trimmed = '\n'.join(map(lambda x: x[osize:], out.split('\n')))
    oo = out_trimmed.split('\n')
    out = ocounto(oo)
    out = '\n'.join(out)

    print(out)
    print("''',")



# print initials
print('korsi = {korsi}')
print('font_glyphs = {')

# print glyphs blocks
for character in characters:

    # for all 4 variations of the character
    print_glyph_block(character)
    print_glyph_block('ـ' + character)
    print_glyph_block('ـ' + character + 'ـ')
    print_glyph_block(character + 'ـ')

# print endings
print('}')