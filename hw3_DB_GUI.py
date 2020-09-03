import sys, pymysql
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QCoreApplication

from datetime import datetime

customerID = "0"
deli_num = 249183
ord_code = 19101912
bask_id = 1
pdc = 1
login_check = 0

class sql(QMainWindow):
    ctn = 0
    global k
    global s
    global login_check
    global customerID

    list = []


    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()

        time = str(datetime.today().year)
        time = time + '/' + str(datetime.today().month) + '/' + str(datetime.today().day)

        self.statusBar()  # 상태 창 생성
        self.statusBar().showMessage('Today  '+str(time))


    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='950205',
                charset='utf8',
                db='postshop',
                port= 3306)
        except:
            print("Database Connection Failed.")
            exit(1)
        print("Database Connection.")
        self.cur = self.conn.cursor()

    def initUI(self):

        self.w = 600
        self.h = 380
        self.btnSize = 40

        self.btnXsize = 300
        self.btnYsize = 40

        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle("Post Office Shopping Mall")

        self.desc = ["Post Office","Shopping Mall"]

        if login_check == 0 :
            self.cmd로그인 = QPushButton("Log In", self)
            self.cmd로그인.resize(self.btnXsize, self.btnSize) # 버튼의 x축 사이즈, y축 사이즈
            self.cmd로그인.clicked.connect(self.logIn)

        elif login_check == 1 :
            self.cmd로그아웃 = QPushButton("Log Out", self)
            self.cmd로그아웃.resize(self.btnXsize, self.btnSize)  # 버튼의 x축 사이즈, y축 사이즈
            self.cmd로그아웃.clicked.connect(self.logIn)


        self.cmd회원가입 = QPushButton("Sign Up", self)
        self.cmd회원가입.resize(self.btnXsize, self.btnSize)
        self.cmd회원가입.clicked.connect(self.signUp)
        self.cmd소개 = QPushButton("Our Services", self)
        self.cmd소개.resize(self.btnXsize, self.btnSize)
        self.cmd소개.clicked.connect(self.our_service)
        self.cmd나가기 = QPushButton("Exit", self)
        self.cmd나가기.resize(self.btnXsize, self.btnSize)
        self.cmd나가기.clicked.connect(self.close_event)

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(67, 134, 207))  # R, G, B
        qp.setFont(QFont('Consolas', 30))
        qp.drawText(170, 60, self.desc[0])

        qp.setPen(QColor(45, 107, 176))  # R, G, B
        qp.setFont(QFont('Consolas', 40))
        qp.drawText(110, 110, self.desc[1])


    def close_event(self):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes: # 메세지 박스 값이 Yes이면
            QCoreApplication.instance().quit() # 종료

    def logIn(self):
        self.log = log_In()
        self.log.show()

    def our_service(self):
        self.s = service()
        self.s.show()

    def signUp(self):
        self.sign = sign_up()
        self.sign.show()

    def new(self):
        self.cur.execute("select count(*) from customer")
        self.conn.commit()
        self.cnt = self.cur.fetchone()
        k.show()

    def resizeEvent(self, QResizeEvent):
        self.btnX = self.width() - 300 # 버튼의 X 위치 변수
        self.btnY = self.height() - 130

        if login_check == 0 :
            self.cmd로그인.move(self.btnX - 150, self.btnY - 50 * 2) # x축 위치 , y축 위치
        else :
            self.cmd로그아웃.move(self.btnX - 150, self.btnY - 50 * 2)  # x축 위치 , y축 위치

        self.cmd회원가입.move(self.btnX - 150, self.btnY - 50 * 1)
        self.cmd소개.move(self.btnX - 150, self.btnY)
        self.cmd나가기.move(self.btnX - 150, self.btnY + 50 * 1)

    def closeEvent(self, QCloseEvent):
        self.conn.close()

    """def enterEvent(self, QEvent):
        self.cmd = "select * from customer"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

        for i in range(len(ar)):
            self.내용.removeRow(i)
            self.내용.insertRow(i)
            self.내용.setData(self.내용.index(i,0), ar[i][0])
            self.내용.setData(self.내용.index(i, 1), ar[i][1])
            self.내용.setData(self.내용.index(i, 2), ar[i][2])"""


class service(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 650, 350)
        self.setWindowTitle("Our Service")
        self.a = "Our Service is"
        self.b = ["Our service sells local foods, artisan-made furnitures and nutritious foods.",
                 "You will be connected to the seller directly from our post office,",
                 "so you can enjoy many and ", "high quality products", " with ", "cheap shipping fee.",
                 "Since we have just started the service, We do not sell many products now.",
                 "If you have any questions or concerns, Please contact us by email below.",
                 "","",""]
        self.c = ["Chang-Hwan  Lee:    chlee@dgu.ac.kr", "Jung-Seob  Lee:    omanma1928@naver.com", "Jea-Ho  Jin:     jinjeaho0206@naver.com"]

        self.cmd엔드 = QPushButton("Exit", self)
        self.cmd엔드.resize(40, 30)
        self.cmd엔드.move(610, 320)
        self.cmd엔드.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(50,103,160)) #R, G, B
        qp.setFont(QFont('Arial', 30))
        qp.drawText(event.rect(), Qt.AlignHCenter, self.a)

        for i in range(0,3):
            qp.setPen(QColor(90,90,90)) #R, G, B
            qp.setFont(QFont('Arial', 13))
            qp.drawText(35, 90 + 25*i , self.b[i])

        for i in range(3,4):
            qp.setPen(QColor(50,103,167)) #R, G, B
            qp.setFont(QFont('Arial', 14))
            qp.drawText(245, 90 + 25*2 , self.b[i])

        for i in range(4,5):
            qp.setPen(QColor(90,90,90)) #R, G, B
            qp.setFont(QFont('Arial', 13))
            qp.drawText(418, 90 + 25*2 , self.b[i])

        for i in range(5,6):
            qp.setPen(QColor(234,194,6)) #R, G, B
            qp.setFont(QFont('Arial', 14))
            qp.drawText(458, 90 + 25*2 , self.b[i])

        for i in range(6, len(self.b)):
            qp.setPen(QColor(90,90,90)) #R, G, B
            qp.setFont(QFont('Arial', 13))
            qp.drawText(35, 90 + 25*(i-3), self.b[i])

        for i in range(0,len(self.c)):
            qp.setPen(QColor(0,0,0)) #R, G, B
            qp.setFont(QFont('Bell MT', 10))
            qp.drawText(16,  82 + 25*(i+len(self.b)-3) , self.c[i])

