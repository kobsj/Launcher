import os, sys, subprocess
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class App(QWidget):
    """docstring for App."""

    def __init__(self):
        super().__init__()
        self.title = "HAL 9000"
        self.left = 300
        self.top = 150
        self.width = 775
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label_main = QLabel('Welcome John. What would you like to do today?', self)
        label_main.move(240, 25)

        button_codeCamp = QPushButton('Free Code Camp', self)
        button_codeCamp.setToolTip('Free Code Camp and Music')
        button_codeCamp.move(25, 200)
        button_codeCamp.resize(125, 50)
        button_codeCamp.clicked.connect(self.startCodeCamp)

        label_codeCamp = QLabel(self)
        pixmap_codecamp = QPixmap('codeCamp.png')
        pixmap_codecamp = pixmap_codecamp.scaledToWidth(75)
        label_codeCamp.setPixmap(pixmap_codecamp)
        label_codeCamp.move(50, 115)

        button_pythonData = QPushButton('Data with Python', self)
        button_pythonData.setToolTip('Udemy Course and Anaconda')
        button_pythonData.move(175, 200)
        button_pythonData.resize(125, 50)
        button_pythonData.clicked.connect(self.startData)

        button_atomProject = QPushButton('Code in Atom', self)
        button_atomProject.setToolTip('Launch Atom')
        button_atomProject.move(325, 200)
        button_atomProject.resize(125, 50)
        button_atomProject.clicked.connect(self.startAtom)

        button_TBD = QPushButton('Option #4 Here', self)
        button_TBD.setToolTip('Place hoilder')
        button_TBD.move(475, 200)
        button_TBD.resize(125, 50)
        button_TBD.clicked.connect(self.startOther)

        button_Other = QPushButton('Something Else', self)
        button_Other.setToolTip('Close Launcher')
        button_Other.move(625, 200)
        button_Other.resize(125, 50)
        button_Other.clicked.connect(self.close)

        self.show()

    @pyqtSlot()
    def startCodeCamp(self):
        subprocess.call(['xdg-open', 'https://www.freecodecamp.org/'])
        subprocess.call(['xdg-open', 'https://www.youtube.com/watch?v=yaKeFoNOneg'])
        exit()

    def startData(self):
        os.system('anaconda-navigator')
        subprocess.call(['xdg-open', 'https://www.udemy.com/course/learning-python-for-data-analysis-and-visualization/'])
        exit()

    def startAtom(self):
        subprocess.call(['bash', '/usr/bin/atom'])
        exit()

    def startOther(self):
        print('Start whatever gets picked')
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
