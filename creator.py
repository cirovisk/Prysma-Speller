import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.ability_template = {
            "nome": "",
            "nível de prysma": 0,
            "tipo": "",
            "ação": "",
            "alcance": "",  
            "duração": "",
            "alvos": "",
            "descrição": "",
        }

        self.labels = {}
        self.line_edits = {}

        for key in self.ability_template.keys():
            self.labels[key] = QLabel(key)
            if key == "descrição":
                self.line_edits[key] = QTextEdit()
                self.line_edits[key].setFixedHeight(100)  # Adjust the value as needed
            else:
                self.line_edits[key] = QLineEdit()
            self.layout.addWidget(self.labels[key])
            self.layout.addWidget(self.line_edits[key])

        self.save_button = QPushButton('Salvar')
        self.save_button.clicked.connect(self.save_to_json)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)
        self.new_button = QPushButton('Novo')
        self.new_button.clicked.connect(self.new_dictionary)
        self.layout.addWidget(self.new_button)

        self.setLayout(self.layout)
        
    def new_dictionary(self):
        for key in self.ability_template.keys():
            self.line_edits[key].clear()

    def save_to_json(self):
        for key in self.ability_template.keys():
            if key == "descrição":
                text = self.line_edits[key].toPlainText()
                self.ability_template[key] = text.replace('\n', ' ')
            else:
                text = self.line_edits[key].text()
                self.ability_template[key] = text.replace('\n', ' ')

        if not os.path.exists('abilities'):
            os.makedirs('abilities')

        with open(f'abilities/{self.ability_template["nome"]}.json', 'w', encoding='utf-8') as f:
            json.dump(self.ability_template, f, ensure_ascii=False)

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()
sys.exit(app.exec_())