class sign_up(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Sign up")
        self.a = ["Welcome to", "Sign   Up"]

        yplus = 80

        self.lblID = QLabel("I   D", self)
        self.lblID.move(25, 25 + yplus)
        self.txtID = QLineEdit(self)
        self.txtID.move(26 + 75, 22 + yplus)
        self.lblPW = QLabel("Password", self)
        self.lblPW.move(25, 60 + yplus)
        self.txtPW = QLineEdit(self)
        self.txtPW.setEchoMode(QLineEdit.Password) # **** 패스워드 설정
        self.txtPW.move(26 + 75, 22 + 33 + yplus)

        self.lblPW2 = QLabel("Re_Password", self)
        self.lblPW2.move(15, 95 + yplus)
        self.txtPW2 = QLineEdit(self)
        self.txtPW2.setEchoMode(QLineEdit.Password)  # **** 패스워드 확인
        self.txtPW2.move(26 + 75, 22 + 68 + yplus)

        self.lblNAME = QLabel("Name", self)
        self.lblNAME.move(25, 130 + yplus)
        self.txtNAME = QLineEdit(self)
        self.txtNAME.move(26 + 75, 22 + 105 + yplus)
        self.lblSEX = QLabel("Sex (M/F)", self)
        self.lblSEX.move(25, 165 + yplus)
        self.txtSEX = QLineEdit(self)
        self.txtSEX.move(26 + 75, 22 + 139 + yplus)
        self.lblADD = QLabel("Address", self)
        self.lblADD.move(25, 200 + yplus)
        self.txtADD = QLineEdit(self)
        self.txtADD.move(26 + 75, 22 + 175 + yplus)
        self.lblPHONE = QLabel("Phone", self)
        self.lblPHONE.move(25, 235 + yplus)
        self.txtPHONE = QLineEdit(self)
        self.txtPHONE.move(26 + 75, 22 + 208 + yplus)

        self.cmd가입 = QPushButton("Sign Up", self)
        self.cmd가입.resize(100, 30)
        self.cmd가입.move(55, 270 + yplus)
        self.cmd가입.clicked.connect(self.insert_customer)
        self.cmd취소 = QPushButton("Exit", self)
        self.cmd취소.resize(80, 30)
        self.cmd취소.move(170, 270 + yplus)
        self.cmd취소.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(67, 134, 207))  # R, G, B
        qp.setFont(QFont('Consolas', 27))
        qp.drawText(55, 40, self.a[0])
        qp.setPen(QColor(45, 107, 176))  # R, G, B
        qp.setFont(QFont('Arial', 30))
        qp.drawText(75, 80, self.a[1])


    def insert_customer(self):
        password1 = self.txtPW.text()
        password2 = self.txtPW2.text()
        if (password1 != password2) and (self.txtID.text() != "") and (self.txtPW.text() != "") and (self.txtNAME.text() != "") and (self.txtSEX.text() != "") and (self.txtADD.text() != "") and (self.txtPHONE.text() != ""):
            QMessageBox.information(self, "Password Error!", "Passwords do not match.", QMessageBox.Yes, QMessageBox.Yes)

        else:
            if (password1 == password2) and (self.txtID.text() != "") and (self.txtPW.text() != "") and (self.txtNAME.text() != "") and (self.txtSEX.text() != "") and (self.txtADD.text() != "") and (self.txtPHONE.text() != ""):
                try:
                    self.cmd = "insert into CUSTOMER (`customer_ID`, `mem_ID`, `customer_pw`, `customer_name`, `customer_address`, `customer_phone`, `customer_gender`) values('{}',{},'{}','{}','{}','{}','{}')" \
                        .format(self.txtID.text(), 1000, self.txtPW.text(), self.txtNAME.text(), self.txtADD.text(), self.txtPHONE.text(), self.txtSEX.text())
                    w.cur.execute(self.cmd)
                    w.conn.commit()
                    self.close()
                except:
                    QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
                return
            elif (password1 == "") or (password2 == "") or (self.txtID.text() == "") or (self.txtPW.text() == "") or (self.txtNAME.text() == "") or (self.txtSEX.text() == "") or (self.txtADD.text() == "") or (self.txtPHONE.text() == ""):
                QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)

class log_In(QWidget):
    global bask_id
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Log in")
        self.a = "Log In ♪"

        self.lblLID = QLabel("I   D", self)
        self.lblLID.move(50, 75)
        self.txtLID = QLineEdit(self)
        self.txtLID.move(60 + 62, 70)
        self.lblLPW = QLabel("Password", self)
        self.lblLPW.move(50, 110)
        self.txtLPW = QLineEdit(self)
        self.txtLPW.move(60 + 62, 70 + 33)
        self.txtLPW.setEchoMode(QLineEdit.Password)

        self.cmd로그인 = QPushButton("Log In", self)
        self.cmd로그인.resize(80, 30)
        self.cmd로그인.move(65, 150)
        self.cmd로그인.clicked.connect(self.ID_PW_MATCH)
        self.cmd엔드 = QPushButton("Exit", self)
        self.cmd엔드.resize(80, 30)
        self.cmd엔드.move(170, 150)
        self.cmd엔드.clicked.connect(self.close)

    def ID_PW_MATCH(self):
        global customerID
        global login_check

        w.cur.execute("select customer_ID, customer_pw from customer")
        val = w.cur.fetchall()

        id = self.txtLID.text()
        password = self.txtLPW.text()

        check = 0

        if len(val) >= 1:

            for x in val:
                if id in x[0] and password in x[1]:
                    check = 1
                    customerID = id
                    login_check = 1
                    if customerID != "operator" :
                        self.mn = main_window()
                        self.close()
                        self.mn.show()
                    else :
                        self.mo = operator_window()
                        self.close()
                        self.mo.show()
        else:
            QMessageBox.information(self, "계정을 만들어주세요.", QMessageBox.Yes, QMessageBox.Yes)

        if check == 0:
            QMessageBox.information(self, "입력 오류", "ID 또는 비밀번호가 틀렸습니다.", QMessageBox.Yes, QMessageBox.Yes)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(67, 134, 207))  # R, G, B
        qp.setFont(QFont('Ubuntu Mono', 32))
        qp.drawText(80, 45, self.a)



