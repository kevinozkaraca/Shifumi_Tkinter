import tkinter
from typing import get_origin
# Taille des éléments
width_fenetre = "800"
height_fenetre = "600"
taille_images = "200"
# Affichage de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Shi-Fu-Mi")
fenetre.geometry(f"{width_fenetre}x{height_fenetre}")
fenetre.resizable(width=False, height=False)
fenetre.configure(background="#A1D2E1")
fenetre.iconphoto(False, tkinter.PhotoImage(file=r"imagesShifumi/icone.png"))
# Images du Shi-Fu-Mi
image_CPU =     [   tkinter.PhotoImage(file=r"imagesShifumi/CPU.PNG"),
                    tkinter.PhotoImage(file=r"imagesShifumi/ciseauxCPU.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/feuilleCPU.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/pierreCPU.png"),
                    ]
image_ciseaux = [   tkinter.PhotoImage(file=r"imagesShifumi/ciseauxCouleur.PNG"),
                    tkinter.PhotoImage(file=r"imagesShifumi/ciseauxLoose.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/ciseauxWin.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/ciseauxNoir.png"),
                    ]
image_feuille = [   tkinter.PhotoImage(file=r"imagesShifumi/feuilleCouleur.PNG"),
                    tkinter.PhotoImage(file=r"imagesShifumi/feuilleLoose.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/feuilleWin.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/feuilleNoir.png"),
                    ]
image_pierre = [    tkinter.PhotoImage(file=r"imagesShifumi/pierreCouleur.PNG"),
                    tkinter.PhotoImage(file=r"imagesShifumi/pierreLoose.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/pierreWin.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/pierreNoir.png"),
                    ]
image_de_fond =     tkinter.PhotoImage(file=r"imagesShifumi/Présentation.png")
#Logique du jeu
def bouton0():
    print("Bouton 0 Actif")
    global boutonFeuille
    global boutonPierre
    global boutonCiseaux
    boutonCiseaux = tkinter.Button(fenetre, 
                               image=image_ciseaux[0], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton0
                            )
    boutonFeuille = tkinter.Button(fenetre, 
                               image=image_feuille[3], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton1
                            )
    boutonPierre = tkinter.Button(fenetre, 
                              image=image_pierre[3], 
                              bd=5, 
                              width=taille_images, 
                              height=taille_images,
                              command=bouton2
                            )
    boutonCiseaux.place(x = 80, y = 255)
    boutonPierre.place(x = 300, y = 255)
    boutonFeuille.place(x = 520, y = 255)
def bouton1():
    print("Bouton 0 Actif")
    global boutonFeuille
    global boutonPierre
    global boutonCiseaux
    boutonCiseaux = tkinter.Button(fenetre, 
                               image=image_ciseaux[3], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton0
                            )
    boutonFeuille = tkinter.Button(fenetre, 
                               image=image_feuille[0], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton1
                            )
    boutonPierre = tkinter.Button(fenetre, 
                              image=image_pierre[3], 
                              bd=5, 
                              width=taille_images, 
                              height=taille_images,
                              command=bouton2
                            )
    boutonCiseaux.place(x = 80, y = 255)
    boutonPierre.place(x = 300, y = 255)
    boutonFeuille.place(x = 520, y = 255)
def bouton2():
    print("Bouton 0 Actif")
    global boutonFeuille
    global boutonPierre
    global boutonCiseaux
    boutonCiseaux = tkinter.Button(fenetre, 
                               image=image_ciseaux[3], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton0
                            )
    boutonFeuille = tkinter.Button(fenetre, 
                               image=image_feuille[3], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton1
                            )
    boutonPierre = tkinter.Button(fenetre, 
                              image=image_pierre[0], 
                              bd=5, 
                              width=taille_images, 
                              height=taille_images,
                              command=bouton2
                            )
    boutonCiseaux.place(x = 80, y = 255)
    boutonPierre.place(x = 300, y = 255)
    boutonFeuille.place(x = 520, y = 255)
# Boutons du Shi-Fu-Mi
fond_de_shifumi = tkinter.Label( fenetre, image = image_de_fond) 
fond_de_shifumi.place(x = 0, y = 0)
image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[0]) 
image_CPUchoix.place(x = 630, y = 480)
boutonCiseaux = tkinter.Button(fenetre, 
                               image=image_ciseaux[0], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton0
                            )
boutonFeuille = tkinter.Button(fenetre, 
                               image=image_feuille[0], 
                               bd=5, 
                               width=taille_images, 
                               height=taille_images,
                               command=bouton1
                            )
boutonPierre = tkinter.Button(fenetre, 
                              image=image_pierre[0], 
                              bd=5, 
                              width=taille_images, 
                              height=taille_images,
                              command=bouton2
                            )
boutonCiseaux.place(x = 80, y = 255)
boutonPierre.place(x = 300, y = 255)
boutonFeuille.place(x = 520, y = 255)
# Mainloop
fenetre.mainloop()
