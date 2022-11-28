import sys

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow
from accessify import private

from View.AddBranchWindow import Ui_Dialog_Add_Branch
from View.AddManagerWindow import Ui_Dialog_Add_Manager
from View.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.create_form_btn.clicked.connect(self.create_form)
        self.ui.add_table_path_btn.clicked.connect(self.open_file_name_dialog)
        self.ui.add_manager_btn.clicked.connect(self.add_manager_dialog)
        self.ui.add_branch_btn.clicked.connect(self.add_branch_dialog)

    @private
    def add_manager_dialog(self):
        add_manager = AddManagerDialogWindow()
        add_manager.show()
        add_manager.exec_()

    @private
    def add_branch_dialog(self):
        add_branch = AddBranchDialogWindow()
        add_branch.show()
        add_branch.exec_()

    @private
    def create_form(self):
        pass  # todo: дописать логику

    @private
    def open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path_selected_file, _ = QFileDialog.getOpenFileName(self,
                                                            "Выберите файл (таблицу)",
                                                            "",
                                                            "Excel Files (*.xls *.xlsm *.xlsx);;All Files (*)",
                                                            # ;;Python Files (*.py)
                                                            options=options)
        # todo: сохранить путь к файлу


class AddManagerDialogWindow(QDialog):
    def __init__(self):
        super(AddManagerDialogWindow, self).__init__()
        self.ui = Ui_Dialog_Add_Manager()
        self.ui.setupUi(self)
        self.ui.buttonBox_new_manager.accepted.connect(self.ok_accept_manager_dialog)
        self.ui.buttonBox_new_manager.rejected.connect(self.cancel_accept_manager_dialog)

    @private
    def ok_accept_manager_dialog(self):
        pass  # todo: дописать логику

    @private
    def cancel_accept_manager_dialog(self):
        pass  # todo: дописать логику


class AddBranchDialogWindow(QDialog):
    def __init__(self):
        super(AddBranchDialogWindow, self).__init__()
        self.ui = Ui_Dialog_Add_Branch()
        self.ui.setupUi(self)

        self.ui.buttonBox_new_branch.accepted.connect(self.ok_accept_branch_dialog)
        self.ui.buttonBox_new_branch.rejected.connect(self.cancel_accept_branch_dialog)

    @private
    def ok_accept_branch_dialog(self):
        pass  # TODO: дописать логику

    @private
    def cancel_accept_branch_dialog(self):
        pass  # TODO: дописать логику


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
