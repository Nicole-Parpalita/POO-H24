# importer le fichier du ui converti en py
from PyQt5.QtCore import pyqtSlot

import interface_gestion

from classe_Etudiant import Etudiant

#Importer le module sys nécessaire à l'exécution.
import sys

#Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

from boite_dialogue_Ajouter_cours import Ui_boiteDialog_cours

from ajouter_cours_dialog import Fenetre_ajouter_cours

# créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (demoQt)         # Nom de mon fichier ui
class demoQt(QtWidgets.QMainWindow, interface_gestion.Ui_MainWindow):
    '''
    Nome de la classe : demoQt
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - exercice_applicatif.Ui_MainWindow : Ma classe générée avec QtDesigner
    '''
    def __init__(self, parent=None):
        '''
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interface_gestion.Ui_MainWindow
        '''
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(demoQt, self).__init__(parent)
        self.setupUi(self) #Préparer l'interface utilisateur.

    # Gérer les évènements
    #   on _ nom de mon objet _ nom de l'évènement
    @pyqtSlot()
    def on_pushButton_Ajouter_clicked(self):
        '''
        Gestionnaire d'évènement pour le bouton Valider
        '''
        try:
            num_etudiant = self.lineEdit_num_etudiant.text()
            nom = self.lineEdit__nom_etudiant.text()
            programme = self.comboBox.currentText()
            date_naissance = self.dateEdit.date().toPyDate()
            if num_etudiant.isdigit() and len(str(num_etudiant)) == 7 and isinstance(nom, str):
                etudiant = Etudiant(num_etudiant, nom, programme, date_naissance)
                Etudiant.ls_etudiants.append(etudiant)
                self.textBrowser.append(str(etudiant))
            else:
                self.label_message_erreur.setText("Attention : valeurs entrées incorrectes !")
                self.lineEdit_num_etudiant.clear()
                self.lineEdit__nom_etudiant.clear()
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    @pyqtSlot()
    def on_comboBox_changed(self):
        """
        Gestionnaire d'évènement pour le changement de sélection dans le combo box
        """
        try:
            programme = self.comboBox.currentText()
            print(programme)
            if Etudiant.ls_etudiants:
                etudiant = Etudiant.ls_etudiants[-1]
                etudiant.programme = programme
                print(etudiant)
                self.textBrowser.append(str(etudiant))
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

    @pyqtSlot()
    def on_pushButton_Modifier_clicked(self):
        """
        Gestionnaire d'évènements si la bouton Modifier est cliqué
        """
        try:
            num_etudiant = self.lineEdit_num_etudiant.text()
            nouveau_nom = self.lineEdit__nom_etudiant.text()
            nouveau_programme = self.comboBox.currentText()
            etudiant = Etudiant.chercher_etudiant(num_etudiant)
            if etudiant:
                if nouveau_nom:
                    etudiant.nom = nouveau_nom
                if nouveau_programme:
                    etudiant.programme = nouveau_programme
                self.textBrowser.clear()
                for etudiant in Etudiant.ls_etudiants:
                    self.textBrowser.append(str(etudiant))
                self.label_message_erreur.setText("Étudiant modifié avec succès !")
            else:
                self.label_message_erreur.setText("Aucun étudiant trouvé...")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

    @pyqtSlot()
    def on_pushButton_Supprimer_clicked(self):
        """
        Gestionnaire d'évènements si le bouton Supprimer est cliqué
        """
        try:
            num_etudiant = self.lineEdit_num_etudiant.text()
            etudiant = Etudiant.chercher_etudiant(num_etudiant)
            if etudiant:
                Etudiant.ls_etudiants.remove(etudiant)
                self.textBrowser.clear()
                for etudiant in Etudiant.ls_etudiants:
                    self.textBrowser.append(str(etudiant))
                self.label_message_erreur.setText("Étudiant supprimé avec succès !")
            else:
                self.label_message_erreur.setText("Aucun étudiant trouvé...")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

    @pyqtSlot()
    def on_pushButton_Sauvegarder_clicked(self):
        """
        Gestionnaire d'évènements si le bouton Sauvegarder est cliqué
        """
        try:
            contenu_texte = self.textBrowser.toPlainText()
            with open("liste_etudiants.txt", "w", encoding="utf-8") as f:
                f.write(contenu_texte)
            self.label_message_erreur.setText("Contenu sauvegardé avec succès !")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

    @pyqtSlot()
    def on_pushButton_Creer_cours_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Creer cours
        """
        dialog = Fenetre_ajouter_cours()
        dialog.show()
        dialog.exec()

# Créer le main qui lance la fenêtre de Qt
def main():
    '''
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = demoQt() #Nom de ma classe
    form.show()
    app.exec()

if __name__ == "__main__":
    main()
