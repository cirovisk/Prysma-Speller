import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

class MainWindow(QWidget):
    """
    Represents the main window of the application.

    This class provides functionality for selecting JSON files, selecting an output directory,
    and joining the selected files into a single output file.
    """

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.select_files_button = QPushButton('Selecione as habilidades')
        self.select_files_button.clicked.connect(self.select_files)
        self.layout.addWidget(self.select_files_button)

        self.select_output_button = QPushButton('Selecione onde vai salvar')
        self.select_output_button.clicked.connect(self.select_output)
        self.layout.addWidget(self.select_output_button)

        self.join_button = QPushButton('Crie uma a skilltree')
        self.join_button.clicked.connect(self.join_files)
        self.layout.addWidget(self.join_button)

        self.files = []
        self.output_dir = ''

        self.setLayout(self.layout)

    def select_files(self):
        self.files, _ = QFileDialog.getOpenFileNames(self, 'Select JSON files', '', 'JSON Files (*.json)')

    def select_output(self):
        self.output_dir = QFileDialog.getExistingDirectory(self, 'Select output directory')

    def join_files(self):
        result = {}
        for file in self.files:
            with open(file, 'r') as f:
                data = json.load(f)
                # Use the filename (without extension) as the key
                key = os.path.splitext(os.path.basename(file))[0]
                result[key] = data

        with open(os.path.join(self.output_dir, 'output.json'), 'w') as f:
            json.dump(result, f)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())