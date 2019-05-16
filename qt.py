from sklearn import mixture
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from PyQt5 import QtWidgets, uic
import sys
from regression import Regression
from clasterization import Clasterization
from classification import Classification
import sys


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.clasterization)
        self.pushButton_2.clicked.connect(self.classification)
        self.pushButton_3.clicked.connect(self.regression)

        self.regress = []
        self.claster = []
        self.classific = []

    def clasterization(self):
        print('clasterization')
        claster = Clasterization()
        self.claster = claster

    def classification(self):
        print('classification')
        classific = Classification()
        self.classific.append(classific)

    def regression(self):
        regr = Regression()
        self.regress.append(regr)


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = Main()

    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook

    sys.exit(app.exec())
