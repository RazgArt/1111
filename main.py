import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QListWidget
Form, Window = uic.loadUiType("UI.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
def output():
    name = form.nameOFcoffee.toPlainText()
    with sqlite3.connect("coffee.sqlite") as con:
        cur=con.cursor()
        rez = cur.execute(f"""SELECT * FROM Coffee WHERE Name == {name}""").fetchall()
        # form.table.setText(rez)
        print(rez)
form.btn.clicked.connect(output)
app.exec_()



