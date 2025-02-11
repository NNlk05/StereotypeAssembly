import sys

# set up the file io
file_name = sys.argv[1]
file = open(file_name)
# read the file
file_text = file.read()
file_text = file_text.lower()

# main loop
file_lines = file_text.strip.split(';')
commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto']

while True:
    file_line = file_lines.pop(0)
    line_words = file_line.split(' ')
    try:
         # check if the first section is a nuber
        int(line_words[0])
    except ValueError:
        raise('The first ')

    for line_word in line_words:
        if len(line_words) == 0 or line_word == ';':
            break
        