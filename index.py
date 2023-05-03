import argparse
import json

parser = argparse.ArgumentParser(description='Program do konwersji danych w formatach .xml, .json i .yml')

parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego')
parser.add_argument('--format', type=str, choices=['xml', 'json', 'yml'], default='json', help='Format pliku wyjściowego')

args = parser.parse_args()


with open(args.input_file, 'r') as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print("Błąd w parsowaniu pliku JSON: ", e)
        exit(1)

with open(args.output_file, 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

print("Konwersja zakończona powodzeniem")
'''
print('Nazwa pliku wejściowego:', args.input_file)
print('Nazwa pliku wyjściowego:', args.output_file)
print('Format pliku wyjściowego:', args.format)
'''