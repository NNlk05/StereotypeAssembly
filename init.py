import sys

RAM_SIZE = 1024

def process_file(file_name):
    """
    Reads and processes the given file.

    Args:
        file_name (str): The name of the file to process.

    Returns:
        list: A list of lines from the file, split by ';'.
    """
    try:
        with open(file_name, 'r') as file:
            file_text = file.read().lower()
    except IndexError:
        sys.exit("Error: No file name provided")
    except FileNotFoundError:
        sys.exit(f"Error: File '{file_name}' not found")
    except IOError:
        sys.exit(f"Error: Unable to open or read file '{file_name}'")
    return file_text.strip().split(';')

def initialize_ram(size):
    """
    Initializes the RAM with the given size.

    Args:
        size (int): The size of the RAM.

    Returns:
        dict: A dictionary representing the RAM.
    """
    return {str(id): 0x0 for id in range(size)}

def dec(num):
    """
    Converts a hexadecimal string to an integer.

    Args:
        num (str): The hexadecimal string.

    Returns:
        int: The converted integer.
    """
    return int(num, 16)

def search_ram(index):
    """
    Reads the vRAM.

    Args:
        index (str): The index to read from.

    Returns:
        int: The value at the given index.
    """
    return ram[index]

def write_ram(index, text):
    """
    Writes to the vRAM.

    Args:
        index (str): The index to write to.
        text (int): The value to write.
    """
    ram[index] = text

class _CommandTranslater:
    """
    Evaluates the code.
    """
    def __init__(self, command, line_words):
        """
        Initializes the CommandTranslater.

        Args:
            command (str): The command to translate.
            line_words (list): The words in the command line.
        """
        if command not in commands:
            raise ValueError(f'SyntaxError at {program_counter}, unknown command: {command}')
        self.command = command
        self.line_words = line_words
        self.execute_command()

    def execute_command(self):
        """
        Executes the given command.
        """
        if self.command == 'add':
            self.add()
        elif self.command == 'sub':
            self.sub()
        elif self.command == 'print':
            self.print()
        elif self.command == 'store':
            self.store()
        elif self.command == 'read':
            self.read()
        elif self.command == 'input':
            self.input()
        elif self.command == 'if':
            self.conditional()
        elif self.command == 'gt':
            self.gt()
        elif self.command == 'lt':
            self.lt()
        elif self.command == 'eq':
            self.eq()
        elif self.command == 'goto':
            self.goto()
        elif self.command == 'exit':
            sys.exit()

    def add(self):
        """
        Adds two numbers and stores the result in vRAM.
        """
        if len(self.line_words) == 4:
            _args = self.line_words[1], self.line_words[2]
            _output = self.line_words[3]
            write_ram(_output, dec(_args[0]) + dec(_args[1]))

    def sub(self):
        """
        Subtracts the second number from the first and stores the result in vRAM.
        """
        if len(self.line_words) == 4:
            _args = self.line_words[1], self.line_words[2]
            _output = self.line_words[3]
            write_ram(_output, dec(_args[0]) - dec(_args[1]))

    def print(self):
        """
        Prints the value stored in vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def store(self):
        """
        Stores a value in vRAM at the specified index.
        """
        if len(self.line_words) == 3:
            _index = self.line_words[1]
            _value = self.line_words[2]
            write_ram(_index, dec(_value))

    def read(self):
        """
        Reads and prints the value stored in vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            print(search_ram(_index))

    def input(self):
        """
        Stores input from the user into vRAM at the specified index.
        """
        if len(self.line_words) == 2:
            _index = self.line_words[1]
            _value = input("Enter value: ")
            write_ram(_index, dec(_value))

    def conditional(self):
        """
        Executes the next command if the condition is true.
        """
        if len(self.line_words) >= 4:
            _arg1 = self.line_words[1]
            _operator = self.line_words[2]
            _arg2 = self.line_words[3]
            if _operator == '==':
                if dec(_arg1) == dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '!=':
                if dec(_arg1) != dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>':
                if dec(_arg1) > dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<':
                if dec(_arg1) < dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '>=':
                if dec(_arg1) >= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])
            elif _operator == '<=':
                if dec(_arg1) <= dec(_arg2):
                    _CommandTranslater(self.line_words[4], self.line_words[5:])

    def gt(self):
        """
        Checks if the first number is greater than the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) > dec(_arg2)

    def lt(self):
        """
        Checks if the first number is less than the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) < dec(_arg2)

    def eq(self):
        """
        Checks if the first number is equal to the second.
        """
        if len(self.line_words) == 3:
            _arg1 = self.line_words[1]
            _arg2 = self.line_words[2]
            return dec(_arg1) == dec(_arg2)

    def goto(self):
        """
        Jumps to the specified line number.
        """
        if len(self.line_words) == 2:
            _line_number = int(self.line_words[1])
            global program_counter
            program_counter = _line_number - 1

def main():
    """
    The main function to run the program.
    """
    file_name = sys.argv[1]
    file_lines = process_file(file_name)
    global ram
    ram = initialize_ram(RAM_SIZE)
    global commands
    commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']

    # main loop
    global program_counter
    program_counter = 0
    while program_counter < len(file_lines):
        try:
            program_counter += 1
            file_line = file_lines.pop(0)
            line_words = file_line.split(' ')
            if not line_words[0].isdigit():
                raise ValueError
        except IndexError:
            sys.exit("Error: Reached end of file unexpectedly")
        except ValueError:
            sys.exit(f"Error at line {program_counter}: lines must start with a number")
        
        # Evaluate the code
        for line_word in line_words:
            if len(line_words) == 0 or line_word == ';':
                continue
        _CommandTranslater(line_words[0], line_words)

if __name__ == "__main__":
    main()