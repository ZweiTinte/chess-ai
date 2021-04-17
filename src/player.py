# coding: utf-8
from random import shuffle, randint
import sys, json, datetime

class Player:
	def __init__(self, color):
		# setting the color (black | white)
		self.color = color
		# sets the opoonent of the player
		self.opponent = None
		# castling booleans
		self.castling_permitted = True
		# True if the player is in check
		self.isInCheck = False
		
	# getter and setter
	def getColor(self):
		return self.color
		
	def setColor(self, color):
		self.color = color
		
	def getOpponent(self):
		return self.opponent
		
	def isInCheck(self):
		return self.isInCheck
		
	def setIsInCheck(self, isInCheck):
		self.isInCheck = isInCheck
		
	def setOpponent(self, opponent):
		self.opponent = opponent

	def castlingIsPermitted(self):
		return self.castling_permitted

	def setCastlingNotPermitted(self):
		self.castling_permitted = False