class MyMenu_list(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global login_check
        global customerID

        self.setGeometry(300, 300, 400, 400)

        self.setWindowTitle("My Menu")
        self.a = ["My", "Menu"]

        self.cmd장바구니 = QPushButton("Cart / Order", self)
        self.cmd장바구니.resize(320, 60)
        self.cmd장바구니.move(40, 150)
        self.cmd장바구니.clicked.connect(self.Basket_move)

        self.cmd개인정보수정 = QPushButton("Edit Personal Information", self)
        self.cmd개인정보수정.resize(320, 60)
        self.cmd개인정보수정.move(40, 230)
        self.cmd개인정보수정.clicked.connect(self.Edit_move)

        self.cmd나가기 = QPushButton("Exit", self)
        self.cmd나가기.resize(320, 60)
        self.cmd나가기.move(40, 310)
        self.cmd나가기.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(67, 134, 207))
        qp.setFont(QFont('Times', 50))
        qp.drawText(155, 55, self.a[0])
        qp.setPen(QColor(45, 107, 236))  # R, G, B
        qp.setFont(QFont('Arial', 55))
        qp.drawText(110, 125, self.a[1])

    def Basket_move(self):
        self.basket = Basket_list()
        self.basket.show()

    def Edit_move(self):
        self.Edit = Edit_User_Info()
        self.Edit.show()

class Edit_User_Info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)

        self.setWindowTitle("Edit Personal Information")
        self.a = ["Personal", "Information"]
        self.b = "You are Our"

        w.cur.execute("select mem_ID from customer where customer_ID = '{tn}'".format(tn=customerID))
        self.val = w.cur.fetchone()

        if self.val[0] == 1000 :
            self.b2 = "NR"
        elif self.val[0] == 1010 :
            self.b2 = "VIP"
        elif self.val[0] == 1020 :
            self.b2 = "VVIP"
        elif self.val[0] == 1030 :
            self.b2 = "SVIP ♣"


        self.yplus = 180
        #"insert into delivery values({},{},{},'{}')".format(deli_num, deli_cost, deli_date, product_type)
        w.cur.execute("select * from customer where customer_ID = '{tn}'".format(tn=customerID))
        self.user_info = w.cur.fetchall()

        w.cur.execute("select customer_mileage from customer where customer_ID = '{tn}'".format(tn=customerID))
        self.user_mileage = w.cur.fetchone()

        mileage = int(self.user_mileage[0])


        self.lblMM = QLabel("Mileage :", self)
        self.lblMM.move(25, 25 + self.yplus - 40)
        self.lblMM = QLabel(str(mileage)+"원", self)
        self.lblMM.move(105, 25 + self.yplus - 40)

        self.lblID = QLabel("I   D", self)
        self.lblID.move(25, 25 + self.yplus)
        self.txtID = QLineEdit(self.user_info[0][0], self)
        self.txtID.move(26 + 75, 22 + self.yplus)
        self.txtID.setReadOnly(True)
        self.lblPW = QLabel("Password", self)
        self.lblPW.move(25, 60 + self.yplus)
        self.txtPW = QLineEdit(self.user_info[0][2], self)
        self.txtPW.setEchoMode(QLineEdit.Password)  # **** 패스워드 설정
        self.txtPW.move(26 + 75, 22 + 33 + self.yplus)
        self.txtPW.setReadOnly(True)
        self.lblNAME = QLabel("Name", self)
        self.lblNAME.move(25, 22 + 68 + self.yplus)
        self.txtNAME = QLineEdit(self.user_info[0][3], self)
        self.txtNAME.move(26 + 75, 22 + 68 + self.yplus)
        self.lblSEX = QLabel("Sex (M/F)", self)
        self.lblSEX.move(25, 130 + self.yplus)
        self.txtSEX = QLineEdit(self.user_info[0][6], self)
        self.txtSEX.move(26 + 75, 22 + 105 + self.yplus)
        self.txtSEX.setReadOnly(True)
        self.lblADD = QLabel("Address", self)
        self.lblADD.move(25, 165 + self.yplus)
        self.txtADD = QLineEdit(self.user_info[0][4], self)
        self.txtADD.move(26 + 75, 22 + 139 + self.yplus)
        self.lblPHONE = QLabel("Phone", self)
        self.lblPHONE.move(25, 200 + self.yplus)
        self.txtPHONE = QLineEdit(self.user_info[0][5], self)
        self.txtPHONE.move(26 + 75, 22 + 175 + self.yplus)

        self.cmd수정 = QPushButton("Save", self)
        self.cmd수정.resize(100, 30)
        self.cmd수정.move(55, 270 + self.yplus)
        self.cmd수정.clicked.connect(self.edit_customer)
        self.cmd취소 = QPushButton("Exit", self)
        self.cmd취소.resize(80, 30)
        self.cmd취소.move(170, 270 + self.yplus)
        self.cmd취소.clicked.connect(self.close)

    def edit_customer(self):
        self.cmd = "update CUSTOMER SET customer_name = '{}', customer_address = '{}', customer_phone = '{}' where customer_ID = '{}'"\
            .format(self.txtNAME.text(), self.txtADD.text(), self.txtPHONE.text(), customerID)
        w.cur.execute(self.cmd)
        w.conn.commit()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Arial', 30))
        qp.drawText(80, 40, self.a[0])
        qp.setPen(QColor(45, 107, 236))  # R, G, B
        qp.setFont(QFont('Arial', 25))
        qp.drawText(65, 75, self.a[1])

        qp.setPen(QColor(67, 134, 207))  # R, G, B
        qp.setFont(QFont('Times', 23))
        qp.drawText(15, 130, self.b)

        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 30))
        qp.drawText(173, 135, self.b2)


