class SpaceFilterWindow:
	def __init__(self):
		self.sg = __import__('PySimpleGUI')
		self.title = "Filtros espaciais"
		self.resolution = (250, 80)
		self.location = (1040, 50)
		self.window = []

	def start(self):
		layout = [
			[
				self.sg.Text(text="Filtros espaciais:", size=(30, 1)),
			],
			[
				self.sg.Combo([
					'Nenhum',
					'Blur (Borramento)',
					'Blur Gaussiano (Borramento)',
					'Blur Mediana',
					'Sobel X',
					'Sobel Y',
					'Laplaciano',
					'Canny'
				], default_value='Nenhum', enable_events=True, size=(30, 1), key='-SPACE_FILTERS-'),
			]
		]
		self.window = self.sg.Window(
			title=self.title,
			layout=layout,
			size=self.resolution,
			finalize=True,
			disable_close=True,
			keep_on_top=True,
			location=self.location
		)
		return self.window