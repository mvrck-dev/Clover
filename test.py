from cgitb import text
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()

      self.initUI()

   def initUI(self):
      hbox = QVBoxLayout()
      self.edit1=QTextEdit()
      hbox.addWidget(self.edit1)
      self.btn1=QPushButton("Copy")
      hbox.addWidget(self.btn1)
      self.edit2=QTextEdit()
      self.btn2=QPushButton("Paste")
      hbox.addWidget(self.edit2)
      hbox.addWidget(self.btn2)
      self.btn1.clicked.connect(self.copytext)
      self.btn2.clicked.connect(self.pastetext)
      self.setLayout(hbox)
      
      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('Clipboard')
      self.show()
      
   def copytext(self):

      #clipboard.setText(self.edit1.copy())
      
      text = self.edit1.toPlainText()
      #copy the test in the edit1 to the clipboard
      clipboard.setText(text)
      
      print (clipboard.text())

      msg=QMessageBox()
      msg.setText(clipboard.text()+" copied on clipboard")
      msg.exec()

   def pastetext(self):
      self.edit2.setText(clipboard.text())

app = QApplication(sys.argv)
clipboard=app.clipboard()
ex = Example()
ex.setWindowTitle("clipboard Example")
sys.exit(app.exec())