###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Basket_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global real_total
        #global customerID
        self.cmd1 = "select max(basket_id) from basket where customer_ID = '{tn}'".format(tn=customerID)
        w.cur.execute(self.cmd1)
        self.bID = w.cur.fetchall()

        if self.bID[0][0] == None:
            self.setGeometry(300, 300, 400, 500)

            self.setWindowTitle("Cart / Order")
            self.a = ["Cart", "Order"]

            self.안내 = QLabel("장바구니가 비어있습니다.", self)
            self.안내.move(70, 200)
            self.cmd엔드1 = QPushButton("Exit", self)
            self.cmd엔드1.resize(50, 30)
            self.cmd엔드1.move(330, 450)
            self.cmd엔드1.clicked.connect(self.close)
            #QMessageBox.information(self, "오류", "장바구니가 비어있습니다.", QMessageBox.Yes, QMessageBox.Yes)
            #self.close()

        else:
            self.setGeometry(300, 300, 400, 650)

            self.setWindowTitle("Cart / Order")
            self.a = ["Cart", "Order"]
            w.cur.execute(
                "select S.product_name, product_price from basket S, product T where customer_ID = '{tn}' AND T.product_name = S.product_name".format(tn=customerID))
            product_print = w.cur.fetchall()


            w.cur.execute(
                "select SUM(product_price) from basket S, product T where customer_ID = '{tn}' AND T.product_name = S.product_name".format(tn=customerID))
            total_price = w.cur.fetchall()

            w.cur.execute(
                "select T.product_kind from basket S, product T where S.customer_ID = '{tn}' AND S.product_name = T.product_name".format(tn=customerID))
            cart_kind = w.cur.fetchall()

            w.cur.execute(
                "select customer_mileage from customer where customer_ID = '{tn}'".format(tn=customerID))
            mileg = w.cur.fetchone()

            self.lblOpt = QLabel("번호           이름                  가격             배송비", self)
            self.lblOpt.move(60, 150)

            deliv_cost = 0
            TOT_deli = 0

            for k in range(0, len(cart_kind)):
                if str(cart_kind[k][0]) == "local":
                    deliv_cost = 5000
                else:
                    deliv_cost = 2500
                TOT_deli = TOT_deli + deliv_cost

            for i in range(0, len(product_print)):
                self.넘버 = QLabel(str(i + 1), self)
                self.넘버.move(70, 140 + (i + 1) * 40)
                self.이름 = QLabel(str(product_print[i][0]), self)
                self.이름.move(120, 140 + (i + 1) * 40)
                self.가격 = QLabel(str(product_print[i][1]), self)
                self.가격.move(220, 140 + (i + 1) * 40)
                self.배송비 = QLabel(str(deliv_cost), self)
                self.배송비.move(300, 140 + (i + 1) * 40)
                self.dd1 = QLabel('============================================================', self)
                self.dd1.move(20, 160 + (i + 1) * 40)

            TOT_p = total_price[0][0] + TOT_deli

            self.lblTotal = QLabel("총 가격 :", self)
            self.lblTotal.move(20, 500)
            self.lblTotal = QLabel(str(TOT_p) + "원", self)
            self.lblTotal.move(90, 500)

            self.lblMileage = QLabel("Mileage :", self)
            self.lblMileage.move(20, 520)
            self.lblMileage = QLabel(str(mileg[0]) + "원", self)
            self.lblMileage.move(90, 520)

            real_total = TOT_p - mileg[0]

            self.lblgg = QLabel("======================", self)
            self.lblgg.move(20, 540)


            self.lbltt = QLabel("결제 금액 :", self)
            self.lbltt.move(20, 565)
            self.lbltt = QLabel(str(real_total) + "원", self)
            self.lbltt.move(90, 565)


            self.lblqt = QLabel("적립 마일리지 :", self)
            self.lblqt.move(20, 585)
            self.lblqt = QLabel(str(real_total*2/100) + "원 + 회원 등급보너스", self)
            self.lblqt.move(105, 585)


            self.cmd구매 = QPushButton("Buy Now", self)
            self.cmd구매.resize(80, 30)
            self.cmd구매.move(230, 605)
            self.cmd구매.clicked.connect(self.BuyNow)
            self.cmd엔드 = QPushButton("Exit", self)
            self.cmd엔드.resize(50, 30)
            self.cmd엔드.move(330, 605)
            self.cmd엔드.clicked.connect(self.close)

    def BuyNow(self):
        global ord_code
        global deli_num
        deli_date = 20191203
        ord_date = deli_date - 3
        product_type = ""
        deli_cost = 0
        ord_code = ord_code + random.randrange(1, 1000000)
        deli_num = deli_num + random.randrange(1, 100000)

        w.cur.execute("select T.product_kind from basket S, product T where S.customer_ID = '{tn}' AND S.product_name = T.product_name".format(tn=customerID))
        cart_info = w.cur.fetchall()

        w.cur.execute("select T.product_price from basket S, product T where S.customer_ID = '{tn}' AND S.product_name = T.product_name".format(tn=customerID))
        prod_price = w.cur.fetchall()

        w.cur.execute("select T.product_code from basket S, product T where S.customer_ID = '{tn}' AND S.product_name = T.product_name".format(tn=customerID))
        prod_code = w.cur.fetchall()

        for k in range(0, len(cart_info)):
            if str(cart_info[k][0]) == "local":
                product_type = "S"
                deli_cost = 5000
            else:
                product_type = "N"
                deli_cost = 2500

            self.cmd = "insert into delivery values({},{},{},'{}')".format(deli_num, deli_cost, deli_date, product_type)
            w.cur.execute(self.cmd)
            w.conn.commit()

            self.cmd2 = "insert into orders values({},'{}',{},{},{},'{}',{})".format(ord_code, str(customerID), deli_num, ord_date, prod_price[k][0]+deli_cost, "배송준비", str(prod_code[k][0]))
            w.cur.execute(self.cmd2)
            w.conn.commit()

            deli_num = deli_num + 1
            ord_code = ord_code + 1
            self.cmd3 = "update customer SET customer_mileage = {} where customer_ID = '{}'".format(4*(prod_price[k][0]+deli_cost)/100,str(customerID))
            w.cur.execute(self.cmd3)
            w.conn.commit()

        ans = QMessageBox.information(self, "Thank you!", "구매해주셔서 감사합니다.♥", QMessageBox.Yes, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            self.close()



    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 50))
        qp.drawText(145, 55, self.a[0])
        qp.setPen(QColor(45, 107, 236))  # R, G, B
        qp.setFont(QFont('Arial', 55))
        qp.drawText(105, 125, self.a[1])

