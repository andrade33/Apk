#dsdfsdfsdfsdfsdfsd
import pandas as pd
from PySide6 import QtWidgets, QtCore
import sqlite3
import pandas
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from ui import main

class MyQtApp(main.Ui_My_App, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.showMinimized()
        self.setWindowTitle("App")
        #self.populate_tree()
        self.populate_list_Widget()

        self.pushButton.clicked.connect(self.fill_form)
        self.toolButton.clicked.connect(self.select_photo)


        #self.populate_table_DB()
        self.table_geral()

        """ 
        def populate_tree(self):
        self.my_treeWidget.setHeaderLabel('TABELA')
        self.my_treeWidget.setStyleSheet("color:#fff000;font-size:15px;")
        self.my_treeWidget.setStyleSheet("QHeaderView{color:blue}")
        self.my_treeWidget.setHeaderLabels(['ID', 'NOME', 'TESTE'])
        self.my_treeWidget.clear()
        x = ['aplle', 'banana', 'pera', 'abacaxi']
        #item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
        for i, e in enumerate(x):
            item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
            item.setText(0, str(i))
            item.setText(1, e)
"""
    """
    def populate_tree(self):
        self.my_treeWidget.clear()
        x = ['aplle', 'banana', 'pera', 'abacaxi']
        item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
        for e in x:
            item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
            item.setText(0, e)
"""
    """
    def populate_table_DB(self):

        #pegando a ref da tree que está no form
        self.my_treeWidget.setStyleSheet(u" QHeaderView{color:black}; color:#fff000;font-size:15px;")

        #conectando ao DB
        cn = sqlite3.connect("system.db")

        #populando tabela usando o pandas
        result = pd.read_sql_query("select * from teste", cn)

        #Transformando o result da query em lista
        result = result.values.tolist()

        #Dando for no result e pegando os resultados pela indice
        for i in result:
            item = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
            item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            #setando o texto da coluna 1 e colocando o indice equivalente dentro da tree.
            item.setText(1, str(i[0]))
            item.setText(2, str(i[1]))
            item.setText(3, str(i[2]))



        
        for item in result:
            if item[0] == self.x:
                QtWidgets.QTreeWidgetItem(self.campo, item)
            else:
                self.campo = QtWidgets.QTreeWidgetItem(self.my_treeWidget, item)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = item[0]

        self.my_treeWidget.setSortingEnabled(True)

        for item in range(1,15):
            self.my_treeWidget.resizeColumnToContents(item)
"""

    def table_geral(self):
        self.my_treeView.setStyleSheet(u" QHeaderView{color:black}; color:#fff000;font-size:15px;")
        db = QSqlDatabase("SQLITE")

        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.my_treeView.setModel(self.model)
        self.model.setTable("teste")
        self.model.select()



    def populate_list_Widget(self):
        pass
        """    
        self.listWidget.clear()
        itens = ['a', 'b', 'c']
        self.listWidget.addItems(itens)"""

    def fill_form(self):
        name = self.name_LE.text()

        if not name:
            QtWidgets.QMessageBox.about(self, "sdfdaf", "fsdfsdf")
            return
        photo = self.photo_LE.text()
        if not photo:
            QtWidgets.QMessageBox.about(self, "ddsdsds", "fsdffffddfsdf")
            return
        QtWidgets.QMessageBox.about(self, "Done", "Gravado")

    def select_photo(self):
        photo_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, "Select Photo")
        if photo_path:
            self.photo_LE.setText(photo_path)

if  __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec()
