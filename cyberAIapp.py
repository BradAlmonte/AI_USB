import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class AIApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Interaction App")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.command_input = QLineEdit(self)
        self.command_input.setPlaceholderText("Enter command to AI...")
        self.layout.addWidget(self.command_input)

        self.run_button = QPushButton("Run AI", self)
        self.run_button.clicked.connect(self.run_ai_command)
        self.layout.addWidget(self.run_button)

        self.result_label = QLabel("AI Response: ")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def run_ai_command(self):
        user_input = self.command_input.text()
        # Replace this with the actual command to interact with your AI model
        response = subprocess.run(['echo', user_input], capture_output=True, text=True)
        self.result_label.setText(f"AI Response: {response.stdout}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIApp()
    window.show()
    sys.exit(app.exec_())
