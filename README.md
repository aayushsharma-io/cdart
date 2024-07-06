# CDART Programming Language

CDART is a minimalistic programming language designed to be simple and easy to use. It is currently in the early stages of development and aims to provide a clean and efficient syntax for common programming tasks.

## Features

- **Simple Syntax**: CDART has a straightforward and easy-to-understand syntax, making it accessible for beginners.
- **Variable Declaration**: Use `let` to declare variables.
- **State Evaluation**: Use `state` to evaluate and print variables and expressions.
- **Modular Design**: Easily import and use modules.

## Current Status

CDART is in the early stages of development. The following features are currently implemented:

- Basic variable declaration and assignment
- State evaluation for variables and string literals
- Simple error handling for undefined variables
- Basic import functionality (placeholder)

## Getting Started

### Prerequisites

- Python 3.x
- Flask (for web server functionality)
- Tkinter (for GUI functionality)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cdart.git
    cd cdart
    ```

2. Install the required Python packages:
    ```sh
    pip install flask
    ```

### Running the Interpreter

To run the CDART interpreter, execute the following command:
```sh
python cdart.py
```
This will start the CDART interpreter with a simple GUI where you can input and execute CDART code.

### Example Code
Here is an example of CDART code that demonstrates variable declaration and state evaluation:

```
let x = 10
let y = "Hello, World!"
state(x)
state(y)
state("A string literal")
state(unknown_variable)
```
### Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your improvements.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Developers and facts:
CDART is initially developed and the idea of Aayush Sharma, then it is continued and now we (4 devs working on cdart) with a vison of simple and minimalistic language.
