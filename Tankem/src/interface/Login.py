## -*- coding: utf-8 -*-
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
from pandac.PandaModules import *
from direct.interval.LerpInterval import *
from direct.interval.IntervalGlobal import *
from direct.showbase.Transitions import Transitions
import webbrowser
import random
import sys
import common
import SingletonDBConnection
DAOMap = common.internal.MapDAODTO.DAOMapOracle.DAOmaporacle()
DTOlistmap = DAOMap.read()

class MenuLogin(ShowBase):
	def __init__(self, gameLogic,mapID,mapName):
		self.gameLogic = gameLogic
		self.mapID = mapID
		self.mapName = mapName
		self.user = common.internal.UtilisateursDAODTO.DAOutilisateur.DAOutilisateur()
		self.wait = True
		#Image d'arrière plan
		self.background=OnscreenImage(parent=render2d, image="../asset/Menu/BackgroundLogin.jpg")

		#On dit à la caméra que le dernier modèle doit s'afficher toujours en arrière
		self.baseSort = base.cam.node().getDisplayRegion(0).getSort()
		base.cam.node().getDisplayRegion(0).setSort(20)

		#Boutons
		btnScale = (0.06,0.06)
		text_scale = 0.12
		borderW = (0.02, 0.02)
		separation = 1
		hauteur = -0.6
		numItemsVisible = 50
		self.couleurBack = (0.243,0.325,0.321,1)
		self.player1ready = False
		self.player2ready = False
		self.player1Infos = ""
		self.player2Infos = ""
		self.couleurDisabled = (0.343,0.325,0.321,1)
		self.couleurBGLabel = (255,255,255,0.3)
		self.couleurShadow = (200,200,200,0.8)
		self.couleurFG = (0,0,0,1)
		self.joueur1 = ""
		self.joueur2 = ""
		#Titre du jeu
		base.disableMouse()
		
		


		self.fieldUsername1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-4,0,0.82) )
		self.fieldUsername2 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(3.4,0,0.82) )
		self.fieldPassword1 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(-4,0,0.59),
									obscured=1 )
		self.fieldPassword2 = DirectEntry(text = "" ,scale=.05,
									initialText="", 
									numLines = 1,
									focus=1,
									pos=(3.4,0,0.59),
									obscured=1 )
		self.messageBox = DirectEntry(text = "" ,scale=.05,
									width =55,
									initialText="Veuillez vous connecter à Tank'em", 
									numLines = 1,
									focus=0,
									pos=(-10.35,0,0.3),
									focusInCommand=self.clearText )
		
		self.textLabel1 = TextNode('testLabel1')
		self.textLabel1.setText("Player1")
		self.textLabel1.setTextColor(0,0,0,1)
		self.textLabel1.setShadow(0.05,0.05)
		self.textLabel1.setShadowColor(self.couleurShadow)
		self.textLabel1.setCardColor(self.couleurBGLabel)
		self.textLabel1.setCardAsMargin(0, 0, 0, 0)
		self.textLabel1.setCardDecal(True)
		self.textLabel1.setAlign(TextNode.ACenter)
		self.nodeLabel1 = aspect2d.attachNewNode(self.textLabel1)
		self.nodeLabel1.setScale(0.10)
		self.nodeLabel1.setPos(-3.75,0,0.9)

		self.textLabel2 = TextNode('textLabel2')
		self.textLabel2.setText("Player2")
		self.textLabel2.setTextColor(0,0,0,1)
		self.textLabel2.setShadow(0.05,0.05)
		self.textLabel2.setShadowColor(self.couleurShadow)
		self.textLabel2.setCardColor(self.couleurBGLabel)
		self.textLabel2.setCardAsMargin(0, 0, 0, 0)
		self.textLabel2.setCardDecal(True)
		self.textLabel2.setAlign(TextNode.ACenter)
		self.nodeLabel2 = aspect2d.attachNewNode(self.textLabel2)
		self.nodeLabel2.setScale(0.10)
		self.nodeLabel2.setPos(3.65,0,0.9)

		self.textPassword1 = TextNode('textPassword1')
		self.textPassword1.setText("Password")
		self.textPassword1.setTextColor(0,0,0,1)
		self.textPassword1.setShadow(0.05,0.05)
		self.textPassword1.setShadowColor(self.couleurShadow)
		self.textPassword1.setCardColor(self.couleurBGLabel)
		self.textPassword1.setCardAsMargin(0, 0, 0, 0)
		self.textPassword1.setCardDecal(True)
		self.textPassword1.setAlign(TextNode.ACenter)
		self.nodePassword1 = aspect2d.attachNewNode(self.textPassword1)
		self.nodePassword1.setScale(0.10)
		self.nodePassword1.setPos(-3.75,0,0.67)

		self.textPassword2 = TextNode('textPassword2')
		self.textPassword2.setText("Password")
		self.textPassword2.setTextColor(0,0,0,1)
		self.textPassword2.setShadow(0.05,0.05)
		self.textPassword2.setShadowColor(self.couleurShadow)
		self.textPassword2.setCardColor(self.couleurBGLabel)
		self.textPassword2.setCardAsMargin(0, 0, 0, 0)
		self.textPassword2.setCardDecal(True)
		self.textPassword2.setAlign(TextNode.ACenter)
		self.nodePassword2 = aspect2d.attachNewNode(self.textPassword2)
		self.nodePassword2.setScale(0.10)
		self.nodePassword2.setPos(3.65,0,0.67)

		self.textMessagebox = TextNode('textMessagebox')
		self.textMessagebox.setText("Message box")
		self.textMessagebox.setTextColor(0,0,0,1)
		self.textMessagebox.setShadow(0.05,0.05)
		self.textMessagebox.setShadowColor(self.couleurShadow)
		self.textMessagebox.setCardColor(self.couleurBGLabel)
		self.textMessagebox.setCardAsMargin(0, 0, 0, 0)
		self.textMessagebox.setCardDecal(True)
		self.textMessagebox.setAlign(TextNode.ACenter)
		self.nodeMessagebox = aspect2d.attachNewNode(self.textMessagebox)
		self.nodeMessagebox.setScale(0.10)
		self.nodeMessagebox.setPos(-3.05,0,0.4)

		self.textJoueur1 = TextNode('textJoueur1')
		self.textJoueur1.setText("")
		self.textJoueur1.setTextColor(0,0,0,1)
		self.textJoueur1.setShadow(0.05,0.05)
		self.textJoueur1.setShadowColor(self.couleurShadow)
		self.textJoueur1.setCardColor(self.couleurBGLabel)
		self.textJoueur1.setCardAsMargin(0, 0, 0, 0)
		self.textJoueur1.setCardDecal(True)
		self.textJoueur1.setAlign(TextNode.ACenter)
		self.nodeJoueur1 = aspect2d.attachNewNode(self.textJoueur1)
		self.nodeJoueur1.setScale(0)
		self.nodeJoueur1.setPos(0.014,0,0.1)

		self.textJoueur2 = TextNode('textJoueur2')
		self.textJoueur2.setText("")
		self.textJoueur2.setTextColor(0,0,0,1)
		self.textJoueur2.setShadow(0.05,0.05)
		self.textJoueur2.setShadowColor(self.couleurShadow)
		self.textJoueur2.setCardColor(self.couleurBGLabel)
		self.textJoueur2.setCardAsMargin(0, 0, 0, 0)
		self.textJoueur2.setCardDecal(True)
		self.textJoueur2.setAlign(TextNode.ACenter)
		self.nodeJoueur2 = aspect2d.attachNewNode(self.textJoueur2)
		self.nodeJoueur2.setScale(0)
		self.nodeJoueur2.setPos(0.014,0,-0.3)

		self.textVersus = TextNode('textVersus')
		self.textVersus.setText("VERSUS")
		self.textVersus.setTextColor(0,0,0,1)
		self.textVersus.setShadow(0.05,0.05)
		self.textVersus.setShadowColor(self.couleurShadow)
		self.textVersus.setCardColor(self.couleurBGLabel)
		self.textVersus.setCardAsMargin(0, 0, 0, 0)
		self.textVersus.setCardDecal(True)
		self.textVersus.setAlign(TextNode.ACenter)
		self.nodeVersus = aspect2d.attachNewNode(self.textVersus)
		self.nodeVersus.setScale(0)
		self.nodeVersus.setPos(0.014,0,-0.1)

		self.textCombattre = TextNode('textCombattre')
		self.textCombattre.setText("Combattrons dans l'arène :")
		self.textCombattre.setTextColor(0,0,0,1)
		self.textCombattre.setShadow(0.05,0.05)
		self.textCombattre.setShadowColor(self.couleurShadow)
		self.textCombattre.setCardColor(self.couleurBGLabel)
		self.textCombattre.setCardAsMargin(0, 0, 0, 0)
		self.textCombattre.setCardDecal(True)
		self.textCombattre.setAlign(TextNode.ACenter)
		self.nodeCombattre = aspect2d.attachNewNode(self.textCombattre)
		self.nodeCombattre.setScale(0)
		self.nodeCombattre.setPos(0.014,0,-0.5)

		self.textFavoris = TextNode('textFavoris')
		self.textFavoris.setText("")
		self.textFavoris.setTextColor(0,0,0,1)
		self.textFavoris.setShadow(0.05,0.05)
		self.textFavoris.setShadowColor(self.couleurShadow)
		self.textFavoris.setCardColor(self.couleurBGLabel)
		self.textFavoris.setCardAsMargin(0, 0, 0, 0)
		self.textFavoris.setCardDecal(True)
		self.textFavoris.setAlign(TextNode.ACenter)
		self.nodeFavoris = aspect2d.attachNewNode(self.textFavoris)
		self.nodeFavoris.setScale(0)
		self.nodeFavoris.setPos(0.014,0,-0.9)

		self.textNiveau = TextNode('textNiveau')
		self.textNiveau.setText("")
		self.textNiveau.setTextColor(0,0,0,1)
		self.textNiveau.setShadow(0.05,0.05)
		self.textNiveau.setShadowColor(self.couleurShadow)
		self.textNiveau.setCardColor(self.couleurBGLabel)
		self.textNiveau.setCardAsMargin(0, 0, 0, 0)
		self.textNiveau.setCardDecal(True)
		self.textNiveau.setAlign(TextNode.ACenter)
		self.nodeNiveau = aspect2d.attachNewNode(self.textNiveau)
		self.nodeNiveau.setScale(0)
		self.nodeNiveau.setPos(0.014,0,-0.7)
		
		self.b2 = DirectButton(text = ("Login", "Login", "Login", "Login"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurBack,
						  frameColor=self.couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayerReady,
						  extraArgs = [True,1],
						  pos = (-3.75,0,0.45))
		self.b3 = DirectButton(text = ("Login", "Login", "Login", "Login"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurBack,
						  frameColor=self.couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.setPlayerReady,
						  extraArgs = [True,2],
						  pos = (3.65,0,0.45))
		self.b4 = DirectButton(text = ("Play", "Play", "Play", "Play"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurDisabled,
						  frameColor=self.couleurDisabled,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  state = DGG.DISABLED,
						  command = self.setNiveauChoisi,
						  extraArgs = [self.mapID],
						  pos = (-3.05,0.4,0.67))

		self.b5 = DirectButton(text = ("Site internet de Tank'em", "Site internet de Tank'em", "Site internet de Tank'em", "Site internet de Tank'em"),
						  text_scale=btnScale,
						  borderWidth = borderW,
						  text_bg=self.couleurBack,
						  frameColor=self.couleurBack,
						  relief=2,
						  textMayChange = 1,
						  pad = (0,0),
						  command = self.openSite,
						  pos = (1.25,-1.4,-0.9))
	
		self.loginIntro()
		#Tank1
		self.tankGauche = loader.loadModel("../asset/Tank/tank")		
		self.tankGauche.reparentTo(render)
		# self.tankGauche.setPos(-17.5,65,-10)
		self.tankGauche.setPos(-46.5,65,-10)
		self.tankGauche.setScale(6.005,6.005,6.005)
		self.tankGauche.setHpr(180, 0.0, 0.0)
		interval = self.tankGauche.hprInterval(4.0, Vec3(-180, 0, 0))
		self.sequenceTourne = Sequence(interval)
		self.sequenceTourne.loop()
		
		#Tank2
		self.tankDroite = loader.loadModel("../asset/Tank/tank")		
		self.tankDroite.reparentTo(render)
		# self.tankDroite.setPos(17.5,65,-10)
		self.tankDroite.setPos(46.5,65,-10)
		self.tankDroite.setScale(6.005,6.005,6.005)
		self.tankDroite.setHpr(180, 0.0, 0.0)
		interval2 = self.tankDroite.hprInterval(4.0, Vec3(540, 0, 0))
		self.sequenceTourne = Sequence(interval2)
		self.sequenceTourne.loop()

		

		#Initialisation de l'effet de transition
		curtain = loader.loadTexture("../asset/Menu/load.png")

		self.transition = Transitions(loader)
		self.transition.setFadeColor(0, 0, 0)
		self.transition.setFadeModel(curtain)

		self.sound = loader.loadSfx("../asset/Menu/shotgun.mp3")
	def openSite(self):
		webbrowser.open_new("http://localhost/Tank'em%20Web/index.php")
	def loginIntro(self):
		self.sequence = Sequence (LerpPosInterval(self.nodeLabel1,1,(-0.75,0,0.9),blendType="easeIn"))
		self.sequence2 = Sequence (LerpPosInterval(self.fieldUsername1,1,(-1,0,0.82),blendType="easeIn"))
		self.sequence3 = Sequence (LerpPosInterval(self.fieldUsername2,1,(0.4,0,0.82),blendType="easeIn"))
		self.sequence4 = Sequence (LerpPosInterval(self.nodeLabel2,1,(0.65,0,0.9),blendType="easeIn"))
		self.sequence5 = Sequence (LerpPosInterval(self.nodePassword1,1,(-0.75,0,0.67),blendType="easeIn"))
		self.sequence13 = Sequence (LerpPosInterval(self.nodeMessagebox,1,(-0.05,0,0.4),blendType="easeIn"))
		self.sequence6 = Sequence (LerpPosInterval(self.nodePassword2,1,(0.65,0,0.67),blendType="easeIn"))
		self.sequence7 = Sequence (LerpPosInterval(self.fieldPassword1,1,(-1,0,0.59),blendType="easeIn"))
		self.sequence8 = Sequence (LerpPosInterval(self.fieldPassword2,1,(0.4,0,0.59),blendType="easeIn"))
		self.sequence9 = Sequence (LerpPosInterval(self.messageBox,1,(-1.35,0,0.3),blendType="easeIn"))
		self.sequence10 = Sequence (LerpPosInterval(self.b2,1,(-0.75,0,0.45),blendType="easeIn"))	
		self.sequence11 = Sequence (LerpPosInterval(self.b3,1,(0.65,0,0.45),blendType="easeIn"))	
		self.sequence12 = Sequence (LerpPosInterval(self.b4,1,(-0.05,0.4,0.67),blendType="easeIn"))	
		self.sequence.start()
		self.sequence4.start()
		self.sequence2.start()	  
		self.sequence3.start()	 
		self.sequence5.start()	 
		self.sequence6.start()	 
		self.sequence7.start()	 
		self.sequence8.start()	 
		self.sequence13.start()	 
		self.sequence9.start()
		self.sequence10.start()	 
		self.sequence11.start()	 
		self.sequence12.start()	 

	def loginOutro(self):
		self.sequence = Sequence (LerpPosInterval(self.nodeLabel1,1,(-3.75,0,0.9),blendType="easeOut"))
		self.sequence2 = Sequence (LerpPosInterval(self.fieldUsername1,1,(-4,0,0.82),blendType="easeOut"))
		self.sequence3 = Sequence (LerpPosInterval(self.fieldUsername2,1,(3.4,0,0.82),blendType="easeOut"))
		self.sequence4 = Sequence (LerpPosInterval(self.nodeLabel2,1,(3.65,0,0.9),blendType="easeOut"))
		self.sequence5 = Sequence (LerpPosInterval(self.nodePassword1,1,(-3.75,0,0.67),blendType="easeOut"))
		self.sequence13 = Sequence (LerpPosInterval(self.nodeMessagebox,1,(-3.05,0,0.4),blendType="easeOut"))
		self.sequence6 = Sequence (LerpPosInterval(self.nodePassword2,1,(3.65,0,0.67),blendType="easeOut"))
		self.sequence7 = Sequence (LerpPosInterval(self.fieldPassword1,1,(-4,0,0.59),blendType="easeOut"))
		self.sequence8 = Sequence (LerpPosInterval(self.fieldPassword2,1,(3.4,0,0.59),blendType="easeOut"))
		self.sequence9 = Sequence (LerpPosInterval(self.messageBox,1,(-5.35,0,0.3),blendType="easeOut"))
		self.sequence10 = Sequence (LerpPosInterval(self.b2,1,(-3.75,0,0.45),blendType="easeOut"))	
		self.sequence11 = Sequence (LerpPosInterval(self.b3,1,(3.65,0,0.45),blendType="easeOut"))	
		self.sequence.start()
		self.sequence4.start()
		self.sequence2.start()	  
		self.sequence3.start()	 
		self.sequence5.start()	 
		self.sequence6.start()	 
		self.sequence7.start()	 
		self.sequence8.start()	 
		self.sequence13.start()	 
		self.sequence9.start()
		self.sequence10.start()	 
		self.sequence11.start()
	def tankIntro(self):
		self.sequence = Sequence (LerpPosInterval(self.tankGauche,2,(-17.5,65,-10)))
		self.sequence2 = Sequence (LerpPosInterval(self.tankDroite,2,(17.5,65,-10)))
		self.sequence2.start()	  
		self.sequence.start()

	def lerpText(self) :
		self.sequence = Sequence (LerpScaleInterval(self.nodeJoueur1, 1, 0.08, 0),
								  LerpScaleInterval(self.nodeVersus, 1, 0.08, 0),
								  LerpScaleInterval(self.nodeJoueur2, 1, 0.08, 0),
								  LerpScaleInterval(self.nodeCombattre, 1, 0.08, 0),
								  LerpScaleInterval(self.nodeNiveau, 1, 0.08, 0))
		self.sequence.start()

	def hex_to_rgb(self,value):
		value = value.lstrip('#')
		lv = len(value)
		if lv == 1:
			v = int(value, 16)*17
			return v, v, v
		if lv == 3:
			return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
		return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

	def setPlayerReady(self,state,num):
		if num == 1 : 
			self.username1 = self.fieldUsername1.get()
			self.password1 = self.fieldPassword1.get()
			self.joueur1 = self.user.read(self.username1,self.password1)
		if num == 2 :
			self.username2 = self.fieldUsername2.get()
			self.password2 = self.fieldPassword2.get()
			self.joueur2 = self.user.read(self.username2,self.password2)

		if self.joueur1 == 1 or self.joueur2 == 1 :
			self.setText("Mauvais nom d'utilisateur")
		elif self.joueur1 == 0 or self.joueur2 == 0 : 
			self.setText("Mauvais mot de passe")
		else :
			if num == 1 : 
				self.player1ready = state
				self.player1Infos = self.joueur1
				self.b2['state'] = DGG.DISABLED
				self.b2['frameColor'] = self.couleurDisabled
				self.b2['text_bg'] = self.couleurDisabled
				self.gameLogic.idJoueur1 = self.joueur1.idJoueur
			if num == 2 :
				self.player2ready = state
				self.player2Infos = self.joueur2
				self.b3['state'] = DGG.DISABLED
				self.b3['frameColor'] = self.couleurDisabled
				self.b3['text_bg'] = self.couleurDisabled
				self.gameLogic.idJoueur2 = self.joueur2.idJoueur
			if self.player1ready == True and self.player2ready == True :
				self.setText("Welcome to Tank'em !")
				self.b4['state'] = DGG.NORMAL
				self.b4['frameColor'] = self.couleurBack
				self.b4['text_bg'] = self.couleurBack
				# self.joueur1.agilite = 7
				# self.joueur1.force = 10
				# self.joueur1.vie = 25
				# self.joueur1.dexterite = 15
				self.calcJoueur1 = self.calculateName(self.joueur1)
				self.calcJoueur2 = self.calculateName(self.joueur2)
				self.textJoueur1.setText(self.username1 + " " + self.calcJoueur1)
				self.textJoueur2.setText(self.username2 + " " + self.calcJoueur2)
				self.textNiveau.setText(self.mapName)
				self.color1 = self.hex_to_rgb(self.joueur1.couleurTank)
				self.color2 = self.hex_to_rgb(self.joueur2.couleurTank)
				print self.color1[0]
				self.tankGauche.setColorScale(self.color1[0]/255.0,self.color1[1]/255.0,self.color1[2]/255.0,1)
				self.tankDroite.setColorScale(self.color2[0]/255.0,self.color2[1]/255.0,self.color2[2]/255.0,1)
				self.lerpText()
				self.tankIntro()
				self.loginOutro()
			elif self.player1ready :
				self.setText('Player 2 must also login')
			elif self.player2ready :
				self.setText('Player 1 must also login')
			else :
				self.setText('Both players must login')

	def getPlayer1(self):
		return self.joueur1
	def getPlayer2(self):
		return self.joueur2
	#callback function to set  text 
	def setText(self,textEntered):
		self.messageBox.enterText(textEntered)
	
	#clear the text
	def clearText(self):
		self.messageBox.enterText('')
	def cacher(self):
			self.tankGauche.removeNode()
			self.tankDroite.removeNode()
			loader.unloadModel( "../asset/Tank/tank" )
			#Est esssentiellement un code de "loading"
			#On remet la caméra comme avant
			base.cam.node().getDisplayRegion(0).setSort(self.baseSort)
			#On cache les menus
			self.background.hide()
			self.b2.hide()
			self.b3.hide()
			self.b4.hide()
			self.fieldUsername1.hide()
			self.fieldUsername2.hide()
			self.fieldPassword1.hide()
			self.fieldPassword2.hide()
			self.messageBox.hide()
			self.nodeLabel1.hide()
			self.nodePassword1.hide()
			self.nodeLabel2.hide()
			self.nodePassword2.hide()
			self.nodeMessagebox.hide()
			self.nodeJoueur1.hide()
			self.nodeJoueur2.hide()
			self.nodeCombattre.hide()
			self.nodeNiveau.hide()
			self.nodeVersus.hide()
			
	def setNiveauChoisi(self,idNiveau):
			self.gameLogic.setIdNiveau(idNiveau)
			self.gameLogic.setPlayers([self.player1Infos, self.player2Infos])
			self.chargeJeu()

	def chargeJeu(self):
			#On démarre!
			Sequence(Func(self.cacher),
					 Func(lambda : self.transition.irisOut(0.2)),
					 SoundInterval(self.sound),
					 Func(lambda : messenger.send("DemarrerPartie")),
					 Wait(0.2), #Bug étrange quand on met pas ça. L'effet de transition doit lagger
					 Func(lambda : self.transition.irisIn(0.2))
			).start()

	def calculateName(self, joueur):
		self.statsJoueur = joueur.getStats()
		#StatsJoueur: 0 = vie, 1 = force, 2 = agilite, 3 = dexterite
		self.bestStat1 = [[0, -1]] #Un array d'arrays contenant deux infos: le nb de points et l'index number
		self.bestStat2 = [[0, -1]]
		self.qualificatifA = ""
		self.qualificatifB = ""
		self.maxStat = 30 #Le stat maximum

		#Si tous les stats sont au maximum
		if(self.statsJoueur[0] == self.maxStat and self.statsJoueur[1] == self.maxStat and self.statsJoueur[2] == self.maxStat and self.statsJoueur[3] == self.maxStat):
			return "dominateur"

		#Regarde chacun des stats du joueur et détermine ce qui est le plus grand
		for idx,stat in enumerate(self.statsJoueur):
			if(stat > self.bestStat1[0][0]): #S'il y a un stat plus grand que le bestStat, on restart le bestStats avec le nouveau stat
				self.bestStat1 = []
				self.bestStat1.append([stat,idx])
			elif(stat == self.bestStat1[0][0] and stat > 0): #S'il y a un stat égal au bestStat, on rajoute les infos dan's 
				self.bestStat1.append([stat,idx])
		self.bestStat1 = random.choice(self.bestStat1)
		print "QualificatifA : " + str(self.bestStat1)

		for idx,stat in enumerate(self.statsJoueur):
			if(idx != self.bestStat1[1]):
				if(stat > self.bestStat2[0][0]):
					self.bestStat2 = []
					self.bestStat2.append([stat,idx])
				elif(stat == self.bestStat2[0][0] and stat > 0):
					self.bestStat2.append([stat,idx])
		self.bestStat2 = random.choice(self.bestStat2)
		print "QualificatifB: " + str(self.bestStat2)

		if(self.bestStat1[1] == 0):
			if(self.bestStat1[0] >= 1):
				self.qualificatifA = "le fougeux"
			if(self.bestStat1[0] >= 5):
				self.qualificatifA = "le pétulant"
			if(self.bestStat1[0] >= 10):
				self.qualificatifA = "l'immortel"
		elif(self.bestStat1[1] == 1):
			if(self.bestStat1[0] >= 1):
				self.qualificatifA = "le crossfiter"
			if(self.bestStat1[0] >= 5):
				self.qualificatifA = "le hulk"
			if(self.bestStat1[0] >= 10):
				self.qualificatifA = "le tout puissant"
		elif(self.bestStat1[1] == 2):
			if(self.bestStat1[0] >= 1):
				self.qualificatifA = "le prompt"
			if(self.bestStat1[0] >= 5):
				self.qualificatifA = "le lynx"
			if(self.bestStat1[0] >= 10):
				self.qualificatifA = "le foudroyant"
		elif(self.bestStat1[1] == 3):
			if(self.bestStat1[0] >= 1):
				self.qualificatifA = "le précis"
			if(self.bestStat1[0] >= 5):
				self.qualificatifA = "l'habile"
			if(self.bestStat1[0] >= 10):
				self.qualificatifA = "le chirurgien"
		
		if(self.bestStat2[1] == 0):
			if(self.bestStat2[0] >= 1):
				self.qualificatifB = "fougeux"
			if(self.bestStat2[0] >= 5):
				self.qualificatifB = "pétulant"
			if(self.bestStat2[0] >= 10):
				self.qualificatifB = "immortel"
		elif(self.bestStat2[1] == 1):
			if(self.bestStat2[0] >= 1):
				self.qualificatifB = "qui fait du crossfit"
			if(self.bestStat2[0] >= 5):
				self.qualificatifB = "brutal"
			if(self.bestStat2[0] >= 10):
				self.qualificatifB = "tout puissant"
		elif(self.bestStat2[1] == 2):
			if(self.bestStat2[0] >= 1):
				self.qualificatifB = "prompt"
			if(self.bestStat2[0] >= 5):
				self.qualificatifB = "lynx"
			if(self.bestStat2[0] >= 10):
				self.qualificatifB = "foudroyant"
		elif(self.bestStat2[1] == 3):
			if(self.bestStat2[0] >= 1):
				self.qualificatifB = "précis"
			if(self.bestStat2[0] >= 5):
				self.qualificatifB = "habile"
			if(self.bestStat2[0] >= 10):
				self.qualificatifB = "chirurgien"

		return self.qualificatifA + " " + self.qualificatifB