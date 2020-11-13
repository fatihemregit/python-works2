import sys
from PyQt5.QtWidgets import *
#**************************************************************************************************************
#                           Açılış Penceresi Arama bölümü
#**************************************************************************************************************
class Pencere(QWidget):
 
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
 
        self.setWindowTitle("Hesaplar")
        self.Arama = QLineEdit()
 
 
        self.Arama_kontrol = QPushButton("Ara")
        self.a = QAbstractScrollArea()
        h_box = QHBoxLayout()
        h_box.addWidget(self.Arama)
 
        h_box.addWidget(self.Arama_kontrol)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.a)
 
        self.setLayout(v_box)
 
#**************************************************************************************************************
#                               Hesap Oluşturma Penceresi
#**************************************************************************************************************
class Pencere2(QWidget):
 
    def __init__(self):
        super().__init__()
        self.çalıştır()
 
    def çalıştır(self):
        self.hesap_başlık = QLabel("Hesap Başlığı :")
        self.hesap_içerik = QAbstractScrollArea()
        self.hesap_başlık_1 = QLineEdit()
        self.hesap_içerik_1 = QLabel("Hesap İçeriği: ")
        h_box = QHBoxLayout()
        h_box.addWidget(self.hesap_başlık)
        h_box.addWidget(self.hesap_başlık_1)
        h_box_1 = QHBoxLayout()
        h_box_1.addWidget(self.hesap_içerik_1)
        h_box_1.addWidget(self.hesap_içerik)
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box_1)
        self.setLayout(v_box)
 
 
#**************************************************************************************************************
#                       Main Page
#**************************************************************************************************************
class Menü(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.pencere = Pencere()
        self.pencre2 = Pencere2()
        self.kk()
    def kk(self):
        menü = self.menuBar()
        self.setWindowTitle("Hesaplar")
 
        self.setCentralWidget(self.pencere)
 
        hesap_oluştur = QAction("Hesap Oluştur", self)
        hesap_oluştur.setShortcut("Ctrl+p")
        hesap_oluştur.triggered.connect(self.hesap_olustur)
 
        ara = QAction("Hesap Ara", self)
 
        ara.triggered.connect(self.arama)
        menü.addAction(ara)
 
        menü.addAction(hesap_oluştur)
 
        self.show()
    def hesap_olustur(self):
        self.setCentralWidget(self.pencre2)
    def arama(self):
        self.setCentralWidget(self.pencere)
 
 
 
 
app = QApplication(sys.argv)
m = Menü()
sys.exit(app.exec_())
