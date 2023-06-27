'''owner of the Eye contollable personal computer B.srimathi lanched at 27.6.2023

'''

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5.QtWidgets import QWidget, QFormLayout, QApplication, QLabel,QPushButton, QDialog,QMainWindow,QVBoxLayout
from pyqt_switch import PyQtSwitch
from PyQt5.QtCore import Qt
import  cv2
import os
import subprocess

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import sqlite3
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('ECPC')
    # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Home', self)
        self.btn_2 = QPushButton('Eye control', self)
        self.btn_3 = QPushButton('play game', self)
        self.btn_4 = QPushButton('Help', self)

        self.btn_1.setObjectName('left_button')
        self.btn_2.setObjectName('left_button')
        self.btn_3.setObjectName('left_button')
        self.btn_4.setObjectName('left_button')

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)

       

        
        

       
        # initialize variable
       
        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()

        self.initUI()

    def initUI(self):
         # Get the dimensions of the screen
        screen_width = QDesktopWidget().screenGeometry().width()
        screen_height = QDesktopWidget().screenGeometry().height()

        # Set the window size as a percentage of the screen dimensions
        width_percent = 0.8  # 80% of the screen width
        height_percent = 0.618  # 61.8% of the screen width
        window_width = int(screen_width * width_percent)
        window_height = int(screen_width * height_percent)

        # Set the window size and center it on the screen
        self.setGeometry(
            (screen_width - window_width) // 2,
            (screen_height - window_height) // 2,
            window_width,
            window_height
        )
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:rgb(0,0,0);
                font-size:20px;
                font-weight:400;
                text-align:left;
            }
            QPushButton#left_button:hover{
                font-weight:600;
                background:rgb(220,220,220);
                border-left:5px solid blue;
            }
            QWidget#left_widget{
                background:rgb(220,220,220);
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)
        self.clean()
        self.btn_1.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button2(self):
        self.right_widget.setCurrentIndex(1)
        self.clean()
        self.btn_2.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button3(self):
        self.right_widget.setCurrentIndex(2)
        self.clean()
        self.btn_3.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    def button4(self):
        self.right_widget.setCurrentIndex(3)
        self.clean()
        self.btn_4.setStyleSheet('''font-weight:600;background:rgb(220,220,220);''')

    # ----------------- 
    # functions

    def clean(self):
        self.btn_1.setStyleSheet('''''')
        self.btn_2.setStyleSheet('''''')
        self.btn_3.setStyleSheet('''''')
        self.btn_4.setStyleSheet('''''')

    
        
    # ----------------- 
    # pages

    def ui1(self):
        
        
        main = QWidget()
        main.setAutoFillBackground(True)
        p = main.palette()
        p.setColor(main.backgroundRole(), QColor(255, 192, 203))
        main.setPalette(p)
         # Create a QLabel widget to display the image
      
        
        pixmap = QPixmap('logo4.png')

        label = QLabel(main)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setFixedSize(400, 300)
       
        label.setScaledContents(True)
        label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
        label.move(200,100)
        ui4_label = QLabel('EYE CONTROLLABLE PERSONAL COMPUTER')
        ui4_label.setAlignment(Qt.AlignCenter)  # Align text to center
        ui4_label.setStyleSheet('''color:black;font-size:45px;background:rgb(200,220,220);''')

        main_layout = QVBoxLayout()
        main_layout.addWidget(ui4_label, 0, Qt.AlignCenter)  # Add label to the center of the layout
        main_layout.addStretch(10)  # Add stretchable space to fill the remaining area

# Set the size policy of the label to expand horizontally and vertically
        ui4_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

