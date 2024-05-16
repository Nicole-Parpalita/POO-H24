from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
import dialog_fournisseur
import class_Fournisseur
from class_Patient import Patient
import os

class FenetreFournisseur(QtWidgets.QDialog, dialog_fournisseur.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre Fournisseur
        """
        super(FenetreFournisseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dialog Fournisseur - dialog_fournisseur.ui")
        self.labelErreur_code_fournisseur.setVisible(False)
        self.labelErreur_nom_compagnie.setVisible(False)

        try:
            self.comboBox_patient.addItems([str(patient.num_patient) for patient in Patient.ls_patients])
        except Exception as e:
            print(f"Une erreur s'est produite lors du remplissage de la combobox des patients : {str(e)}")

        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_ajouter_listview_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Ajouter le patient au listview
        """
        try:
            nom_fournisseur = self.lineEdit_nom_compagnie.text()

            fournisseur = None

            print("Début de l'ajout des patients à la listView")

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
            print(f"Une erreur s'est produite lors de l'ajout des patients à la listView : {str(e)}")

    @pyqtSlot()
    def on_pushButton_serialiser_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Sérialiser fournisseur
        """
        try:
            # Récupérer les valeurs des champs de saisie
            code_fournisseur = self.lineEdit_code_fournisseur.text()
            nom_compagnie = self.lineEdit_nom_compagnie.text()
            num_patient = self.comboBox_patient.currentText()

            # Vérifier la validité des valeurs entrées
            if len(code_fournisseur) != 6 or not code_fournisseur.startswith("F") or not code_fournisseur[1:].isdigit():
                self.labelErreur_code_fournisseur.setVisible(True)
                return

            if len(nom_compagnie) > 30 or not nom_compagnie.isalnum():
                self.labelErreur_nom_compagnie.setVisible(True)
                return

            # Ajouter le fournisseur à la liste des fournisseurs
            fournisseur = class_Fournisseur.Fournisseur(code_fournisseur, nom_compagnie,
                                                        [patient for patient in Patient.ls_patients if
                                                         patient.num_patient == int(num_patient)])
            class_Fournisseur.Fournisseur.ls_fournisseurs.append(fournisseur)

            # Sérialiser le fournisseur dans un fichier JSON
            fichier_json = f"{code_fournisseur}.json"
            fournisseur.serialiserFournisseur(fichier_json)
        except Exception as e:
            print(f"Une erreur s'est produite lors de la sérialisation du fournisseur : {str(e)}")

    @pyqtSlot()
    def on_pushButton_deserialiser_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Désérialiser fournisseur
        """
        try:
            code_fournisseur = self.lineEdit_code_fournisseur.text()
            fichier_json = f"{code_fournisseur}.json"

            if not os.path.exists(fichier_json):
                print("Le fichier JSON n'existe pas.")
                return

            fournisseur = class_Fournisseur.Fournisseur.deserialiserFournisseur(fichier_json)

            for patient in fournisseur.ls_patients:
                item = QtGui.QStandardItem(str(patient.num_patient))
                self.model.appendRow(item)

        except Exception as e:
            print(f"Une erreur s'est produite lors de la désérialisation du fournisseur : {str(e)}")