import boite_dialogue_Ajouter_cours
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import sys
from classe_Cours import Cours

class Fenetre_ajouter_cours(QtWidgets.QDialog, boite_dialogue_Ajouter_cours.Ui_boiteDialog_cours):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui permet d'ajouter des cours
        """
        super(Fenetre_ajouter_cours, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Ajouter un cours")

    @pyqtSlot()
    def on_pushButton_Ajouter_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Ajouter
        """
        try:
            sigle = self.lineEdit_sigle.text()
            nom = self.lineEdit_nom.text()
            nb_heures = self.lineEdit_nb_heures.text()
            if isinstance(sigle, str) and len(sigle) == 5 and sigle[0].isalpha() and isinstance(nom, str) and len(nom) <= 50 and isinstance(nb_heures, int) and nb_heures > 0:
                cours = Cours(sigle, nom, nb_heures)
                Cours.ls_cours.append(cours)
                self.textBrowser.append(str(cours))
            else:
                self.label_message_erreur.setText("Attention : valeurs entrées incorrectes")
                self.lineEdit_sigle.clear()
                self.lineEdit_nom.clear()
                self.lineEdit_nb_heures.clear()
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
