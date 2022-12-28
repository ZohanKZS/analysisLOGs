from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextBrowser, QPushButton, QLineEdit,
                             QFileDialog, QTableWidget, QTableWidgetItem, QLabel,QCheckBox)
from PyQt6.QtGui import QIcon, QTextOption, QColor
from PyQt6.QtCore import Qt
import os
import datetime as dt

VER = '1.0.0.5'
d = dt.datetime.now()
#dstr='{:%d/%m/%y %H:%M:%S}'.format(d)
dstr='{:%d.%m.%y}'.format(d)
dstr='19.12.22'

VER1 = '1.0.0.5 ('+dstr+')'


def memoAdd1(self, s):
    self.memo1.append(str(s))


def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size


def getFolderCount(folder):
    total_size = os.path.getsize(folder)
    k = 0
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
            k += 1
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return k


class AppDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Delete logs files KZS v'+VER1)
        self.setWindowIcon(QIcon('zohan.ico'))
        self.resize(480, 480)
        self.setFixedSize(970, 480)
        self.move(10, 500)
        # self.setStyleSheet('''
        #                 QPushButton {
        #                     background:yellow;
        #                     border-radius:3px;
        #                     border: 1px solid #3873d9;
        #                     background-color: qlineargradient( x1: 0, y1: 1, x2: 1, y2: 0, stop: 0 silver, stop: 1 gray);
        #                 }        
        # ''')
        self.statusBar().showMessage('')

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText('Set file path...')
        self.edit.setText('C:\\000\\111')
        self.edit.resize(280, 20)
        self.edit.move(10, 0)

        self.tbt = QPushButton('...', self, clicked=self.tbtClick)
        self.tbt.resize(25, 20)
        self.tbt.move(290, 0)

        self.bt = QPushButton('Получить файлы', self, clicked=self.btClick)
        self.bt.move(10, 25)
        self.bt.resize(110, 25)

        self.bt1 = QPushButton('Удалить', self, clicked=self.bt1Click)
        self.bt1.move(125, 25)
        self.bt1.resize(110, 25)

        self.chek = QCheckBox('Open folder', self)
        self.chek.move(480, 5)
        self.chek.resize(110, 25)    
        # self.chek.setChecked(True)    
        

        self.bt2 = QPushButton('Получить файлы ASBC', self, clicked=self.bt2Click)
        self.bt2.move(480, 25)
        self.bt2.resize(140, 25)

        self.bt2 = QPushButton('Получить файлы Тест', self, clicked=self.bt3Click)
        self.bt2.move(630, 25)
        self.bt2.resize(140, 25)

        self.memo1 = QTextBrowser(self)
        self.memo1.move(10, 55)
        self.memo1.resize(460, 400)
        self.memo1.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        styleMemo = '''
            border: 1px solid black;
            background:silver;
            color:rgb(50,50,50);
            font-weight:bold;
            font-family: arial;
            font-size:12px;
            font-style:normal;


            '''
        self.memo1.setStyleSheet(styleMemo)


        self.bt1 = QPushButton('C', self, clicked=self.memo1.clear)
        self.bt1.move(245, 25)
        self.bt1.resize(25, 25)         

        self.tab1 = QTableWidget(1, 3, self,cellClicked=self.CellClick)
        self.tab1.move(480, 55)
        self.tab1.resize(480, 400)
        #border-top-color: green;
        #border-bottom-color: red;

        styleTab="""
            border: 1px solid black;
            border-radius: 4px;
            background-color: silver;
            
            gridline-color: #777;
            selection-background-color: #ccdfff;
            color:#000;
            font-size:12px;
            font-weight:bold;
        """

        styleTab1='''
            border: 1px solid black; 
            background:silver;
            gridline-color:rgb(100,100,100);
            font-family: arial;
            font-weight:bold;

            QTableWidget::header:horizontal: {
                color: yellow;
                border-style: solid;
                
            }
     
        '''
        self.tab1.setStyleSheet(styleTab)

        headls = ['Путь к файлу', 'Размер', 'Кол-во']
        self.tab1.setHorizontalHeaderLabels(headls)

        self.label1=QLabel('Total size:',self)
        self.label1.move(780, 30)
        self.label1.resize(250,20)
        styleLBL='''
            font-family: arial;
            font-weight:bold;
            font-size:15px;
            color:green;
            '''
        self.label1.setStyleSheet(styleLBL)




        


    def DataOutPut(self,mfp):

        self.tab1.setRowCount(len(mfp))
        
        k = 0
        total=0
        for i in mfp:
            # self.memo1.append(i)
            size = ('{:10.2f}'.format(getFolderSize(i)/1024))
            sizef=getFolderSize(i)/1024

            size = f'{float(size):,}'.replace(',', ' ')
            self.tab1.setItem(k, 0, QTableWidgetItem(i))

            ite = QTableWidgetItem(size+'KB')
            ite.setTextAlignment(Qt.AlignmentFlag.AlignRight |
                                 Qt.AlignmentFlag.AlignVCenter)
            self.tab1.setItem(k, 1, ite)

            count = getFolderCount(i)
            ite = QTableWidgetItem(str(count))
            ite.setTextAlignment(Qt.AlignmentFlag.AlignRight |
                                 Qt.AlignmentFlag.AlignVCenter)
            self.tab1.setItem(k, 2, ite)

            total+=sizef

            k += 1

        total='{:10.2f}'.format(total)
        total=f'{float(total):,}'.replace(',', ' ')

        self.label1.setText('Total size:'+total+'KB')
        self.tab1.resizeColumnsToContents()
        self.tab1.resizeRowsToContents()

    def bt2Click(self):
        # lsfp = ['feed', 'forte', 'halyk', 'jusan', 'wolt', 'plaza']
        mfp = []
        # for i in lsfp:
        #     mfp.append(f'C:/inetpub/wwwroot/{i}/archive')

        fn=open('config.txt','r',encoding='utf-8')
        for i in fn:
            it=i.replace('\n','')

            mfp.append(it)


        self.DataOutPut(mfp)


    def CellClick(self,r,c):
        # print(str(r),'   ',str(c))
        # print(self.tab1.item(r,c).text())
        tt=self.tab1.item(r,c).text()
        self.edit.setText(tt)
        self.btClick()
        if self.chek.isChecked():
            # os.system(r"explorer.exe "+tt)
            # os.system(r'explorer /select,"'+tt+'"')
            os.system('explorer /open,"'+tt.replace('/','\\')+'"')

    def bt3Click(self):
        lsfp = ['pyqt5', 'snifmouse', 'snifmouse2', 'данные в таблице']
        mfp = []
        for i in lsfp:
            mfp.append(f'Z:\mac16\PyProject\{i}')

        self.DataOutPut(mfp)

    def bt1Click(self):
        self.memo1.clear()

        pth = self.edit.text()
        for root, dirs, files in os.walk(pth):
            for filename in files:
                d = dt.datetime.now()-dt.timedelta(days=3)
                fn = str(root)+'/'+str(filename)
                t = os.path.getmtime(fn)
                tfn = dt.datetime.fromtimestamp(t)
                if tfn < d:
                    # self.memo1.setTextColor(QColor.fromRgb(100,100,100))
                    # self.memo1.append(fn+'    '+str(tfn))
                    os.remove(fn)
                else:
                    # self.memo1.setTextColor(QColor.fromRgb(50,50,50))
                    # self.memo1.append(fn+'    '+str(tfn))
                    pass

    def btClick(self):

        self.memo1.clear()

        pth = "C:\\000\\111"
        root1 = ''
        pth = self.edit.text()
        n = 0
        for root, dirs, files in os.walk(pth):
            for filename in files:
                #                d=dt.datetime(2022,10,27)
                d = dt.datetime.now()-dt.timedelta(days=11)
                fn = str(root)+'/'+str(filename)
                t = os.path.getmtime(fn)
                tfn = dt.datetime.fromtimestamp(t)
                if tfn < d:
                    self.memo1.setTextColor(QColor.fromRgb(100, 100, 100))
                    self.memo1.append(fn+'    '+str(tfn))
                else:
                    self.memo1.setTextColor(QColor.fromRgb(50, 50, 50))
                    self.memo1.append(fn+'    '+str(tfn))
                n += 1

        self.statusBar().showMessage('Count rows - '+str(n))

    # with os.scandir(pth) as listOfEntries:
    #     for entry in listOfEntries:
    #         #if entry.is_file():
    #         memoAdd1(self,str(entry))
    # memoAdd1(self,listOfEntries)

    def tbtClick(self):
        r = QFileDialog.getExistingDirectory(self, 'Open catalog...')
        self.edit.setText(r)
        print(r)


if __name__ == '__main__':
    app = QApplication([])

    demo = AppDialog()
    demo.show()

    app.exec()
