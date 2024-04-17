from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import listview_dialogue

class FenetreListView(QtWidgets.QDialog, listview_dialogue.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(FenetreListView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiants/étudiantes")

    @pyqtSlot()
    def on_pushButton_Quitter_clicked(self):
        self.close()