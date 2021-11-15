import tkinter
# Taille des éléments
width_fenetre = "800"
height_fenetre = "600"
taille_images = "150"
# Affichage de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Shi-Fu-Mi")
fenetre.geometry(f"{width_fenetre}x{height_fenetre}")
fenetre.resizable(width=False, height=False)

fenetre.configure(background="#A1D2E1")
fenetre.iconphoto(False, tkinter.PhotoImage(file=r"imagesShifumi/icone.png"))
# Images du Shi-Fu-Mi
image_ciseaux = tkinter.PhotoImage(file=r"imagesShifumi/ciseauxCouleur.png")
image_feuille = tkinter.PhotoImage(file=r"imagesShifumi/feuilleCouleur.png")
image_pierre = tkinter.PhotoImage(file=r"imagesShifumi/pierreCouleur.png")
image_de_fond = tkinter.PhotoImage(file=r"imagesShifumi/Présentation.png")
# Boutons du Shi-Fu-Mi
fond_de_shifumi = tkinter.Label( fenetre, image = image_de_fond) 
fond_de_shifumi.place(x = 0, y = 0)
boutonCiseaux = tkinter.Button(fenetre, image=image_ciseaux, bd=5, width=taille_images, height=taille_images)
boutonFeuille = tkinter.Button(fenetre, image=image_feuille, bd=5, width=taille_images, height=taille_images)
boutonPierre = tkinter.Button(fenetre, image=image_pierre, bd=5, width=taille_images, height=taille_images)
boutonCiseaux.place(x=88, y=240)
boutonPierre.place(x=324, y=240)
boutonFeuille.place(x=561, y=240)

# Mainloop
fenetre.mainloop()
