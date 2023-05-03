import argparse
import json
import yaml
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Program do konwersji danych w formatach .xml, .json i .yml')

parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego')
parser.add_argument('--format', type=str, choices=['xml', 'json', 'yml'], default='json', help='Format pliku wyjściowego')

args = parser.parse_args()

if args.input_file.endswith('.json'):
    with open(args.input_file, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print("Błąd w parsowaniu pliku JSON: ", e)
            exit(1)
elif args.input_file.endswith('.yml') or args.input_file.endswith('.yaml'):
    with open(args.input_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print("Błąd w parsowaniu pliku YAML: ", e)
            exit(1)
elif args.input_file.endswith('.xml'):
    try:
        tree = ET.parse(args.input_file)
        data = tree.getroot()
    except ET.ParseError as e:
        print("Błąd w parsowaniu pliku XML: ", e)
        exit(1)
else:
    print("Nieobsługiwany foramt pliku wejściowego: ", args.input_file)
    exit(1)

if args.format == "json":
    with open(args.output_file, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
elif args.format == "yml" or args.format == "yaml":
    with open(args.output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
else:
    print("Niebsługiwany plik formatu wyjściowego:", args.format)
    exit(1)
print("Konwersja zakończona powodzeniem")
'''
print('Nazwa pliku wejściowego:', args.input_file)
print('Nazwa pliku wyjściowego:', args.output_file)
print('Format pliku wyjściowego:', args.format)
'''