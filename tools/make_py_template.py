characters = 'ابپتثجچحخدذرزٓسشصضطظعغفقکگلمنوهی'

def write_template(character):
    print("'"+character+"'", ": '''")
    print("''',")

for character in characters:
    write_template(character)
    write_template('ـ' + character)
    write_template('ـ' + character + 'ـ')
    write_template(character + 'ـ')