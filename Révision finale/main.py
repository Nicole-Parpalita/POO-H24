from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import mainWindow_pharmacie
from DialogMedicament import FenetreMedicament
from DialogPatient import FenetrePatient
from Dialog_Recherche import FenetreRecherche
from DialogFournisseur import FenetreFournisseur


class demoQt(QtWidgets.QMainWindow, mainWindow_pharmacie.Ui_MainWindow):
    """
    Nom de la classe : demoQt
    Héritages:
    - QtWidgets.QMainWindow : Type d'interface créée par QtDesigner
    - mainWindow_pharmacie.Ui_MainWindow : Ma classe générée par QtDesigner
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe demoQt
        :param parent: QtWidgets.QMainWindow et mainWindow_pharmacie.Ui_MainWindow
        """
        super(demoQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion de la pharmacie Healthcaere - MainWindow_pharmacie.ui")

    @pyqtSlot()
    def on_pushButton_medicament_clicked(self):
        """
        Gestionaire d'évènements pour le bouton Médicament
        """
        dialog = FenetreMedicament()
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_patient_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Patient
        """
        dialog = FenetrePatient()
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Rechercher
        """
        dialog = FenetreRecherche()
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_fournisseur_clicked(self):
        """
        Gestionnaire d'évènements pour le bouton Fournisseur
        """
        dialog = FenetreFournisseur()
        dialog.show()
        dialog.exec_()


if __name__ == '__main__':
    # Créer une instance de l'application
    app = QtWidgets.QApplication(sys.argv)

    # Créer une instance de votre classe principale
    main_window = demoQt()

    # Afficher la fenêtre principale
    main_window.show()

    # Lancer la boucle d'événements de l'application
    sys.exit(app.exec_())