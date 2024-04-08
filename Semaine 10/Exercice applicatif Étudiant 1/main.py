# importer le fichier du ui converti en py
from PyQt5.QtCore import pyqtSlot

import exercice_applicatif

from classe_Etudiant import Etudiant

#Importer le module sys nécessaire à l'exécution.
import sys

#Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (demoQt)         # Nom de mon fichier ui
class demoQt(QtWidgets.QMainWindow, exercice_applicatif.Ui_MainWindow):
    '''
    Nome de la classe : demoQt
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - exercice_applicatif.Ui_MainWindow : Ma classe générée avec QtDesigner
    '''
    def __init__(self, parent=None):
        '''
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et exercice_applicatif.Ui_MainWindow
        '''
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(demoQt, self).__init__(parent)
        self.setupUi(self) #Préparer l'interface utilisateur.

    # Gérer les évènements
    #   on _ nom de mon objet _ nom de l'évènement
    @pyqtSlot()
    def on_pushButton_creer_objet_clicked(self):
        '''
        Gestionnaire d'évènement pour le bouton Créer l'objet
        '''
        try:
            num_etudiant = self.lineEdit_num_etudiant.text()
            nom = self.lineEdit_nom.text()
            prenom = self.lineEdit_prenom.text()
            programme = self.lineEdit_programme.text()

            etudiant = Etudiant(num_etudiant, nom, prenom, programme)
            self.label_affichage.setText(str(etudiant))
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

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