###
class operator_window(QWidget): # Log in 후 쇼핑 및 정보 조회 등을 위한 윈도우
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 700)
        self.btnXsize = 250
        self.btnSize = 70
        ymove = 120

        self.setWindowTitle("Management")
        self.a = "Management"


        self.cmd등록 = QPushButton("Insert Product", self)
        self.cmd등록.resize(self.btnXsize, self.btnSize)  # 버튼의 x축 사이즈, y축 사이즈
        self.cmd등록.move(75, 60 + ymove)
        self.cmd등록.clicked.connect(self.insert_move)
        self.cmd수정 = QPushButton("Update Product", self)
        self.cmd수정.resize(self.btnXsize, self.btnSize)
        self.cmd수정.move(75, 160 + ymove)
        self.cmd수정.clicked.connect(self.update_move)
        self.cmd삭제 = QPushButton("Delete Product", self)
        self.cmd삭제.resize(self.btnXsize, self.btnSize)
        self.cmd삭제.move(75, 260 + ymove)
        self.cmd삭제.clicked.connect(self.delete_move)
        self.cmd마이메뉴 = QPushButton("My Menu", self)
        self.cmd마이메뉴.resize(self.btnXsize, self.btnSize)
        self.cmd마이메뉴.move(75, 360 + ymove)
        self.cmd마이메뉴.clicked.connect(self.MyMenu_move)

        self.cmd로그아웃 = QPushButton("Log Out", self)
        self.cmd로그아웃.resize(self.btnXsize, self.btnSize)
        self.cmd로그아웃.move(75, 460 + ymove)
        self.cmd로그아웃.clicked.connect(self.close_event)

    def close_event(self):
        ans = QMessageBox.question(self, "종료 확인", "종료하시면 로그아웃 됩니다.\n  종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes: # 메세지 박스 값이 Yes이면
            customerID = ""
            login_check = 0
            self.close() # 종료

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(45, 107, 236))  # R, G, B
        qp.setFont(QFont('Arial', 45))
        qp.drawText(25, 100, self.a)

    def insert_move(self):
        self.insert = insert_list()
        self.insert.show()

    def update_move(self):
        self.update = update_list()
        self.update.show()

    def delete_move(self):
        self.delete = delete_list()
        self.delete.show()

    def MyMenu_move(self):
         self.MyMenu = MyMenu_list()
         self.MyMenu.show()


class insert_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Insertion")
        self.a = "Insert Product"

        yplus = 80
        txplus = 10

        self.lblID = QLabel("I    D", self)
        self.lblID.move(25, 25 + yplus)
        self.txtID = QLineEdit(self)
        self.txtID.move(26 + 75 + txplus, 22 + yplus)

        self.lblPV = QLabel("#_Provider", self)
        self.lblPV.move(25, 60 + yplus)
        self.txtPV = QLineEdit(self)
        self.txtPV.move(26 + 75 + txplus, 22 + 33 + yplus)

        self.lblKD = QLabel("Kind", self)
        self.lblKD.move(25, 95 + yplus)
        self.txtKD = QLineEdit(self)
        self.txtKD.move(26 + 75 + txplus, 22 + 68 + yplus)

        self.lblPR = QLabel("Price", self)
        self.lblPR.move(25, 130 + yplus)
        self.txtPR = QLineEdit(self)
        self.txtPR.move(26 + 75 + txplus, 22 + 105 + yplus)

        self.lblWR = QLabel("#_Warehouse", self)
        self.lblWR.move(25, 165 + yplus)
        self.txtWR = QLineEdit(self)
        self.txtWR.move(26 + 75 + txplus, 22 + 139 + yplus)

        self.lblNAME = QLabel("Name", self)
        self.lblNAME.move(25, 200 + yplus)
        self.txtNAME = QLineEdit(self)
        self.txtNAME.move(26 + 75 + txplus, 22 + 175 + yplus)

        self.lblSTOCK = QLabel("Stock", self)
        self.lblSTOCK.move(25, 235 + yplus)
        self.txtSTOCK = QLineEdit(self)
        self.txtSTOCK.move(26 + 75 + txplus, 22 + 208 + yplus)

        self.cmd등록 = QPushButton("Register", self)
        self.cmd등록.resize(100, 30)
        self.cmd등록.move(55, 270 + yplus)
        self.cmd등록.clicked.connect(self.insert_product)

        self.cmd취소 = QPushButton("Exit", self)
        self.cmd취소.resize(80, 30)
        self.cmd취소.move(170, 270 + yplus)
        self.cmd취소.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 35))
        qp.drawText(20, 55, self.a)

    def insert_product(self):
        if (self.txtID.text() != "") and (self.txtPV.text() != "") and (self.txtKD.text() != "") and (self.txtPR.text() != "") and \
                (self.txtWR.text() != "") and (self.txtNAME.text() != "") and (self.txtSTOCK.text() != ""):
            try:
                self.cmd = "insert into product (`product_code`, `provider_num`, `product_kind`, `product_price`, " \
                           "`warehouse_code`, `product_name`, `product_stock`) " \
                           "values({},{},'{}',{},{},'{}',{})" \
                    .format(self.txtID.text(), self.txtPV.text(), self.txtKD.text(), self.txtPR.text(), self.txtWR.text(),
                            self.txtNAME.text(), self.txtSTOCK.text())
                w.cur.execute(self.cmd)
                w.conn.commit()
                QMessageBox.information(self, "등록 완료", "물품이 등록되었습니다!", QMessageBox.Yes, QMessageBox.Yes)
                self.close()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return
        elif (self.txtID.text() == "") or (self.txtPW.text() == "") or (self.txtNAME.text() == "") \
                or (self.txtSEX.text() == "") or (self.txtADD.text() == "") or (self.txtPHONE.text() == ""):
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)

