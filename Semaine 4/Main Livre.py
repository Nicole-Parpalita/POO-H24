from Livre import Livre

if __name__ == '__main__':

    livre = Livre()
    ls_livres = []

    while True:
        try:
            input("Quel est l'ISBN du livre? ")
            livre._id_unique = ""
