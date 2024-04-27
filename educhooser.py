from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QCheckBox, QGridLayout, 
                               QMainWindow, QWizard)
import sys
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class MainWindow(QWizard):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduChooser")
        
        title = QLabel()
        title.setText("Select which metapackages you would like to install:")
        
        self.pri_btn = QCheckBox()
        self.pri_btn.setText("EduIce Primary")
        self.pri_btn.setCheckState(Qt.CheckState.Unchecked)
        self.pri_btn.stateChanged.connect(self.primary)
        
        self.sec_btn = QCheckBox()
        self.sec_btn.setText("EduIce Secondary")
        self.sec_btn.setCheckState(Qt.CheckState.Unchecked)
        self.sec_btn.stateChanged.connect(self.secondary)
        
        self.ter_btn = QCheckBox()
        self.ter_btn.setText("EduIce Tertiary")
        self.ter_btn.setCheckState(Qt.CheckState.Unchecked)
        self.ter_btn.stateChanged.connect(self.tertiary)
        
        self.all_btn = QCheckBox()
        self.all_btn.setText("EduIce All")
        self.all_btn.setCheckState(Qt.CheckState.Unchecked)
        self.all_btn.stateChanged.connect(self.all)
        
        next_btn = QPushButton()
        next_btn.setText("Next")
        next_btn.clicked.connect(self.next)
        
        grid = QGridLayout()
        grid.addWidget(title, 0, 0)
        grid.addWidget(self.pri_btn, 1, 0)
        grid.addWidget(self.sec_btn, 2, 0)
        grid.addWidget(self.ter_btn, 3, 0)
        grid.addWidget(self.all_btn, 4, 0)
        grid.addWidget(next_btn, 5, 1)
        
        self.setLayout(grid)
        
    
    def primary(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        if Qt.CheckState.Checked.value == True:
            pri = True
        else:
            pri = False
    
    def secondary(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        if Qt.CheckState.Checked.value == True:
            sec = True
        else:
            sec = False
    
    def tertiary(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        if Qt.CheckState.Checked.value == True:
            ter = True
        else:
            ter = False
    
    def all(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        if Qt.CheckState.Checked.value == True:
            all = True
        else:
            all = False
    
    def next(self):
        self.nextId()

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())