class update_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Update")
        self.a = "Update Product"

        yplus = 80
        txplus = 10

        self.lblID = QLabel("ID to Update", self)
        self.lblID.move(25, 25 + yplus)
        self.txtID = QLineEdit(self)
        self.txtID.move(26 + 75 + txplus, 22 + yplus)

        self.lblPV = QLabel("#_Provider", self)
        self.lblPV.move(25, 60 + yplus)
        self.txtPV = QLineEdit(self)
        self.txtPV.move(26 + 75 + txplus, 22 + 33 + yplus)

        self.lblKD = QLabel("Kind", self)
        self.lblKD.move(25, 95 + yplus)
        self.txtKD = QLineEdit(self)
        self.txtKD.move(26 + 75 + txplus, 22 + 68 + yplus)

        self.lblPR = QLabel("Price", self)
        self.lblPR.move(25, 130 + yplus)
        self.txtPR = QLineEdit(self)
        self.txtPR.move(26 + 75 + txplus, 22 + 105 + yplus)

        self.lblWR = QLabel("#_Warehouse", self)
        self.lblWR.move(25, 165 + yplus)
        self.txtWR = QLineEdit(self)
        self.txtWR.move(26 + 75 + txplus, 22 + 139 + yplus)

        self.lblNAME = QLabel("Name", self)
        self.lblNAME.move(25, 200 + yplus)
        self.txtNAME = QLineEdit(self)
        self.txtNAME.move(26 + 75 + txplus, 22 + 175 + yplus)

        self.lblSTOCK = QLabel("Stock", self)
        self.lblSTOCK.move(25, 235 + yplus)
        self.txtSTOCK = QLineEdit(self)
        self.txtSTOCK.move(26 + 75 + txplus, 22 + 208 + yplus)

        self.cmd등록 = QPushButton("Update", self)
        self.cmd등록.resize(100, 30)
        self.cmd등록.move(55, 270 + yplus)
        self.cmd등록.clicked.connect(self.update_product)

        self.cmd취소 = QPushButton("Exit", self)
        self.cmd취소.resize(80, 30)
        self.cmd취소.move(170, 270 + yplus)
        self.cmd취소.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 32))
        qp.drawText(20, 55, self.a)

    def update_product(self):
        if (self.txtID.text() != "") and (self.txtPV.text() != "") and (self.txtKD.text() != "") and (self.txtPR.text() != "") and \
                (self.txtWR.text() != "") and (self.txtNAME.text() != "") and (self.txtSTOCK.text() != ""):
            try:
                self.cmd = "update product SET product_code = {}, provider_num = {}, product_kind = '{}', product_price = {}, " \
                           "warehouse_code = {}, product_name = '{}', product_stock = {}) " \
                    .format(self.txtID.text(), self.txtPV.text(), self.txtKD.text(), self.txtPR.text(), self.txtWR.text(),
                            self.txtNAME.text(), self.txtSTOCK.text())
                w.cur.execute(self.cmd)
                w.conn.commit()
                QMessageBox.information(self, "수정 완료", "물품이 수정되었습니다!", QMessageBox.Yes, QMessageBox.Yes)
                self.close()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return
        elif (self.txtID.text() == "") or (self.txtPW.text() == "") or (self.txtNAME.text() == "") \
                or (self.txtSEX.text() == "") or (self.txtADD.text() == "") or (self.txtPHONE.text() == ""):
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)



