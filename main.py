import tkinter
# Taille de la fenetre
width_fenetre = "800"
height_fenetre = "600"
taille_images = "200"

# Affichage de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Shi-Fu-Mi")
fenetre.geometry(f"{width_fenetre}x{height_fenetre}")
fenetre.resizable(width=False, height=False)
fenetre.configure(background="#A1D2E1")
# Images du Shi-Fu-Mi
imagesCiseaux = tkinter.PhotoImage(file = r"imagesShifumi/ciseauxCouleur.PNG")
imagesFeuille = tkinter.PhotoImage(file = r"imagesShifumi/feuilleCouleur.PNG")
imagesPierre = tkinter.PhotoImage(file = r"imagesShifumi/pierreCouleur.PNG")
# Boutons du Shi-Fu-Mi
boutonCiseaux = tkinter.Button(fenetre,image=imagesCiseaux, bd=5, width=taille_images,height=taille_images)
boutonFeuille = tkinter.Button(fenetre,image=imagesFeuille, bd=5, width=taille_images,height=taille_images)
boutonPierre = tkinter.Button(fenetre,image=imagesPierre, bd=5, width=taille_images,height=taille_images)
boutonCiseaux.place(x=50,y=100)
boutonPierre.place(x=300,y=100)
boutonFeuille.place(x=550,y=100)
# Mainloop
fenetre.mainloop()