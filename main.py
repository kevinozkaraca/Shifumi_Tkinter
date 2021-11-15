import tkinter
from typing import get_origin
import random
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
image_CPU =     [   tkinter.PhotoImage(file=r"imagesShifumi/ciseauxCPU.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/feuilleCPU.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/pierreCPU.png"),
                    tkinter.PhotoImage(file=r"imagesShifumi/CPU.PNG"),
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
choixDuJoueur = -1
def bouton0():
    global choixDuJoueur
    choixDuJoueur = 0
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
    choixCPUcompare()
def bouton1():
    global choixDuJoueur
    choixDuJoueur = 1
    print("Bouton 1 Actif")
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
    choixCPUcompare()
def bouton2():
    global choixDuJoueur
    choixDuJoueur = 2
    print("Bouton 2 Actif")
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
    choixCPUcompare()
# Possibilités aléatoires
def choixCPUcompare():
    for i in range(1):
        i = random.randint(0, 2)
        print(i)
    choixCPU = i
    if choixDuJoueur == choixCPU :
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixDuJoueur]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 0 & choixCPU == 1:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 0 & choixCPU == 2:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 1 & choixCPU == 0:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 1 & choixCPU == 2:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 2 & choixCPU == 0:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)
    elif choixDuJoueur == 2 & choixCPU == 1:
        image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[choixCPU]) 
        image_CPUchoix.place(x = 630, y = 480)     
# Boutons du Shi-Fu-Mi
fond_de_shifumi = tkinter.Label( fenetre, image = image_de_fond) 
fond_de_shifumi.place(x = 0, y = 0)
image_CPUchoix = tkinter.Label( fenetre, image = image_CPU[3]) 
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
