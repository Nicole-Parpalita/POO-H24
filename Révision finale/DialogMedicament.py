from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import dialog_medicament
import class_Medicament

class FenetreMedicament(QtWidgets.QDialog, dialog_medicament.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre Medicament
        """
        super(FenetreMedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dialog Medicament - dialog_medicament.ui")
