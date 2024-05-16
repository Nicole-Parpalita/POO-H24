from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import dialog_medicament
import class_Medicament
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
    def on_pushButton_ajouter(self):
        """
        Gestionnaire d'évènements pour le bouton Ajouter
        """
        code_medicament = self.lineEdit_code_medicament.text()
        nom_chimique = self.lineEdit_nom_chimique.text()
        nom_commercial = self.lineEdit_nom_commercial.text()
        prix = self.lineEdit_prix.text()
        categorie = self.comboBox_categorie.currentText()
        medicament = None

        if categorie == "Antibiotique":
            medicament = Antibiotique()
            medicament.code_medicament = code_medicament
            if medicament.code_medicament != code_medicament:
                self.labelErreur_existe_pas.setVisible(True)
                self.labelErreur_code_medicament.setVisible(True)
                self.lineEdit_code_medicament.clear()
            medicament.nom_chimique = nom_chimique
            if medicament.nom_chimique != nom_chimique:
                self.labelErreur_nom_chimique.setVisible(True)
                self.lineEdit_nom_chimique.clear()
            medicament.prix = prix
            if medicament.prix != prix:
                self.labelErreur_prix.setVisible(True)
                self.lineEdit_prix.clear()
            duree_prise_max = self.lineEdit_duree_prise_max.text()
            medicament.duree_prise_max = duree_prise_max
            if medicament.duree_prise_max != duree_prise_max:
                self.labelErreur_duree_prise_max.setVisible(True)
                self.lineEdit_duree_prise_max.clear()
            if (medicament.code_medicament == code_medicament and medicament.nom_chimique == nom_chimique and
                    medicament.prix == prix and medicament.duree_prise_max == duree_prise_max):
                class_Medicament.Medicament.ls_medicaments.append(medicament)
                print("Le médicament à été ajouté de type antibiotique.")
        elif categorie == "Analgésique":
            self.lineEdit_duree_prise_max.setEnabled(False)
            self.lineEdit_dose_quot_max.setEnabled(True)
            medicament = Analgesique()
            medicament.code_medicament = code_medicament
            if medicament.code_medicament != code_medicament:
                self.labelErreur_existe_pas.setVisible(True)
                self.labelErreur_code_medicament.setVisible(True)
                self.lineEdit_code_medicament.clear()
            medicament.nom_chimique = nom_chimique
            if medicament.nom_chimique != nom_chimique:
                self.labelErreur_nom_chimique.setVisible(True)
                self.lineEdit_nom_chimique.clear()
            medicament.prix = prix
            if medicament.prix != prix:
                self.labelErreur_prix.setVisible(True)
                self.lineEdit_prix.clear()
            dose_quot_max = self.lineEdit_dose_quot_max.text()
            medicament.dose_quot_max = dose_quot_max
            if medicament.dose_quot_max != dose_quot_max:
                self.labelErreur_dose_quot_max.setVisible(True)
                self.lineEdit_dose_quot_max.clear()
            if (medicament.code_medicament == code_medicament and medicament.nom_chimique == nom_chimique and
                    medicament.prix == prix and medicament.dose_quot_max == dose_quot_max):
                class_Medicament.Medicament.ls_medicaments.append(medicament)
                print("Le médicament à été ajouté de type analgésique.")
        else:
            self.lineEdit_dose_quot_max.setEnabled(False)
            self.comboBox_effet_medic.setEnabled(True)
            medicament = Corticoide()
            if medicament.code_medicament != code_medicament:
                self.labelErreur_existe_pas.setVisible(True)
                self.labelErreur_code_medicament.setVisible(True)
                self.lineEdit_code_medicament.clear()
            medicament.nom_chimique = nom_chimique
            if medicament.nom_chimique != nom_chimique:
                self.labelErreur_nom_chimique.setVisible(True)
                self.lineEdit_nom_chimique.clear()
            medicament.prix = prix
            if medicament.prix != prix:
                self.labelErreur_prix.setVisible(True)
                self.lineEdit_prix.clear()
            effet_medic = self.comboBox_effet_medic.currentText()
            if (medicament.code_medicament == code_medicament and medicament.nom_chimique == nom_chimique and
                    medicament.prix == prix and medicament.effet_medic == effet_medic):
                class_Medicament.Medicament.ls_medicaments.append(medicament)
                print("Le médicament à été ajouté de type coticoïde.")

    @pyqtSlot()
    def on_comboBox_categorie_changed(self):
        """
        Gestionnaire d'évènements pour le changement de sélection dans la combobox catégorie
        """
        categorie = self.comboBox_categorie.currentText()

        if categorie == "Antibiotique":
            self.lineEdit_duree_prise_max.setEnabled(True)
            self.lineEdit_dose_quot_max.setEnabled(False)
            self.comboBox_effet_medic.setEnabled(False)
        elif categorie == "Analgésique":
            self.lineEdit_duree_prise_max.setEnabled(False)
            self.lineEdit_dose_quot_max.setEnabled(True)
            self.comboBox_effet_medic.setEnabled(False)
        else:
            self.lineEdit_dose_quot_max.setEnabled(False)
            self.comboBox_effet_medic.setEnabled(True)
            self.lineEdit_duree_prise_max.setEnabled(False)