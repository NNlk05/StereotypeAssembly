import sys

RAM_SIZE = 1024

# set up the file io
file_name = sys.argv[1]
file = open(file_name)
# read the file
file_text = file.read()
file_text = file_text.lower()
commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']

file_lines = file_text.strip.split(';')
ram = {}
# init ram
for id in range(0, RAM_SIZE):
   ram[str(id)] =  HexNumber(0)

class CommandTranslater:
    def __init__(self, command, line_words):
        if command not in command:
            raise(f'SyntaxError at {program_counter}, unknown command.')
        
        self.command = command
        translated_command = ''
        if command == 'add':
            if len(line_words) == 3:
                

class HexNumber:
    def __init__(num):
       self.hex = hex(num)
       self.dec = nub
    def read_dec(self):
        return int(self.hex, 16)

# main loop
program_counter = 0
while True:
    program_counter = program_counter + 1
    file_line = file_lines.pop(0)
    line_words = file_line.split(' ')
    try:
         # check if the first section is a nuber
        int(line_words[0])
    except ValueError:
        raise(f'Error at line {program_counter}: lines must start with a number.')
    # Translate the code into python 
    for line_word in line_words:
        if len(line_words) == 0 or line_word == ';':
            continue
        