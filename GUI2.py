import sys
import downloader
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,QPushButton,QHBoxLayout,
                             QTextEdit, QGridLayout, QApplication,QInputDialog, QTableWidgetItem,QTableWidget,QVBoxLayout,QHeaderView)



class Example(QWidget):

    def __init__(self):
        super().__init__()
#布局
        layout = QVBoxLayout()


#控件1
        URL = QLabel('URL:')
        urlEdit = QLineEdit()
        layout.addWidget(URL)
        layout.addWidget(urlEdit)
        layout.setSpacing(10)

#对话框输入
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter the video URL:')
        if ok:
            urlEdit.setText(str(text))
            global url
            url = urlEdit.text()
#控件2.1
        extractorbtn = QPushButton('extract', self)
        layout.addWidget(extractorbtn)
        extractorbtn.clicked.connect(lambda: self.extractor)
#控件2.2
        downloadbtn = QPushButton('download', self)
        layout.addWidget(downloadbtn)
        downloadbtn.clicked.connect(self.download)

#控件3
        self.TableWidget = QTableWidget()
        self.TableWidget.setColumnCount(4)
        self.TableWidget.setHorizontalHeaderLabels(['format_code', 'extension', 'resolution', 'format_note', 'file_size'])
        self.TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.TableWidget)


#控件4
        self.formatcode = QLabel('format code:')
        self.code = QLineEdit()
        layout.addWidget(self.formatcode)
        layout.addWidget(self.code)

        self.setLayout(layout)

        self.setGeometry(700, 700, 800, 800)
        self.setWindowTitle('layout')
        self.show()
#####################
    #func of extractor

    @property
    def extractor(self):
        sample = downloader.Videocapture()
        try:
            a, b = sample.video(url)#'https://www.youtube.com/watch?v=omwngAlNG6Q'
            format_code, extension, resolution, format_note, file_size, file_count = sample.sort(a)
            self.showinfo(format_code, extension, resolution, format_note, file_size, file_count)
        except Exception as e:
            pass
#func of fill the info list
    def showinfo(self, format_code, extension, resolution, format_note, file_size, file_count):

        self.TableWidget.setRowCount(file_count)
        for i in range(0, file_count):
            self.TableWidget.setItem(i, 0, QTableWidgetItem(format_code[i]))
            self.TableWidget.setItem(i, 1, QTableWidgetItem(extension[i]))
            self.TableWidget.setItem(i, 2, QTableWidgetItem(resolution[i]))
            self.TableWidget.setItem(i, 3, QTableWidgetItem(format_note[i]))
            self.TableWidget.setItem(i, 4, QTableWidgetItem(str(file_size[i])))
#func of download
    def download(self):
        print(1)
        sample1 = downloader.Videocapture()
        a, b = sample1.video(url)
        b.params = {'format': str(self.code.text())}
        try:
            b.process_video_result(a)
        except Exception as e:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())