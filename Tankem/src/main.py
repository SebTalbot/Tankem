## -*- coding: utf-8 -*-
#Ajout des chemins vers les librarires
from util import inclureCheminCegep
import sys
# from Menu import MenuPrincipal
#TEST

#Importe la configuration de notre jeu
from panda3d.core import loadPrcFile
loadPrcFile("config/ConfigTankem.prc")

#Module de Panda3DappendObject
from direct.showbase.ShowBase import ShowBase
from interface import *
#Modules internes

from gameLogic import GameLogic

#Tests de Nicolas


class Tankem(ShowBase):
	def __init__(self):

		ShowBase.__init__(self)
		# settings.init()
		self.demarrer()
	

	def demarrer(self):
<<<<<<< HEAD
=======
		# self.daoJoueur = common.internal.UtilisateursDAODTO.DAOutilisateur.DAOutilisateur()
		# self.joueur = self.daoJoueur.read("Test2","AAAaaa111")
		
>>>>>>> a3b58809d5c12953ce2c075359d3e764cbf86fa2
		self.gameLogic = GameLogic(self)
		#Commenter/décommenter la ligne de votre choix pour démarrer le jeu
		#Démarre dans le menu
		self.menuPrincipal = MenuPrincipal(self.gameLogic)
		#Démarre directement dans le jeu
		#messenger.send("DemarrerPartie")

#Main de l'application.. assez simple!
app = Tankem()
app.run()