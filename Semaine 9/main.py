# importer le fichier du ui converti en py
import mon_interface_graphique

#Importer le module sys nécessaire à l'exécution.
import sys

#Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets

# créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (demoQt)         # Nom de mon fichier ui
class demoQt(QtWidgets.QMainWindow, mon_interface_graphique.Ui_MainWindow):
    '''
    Nome de la classe : demoQt
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - code_interface_genere.Ui_MainWindow : Ma classe générée avec QtDesigner
    '''
    def __init__(self, parent=None):
        '''
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et code_interface_genere.Ui_MainWindow
        '''
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(demoQt, self).__init__(parent)
        self.setupUi(self) #Préparer l'interface utilisateur.

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
