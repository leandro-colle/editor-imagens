import numpy as np
from math import sqrt, exp

class FrequencyFilterOperation:

	@staticmethod
	def distance(p1, p2):
		return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

	@staticmethod
	def idealHightPass(d0, image):
		base = np.ones(image[:2])
		lines, columns = image[:2]
		centro = (lines/2, columns/2)
		
		for x in range(columns):
			for y in range(lines):
				if FrequencyFilterOperation.distance((y,x), centro) < d0:
					base[y, x] = 0

		return base
	
	@staticmethod
	def butterworthHightPass(d0, image, n):
		base = np.zeros(image[:2])
		lines, columns = image[:2]
		centro = (lines/2, columns/2)
		
		for x in range(columns):
			for y in range(lines):
				base[y, x] = 1-1/(1+(FrequencyFilterOperation.distance((y,x), centro)/d0)**(2*n))

		return base

	@staticmethod
	def gaussianoHightPass(d0, image):
		base = np.zeros(image[:2])
		lines, columns = image[:2]
		centro = (lines/2, columns/2)
		
		for x in range(columns):
			for y in range(lines):
				base[y, x] = 1-exp(((-FrequencyFilterOperation.distance((y,x), centro)**2)/(2*(d0**2))))

		return base

	def idealLowPass(D0, image):
		base = np.zeros(image[:2])
		lines, columns = image[:2]
		centro = (lines/2,columns/2)
		
		for x in range(columns):
			for y in range(lines):
				if FrequencyFilterOperation.distance((y,x), centro) < D0:
					base[y, x] = 1

		return base

	def butterworthLowPass(D0, image, n):
		base = np.zeros(image[:2])
		lines, columns = image[:2]
		centro = (lines/2, columns/2)
		
		for x in range(columns):
			for y in range(lines):
				base[y, x] = 1/(1+(FrequencyFilterOperation.distance((y,x), centro)/D0)**(2*n))
				
		return base

	def gaussianoLowPass(D0, image):
		base = np.zeros(image[:2])
		lines, columns = image[:2]
		centro = (lines/2, columns/2)
		
		for x in range(columns):
			for y in range(lines):
				base[y, x] = exp(((-FrequencyFilterOperation.distance((y,x), centro)**2)/(2*(D0**2))))
				
		return base