# Set the layout of your main widget to the main_layout
       

     

        
        main.setLayout(main_layout)
        return main
    
    def ui2(self):
        
        welcome1 = WelcomeScreen()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(welcome1)
        widget.setAutoFillBackground(True)
        p = widget.palette()
        p.setColor(widget.backgroundRole(), QColor(200, 200, 255))
        widget.setPalette(p)
        return widget
        
    def ui3(self):
        
        
        welcome2 = game()
        widget1 = QtWidgets.QStackedWidget()
        widget1.addWidget(welcome2)
        widget1.setAutoFillBackground(True)
        p = widget1.palette()
        p.setColor(widget1.backgroundRole(), QColor(200, 200, 255))
        widget1.setPalette(p)
        main = QWidget()
        pixmap = QPixmap('logo.png')
        label = QLabel(main)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setFixedSize(400, 300)
        label.setScaledContents(True)
        label.setPixmap(pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio))
        label.move(200,100)
        return widget1
        
        

    def ui4(self):
        ui4_label1 = QLabel('How to use this App')
        ui4_label1.setStyleSheet('''color:black;font-size:45px;background:rgb(200,220,220);''')
        ui4_label2 = QLabel('Click-Blink left eye')
        
        ui4_label2.setStyleSheet('''font-size:20px;''')
        ui4_label3 = QLabel('DoubleClick-Blink right eye')
        
        ui4_label3.setStyleSheet('''font-size:20px;''')
        ui4_label4 = QLabel('Control the home device by blinking eye')
        
        ui4_label4.setStyleSheet('''font-size:20px;''')
        ui4_label6 = QLabel('Commands in Voice Assistant')
        ui4_label6.setStyleSheet('''font-size:30px;''')
        ui4_label7 = QLabel('Enable eye mouse\ndisable eye mouse\nenable keyboard\ndisable keyboard \nExit-bye!\nwikipedia\nsend email by voice \ngoogle')
        ui4_label7.setStyleSheet('''font-size:20px;''')
        ui4_label8 = QLabel('Developed by Srimathi\nTo contact: srimathibaskaran25@gmail.com')
        ui4_label8.setStyleSheet('''font-size:20px;''')
        ui4_label5 = QLabel('©2023')

        footer_layout = QHBoxLayout()
        footer_layout.addStretch(5)
        

        main_layout = QVBoxLayout()
        main_layout.addWidget(ui4_label1)
        main_layout.addWidget(ui4_label2)
        main_layout.addWidget(ui4_label3)
        main_layout.addWidget(ui4_label4)
        main_layout.addWidget(ui4_label6)
        
        
        main_layout.addWidget(ui4_label7)
        main_layout.addWidget(ui4_label8)
        main_layout.addWidget(ui4_label5)
        main_layout.addStretch(10)
        main_layout.addLayout(footer_layout)
        main = QWidget()
        main.setLayout(main_layout)
        return main


    
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.__initUi()
        
        
    def __initUi(self):
        switch1 = PyQtSwitch()
        switch2 = PyQtSwitch()
        switch3 = PyQtSwitch()
        
        #switch.setAlignment(Qt.AlignCenter)
        switch1.toggled.connect(self.run_file)
        switch2.toggled.connect(self.run_file2)
        switch3.toggled.connect(self.run_file3)
        switch1.setAnimation(True)
        switch2.setAnimation(True)
        switch3.setAnimation(True)
        #switch.addWidget(Qt.AlignCenter, Qt.AlignCenter)

        switch1.setCircleDiameter(40)
        switch2.setCircleDiameter(40)
        switch3.setCircleDiameter(40)

        self.__label1 = QLabel('Normal Label', self)
        self.__label2=  QLabel('Normal Label', self)
        self.__label3=  QLabel('Normal Label', self)

        lay = QFormLayout()
        lay.setFormAlignment(Qt.AlignCenter )
        
        self.__label1.setText('Eye controlled mouse')
        self.__label1.setStyleSheet("border :3px solid blue;")
        self.__label1.setStyleSheet(''' font-size: 30px; ''')
       
        self.__label2.setText('Eye controlled keyboard')

        self.__label2.setStyleSheet("border :3px solid yellow;")
        self.__label2.setStyleSheet(''' font-size: 30px; ''')
        self.__label3.setText('Voice assistant')

        self.__label3.setStyleSheet("border :3px solid yellow;")
        self.__label3.setStyleSheet(''' font-size: 30px; ''')
        lay.setSpacing(80)
        lay.addRow(self.__label1, switch1)
        lay.setSpacing(40)
        lay.addRow(self.__label2, switch2)
        lay.setSpacing(40)
        lay.addRow(self.__label3, switch3)
       
        self.setLayout(lay)
    def run_file(self, checked):
        if checked:
            
            self.process = subprocess.Popen(["python", "mains.py"])
            
        else:
            
            if self.process:
                subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
                self.process.kill()
                self.process.kill()
                self.process.kill()
                self.process = None
    def run_file2(self, checked):
        if checked:
            
            
            self.process= subprocess.Popen(["python", "vkeyboard.py"])
        else:
            
            if self.process:
                subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
                self.process.kill()
                self.process.kill()
                self.process.kill()
                self.process = None
  
   
    def run_file3(self, checked):
        if checked:
           
            self.process = subprocess.Popen(["python", "voice.py"])
        else:
            
            if self.process:
                self.process.kill()
                self.process = None

    

class game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100,
                         300, 500)
        self.UiComponents()
        self.show()


    def UiComponents(self):
        self.turn = 0
        self.times = 0
        self.push_list = []

        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x = 90
        y = 90
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)
                self.push_list[i][j].setFont(QFont(QFont('Times', 35)))
                self.push_list[i][j].clicked.connect(self.action_called)


        self.label = QLabel(self)

        self.label.setGeometry(20, 300, 260, 60)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : green;"
                                 "}")

        self.label.setAlignment(Qt.AlignCenter)

        self.label.setFont(QFont('Times', 15))

        reset_game = QPushButton("Reset-Game", self)

        reset_game.setGeometry(50, 380, 200, 50)

        reset_game.clicked.connect(self.reset_game_action)

    def reset_game_action(self):

        self.turn = 0
        self.times = 0

        self.label.setText("")

        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")

    def action_called(self):

        self.times += 1
        button = self.sender()
        button.setEnabled(False)
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        win = self.who_wins()
        text = ""

        if win == True:
            if self.turn == 0:
                text = "O Won"
            else:
                text = "X Won"

            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)

        elif self.times == 9:
            text = "Match is Draw"

        self.label.setText(text)

    def who_wins(self):
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True

        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True

        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True

        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    p = QPalette()
    gradient = QLinearGradient(0, 0, 0, 200)
    gradient.setColorAt(0.0, QColor(140, 240, 240))
    gradient.setColorAt(1.0, QColor(140, 160, 160))
    p.setBrush(QPalette.Window, QBrush(gradient))
    ex.setPalette(p)
    ex.show()
    sys.exit(app.exec_())
