# -*- coding: utf-8 -*-
#
# Created by: PyQt5 View code generator 5.15.7
#


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Add_Branch(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 350)
        Dialog.setStyleSheet("background-color: #D5F2E3;")
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonBox_new_branch = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_new_branch.setGeometry(QtCore.QRect(220, 290, 160, 35))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox_new_branch.setFont(font)
        self.buttonBox_new_branch.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_new_branch.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_new_branch.setCenterButtons(True)
        self.buttonBox_new_branch.setObjectName("buttonBox_new_branch")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(125, 20, 350, 30))
        self.label.setStyleSheet("QLabel {\n"
                                 "    color: black;\n"
                                 "    font: bold 18px consolas, sans-serif;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.branch_name_field = QtWidgets.QLineEdit(Dialog)
        self.branch_name_field.setGeometry(QtCore.QRect(240, 75, 300, 29))
        self.branch_name_field.setStyleSheet("QLineEdit {\n"
                                             "    color: black;    \n"
                                             "    background-color: white;\n"
                                             "    fonr: 14px consolas, sans-serif;\n"
                                             "    border: 1px solid black;\n"
                                             "    border-radius: 2px;    \n"
                                             "}")
        self.branch_name_field.setText("")
        self.branch_name_field.setObjectName("branch_name_field")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(20, 75, 220, 30))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(20, 185, 220, 60))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.name_organizetion_receivng_forms_field = QtWidgets.QTextEdit(Dialog)
        self.name_organizetion_receivng_forms_field.setGeometry(QtCore.QRect(240, 185, 300, 60))
        self.name_organizetion_receivng_forms_field.setStyleSheet("QTextEdit {\n"
                                                                  "    color: black;    \n"
                                                                  "    background-color: white;\n"
                                                                  "    fonr: 14px consolas, sans-serif;\n"
                                                                  "    border: 1px solid black;\n"
                                                                  "    border-radius: 2px;    \n"
                                                                  "}")
        self.name_organizetion_receivng_forms_field.setObjectName("name_organizetion_receivng_forms_field")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(20, 115, 220, 60))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_7.setObjectName("label_7")
        self.branch_adress_field = QtWidgets.QTextEdit(Dialog)
        self.branch_adress_field.setGeometry(QtCore.QRect(240, 115, 300, 60))
        self.branch_adress_field.setStyleSheet("QTextEdit {\n"
                                               "    color: black;    \n"
                                               "    background-color: white;\n"
                                               "    fonr: 14px consolas, sans-serif;\n"
                                               "    border: 1px solid black;\n"
                                               "    border-radius: 2px;    \n"
                                               "}")
        self.branch_adress_field.setObjectName("branch_adress_field")

        self.retranslateUi(Dialog)
        self.buttonBox_new_branch.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox_new_branch.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новый филиал"))
        self.label.setText(_translate("Dialog", "Укажите данные нового филиала"))
        self.label_4.setText(_translate("Dialog", "Наименование филиала"))
        self.label_5.setText(_translate("Dialog", "Наименование органа\n"
                                                  "МВД принимающего бланки"))
        self.name_organizetion_receivng_forms_field.setHtml(_translate("Dialog",
                                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                       "p, li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "Адрес филиала"))
        self.branch_adress_field.setHtml(_translate("Dialog",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
