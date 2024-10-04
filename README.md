# Figlet to C Array

A Python script that converts input text into a C array representation of its figlet format. This is useful for developers who want to include stylized text in their C programs.

## Features

- Converts any input text into a stylized figlet format.
- Outputs the figlet text as a C array, ready to be included in C code.
- Handles escaping of special characters for C strings.

## Installation

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

You will also need to install the `pyfiglet` library. You can do this using pip:

```bash
pip install pyfiglet
```

## Usage

To use the script, run the following command in your terminal:

```bash
python figlet_to_c_array.py "your text here"
```

For example:

```bash
python figlet_to_c_array.py "hello world"
```

This will output:

```c
const char* figlet_text[] = {
    " _          _ _                            _     _ ",
    "| |__   ___| | | ___   __      _____  _ __| | __| |",
    "| '_ \\ / _ \\ | |/ _ \\  \\ \\ /\\ / / _ \\| '__| |/ _` |",
    "| | | |  __/ | | (_) |  \\ V  V / (_) | |  | | (_| |",
    "|_| |_|\\___|_|_|\\___/    \\_/\\_/ \\___/|_|  |_|\\__,_|",
    "                                                   ",
    NULL
};

```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
