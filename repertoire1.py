# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\nsi_t\repertoire.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("")
        self.info_text = QtWidgets.QTextEdit(Dialog)
        self.info_text.setGeometry(QtCore.QRect(130, 10, 131, 21))
        self.info_text.setObjectName("info_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 61, 20))
        self.label.setObjectName("label")
        self.recherche_bouton = QtWidgets.QPushButton(Dialog)
        self.recherche_bouton.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.recherche_bouton.setObjectName("recherche_bouton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.label_2.setObjectName("label_2")
        self.num_text = QtWidgets.QTextEdit(Dialog)
        self.num_text.setGeometry(QtCore.QRect(240, 90, 131, 21))
        self.num_text.setObjectName("num_text")
        self.name_text = QtWidgets.QTextEdit(Dialog)
        self.name_text.setGeometry(QtCore.QRect(70, 90, 131, 21))
        self.name_text.setObjectName("name_text")
        self.ajout_button = QtWidgets.QPushButton(Dialog)
        self.ajout_button.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.ajout_button.setObjectName("ajout_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        self.suprime_button = QtWidgets.QPushButton(Dialog)
        self.suprime_button.setGeometry(QtCore.QRect(310, 130, 75, 23))
        self.suprime_button.setObjectName("suprime_button")
        self.print_button = QtWidgets.QPushButton(Dialog)
        self.print_button.setGeometry(QtCore.QRect(140, 240, 121, 23))
        self.print_button.setObjectName("print_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.info_text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nom ou numeros</p></body></html>"))
        self.label.setText(_translate("Dialog", "Recherché:"))
        self.recherche_bouton.setText(_translate("Dialog", "ok"))
        self.label_2.setText(_translate("Dialog", " contact:"))
        self.num_text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numéros</p></body></html>"))
        self.name_text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nom</p></body></html>"))
        self.ajout_button.setText(_translate("Dialog", "ajouté"))
        self.label_3.setText(_translate("Dialog", "ou"))
        self.suprime_button.setText(_translate("Dialog", "suprimé"))
        self.print_button.setText(_translate("Dialog", "Affiché répertoire"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
