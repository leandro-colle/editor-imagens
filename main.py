import cv2
import numpy as np
import PySimpleGUI as sg

from Utils.Image import Image
from Windows.MainWindow import MainWindow
from Windows.SpaceFilterWindow import SpaceFilterWindow
from Windows.FrequencyFilterWindow import FrequencyFilterWindow
from Windows.GeometricTransformationWindow import GeometricTransformationWindow
from Operations.FrequencyFilterOperation import FrequencyFilterOperation

def main():
	originalImage = image = [];
	height, width = (0, 0)

	mainWindowClass = MainWindow()
	mainWindow = mainWindowClass.start()
	spaceFilterWindowClass = SpaceFilterWindow()
	spaceFilterWindow = spaceFilterWindowClass.start()
	frequencyFilterWindowClass = FrequencyFilterWindow()
	frequencyFilterWindow = frequencyFilterWindowClass.start()
	geometricTransformationWindowClass = GeometricTransformationWindow()
	geometricTransformationWindow = geometricTransformationWindowClass.start()

	while True:
		eventMain, valuesMain = mainWindow.read(timeout=20)
		eventSpaceFilter, valuesSpaceFilter = spaceFilterWindow.read(timeout=20)
		eventFrequencyFilter, valuesFrequencyFilter = frequencyFilterWindow.read(timeout=20)
		eventGeometricTransformation, valuesGeometricTransformation = geometricTransformationWindow.read(timeout=20)

		if eventMain == "Exit" or eventMain == sg.WIN_CLOSED:
			break

		if eventMain == "-FILE-":
			originalImage = image = Image.readImgSrc(valuesMain["-FILE-"])
			height, width = image.shape[:2]
			Image.writeImgSrc(image, mainWindow["-IMAGE-"], (width, height))
			continue

		image = originalImage
		height, width = (0, 0) if len(image) == 0 else image.shape[:2]

		if eventSpaceFilter == "-SPACE_FILTERS-" or eventFrequencyFilter == "-FREQUENCY_FILTERS-" or eventGeometricTransformation == "-CHECK_ESCALA-" or eventGeometricTransformation == "-CHECK_ANGULO-" or eventGeometricTransformation == "-CHECK_ESPELHAMENTO-" or eventGeometricTransformation == "-CHECK_TRANSLACAO-":
			if len(image) == 0 or (len(image) == 0 and (valuesSpaceFilter["-SPACE_FILTERS-"] != "Nenhum" or valuesFrequencyFilter["-FREQUENCY_FILTERS-"] != "Nenhum")):
				spaceFilterWindow["-SPACE_FILTERS-"].update(value="Nenhum")
				frequencyFilterWindow["-FREQUENCY_FILTERS-"].update(value="Nenhum")
				geometricTransformationWindow["-CHECK_ESCALA-"].update(value=False)
				geometricTransformationWindow["-CHECK_ANGULO-"].update(value=False)
				geometricTransformationWindow["-CHECK_ESPELHAMENTO-"].update(value=False)
				geometricTransformationWindow["-CHECK_TRANSLACAO-"].update(value=False)
				sg.popup("Selecione uma imagem válida antes de continuar.", title="Atenção!")
				continue

		if eventSpaceFilter == "-SPACE_FILTERS-" or valuesSpaceFilter["-SPACE_FILTERS-"] != "Nenhum":
			if valuesSpaceFilter["-SPACE_FILTERS-"] == "Blur (Borramento)":
				image = cv2.blur(image, (21, 21), 50)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Blur Gaussiano (Borramento)":
				image = cv2.GaussianBlur(image, (21, 21), 50)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Blur Mediana":
				image = cv2.medianBlur(image, 21)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Sobel X":
				image = cv2.Sobel(image, cv2.CV_8U,  0, 1, ksize=3)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Sobel Y":
				image = cv2.Sobel(image, cv2.CV_8U,  1, 0, ksize=3)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Laplaciano":
				image = cv2.Laplacian(image, cv2.CV_8U, 3)
			elif valuesSpaceFilter["-SPACE_FILTERS-"] == "Canny":
				image = cv2.Canny(image, 100, 200)
		
		if eventFrequencyFilter == "-FREQUENCY_FILTERS-"  or valuesFrequencyFilter["-FREQUENCY_FILTERS-"] != "Nenhum":
			if valuesFrequencyFilter["-FREQUENCY_FILTERS-"] == "Passa alta" or valuesFrequencyFilter["-FREQUENCY_FILTERS-"] == "Passa baixa":
				frequencyFilterWindowClass.showOptions()

				if len(image.shape) > 2:
					image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				middle = np.fft.fftshift(np.fft.fft2(image))

				if valuesFrequencyFilter["-FREQUENCY_FILTERS-"] == "Passa alta":
					if valuesFrequencyFilter["-IDEAL-"]:
						middlePassFilter = middle * FrequencyFilterOperation.idealHightPass(50, image.shape)
					elif valuesFrequencyFilter["-BUTTERWORTH-"]:
						middlePassFilter = middle * FrequencyFilterOperation.butterworthHightPass(50, image.shape, 10)
					elif valuesFrequencyFilter["-GAUSSIANO-"]:
						middlePassFilter = middle * FrequencyFilterOperation.gaussianoHightPass(50, image.shape)
				elif valuesFrequencyFilter['-FREQUENCY_FILTERS-'] == "Passa baixa":
					if valuesFrequencyFilter["-IDEAL-"]:
						middlePassFilter = middle * FrequencyFilterOperation.idealLowPass(50, image.shape)
					elif valuesFrequencyFilter["-BUTTERWORTH-"]:
						middlePassFilter = middle * FrequencyFilterOperation.butterworthLowPass(50, image.shape, 10)
					elif valuesFrequencyFilter["-GAUSSIANO-"]:
						middlePassFilter = middle * FrequencyFilterOperation.gaussianoLowPass(50, image.shape)

				passFilter = np.fft.ifftshift(middlePassFilter)
				reversePassFilter = np.fft.ifft2(passFilter)
				image = np.array(np.abs(reversePassFilter), dtype=np.uint8)
			else:
				frequencyFilterWindowClass.hideOptions()

		if valuesGeometricTransformation["-CHECK_ESCALA-"] == True:
			image = cv2.resize(image, None, fx=valuesGeometricTransformation["-SLIDER_ESCALA-"], fy=valuesGeometricTransformation["-SLIDER_ESCALA-"], interpolation=cv2.INTER_CUBIC)
		if valuesGeometricTransformation["-CHECK_ANGULO-"] == True:
			matrix = cv2.getRotationMatrix2D((width/2, height/2), valuesGeometricTransformation["-SLIDER_ROTACAO-"], 1)
			image = cv2.warpAffine(image, matrix, (width, height))
		if valuesGeometricTransformation["-CHECK_ESPELHAMENTO-"] == True:
			if valuesGeometricTransformation["-H-"]:
				image = cv2.flip(image, 1)
			elif valuesGeometricTransformation["-V-"]:
				image = cv2.flip(image, 0)
			elif valuesGeometricTransformation["-HV-"]:
				image = cv2.flip(image, -1)
		if valuesGeometricTransformation["-CHECK_TRANSLACAO-"] == True:
			if valuesGeometricTransformation["-CE-"]:
				displacement = np.float32([[1, 0, -50], [0, 1, -90]])
				image = cv2.warpAffine(image, displacement, (width, height))
			elif valuesGeometricTransformation["-BD-"]:
				displacement = np.float32([[1, 0, 25], [0, 1, 50]])
				image = cv2.warpAffine(image, displacement, (width, height))

		image = originalImage if valuesMain["-SHOW_ORIGINAL-"] == True else image
		Image.writeImgSrc(image, mainWindow["-IMAGE-"], (width, height))

	mainWindow.close()

if __name__ == "__main__":
	main()