class delete_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Delete")
        self.a = "Delete Product"

        yplus = 0
        txplus = 10

        self.lblID = QLabel("ID to Delete", self)
        self.lblID.move(25, 82 + yplus)
        self.txtID = QLineEdit(self)
        self.txtID.move(26 + 75 + txplus, 77 + yplus)

        self.cmd등록 = QPushButton("Delete", self)
        self.cmd등록.resize(100, 30)
        self.cmd등록.move(55, 130 + yplus)
        self.cmd등록.clicked.connect(self.delete_product)

        self.cmd취소 = QPushButton("Exit", self)
        self.cmd취소.resize(80, 30)
        self.cmd취소.move(170, 130 + yplus)
        self.cmd취소.clicked.connect(self.close)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 32))
        qp.drawText(20, 55, self.a)

    def delete_product(self):
        if (self.txtID.text() != ""):
            try:
                self.cmd = "delete from product where product_code = {tn};".format(tn=self.txtID.text())
                w.cur.execute(self.cmd)
                w.conn.commit()
                QMessageBox.information(self, "삭제 완료", "물품이 삭제되었습니다!", QMessageBox.Yes, QMessageBox.Yes)
                self.close()
            except:
                QMessageBox.information(self, "삽입 오류", "올바른 형식으로 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            return
        elif (self.txtID.text() == ""):
            QMessageBox.information(self, "입력 오류", "빈칸 없이 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)




class main_window(QWidget): # Log in 후 쇼핑 및 정보 조회 등을 위한 윈도우
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 700)
        self.btnXsize = 250
        self.btnSize = 70
        ymove = 120

        self.setWindowTitle("Welcome")
        self.a = ["Order", "Personal"]


        self.cmd음식 = QPushButton("Food", self)
        self.cmd음식.resize(self.btnXsize, self.btnSize)  # 버튼의 x축 사이즈, y축 사이즈
        self.cmd음식.move(75, 60 + ymove)
        self.cmd음식.clicked.connect(self.Food_move)
        self.cmd특산물 = QPushButton("Local Products", self)
        self.cmd특산물.resize(self.btnXsize, self.btnSize)
        self.cmd특산물.move(75, 160 + ymove)
        self.cmd특산물.clicked.connect(self.Local_move)
        self.cmd가구 = QPushButton("Furniture", self)
        self.cmd가구.resize(self.btnXsize, self.btnSize)
        self.cmd가구.move(75, 260 + ymove)
        self.cmd가구.clicked.connect(self.Fur_move)
        self.cmd마이메뉴 = QPushButton("My Menu", self)
        self.cmd마이메뉴.resize(self.btnXsize, self.btnSize)
        self.cmd마이메뉴.move(75, 360 + ymove)
        self.cmd마이메뉴.clicked.connect(self.MyMenu_move)

        self.cmd로그아웃 = QPushButton("Log Out", self)
        self.cmd로그아웃.resize(self.btnXsize, self.btnSize)
        self.cmd로그아웃.move(75, 460 + ymove)
        self.cmd로그아웃.clicked.connect(self.close_event)

    def close_event(self):
        ans = QMessageBox.question(self, "종료 확인", "종료하시면 로그아웃 됩니다.\n  종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes: # 메세지 박스 값이 Yes이면
            customerID = ""
            login_check = 0
            self.close() # 종료

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)

    def drawText(self, event, qp):
        qp.setPen(QColor(221, 210, 0))  # R, G, B
        qp.setFont(QFont('Times', 45))
        qp.drawText(130, 60, self.a[0])
        qp.setPen(QColor(45, 107, 236))  # R, G, B
        qp.setFont(QFont('Arial', 45))
        qp.drawText(85, 130, self.a[1])


    def Food_move(self):
        self.food = Food_list()
        self.food.show()

    def Local_move(self):
        self.local = Local_list()
        self.local.show()

    def Fur_move(self):
        self.furnit = Furniture_list()
        self.furnit.show()

    def MyMenu_move(self):
        self.MyMenu = MyMenu_list()
        self.MyMenu.show()



class Food_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global pdc
        global bask_id
        self.setGeometry(300, 300, 400, 500)
        w.cur.execute("select product_name, product_stock, product_price, product_code from product where product_kind='food'")
        prod = w.cur.fetchall()
        w.cur.execute("select count(product_kind) from product where product_kind = 'food'")
        kind = w.cur.fetchall()
        pdc = prod

        kind = int(kind[0][0])

        asd = [str(prod[0])]

        self.lblOpt = QLabel("선택        이름                  재고          가격", self)
        self.lblOpt.move(50, 20)


        for i in range(0, kind):
             #if str(kind[i][0]) == "food" :
             self.lblAS = QLabel(str(prod[i][0]), self)
             self.lblAS.move(100, 60 * (i+1))
             self.dd1 =  QLabel('=========================================================================', self)
             self.dd1.move (10, 60 * (i+1) + 20)
             self.lblAS_1 = QLabel(str(prod[i][1]), self)
             self.lblAS_1.move(200, 60 * (i+1))
             self.lblAS_2 = QLabel(str(prod[i][2]), self)
             self.lblAS_2.move(260, 60 * (i+1))



             #elif "product" == prod[i][3] :

        self.check1 = QCheckBox("", self)
        self.check1.move(50, 60 * 1)
        self.check2 = QCheckBox("", self)
        self.check2.move(50, 60 * 2)
        self.check3 = QCheckBox("", self)
        self.check3.move(50, 60 * 3)

        if kind > 3 :
            self.check4 = QCheckBox("", self)
            self.check4.move(50, 60 * 4)

        #elif "food" == prod[i][3] :
        #    QMessageBox.information(self, "입력 오류", "ID 또는 비밀번호가 틀렸습니다.", QMessageBox.Yes, QMessageBox.Yes)
        #     break

        self.cmd담기 = QPushButton("장바구니 담기", self)
        self.cmd담기.resize(90, 50)
        self.cmd담기.move(100, 350)
        self.cmd담기.clicked.connect(self.move_basket)

        self.cmd취소= QPushButton("닫 기", self)
        self.cmd취소.resize(90, 50)
        self.cmd취소.move(200, 350)
        self.cmd취소.clicked.connect(self.close)

    total_price = 0
        #self.lblLID = QLabel(, self)
        #self.lblLID.move(50, 75)

    def move_basket(self):
        self.ccheck = 0
        global bask_id ## bsktet
        self.cmd1 = "select max(basket_id) from basket"
        w.cur.execute(self.cmd1)
        self.bID = w.cur.fetchall()

        if self.bID[0][0] == None:
            bask_id = 1
        else:
            bask_id = self.bID[0][0] + 1

        if self.check1.isChecked() == True:
            self.cmd = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[0][0])
            w.cur.execute(self.cmd)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck+1

        if self.check2.isChecked() == True:
            self.cmd2 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[1][0])
            w.cur.execute(self.cmd2)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.check3.isChecked() == True:
            self.cmd3 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[2][0])
            w.cur.execute(self.cmd3)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.ccheck >= 1 :
            QMessageBox.information(self, "확인!", "장바구니에 담겼습니다.", QMessageBox.Yes, QMessageBox.Yes)



