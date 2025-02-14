import sys

RAM_SIZE = 1024

# set up the file io
file_name = sys.argv[1]
file = open(file_name)
# read the file
file_text = file.read()
file_text = file_text.lower()
commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']



def dec(num):
    return int(num, 16)

file_lines = file_text.strip.split(';')
ram = {}
# init ram
for id in range(0, RAM_SIZE):
   ram[str(id)] =  0x0

def search_ram(index):
    """
    Reads the vRAM
    """
    return ram[index]

def write_ram(index, text):
    """
    Writes to the vRAM
    """
    ram[index] = text


class _CommandTranslater:
    """
    Eval the code
    """
    def __init__(self, command, line_words):
        if command not in command:
            raise(f'SyntaxError at {program_counter}, unknown command.')
        
        self.command = command
        translated_command = ''
        if command == 'add':
            if len(line_words) == 4:
                _args = line_words[1], line_words[2]
                _output = line_words[3]
                write_ram(dec(_output), )




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
    # Eval the code 
    for line_word in line_words:
        if len(line_words) == 0 or line_word == ';':
            continue
        