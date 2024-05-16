from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import dialog_medicament
from class_Medicament import Medicament
from class_Antibiotique import Antibiotique
from class_Analgesique import Analgesique
from class_Corticoide import Corticoide

class FenetreMedicament(QtWidgets.QDialog, dialog_medicament.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre Medicament
        """
        super(FenetreMedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dialog Medicament - dialog_medicament.ui")

        self.labelErreur_existe_pas.setVisible(False)
        self.labelErreur_existe.setVisible(False)
        self.labelErreur_code_medicament.setVisible(False)
        self.labelErreur_nom_chimique.setVisible(False)
        self.labelErreur_nom_commercial.setVisible(False)
        self.labelErreur_prix.setVisible(False)
        self.labelErreur_duree_prise_max.setVisible(False)
        self.labelErreur_dose_quot_max.setVisible(False)

        self.lineEdit_duree_prise_max.setEnabled(True)
        self.lineEdit_dose_quot_max.setEnabled(False)
        self.comboBox_effet_medic.setEnabled(False)

        self.comboBox_categorie.currentIndexChanged.connect(self.on_comboBox_categorie_changed)
        self.on_comboBox_categorie_changed()

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        try:
            code_medicament = self.lineEdit_code_medicament.text()
            nom_chimique = self.lineEdit_nom_chimique.text()
            nom_commercial = self.lineEdit_nom_commercial.text()
            prix = float(self.lineEdit_prix.text())
            categorie = self.comboBox_categorie.currentText()

            if not (3 <= len(code_medicament) == 6 and code_medicament[:2].isalpha() and code_medicament[
                                                                                         3:].isnumeric()):
                raise ValueError("Le code de médicament doit être composé de trois lettres suivies de 3 chiffres.")
            if len(nom_chimique) > 50:
                raise ValueError("Le nom chimique doit être composé d'un maximum de 50 caractères.")
            if len(nom_commercial) > 50:
                raise ValueError("Le nom commercial doit être composé d'un maximum de 50 caractères.")
            if not (5 <= prix <= 100):
                raise ValueError("Le prix doit avoir une valeur entre 5$ et 100$.")

            medicament = None

            if categorie == "Antibiotique":
                duree_prise_max = int(self.lineEdit_duree_prise_max.text())
                medicament = Antibiotique(code_medicament, nom_chimique, nom_commercial, prix, categorie, duree_prise_max)
            elif categorie == "Analgésique":
                dose_quot_max = int(self.lineEdit_dose_quot_max.text())
                medicament = Analgesique(code_medicament, nom_chimique, nom_commercial, prix, categorie, dose_quot_max)
            else:
                effet_medic = self.comboBox_effet_medic.currentText()
                medicament = Corticoide(code_medicament, nom_chimique, nom_commercial, prix, categorie, effet_medic)

            print(f"Le médicament {medicament.nom_commercial} a été ajouté avec succès.")

        except ValueError as ve:
            print(f"Une erreur de valeur est survenue: {ve}")

        except Exception as e:
            print(f"Une erreur s'est produite lors de l'ajout du médicament : {e}")

    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        try:
            code_medicament = self.lineEdit_code_medicament.text()
            medicament = None

            # Vérifier dans la liste ls_medicaments de la classe Medicament
            for med in Medicament.ls_medicaments:
                if med.code_medicament == code_medicament:
                    medicament = med
                    break

            # Si le médicament n'est pas trouvé dans la liste Medicament.ls_medicaments
            if not medicament:
                # Vérifier dans la liste ls_medicaments de la classe Antibiotique
                for med in Antibiotique.ls_medicaments:
                    if med.code_medicament == code_medicament:
                        medicament = med
                        break

            # Si le médicament n'est pas trouvé dans la liste Antibiotique.ls_medicaments
            if not medicament:
                # Vérifier dans la liste ls_medicaments de la classe Analgesique
                for med in Analgesique.ls_medicaments:
                    if med.code_medicament == code_medicament:
                        medicament = med
                        break

            # Si le médicament n'est pas trouvé dans la liste Analgesique.ls_medicaments
            if not medicament:
                # Vérifier dans la liste ls_medicaments de la classe Corticoide
                for med in Corticoide.ls_medicaments:
                    if med.code_medicament == code_medicament:
                        medicament = med
                        break

            if medicament:
                print("\n******** Information sur le médicament ********")
                print(f"- Code du médicament: {medicament.code_medicament}\n"
                      f"- Nom chimique: {medicament.nom_chimique}\n"
                      f"- Nom commercial: {medicament.nom_commercial}\n"
                      f"- Prix: {medicament.prix}\n"
                      f"- Catégorie: {medicament.categorie}")

                if isinstance(medicament, Antibiotique):
                    print(f"- Durée prise maximale: {medicament.duree_prise_max}")
                elif isinstance(medicament, Analgesique):
                    print(f"- Dose quotidienne maximale: {medicament.dose_quot_max}")
                elif isinstance(medicament, Corticoide):
                    print(f"- Effet du médicament: {medicament.effet_medic}")
            else:
                print("Le code médicament n'existe pas.")

        except Exception as e:
            print(f"Une erreur s'est produite lors de la recherche du médicament : {e}")

    @pyqtSlot()
    def on_comboBox_categorie_changed(self):
        """
        Gestionnaire d'évènements pour le changement de sélection dans la combobox catégorie
        """
        try:
            print("Changement de catégorie...")
            categorie = self.comboBox_categorie.currentText()

            if categorie == "Antibiotique":
                print("Catégorie : Antibiotique")
                self.lineEdit_duree_prise_max.setEnabled(True)
                self.lineEdit_dose_quot_max.setEnabled(False)
                self.comboBox_effet_medic.setEnabled(False)
            elif categorie == "Analgésique":
                print("Catégorie : Analgésique")
                self.lineEdit_duree_prise_max.setEnabled(False)
                self.lineEdit_dose_quot_max.setEnabled(True)
                self.comboBox_effet_medic.setEnabled(False)
            else:
                print("Catégorie : Autre")
                self.lineEdit_dose_quot_max.setEnabled(False)
                self.comboBox_effet_medic.setEnabled(True)
                self.lineEdit_duree_prise_max.setEnabled(False)
        except Exception as e:
            print(f"Une erreur s'est produite lors de la gestion du changement de catégorie : {e}")
