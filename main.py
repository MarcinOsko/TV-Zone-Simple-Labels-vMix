import sys
from PyQt6.QtWidgets import QApplication
from SimpleLabels import SimpleLabels

app = QApplication(sys.argv)
app.setApplicationName("Simple Labels for vMix")
library = SimpleLabels()
sys.exit(app.exec())
