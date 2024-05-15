from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import dialog_patient
import class_Patient

class FenetrePatient(QtWidgets.QDialog, dialog_patient.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre Patient
        """
        super(FenetrePatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dialog Patient - dialog_patient.ui")

        self.labelErreur_num_patient = self.labelErreur_num_patient
        self.labelErreur_date_naissance = self.labelErreur_date_naissance
        self.labelErreur_existe = self.labelErreur_existe
        self.labelErreur_nom = self.labelErreur_nom
        self.labelErreur_prenom = self.labelErreur_prenom
        self.labelErreur_existe_pas = self.labelErreur_existe_pas

        self.labelErreur_num_patient.setVisible(False)
        self.labelErreur_date_naissance.setVisible(False)
        self.labelErreur_existe.setVisible(False)
        self.labelErreur_nom.setVisible(False)
        self.labelErreur_prenom.setVisible(False)
        self.labelErreur_existe_pas.setVisible(False)

    @pyqtSlot()
    def on_pushButton_ajouter_patient_clicked(self):
        """
        Gestionnaire d'évènements du bouton Ajouter patient
        """
        from datetime import datetime

        try:
            num_patient = self.lineEdit_num_patient.text().strip()
            nom_patient = self.lineEdit_nom_patient.text().strip().capitalize()
            prenom_patient = self.lineEdit_prenom_patient.text().strip().capitalize()
            date_naissance = self.dateEdit.date().toPyDate()

            try:
                if not num_patient.isdigit() or len(num_patient) != 7 or num_patient[0] in [0, 2, 4, 6, 8]:
                    self.labelErreur_num_patient.setVisible(True)
                    self.lineEdit_num_patient.clear()
                    return

                if class_Patient.Patient.ls_patients:
                    for patient in class_Patient.Patient.ls_patients:
                        if num_patient == patient.num_patient:
                            self.labelErreur_existe.setVisible(True)
                            self.lineEdit_num_patient.clear()
                            return

                if len(nom_patient) > 50:
                    self.labelErreur_nom.setVisible(True)
                    self.lineEdit_nom_patient.clear()
                    return

                if len(prenom_patient) > 50:
                    self.labelErreur_prenom.setVisible(True)
                    self.lineEdit_prenom_patient.clear()
                    return

                if date_naissance > datetime.now().date():
                    self.labelErreur_date_naissance.setVisible(True)
                    self.dateEdit.clear()
                    return

                patient = class_Patient.Patient(num_patient, nom_patient, prenom_patient, date_naissance)
                class_Patient.Patient.ls_patients.append(patient)
                print("Patient ajouté avec succès.")

            except ValueError as e:
                print(f"Erreur de conversion de données : {e}")

        except Exception as ex:
            print(f"Une erreur s'est produite lors de l'ajout du patient : {ex}")

    @pyqtSlot()
    def on_pushButton_supprimer_patient_clicked(self):
        """
        Gestionnaire d'évènements du bouton Supprimer patient
        """
        num_patient = self.lineEdit_num_patient.text().strip()

        try:
            # Vérifier si le numéro de patient est valide
            if not num_patient.isdigit() or len(num_patient) != 7 or num_patient[0] in [0, 2, 4, 6, 8]:
                self.labelErreur_num_patient.setVisible(True)
                self.lineEdit_num_patient.clear()
                return

            # Vérifier si le patient existe dans la liste
            patient_trouve = None
            for patient in class_Patient.Patient.ls_patients:
                if num_patient == patient.num_patient:
                    patient_trouve = patient
                    break

            if patient_trouve is None:
                self.labelErreur_existe_pas.setVisible(True)
                self.lineEdit_num_patient.clear()
                return

            # Supprimer le patient de la liste
            class_Patient.Patient.ls_patients.remove(patient_trouve)
            print("Patient supprimé avec succès.")

        except Exception as ex:
            print(f"Une erreur s'est produite lors de la suppression du patient : {ex}")
