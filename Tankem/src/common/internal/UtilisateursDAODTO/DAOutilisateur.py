#-*- coding:utf-8 -*-
from DAOorigine import DAOorigine
from DTOJoueur import DTOJoueur
import cx_Oracle
from SingletonDBConnection import SingletonDBConnection

class DAOutilisateur():

	def __init__(self):
		self.connection = SingletonDBConnection().getConnection()

	def read(self, username, password):
		try:
			curRead = self.connection.cursor()
			curRead.execute("SELECT * from joueur WHERE ingamename=:player_username",player_username = username)
			for result in curRead:
				if(result[5] == password):
					self.dtoJoueur = DTOJoueur(result[0], result[1],
												result[2], result[3],
												result[4], result[5],
												result[6], result[7],
												result[8], result[9],
												result[10], result[11],
												result[12], result[13],
												result[14])
					return self.dtoJoueur #Retourne l'objet Joueur
				else:
					#Return 0 si ce n'est pas le bon password
					return 0
			if(curRead.rowcount == 0):
				#return 1 si ce n'est pas un bon username
				return 1 

			# self.connection.close() #Au cas ou qu'il y a trop de connection, utiliser cette fonction

		except cx_Oracle.DatabaseError as e:
			error, = e.args
			print("Erreur de commande")
			print(error.code)
			print(error.message)
			print(error.context)
