from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel

import boite_associer_cours
from classe_Etudiant import Etudiant
from classe_Cours import Cours

class Fenetreassociercours(QtWidgets.QDialog, boite_associer_cours.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui permet d'associer des cours à des étudiant
        """
        super(Fenetreassociercours, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Associer cours")
        for elt in Etudiant.ls_etudiants:
            self.comboBox_etudiant.addItem(elt.num_etudiant)
        for elt in Cours.ls_courses:
            self.comboBox_cours.addItem(elt.sigle)

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènements si le bouton ajouter est appuyé
        """
        etudiant_index = self.comboBox_etudiant.currentIndex()
        cours_index = self.comboBox_cours.currentIndex()

        if etudiant_index == -1 or cours_index == -1:
            return

        etudiant = Etudiant.ls_etudiants[etudiant_index]
        cours = Cours.ls_cours[cours_index]

        item = QStandardItem(f"{cours.sigle}")
        self.model.appendRow(item)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Gestionnaire d'évènements pout le bouton Associer
        """
        etudiant_index = self.comboBox_etudiant.currentIndex()
        cours_index = self.comboBox_cours.currentIndex()

        if etudiant_index == -1  or cours_index == -1:
            return

        etudiant = Etudiant.ls_etudiants[etudiant_index]
        cours = Cours.ls_cours[cours_index]

        etudiant.cours.remove(cours)

        self.model.clear()
        for cours_etudiant in etudiant.ls_cours:
            item = QStandardItem(f"{cours_etudiant.sigle}")
            self.model.appendRow(item)