# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.7
#


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 620)
        MainWindow.setStyleSheet("background-color: #D5F2E3;\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_form_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_form_btn.setGeometry(QtCore.QRect(90, 510, 220, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_form_btn.sizePolicy().hasHeightForWidth())
        self.create_form_btn.setSizePolicy(sizePolicy)
        self.create_form_btn.setBaseSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.create_form_btn.setFont(font)
        self.create_form_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.create_form_btn.setAutoFillBackground(False)
        self.create_form_btn.setStyleSheet("QPushButton {\n"
                                           "    color: white;\n"
                                           "    background-color: #73BA9B;\n"
                                           "    font: 700 16px consolas, sans-serif;\n"
                                           "    border: 1px solid white;\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: #3A7C5D;\n"
                                           "}")
        self.create_form_btn.setObjectName("create_form_btn")
        self.branch_cmb = QtWidgets.QComboBox(self.centralwidget)
        self.branch_cmb.setGeometry(QtCore.QRect(90, 430, 220, 50))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.branch_cmb.setFont(font)
        self.branch_cmb.setStyleSheet("QComboBox {\n"
                                      "    color: white;\n"
                                      "    background-color: #73BA9B;\n"
                                      "    font: 700 16px consolas, sans-serif;\n"
                                      "    border: 1px solid white;\n"
                                      "    border-radius: 5px;    \n"
                                      "}\n"
                                      "")
        self.branch_cmb.setObjectName("branch_cmb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(90, 320, 220, 20))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    padding: 2px;    \n"
                                 "    color: white;\n"
                                 "    background-color: #73BA9B;\n"
                                 "    font: 700 16px consolas, sans-serif;\n"
                                 "    border-radius: 5px;\n"
                                 "}")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_branch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_branch_btn.setGeometry(QtCore.QRect(10, 10, 120, 55))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.add_branch_btn.setFont(font)
        self.add_branch_btn.setStyleSheet("QPushButton {\n"
                                          "    color: white;\n"
                                          "    background-color: #73BA9B;\n"
                                          "    border: 1px solid white;\n"
                                          "    border-radius: 5px;\n"
                                          "    white-space: normal;\n"
                                          "    font: 700 16px consolas, sans-serif;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: #3A7C5D;\n"
                                          "}")
        self.add_branch_btn.setObjectName("add_branch_btn")
        self.blank_type_cmb = QtWidgets.QComboBox(self.centralwidget)
        self.blank_type_cmb.setGeometry(QtCore.QRect(90, 340, 220, 50))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.blank_type_cmb.setFont(font)
        self.blank_type_cmb.setStyleSheet("QComboBox {\n"
                                          "    color: white;\n"
                                          "    background-color: #73BA9B;\n"
                                          "    font: 700 16px consolas, sans-serif;\n"
                                          "    border: 1px solid white;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "")
        self.blank_type_cmb.setObjectName("blank_type_cmb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(90, 410, 220, 20))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
                                   "    padding: 2px;    \n"
                                   "    color: white;\n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border-radius: 5px;\n"
                                   "}")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(75, 250, 150, 55))
        self.label_3.setStyleSheet("QLabel {\n"
                                   "    padding: 2px;\n"
                                   "    color: white;\n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 12px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 5px;\n"
                                   "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.input_line_number_field = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line_number_field.setGeometry(QtCore.QRect(225, 250, 150, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_line_number_field.setFont(font)
        self.input_line_number_field.setStyleSheet("QLineEdit {\n"
                                                   "    padding: 2px;\n"
                                                   "    color: black;\n"
                                                   "    background-color: white;\n"
                                                   "    font-weight: bold;\n"
                                                   "    border: 2px solid black;\n"
                                                   "    border-radius: 5px;\n"
                                                   "}")
        self.input_line_number_field.setAlignment(QtCore.Qt.AlignCenter)
        self.input_line_number_field.setObjectName("input_line_number_field")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 150, 30))
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(10, 111, 150, 30))
        self.label_5.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(10, 142, 150, 30))
        self.label_6.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 173, 150, 30))
        self.label_7.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(10, 204, 150, 30))
        self.label_8.setStyleSheet("QLabel {\n"
                                   "    color: white;    \n"
                                   "    background-color: #73BA9B;\n"
                                   "    font: 700 16px consolas, sans-serif;\n"
                                   "    border: 1px solid white;\n"
                                   "    border-radius: 2px;    \n"
                                   "}")
        self.label_8.setObjectName("label_8")
        self.last_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_field.setGeometry(QtCore.QRect(160, 80, 210, 29))
        self.last_name_field.setStyleSheet("QLineEdit {\n"
                                           "    color: black;    \n"
                                           "    background-color: white;\n"
                                           "    font: 16px consolas, sans-serif;\n"
                                           "    border: 1px solid black;\n"
                                           "    border-radius: 2px;    \n"
                                           "}")
        self.last_name_field.setText("")
        self.last_name_field.setObjectName("last_name_field")
        self.first_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_field.setGeometry(QtCore.QRect(160, 111, 210, 29))
        self.first_name_field.setStyleSheet("QLineEdit {\n"
                                            "    color: black;    \n"
                                            "    background-color: white;\n"
                                            "    font: 16px consolas, sans-serif;\n"
                                            "    border: 1px solid black;\n"
                                            "    border-radius: 2px;    \n"
                                            "}")
        self.first_name_field.setText("")
        self.first_name_field.setObjectName("first_name_field")
        self.middle_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.middle_name_field.setGeometry(QtCore.QRect(160, 142, 210, 29))
        self.middle_name_field.setStyleSheet("QLineEdit {\n"
                                             "    color: black;    \n"
                                             "    background-color: white;\n"
                                             "    font: 16px consolas, sans-serif;\n"
                                             "    border: 1px solid black;\n"
                                             "    border-radius: 2px;    \n"
                                             "}")
        self.middle_name_field.setText("")
        self.middle_name_field.setObjectName("middle_name_field")
        self.birthday_field = QtWidgets.QLineEdit(self.centralwidget)
        self.birthday_field.setGeometry(QtCore.QRect(160, 173, 210, 29))
        self.birthday_field.setStyleSheet("QLineEdit {\n"
                                          "    color: black;    \n"
                                          "    background-color: white;\n"
                                          "    font: 16px consolas, sans-serif;\n"
                                          "    border: 1px solid black;\n"
                                          "    border-radius: 2px;    \n"
                                          "}")
        self.birthday_field.setObjectName("birthday_field")
        self.nationality_field = QtWidgets.QLineEdit(self.centralwidget)
        self.nationality_field.setGeometry(QtCore.QRect(160, 204, 210, 29))
        self.nationality_field.setStyleSheet("QLineEdit {\n"
                                             "    color: black;    \n"
                                             "    background-color: white;\n"
                                             "    font: 16px consolas, sans-serif;\n"
                                             "    border: 1px solid black;\n"
                                             "    border-radius: 2px;    \n"
                                             "}")
        self.nationality_field.setObjectName("nationality_field")
        self.add_table_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_table_path_btn.setGeometry(QtCore.QRect(160, 10, 120, 55))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.add_table_path_btn.setFont(font)
        self.add_table_path_btn.setStyleSheet("QPushButton {\n"
                                              "    padding: 2px;\n"
                                              "    color: white;\n"
                                              "    background-color: #73BA9B;\n"
                                              "    font: 700 14px consolas, sans-serif;\n"
                                              "    border: 1px solid white;\n"
                                              "    border-radius: 5px;    \n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: #3A7C5D;\n"
                                              "}")
        self.add_table_path_btn.setObjectName("add_table_path_btn")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(312, 510, 48, 48))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("assets\images\Microsoft-Excel-2013-icon.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(312, 340, 48, 48))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("assets\images\Document-Microsoft-Excel-icon.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(312, 430, 48, 48))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("assets\images\city-icon.png"))
        self.label_11.setObjectName("label_11")
        self.add_manager_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_manager_btn.setGeometry(QtCore.QRect(310, 10, 120, 55))
        font = QtGui.QFont()
        font.setFamily("consolas,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.add_manager_btn.setFont(font)
        self.add_manager_btn.setStyleSheet("QPushButton {\n"
                                           "    padding: 2px;\n"
                                           "    color: white;\n"
                                           "    background-color: #73BA9B;\n"
                                           "    font: 700 16px consolas, sans-serif;\n"
                                           "    border: 1px solid white;\n"
                                           "    border-radius: 5px;    \n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: #3A7C5D;\n"
                                           "}")
        self.add_manager_btn.setObjectName("add_manager_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бланки для ФМС"))
        self.create_form_btn.setText(_translate("MainWindow", "Сформировать\n""бланк"))
        self.label.setText(_translate("MainWindow", "Выберите тип бланка"))
        self.add_branch_btn.setText(_translate("MainWindow", "Добавить\n""филиал"))
        self.label_2.setText(_translate("MainWindow", "Выберите филиал"))
        self.label_3.setText(_translate("MainWindow", "Номер\n""строки\n""из таблицы"))
        self.label_4.setText(_translate("MainWindow", "Фамилия"))
        self.label_5.setText(_translate("MainWindow", "Имя"))
        self.label_6.setText(_translate("MainWindow", "Отчество"))
        self.label_7.setText(_translate("MainWindow", "Дата рождения"))
        self.label_8.setText(_translate("MainWindow", "Гражданство"))
        self.add_table_path_btn.setText(_translate("MainWindow", "Указать\n""путь к\n""таблице"))
        self.add_manager_btn.setText(_translate("MainWindow", "Добавить\n""менеджера"))
