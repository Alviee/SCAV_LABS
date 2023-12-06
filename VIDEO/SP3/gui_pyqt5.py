# ÁLVARO JIMENEZ | NIA: 240903
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import sp3_gui_functions as spGUI
import P1.main_p1 as mP1


# Exercise 3: GUI with PyQt5

class UI_MainWindow(QMainWindow):

    def __init__(self):
        super(UI_MainWindow, self).__init__()
        self.screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, 800, 400)
        self.setWindowTitle("Alvie's GUI")

        self.setupUI()

    def setupUI(self):
        self.label_gif3 = QLabel(self)
        self.label_gif3.setFixedSize(800, 400)
        self.label_gif3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif3.setScaledContents(True)
        self.gif3 = QtGui.QMovie("porygon.gif")
        self.label_gif3.setMovie(self.gif3)
        self.label_gif3.lower()
        self.gif3.start()

        self.text1 = QLabel(self)
        self.text1.setText("HI!!! This is Alvie's GUI. Here you will find some buttons to interact as well as a ")
        self.text1.setGeometry(50, 30, self.screen.width(), 30)

        self.text2 = QLabel(self)
        self.text2.setText("menubar which hides some functionalities!!!! Enjoy :)")
        self.text2.setGeometry(50, 60, self.screen.width(), 30)

        self.button1 = QPushButton(self)
        self.button1.setText('Browse Video 1')
        self.button1.setGeometry(50, 140, 200, 50)
        self.button1.clicked.connect(self.getFirstVideo)

        self.button2 = QPushButton(self)
        self.button2.setText('Browse Image')
        self.button2.setGeometry(550, 140, 200, 50)
        self.button2.clicked.connect(self.getImage)

        self.button3 = QPushButton(self)
        self.button3.setText('Browse Video 2')
        self.button3.setGeometry(300, 180, 200, 50)
        self.button3.clicked.connect(self.getSecondVideo)

        self.button4 = QPushButton(self)
        self.button4.setText('Lower Resolution (Video 2)')
        self.button4.setGeometry(550, 220, 200, 50)
        self.button4.clicked.connect(self.videoTask2)

        self.button5 = QPushButton(self)
        self.button5.setText('Are you bored?')
        self.button5.setGeometry(550, 290, 200, 50)
        self.button5.clicked.connect(self.bestOf2010)

        self.button6 = QPushButton(self)
        self.button6.setText('Motion Vectors (Video 1)')
        self.button6.setGeometry(300, 220, 200, 50)
        self.button6.clicked.connect(self.videoTask1)

        self.button7 = QPushButton(self)
        self.button7.setText('B/W Image Compression')
        self.button7.setGeometry(300, 290, 200, 50)
        self.button7.clicked.connect(self.videoTask3)

        self.label_gif1 = QLabel(self)
        self.gif1 = QtGui.QMovie("pikachu.gif")
        self.label_gif1.setMovie(self.gif1)
        self.gif1.start()

        self.label_gif2 = QLabel(self)
        self.gif2 = QtGui.QMovie("lugia.gif")
        self.label_gif2.setMovie(self.gif2)
        self.gif2.start()

        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('File')
        editMenu = self.menuBar.addMenu('Edit')
        modifyAction = editMenu.addMenu('Music')
        whatsThis = fileMenu.addMenu('???')
        doNotdoIt1 = whatsThis.addMenu('Look Away')
        doNotdoIt2 = doNotdoIt1.addMenu('Stop')
        doNotdoIt3 = doNotdoIt2.addMenu('Seriously do not keep going')
        doNotdoIt4 = doNotdoIt3.addMenu('Really?')

        finalEgg = QAction('Okay...', self)
        doNotdoIt4.addAction(finalEgg)
        finalEgg.triggered.connect(self.easterEgg)

        exitAction = QAction('Exit App', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda: QApplication.quit())

        fileMenu.addAction(exitAction)

        yesAction = QAction('Music: ON', self)
        noAction = QAction('Music: OFF', self)
        modifyAction.addAction(yesAction)
        modifyAction.addAction(noAction)

        self.player = QMediaPlayer(self)
        yesAction.triggered.connect(self.playAudioFile)
        noAction.triggered.connect(self.stopAudioFile)

    def resizeEvent(self, event):
        size = event.size()
        w_s = size.width()
        h_s = size.height()
        self.label_gif1.setGeometry(w_s - 190, h_s - 410, 300, 200)
        self.label_gif2.setGeometry(w_s - 750, h_s - 210, 300, 200)
        self.label_gif3.setFixedSize(w_s, h_s)

        button_width = 200
        button_height = 50
        margin = 50

        self.button1.setGeometry(w_s - 700 - margin, h_s - 250, button_width, button_height)
        self.button2.setGeometry(w_s - 200 - margin, h_s - 250,
                                 button_width, button_height)
        self.button3.setGeometry(w_s - 450 - margin, size.height() - 250,
                                 button_width, button_height)
        self.button4.setGeometry(w_s - 200 - margin, h_s - 180,
                                 button_width, button_height)
        self.button5.setGeometry(w_s - 200 - margin, h_s - 110,
                                 button_width, button_height)
        self.button6.setGeometry(w_s - 450 - margin, h_s - 180,
                                 button_width, button_height)
        self.button7.setGeometry(w_s - 450 - margin, h_s - 110,
                                 button_width, button_height)
        self.text1.setGeometry(w_s - 745, h_s - 350, w_s, 30)
        self.text2.setGeometry(w_s - 745, h_s - 320, w_s, 30)

        QMainWindow.resizeEvent(self, event)

    def getFirstVideo(self):
        try:
            filename1 = QFileDialog.getOpenFileName()
            path1 = filename1[0].split('.')
            if (path1[1] != 'mp4') and (path1[1] != 'webm'):
                self.showErrorDialog()
            else:
                self.video1 = filename1[0]
                self.showGoodDialog()
        except Exception as e:
            self.showErrorDialog()

    def getSecondVideo(self):
        try:
            filename2 = QFileDialog.getOpenFileName()
            path2 = filename2[0].split('.')
            if (path2[1] != 'mp4') and (path2 != 'webm'):
                self.showErrorDialog()
            else:
                self.video2 = filename2[0]
                self.showGoodDialog()
        except:
            self.showErrorDialog()

    def getImage(self):
        try:
            filename3 = QFileDialog.getOpenFileName()
            path3 = filename3[0].split('.')
            if (path3[1] != 'jpg') and (path3 != 'jpeg') and (path3[1] != 'png'):
                self.showErrorDialog()
            else:
                self.imageInput = filename3[0]
                self.showGoodDialog()
        except:
            self.showErrorDialog()

    def bestOf2010(self):
        url = QtCore.QUrl('https://www.youtube.com/watch?v=VW-XtICdVUk')
        QtGui.QDesktopServices.openUrl(url)

    def easterEgg(self):
        url = QtCore.QUrl('https://www.youtube.com/watch?v=DLzxrzFCyOs')
        QtGui.QDesktopServices.openUrl(url)

    def playAudioFile(self):
        file_path = os.path.join(os.getcwd(), 'music.mp3')
        url = QtCore.QUrl.fromLocalFile(file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def stopAudioFile(self):
        self.player.stop()

    def videoTask1(self):
        try:
            self.gui_class = spGUI.GUI_FUNCTIONS()
            self.gui_class.display_macro_motion_GUI(self.video1)
            self.showGoodDialog()
        except Exception as e:
            self.showErrorDialog()


    def videoTask2(self):
        try:
           self.gui_class.lower_resolution_GUI(self.video1)
           self.showGoodDialog()
        except:
            self.showErrorDialog()

    def videoTask3(self):
        try:
            mP1.bw_compression(self.imageInput)
            self.showGoodDialog()
        except:
            self.showErrorDialog()


    def showErrorDialog(self):
        dialog1 = QMessageBox(self)
        dialog1.setText('Oops! An error happened :(')
        dialog1.setWindowTitle('ERROR')
        dialog1.exec_()

    def showGoodDialog(self):
        dialog1 = QMessageBox(self)
        dialog1.setText('Success!')
        dialog1.setWindowTitle('WAHOO')
        dialog1.exec_()

def main():
    app = QApplication(sys.argv)
    window = UI_MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
