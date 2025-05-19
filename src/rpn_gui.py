
from rpn import RPN as calc
import sys
sys.path.append("/opt/homebrew/lib/python3.13/site-packages")
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    expr = ""
    current_value = ""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPN Calculator")
        self.setFixedSize(QSize(420, 160))
        enclosing_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        enclosing_layout.addLayout(input_layout)
        button_layout = QHBoxLayout()
        enclosing_layout.addLayout(button_layout)   
        message_layout = QVBoxLayout()
        enclosing_layout.addLayout(message_layout)

        prompt = QLabel("Enter a number or operator (+,-,*,/,%,P), or C to clear, Q to quit")
        input_layout.addWidget(prompt)

        self.input_field = QLineEdit() 
        self.input_field.returnPressed.connect(self.value_entered)
        input_layout.addWidget(self.input_field)

        self.enter_button = QPushButton("Enter")
        self.enter_button.setStyleSheet("background-color: lightblue;")
        self.enter_button.setToolTip("Press to enter a number or operator") 
        self.enter_button.pressed.connect(self.value_entered)
        button_layout.addWidget(self.enter_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet("background-color: lightblue;")
        self.clear_button.setToolTip("Press to enter a number or operator") 
        self.clear_button.setAutoDefault(True)
        self.clear_button.pressed.connect(self.clear_expression)
        button_layout.addWidget(self.clear_button)

        exit_button = QPushButton("Exit")
        exit_button.setStyleSheet("background-color: lightblue;")
        exit_button.setToolTip("Press to close the calculator") 
        exit_button.pressed.connect(self.close)
        exit_button.setAutoDefault(True)
        button_layout.addWidget(exit_button)
         
        self.result = QLabel(" ")
        message_layout.addWidget(self.result)
         
        self.message_area = QLabel("Ready")
        message_layout.addWidget(self.message_area)

        widget = QWidget()
        widget.setLayout(enclosing_layout)
        self.setCentralWidget(widget)
        self.show() 

    def value_entered(self):
        input_value = self.input_field.text().strip().lower()
        if input_value == "c":
            calc.enter(calc, input_value) 
            self.clear_expression()
            return
        elif input_value == "q":
            self.close()
        try:    
            self.current_value = calc.enter(calc, input_value)  
        except ValueError as e:
            self.result.setText("Error: Unrecognized input value")
            self.message_area.setText(self.expr)
            self.input_field.clear()
            self.input_field.setFocus()
            return    
        self.result.setText(f"Current value: {self.current_value}")  
        self.expr += " " + self.input_field.text()
        self.message_area.setText(f"Expr: {self.expr}")
        self.input_field.clear()
        self.input_field.setFocus()    

    def clear_expression(self):
        self.expr = ""
        self.current_value = ""
        self.result.setText(" ")
        self.message_area.setText("Ready")
        self.input_field.clear()
        self.input_field.setFocus()    

app = QApplication(sys.argv)
w = MainWindow()
app.exec()