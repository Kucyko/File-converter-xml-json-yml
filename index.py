import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import xmltodict
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QFileDialog

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Konwerter danych')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        input_label = QLabel('Nazwa pliku wejściowego:')
        self.input_lineedit = QLineEdit()
        layout.addWidget(input_label)
        layout.addWidget(self.input_lineedit)

        output_label = QLabel('Nazwa pliku wyjściowego:')
        self.output_lineedit = QLineEdit()
        layout.addWidget(output_label)
        layout.addWidget(self.output_lineedit)

        convert_button = QPushButton('Konwertuj')
        convert_button.clicked.connect(self.convert)
        layout.addWidget(convert_button)

        self.setLayout(layout)

    def convert(self):
        input_file = self.input_lineedit.text()
        output_file = self.output_lineedit.text()

        if input_file.endswith('.json'):
            with open(input_file, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    self.show_error_message("Błąd w parsowaniu pliku JSON: " + str(e))
                    return
        elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
            with open(input_file, 'r') as f:
                try:
                    data = yaml.safe_load(f)
                except yaml.YAMLError as e:
                    self.show_error_message("Błąd w parsowaniu pliku YAML: " + str(e))
                    return
        elif input_file.endswith('.xml'):
            try:
                tree = ET.parse(input_file)
                root = tree.getroot()

                data = dict()
                for child in root:
                    data[child.tag] = child.text

            except ET.ParseError as e:
                self.show_error_message("Błąd parsowania pliku XML: " + str(e))
                return
            except Exception as e:
                self.show_error_message("Błąd odczytu pliku: " + str(e))
                return
        else:
            self.show_error_message("Nieobsługiwany format pliku wejściowego: " + input_file)
            return

        output_format = output_file.split('.')[-1]

        if output_format == "json":
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
        elif output_format == "yml" or output_format == "yaml":
            with open(output_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False)
        elif output_format == "xml":
            try:
                root = ET.Element('data')
                for key, value in data.items():
                    child = ET.SubElement(root, key)
                    child.text = str(value)

                tree = ET.ElementTree(root)
                tree.write(output_file, encoding='utf-8', xml_declaration=True)
            except Exception as e:
                self.show_error_message("Błąd zapisu pliku XML: " + str(e))
                return
        else:
            self.show_error_message("Nieobsługiwany format pliku wyjściowego: " + output_format)
            return

        
        self.show_success_message("Konwersja zakończona powodzeniem")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Błąd", message)

    def show_success_message(self, message):
        QMessageBox.information(self, "Sukces", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter_app = ConverterApp()
    converter_app.show()
    sys.exit(app.exec_())
