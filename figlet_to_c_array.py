import pyfiglet
import argparse

def figlet_to_c_array(text):
    figlet_text = pyfiglet.figlet_format(text)
    lines = figlet_text.splitlines()
    c_array = 'const char* figlet_text[] = {\n'
    for line in lines:
        escaped_line = line.replace('\\', '\\\\').replace('"', '\\"')
        c_array += f'    "{escaped_line}",\n'
    c_array += '    NULL\n};'
    return c_array

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert text to a C array representation of figlet text.')
    parser.add_argument('text', type=str, help='The text to convert to figlet format.')
    args = parser.parse_args()
    text = args.text
    c_array_output = figlet_to_c_array(text)
    print(c_array_output)
