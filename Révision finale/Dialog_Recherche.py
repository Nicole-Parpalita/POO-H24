from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import pyqtSlot
import dialogRecherche
import class_Fournisseur

class FenetreRecherche(QtWidgets.QDialog, dialogRecherche.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre Recherche
        """
        super(FenetreRecherche, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dialog Recherche - dialogRecherche.ui")

        for fournisseur in class_Fournisseur.Fournisseur.ls_fournisseurs:
            self.comboBox_nom_fournisseur.addItem(fournisseur.nom_compagnie)

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_afficher_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Afficher
        """
        try:
            # Récupérer le nom du fournisseur sélectionné dans comboBox_nom_fournisseur
            nom_fournisseur = self.comboBox_nom_fournisseur.currentText()

            # Rechercher le fournisseur correspondant dans la liste des fournisseurs
            fournisseur = None
            for f in class_Fournisseur.Fournisseur.ls_fournisseurs:
                if f.nom_compagnie == nom_fournisseur:
                    fournisseur = f
                    break

            if fournisseur:
                for patient in fournisseur.ls_patients:
                    item = QtGui.QStandardItem(str(patient.num_patient))
                    self.model.appendRow(item)
            else:
                item = QtGui.QStandardItem("Aucun fournisseur trouvé avec ce nom.")
                self.model.appendRow(item)
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'affichage des patients : {str(e)}")
