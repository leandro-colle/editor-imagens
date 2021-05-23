import os
import cv2

class Image:

	@staticmethod
	def readImgSrc(fileName):
		if os.path.exists(fileName):
			return cv2.imread(fileName)
		else:
			return [];

	@staticmethod
	def writeImgSrc(image, window, resolution):
		if len(image) > 0:
			image = cv2.imencode('.png', image)[1].tobytes()
		window.update(data=image, size=resolution)