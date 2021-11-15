import tkinter
# Taille de la fenetre
width_fenetre = "800"
height_fenetre = "600"
taille_images = "200"
# Images du Shi-Fu-Mi
images_ciseaux = tkinter.PhotoImage(file = r"imagesShifumi/ciseauxCouleur.PNG")
images_feuille = tkinter.PhotoImage(file = r"imagesShifumi/feuilleCouleur.PNG")
images_pierre = tkinter.PhotoImage(file = r"imagesShifumi/pierreCouleur.PNG")
images_de_fond = tkinter.PhotoImage(file = r"imagesShifumi/Présentation.PNG")
# Affichage de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Shi-Fu-Mi")
fenetre.geometry(f"{width_fenetre}x{height_fenetre}")
fenetre.resizable(width=False, height=False)
fenetre.configure(background="#A1D2E1") 
fenetre.iconphoto(False, tkinter.PhotoImage(file='imagesShifumi/icone.png'))

# Boutons du Shi-Fu-Mi
boutonCiseaux = tkinter.Button(fenetre,image=images_ciseaux, bd=5, width=taille_images,height=taille_images)
boutonFeuille = tkinter.Button(fenetre,image=images_feuille, bd=5, width=taille_images,height=taille_images)
boutonPierre = tkinter.Button(fenetre,image=images_pierre, bd=5, width=taille_images,height=taille_images)
boutonCiseaux.place(x=50,y=280)
boutonPierre.place(x=300,y=280)
boutonFeuille.place(x=550,y=280)
# Mainloop
fenetre.mainloop()