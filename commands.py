from init import program_counter
commands = ['add','sub', 'print', 'store', 'read', 'input', 'if', 'gt', 'lt', 'eq', 'goto', 'exit']

class CommandTranslater:
    def __init__(command):
        if command not in command:
            raise(f'SyntaxError at {program_counter}, ')
            