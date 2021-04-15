# coding: utf-8
from random import shuffle, randint
import sys, json, datetime

class Unit:
	def __init__(self, power, owner):
		# setting owner of the unit (black | white)
		self.owner = owner
		# setting power of the unit
		"""
		1 = pawn
		2 = rook
		3 = knight
		4 = left bishop
		5 = right bishop
		6 = queen
		7 = king
		"""
		self.power = power
		self.moves = []
		# special pawn move
		self.en_passant_possible = False
		# rook castling variable
		self.moved = False
		
	# add a move to the list
	def addMove(self, move):
		self.moves.append(move)
		
	# returns the power of a unit as word
	def getPowerString(self):
		if self.power == 1:
			return "pawn"
		elif self.power == 2:
			return "rook"
		elif self.power == 3:
			return "knight"
		elif self.power == 4:
			return "bishop"
		elif self.power == 5:
			return "bishop"
		elif self.power == 6:
			return "queen"
		elif self.power == 7:
			return "king"
		else:
			return "ERROR"

	# resets the moves array
	def resetMoves(self):
		self.moves = []

	# getter and setter
	def getMoves(self):
		return self.moves
		
	def setMoves(self):
		self.moves = moves
		
	def getOwner(self):
		return self.owner
		
	def setOwner(self, owner):
		self.owner = owner
		
	def getPower(self):
		return self.power
		
	def setPower(self, power):
		self.power = power
		
	def isInGame(self):
		return self.inGame
		
	def setInGame(self, inGame):
		self.inGame = inGame
