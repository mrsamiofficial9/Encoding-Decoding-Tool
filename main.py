import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLineEdit, QLabel
from PyQt5.QtGui import QPalette, QColor

import base64
import base58
import binascii

class EncodingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Encoding/Decoding Tool')
        self.setGeometry(100, 100, 400, 200)

        # Apply some basic styling using QSS
        self.setStyleSheet('''
            QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 16px;
            }
            QLineEdit, QComboBox {
                font-size: 14px;
                background-color: #ffffff;
            }
            QPushButton {
                font-size: 14px;
                background-color: #3498db;
                color: #ffffff;
                border: 1px solid #3498db;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #3cb0fd;
                border: 1px solid #3cb0fd;
            }
        ''')

        self.input_label = QLabel('Input Text:')
        self.input_text = QLineEdit()

        self.encoding_label = QLabel('Select Encoding/Decoding Type:')
        self.encoding_combo = QComboBox()
        self.encoding_combo.addItems(['Base64 Encode', 'Base64 Decode', 'Base58 Encode', 'Base58 Decode', 'Base32 Encode', 'Base32 Decode', 'Hex Encode', 'Hex Decode'])

        self.result_label = QLabel('Result:')
        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)

        self.encode_decode_button = QPushButton('Encode/Decode')
        self.encode_decode_button.clicked.connect(self.encode_decode)

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_text)
        vbox.addWidget(self.encoding_label)
        vbox.addWidget(self.encoding_combo)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_text)
        vbox.addWidget(self.encode_decode_button)

        self.setLayout(vbox)

    def encode_decode(self):
        input_text = self.input_text.text()
        encoding_type = self.encoding_combo.currentText()
        result = ''

        if encoding_type == 'Base64 Encode':
            result = base64.b64encode(input_text.encode()).decode()
        elif encoding_type == 'Base64 Decode':
            try:
                result = base64.b64decode(input_text).decode()
            except:
                result = 'Invalid Base64 input'
        elif encoding_type == 'Base58 Encode':
            result = base58.b58encode(input_text.encode()).decode()
        elif encoding_type == 'Base58 Decode':
            try:
                result = base58.b58decode(input_text).decode()
            except:
                result = 'Invalid Base58 input'
        elif encoding_type == 'Base32 Encode':
            result = base64.b32encode(input_text.encode()).decode()
        elif encoding_type == 'Base32 Decode':
            try:
                result = base64.b32decode(input_text).decode()
            except:
                result = 'Invalid Base32 input'
        elif encoding_type == 'Hex Encode':
            result = binascii.hexlify(input_text.encode()).decode()
        elif encoding_type == 'Hex Decode':
            try:
                result = binascii.unhexlify(input_text).decode()
            except:
                result = 'Invalid Hex input'

        self.result_text.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncodingApp()
    ex.show()
    sys.exit(app.exec_())