class Local_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global pdc
        global bask_id
        self.setGeometry(300, 300, 400, 500)
        w.cur.execute("select product_name, product_stock, product_price, product_code from product where product_kind='local'")
        prod = w.cur.fetchall()
        w.cur.execute("select count(product_kind) from product where product_kind = 'local'")
        kind = w.cur.fetchall()
        pdc = prod

        kind = int(kind[0][0])

        asd = [str(prod[0])]

        self.lblOpt = QLabel("선택        이름                  재고          가격", self)
        self.lblOpt.move(50, 20)



        for i in range(0, kind):
             #if str(kind[i][0]) == "food" :
             self.lblAS = QLabel(str(prod[i][0]), self)
             self.lblAS.move(100, 60 * (i+1))
             self.dd1 =  QLabel('=========================================================================', self)
             self.dd1.move (10, 60 * (i+1) + 20)
             self.lblAS_1 = QLabel(str(prod[i][1]), self)
             self.lblAS_1.move(200, 60 * (i+1))
             self.lblAS_2 = QLabel(str(prod[i][2]), self)
             self.lblAS_2.move(260, 60 * (i+1))



             #elif "product" == prod[i][3] :

        self.check1 = QCheckBox("", self)
        self.check1.move(50, 60 * 1)
        self.check2 = QCheckBox("", self)
        self.check2.move(50, 60 * 2)
        self.check3 = QCheckBox("", self)
        self.check3.move(50, 60 * 3)

        if kind > 3 :
            self.check4 = QCheckBox("", self)
            self.check4.move(50, 60 * 4)

        #elif "food" == prod[i][3] :
        #    QMessageBox.information(self, "입력 오류", "ID 또는 비밀번호가 틀렸습니다.", QMessageBox.Yes, QMessageBox.Yes)
        #     break

        self.cmd담기 = QPushButton("장바구니 담기", self)
        self.cmd담기.resize(90, 50)
        self.cmd담기.move(100, 350)
        self.cmd담기.clicked.connect(self.move_basket)

        self.cmd취소= QPushButton("닫 기", self)
        self.cmd취소.resize(90, 50)
        self.cmd취소.move(200, 350)
        self.cmd취소.clicked.connect(self.close)

    total_price = 0
        #self.lblLID = QLabel(, self)
        #self.lblLID.move(50, 75)

    def move_basket(self):
        self.ccheck = 0
        global bask_id ## bsktet
        self.cmd1 = "select max(basket_id) from basket"
        w.cur.execute(self.cmd1)
        self.bID = w.cur.fetchall()

        if self.bID[0][0] == None:
            bask_id = 1
        else:
            bask_id = self.bID[0][0] + 1

        if self.check1.isChecked() == True:
            self.cmd = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[0][0])
            w.cur.execute(self.cmd)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck+1

        if self.check2.isChecked() == True:
            self.cmd2 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[1][0])
            w.cur.execute(self.cmd2)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.check3.isChecked() == True:
            self.cmd3 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[2][0])
            w.cur.execute(self.cmd3)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.ccheck >= 1 :
            QMessageBox.information(self, "확인!", "장바구니에 담겼습니다.", QMessageBox.Yes, QMessageBox.Yes)

class Furniture_list(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global pdc
        global bask_id
        self.setGeometry(300, 300, 400, 500)
        w.cur.execute("select product_name, product_stock, product_price, product_code from product where product_kind='fur'")
        prod = w.cur.fetchall()
        w.cur.execute("select count(product_kind) from product where product_kind = 'fur'")
        kind = w.cur.fetchall()
        pdc = prod

        kind = int(kind[0][0])

        asd = [str(prod[0])]

        self.lblOpt = QLabel("선택        이름                  재고          가격", self)
        self.lblOpt.move(50, 20)



        for i in range(0, kind):
             #if str(kind[i][0]) == "food" :
             self.lblAS = QLabel(str(prod[i][0]), self)
             self.lblAS.move(100, 60 * (i+1))
             self.dd1 =  QLabel('=========================================================================', self)
             self.dd1.move (10, 60 * (i+1) + 20)
             self.lblAS_1 = QLabel(str(prod[i][1]), self)
             self.lblAS_1.move(200, 60 * (i+1))
             self.lblAS_2 = QLabel(str(prod[i][2]), self)
             self.lblAS_2.move(260, 60 * (i+1))



             #elif "product" == prod[i][3] :

        self.check1 = QCheckBox("", self)
        self.check1.move(50, 60 * 1)
        self.check2 = QCheckBox("", self)
        self.check2.move(50, 60 * 2)
        self.check3 = QCheckBox("", self)
        self.check3.move(50, 60 * 3)

        if kind > 3 :
            self.check4 = QCheckBox("", self)
            self.check4.move(50, 60 * 4)

        #elif "food" == prod[i][3] :
        #    QMessageBox.information(self, "입력 오류", "ID 또는 비밀번호가 틀렸습니다.", QMessageBox.Yes, QMessageBox.Yes)
        #     break

        self.cmd담기 = QPushButton("장바구니 담기", self)
        self.cmd담기.resize(90, 50)
        self.cmd담기.move(100, 350)
        self.cmd담기.clicked.connect(self.move_basket)

        self.cmd취소= QPushButton("닫 기", self)
        self.cmd취소.resize(90, 50)
        self.cmd취소.move(200, 350)
        self.cmd취소.clicked.connect(self.close)

    total_price = 0
        #self.lblLID = QLabel(, self)
        #self.lblLID.move(50, 75)

    def move_basket(self):
        self.ccheck = 0
        global bask_id ## bsktet
        self.cmd1 = "select max(basket_id) from basket"
        w.cur.execute(self.cmd1)
        self.bID = w.cur.fetchall()

        if self.bID[0][0] == None:
            bask_id = 1
        else:
            bask_id = self.bID[0][0] + 1


        if self.check1.isChecked() == True:
            self.cmd = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[0][0])
            w.cur.execute(self.cmd)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck+1

        if self.check2.isChecked() == True:
            self.cmd2 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[1][0])
            w.cur.execute(self.cmd2)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.check3.isChecked() == True:
            self.cmd3 = "insert into basket values({},'{}','{}')".format(bask_id, customerID, pdc[2][0])
            w.cur.execute(self.cmd3)
            w.conn.commit()
            bask_id = bask_id + 1
            self.ccheck = self.ccheck + 1

        if self.ccheck >= 1 :
            QMessageBox.information(self, "확인!", "장바구니에 담겼습니다.", QMessageBox.Yes, QMessageBox.Yes)








app = QApplication(sys.argv)
w = sql() # 초기 생성된 창
#k = insert() # 새로 생성되는 창
#s = service()
#sign = sign_up()
#log = log_In()
#mn = main_window()
#food = Food_list()
#local = Local_list()
#furnit = Furniture_list()

#MyMenu = MyMenu_list()
#basket = Basket_list()
#Edit = Edit_User_Info()

sys.exit(app.exec_())

