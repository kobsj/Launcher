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

        label_pythonData = QLabel(self)
        pixmap_pythonData = QPixmap('Udemy-Logo.png')
        pixmap_pythonData = pixmap_pythonData.scaledToWidth(75)
        label_pythonData.setPixmap(pixmap_pythonData)
        label_pythonData.move(200, 125)

        button_atomProject = QPushButton('Code in Atom', self)
        button_atomProject.setToolTip('Launch Atom')
        button_atomProject.move(325, 200)
        button_atomProject.resize(125, 50)
        button_atomProject.clicked.connect(self.startAtom)

        label_atomProject = QLabel(self)
        pixmap_atomProject = QPixmap('atom.png')
        pixmap_atomProject = pixmap_atomProject.scaledToWidth(75)
        label_atomProject.setPixmap(pixmap_atomProject)
        label_atomProject.move(350, 110)

        button_TBD = QPushButton('Code in Eclipse', self)
        button_TBD.setToolTip('Launch Eclipse')
        button_TBD.move(475, 200)
        button_TBD.resize(125, 50)
        button_TBD.clicked.connect(self.startEclipse)

        label_TBD = QLabel(self)
        pixmap_TBD = QPixmap('eclipse.png')
        pixmap_TBD = pixmap_TBD.scaledToWidth(75)
        label_TBD.setPixmap(pixmap_TBD)
        label_TBD.move(500, 110)

        button_Other = QPushButton('Something Else', self)
        button_Other.setToolTip('Close Launcher')
        button_Other.move(625, 200)
        button_Other.resize(125, 50)
        button_Other.clicked.connect(self.close)

        label_Other = QLabel(self)
        pixmap_Other = QPixmap('other.png')
        pixmap_Other = pixmap_Other.scaledToWidth(75)
        label_Other.setPixmap(pixmap_Other)
        label_Other.move(650, 110)

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

    def startEclipse(self):
        subprocess.call(['/home/pkgastronaut/eclipse/cpp-2020-03/eclipse/eclipse'])
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
