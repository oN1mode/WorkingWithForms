# -*- coding: utf-8 -*-
#
# Created by: PyQt5 View code generator 5.15.7
#


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Add_Manager(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setStyleSheet("background-color: #D5F2E3;")
        self.buttonBox_new_manager = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox_new_manager.setGeometry(QtCore.QRect(220, 340, 160, 35))
        self.buttonBox_new_manager.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_new_manager.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_new_manager.setCenterButtons(True)
        self.buttonBox_new_manager.setObjectName("buttonBox_new_manager")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(20, 145, 200, 30))
        self.label_6.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.series_passport_field = QtWidgets.QLineEdit(Dialog)
        self.series_passport_field.setGeometry(QtCore.QRect(220, 180, 350, 29))
        self.series_passport_field.setStyleSheet("QLineEdit {\n"
                                                 "    color: black;    \n"
                                                 "    background-color: white;\n"
                                                 "    fonr: 14px consolas, sans-serif;\n"
                                                 "    border: 1px solid black;\n"
                                                 "    border-radius: 2px;    \n"
                                                 "}")
        self.series_passport_field.setText("")
        self.series_passport_field.setObjectName("series_passport_field")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 200, 30))
        self.label_5.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.number_passport_field = QtWidgets.QLineEdit(Dialog)
        self.number_passport_field.setGeometry(QtCore.QRect(220, 215, 350, 29))
        self.number_passport_field.setStyleSheet("QLineEdit {\n"
                                                 "    color: black;    \n"
                                                 "    background-color: white;\n"
                                                 "    fonr: 14px consolas, sans-serif;\n"
                                                 "    border: 1px solid black;\n"
                                                 "    border-radius: 2px;    \n"
                                                 "}")
        self.number_passport_field.setText("")
        self.number_passport_field.setObjectName("number_passport_field")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(20, 75, 200, 30))
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
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 200, 30))
        self.label_7.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_7.setObjectName("label_7")
        self.full_name_manager = QtWidgets.QLineEdit(Dialog)
        self.full_name_manager.setGeometry(QtCore.QRect(220, 75, 350, 29))
        self.full_name_manager.setStyleSheet("QLineEdit {\n"
                                             "    color: black;    \n"
                                             "    background-color: white;\n"
                                             "    fonr: 14px consolas, sans-serif;\n"
                                             "    border: 1px solid black;\n"
                                             "    border-radius: 2px;    \n"
                                             "}")
        self.full_name_manager.setText("")
        self.full_name_manager.setObjectName("full_name_manager")
        self.position_manager = QtWidgets.QLineEdit(Dialog)
        self.position_manager.setGeometry(QtCore.QRect(220, 110, 350, 29))
        self.position_manager.setStyleSheet("QLineEdit {\n"
                                            "    color: black;    \n"
                                            "    background-color: white;\n"
                                            "    fonr: 14px consolas, sans-serif;\n"
                                            "    border: 1px solid black;\n"
                                            "    border-radius: 2px;    \n"
                                            "}")
        self.position_manager.setText("")
        self.position_manager.setObjectName("position_manager")
        self.number_proxy_field = QtWidgets.QLineEdit(Dialog)
        self.number_proxy_field.setGeometry(QtCore.QRect(220, 145, 350, 29))
        self.number_proxy_field.setStyleSheet("QLineEdit {\n"
                                              "    color: black;    \n"
                                              "    background-color: white;\n"
                                              "    fonr: 14px consolas, sans-serif;\n"
                                              "    border: 1px solid black;\n"
                                              "    border-radius: 2px;    \n"
                                              "}")
        self.number_proxy_field.setText("")
        self.number_proxy_field.setObjectName("number_proxy_field")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(20, 215, 200, 30))
        self.label_8.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 300, 30))
        self.label.setStyleSheet("QLabel {\n"
                                 "    color: black;\n"
                                 "    font: bold 18px consolas, sans-serif;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.date_issue_passport_field = QtWidgets.QLineEdit(Dialog)
        self.date_issue_passport_field.setGeometry(QtCore.QRect(220, 250, 350, 29))
        self.date_issue_passport_field.setStyleSheet("QLineEdit {\n"
                                                     "    color: black;    \n"
                                                     "    background-color: white;\n"
                                                     "    fonr: 14px consolas, sans-serif;\n"
                                                     "    border: 1px solid black;\n"
                                                     "    border-radius: 2px;    \n"
                                                     "}")
        self.date_issue_passport_field.setText("")
        self.date_issue_passport_field.setObjectName("date_issue_passport_field")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QtCore.QRect(20, 250, 200, 30))
        self.label_9.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_9.setObjectName("label_9")
        self.passport_issued_by_field = QtWidgets.QLineEdit(Dialog)
        self.passport_issued_by_field.setGeometry(QtCore.QRect(220, 285, 350, 29))
        self.passport_issued_by_field.setStyleSheet("QLineEdit {\n"
                                                    "    color: black;    \n"
                                                    "    background-color: white;\n"
                                                    "    fonr: 14px consolas, sans-serif;\n"
                                                    "    border: 1px solid black;\n"
                                                    "    border-radius: 2px;    \n"
                                                    "}")
        self.passport_issued_by_field.setText("")
        self.passport_issued_by_field.setObjectName("passport_issued_by_field")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QtCore.QRect(20, 285, 200, 30))
        self.label_10.setStyleSheet("QLabel {\n"
                                    "    color: white;    \n"
                                    "    background-color: #73BA9B;\n"
                                    "    font: 700 16px consolas, sans-serif;\n"
                                    "    border: 1px solid white;\n"
                                    "    border-radius: 2px;    \n"
                                    "}")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        self.buttonBox_new_manager.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox_new_manager.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новый менеджер"))
        self.label_6.setText(_translate("Dialog", "Номер доверенности"))
        self.label_5.setText(_translate("Dialog", "Должность"))
        self.label_4.setText(_translate("Dialog", "ФИО"))
        self.label_7.setText(_translate("Dialog", "Серия паспорта"))
        self.label_8.setText(_translate("Dialog", "Номер паспорта"))
        self.label.setText(_translate("Dialog", "Укажите данные менеджера"))
        self.label_9.setText(_translate("Dialog", "Дата выдачи паспорта"))
        self.label_10.setText(_translate("Dialog", "Кем выдан паспорт"))
