from plistlib import load
import sys
import json
import re
import time
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QCheckBox, QPushButton, QTableWidget
from PyQt5.uic import loadUi
from login import Ui_MainWindow
from datetime import datetime
class Login(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def open_json(self):
        with open ('save_acc.json', 'r', encoding='utf-8') as fr:
            data = json.load(fr)
        fr.close()
        return data
    
    def connectSignalsSlots(self):
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.checkBox1.stateChanged.connect(self.b_RememberInfor)
        self.createaccbutton.clicked.connect(self.gotocreate)
    
    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def b_RememberInfor(self):
        return self.checkBox1.isChecked()

    def getInfor(self):
        list_infor  = []
        username = self.username.text()
        password = self.password.text()
        list_infor.append(username)
        list_infor.append(password)
        return list_infor  

    def loginfunction(self):
        if self.checkBox1.isChecked() == True:
            infor = self.getInfor()
            data = self.open_json()
            if infor[0] in data.keys():
                QMessageBox.about(self, "Report","Login Succesfully")
                home = Home()
                widget.addWidget(home)
                widget.setCurrentIndex(widget.currentIndex() + 1)  
            else:
                QMessageBox.about(self, "Report","Account does not exit. Try again")  