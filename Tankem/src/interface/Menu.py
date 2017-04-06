## -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import *
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import *
from direct.showbase.Transitions import Transitions

import sys
import common

DAOMap = common.internal.MapDAODTO.DAOMapOracle.DAOmaporacle()
DTOlistmap = DAOMap.read()

class MenuPrincipal(ShowBase):
	def __init__(self):

		#Image d'arrière plan
		self.background=OnscreenImage(parent=render2d, image="../asset/Menu/background.jpg")

		#On dit à la caméra que le dernier modèle doit s'afficher toujours en arrière
		self.baseSort = base.cam.node().getDisplayRegion(0).getSort()
		base.cam.node().getDisplayRegion(0).setSort(20)

		#Titre du jeu
		self.textTitre = OnscreenText(text = "Tank'em!",
									  pos = (0,0.6), 
									  scale = 0.32,
									  fg=(0.8,0.9,0.7,1),
									  align=TextNode.ACenter)

		#Boutons
		btnScale = (0.18,0.18)
		text_scale = 0.12
		borderW = (0.04, 0.04)
		couleurBack = (0.243,0.325,0.121,1)
		separation = 1
		hauteur = -0.6
		itemHeight = 0.11
		numItemsVisible = 50
		itemHeight = 0.11
		
		self.b1 = DirectButton(text = ("Jouer", "Carnage!", "DESTRUCTION", "disabled"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=couleurBack,
						  frameColor=couleurBack,
						  relief=4,
						  textMayChange = 1,
						  pad = (0.35,0),
						  command=self.chargeJeu,
						  pos = (separation,0,hauteur+0.8))



		self.b2 = DirectButton(text = ("Quitter", "Cyka Bliat", "Bye!", "disabled"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=couleurBack,
						  frameColor=couleurBack,
						  relief=4,
						  textMayChange = 1,
						  pad = (0.30,0),
						  command = lambda : sys.exit(),
						  pos = (separation,0,hauteur))
		#Scroll list
		self.scrollList = DirectScrolledList(
							decButton_pos = (0.25,0,0.53),
							decButton_text = "Jouer",
							decButton_text_scale = 0.04,
							decButton_borderWidth = (0.005,0.005),
							decButton_pad = (0.03,0.03),
							frameSize = (-0.2,0.7,-0.5,0.59),
							frameColor=(0,0,0,0),
							pos = (-1,0,0),
							numItemsVisible = numItemsVisible,
							forceHeight = 0.11,
							itemFrame_frameSize = (-0.2,0.7,-0.5,0.59),
							itemFrame_pos = (0,0,0),
		)
		for map in DTOlistmap.getArrayMaps():
			self.name = map.getName()
			self.l = DirectButton(text = self.name, text_scale=0.08,borderWidth = (0.005,0.005),pos = (0,0,0),command = lambda : self.setNiveauChoisi(map.getId()))
			self.scrollList.addItem(self.l)
		
		#Initialisation de l'effet de transition
		curtain = loader.loadTexture("../asset/Menu/load.png")

		self.transition = Transitions(loader)
		self.transition.setFadeColor(0, 0, 0)
		self.transition.setFadeModel(curtain)

		self.sound = loader.loadSfx("../asset/Menu/shotgun.mp3")

	def cacher(self):
			#Est esssentiellement un code de "loading"

			#On remet la caméra comme avant
			base.cam.node().getDisplayRegion(0).setSort(self.baseSort)
			#On cache les menus
			self.background.hide()
			self.b1.hide()
			self.b2.hide()
			self.scrollList.hide()
			self.textTitre.hide()

	def setNiveauChoisi(self,idNiveau):
			idNiveauChoisi = idNiveau
			self.chargeJeu()

	def chargeJeu(self):
			#On démarre!
			Sequence(Func(lambda : self.transition.irisOut(0.2)),
					 SoundInterval(self.sound),
					 Func(self.cacher),
					 Func(lambda : messenger.send("DemarrerPartie")),
					 Wait(0.2), #Bug étrange quand on met pas ça. L'effet de transition doit lagger
					 Func(lambda : self.transition.irisIn(0.2))
			).start()
			