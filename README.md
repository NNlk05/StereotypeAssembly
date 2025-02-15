# StereotypeAssembly

A Stereotype, Hackerly language

## Overview

StereotypeAssembly is a simple assembly-like language designed to be easily understood and manipulated. This project provides an interpreter for StereotypeAssembly written in Python.

## Features

- Basic arithmetic operations (addition, subtraction)
- Memory storage and retrieval
- Conditional execution
- Input handling
- Program flow control with `goto` statements

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/NNlk05/StereotypeAssembly.git
cd StereotypeAssembly
```

### Usage

To run a StereotypeAssembly program, use the following command:

```bash
python init.min.py <filename>
```

Replace `<filename>` with the name of your StereotypeAssembly program file.

### Example Programs

#### Basic Example: Hello, World!

This program prints "Hello, World!" to the console.

Find the named `hello_world.asm`, it should look like: :

```asm
0 print "Hello, World!";
1 exit;
```

Run the example program:

```bash
python init.min.py hello_world.asm
```

#### Quine

A quine is a program that outputs its own source code.

Find the named `quine.asm`, it should look like: :

```asm
0 store 0x0 "0 store 0x0 ";
1 store 0x1 "quine.asm";
2 print 0x0;
3 print 0x1;
4 exit;
```

Run the example program:

```bash
python init.min.py quine.asm
```

#### Truth-machine

A truth-machine is a program that asks for input. If the input is 0, it outputs 0 and terminates. If the input is 1, it outputs 1 indefinitely.

Find the named `truth_machine.asm`, it should look like: :

```asm
0 input 0x0;
1 if 0x0 == 0 goto 3;
2 if 0x0 == 1 goto 5;
3 print 0x0;
4 exit;
5 print 0x1;
6 goto 5;
```

Run the example program:

```bash
python init.min.py truth_machine.asm
```

## Language Syntax

### Commands

- `add <arg1> <arg2> <output>`: Adds `arg1` and `arg2`, stores the result in `output`.
- `sub <arg1> <arg2> <output>`: Subtracts `arg2` from `arg1`, stores the result in `output`.
- `print <index>`: Prints the value stored in memory at `index`.
- `store <index> <value>`: Stores `value` in memory at `index`.
- `read <index>`: Reads and prints the value stored in memory at `index`.
- `input <index>`: Stores user input in memory at `index`.
- `if <arg1> <operator> <arg2> <command> [args...]`: Executes `command` if the condition `<arg1> <operator> <arg2>` is true.
- `gt <arg1> <arg2>`: Checks if `arg1` is greater than `arg2`.
- `lt <arg1> <arg2>`: Checks if `arg1` is less than `arg2`.
- `eq <arg1> <arg2>`: Checks if `arg1` is equal to `arg2`.
- `goto <line_number>`: Jumps to the specified line number.
- `exit`: Exits the program.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
