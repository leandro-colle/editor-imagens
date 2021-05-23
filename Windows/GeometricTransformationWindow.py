class GeometricTransformationWindow:
	def __init__(self):
		self.sg = __import__('PySimpleGUI')
		self.title = "Transformações geométricas"
		self.resolution = (250, 300)
		self.location = (1040, 370)
		self.window = []

	def start(self):
		layout = [
			[
				self.sg.Text(text="Transformações geométricas:", size=(30, 1))
			],
			[
				self.sg.Column([
					[self.sg.Checkbox(text="Escala", key="-CHECK_ESCALA-", enable_events=True)],
					[self.sg.Slider((1, 5), 1, 0.1, orientation='h', size=(30, 10), key='-SLIDER_ESCALA-')],
					[self.sg.HSeparator()],
					[self.sg.Checkbox(text="Ângulo", key="-CHECK_ANGULO-", enable_events=True)],
					[self.sg.Slider((0, 360), 1, 1, orientation='h', size=(30, 10), key='-SLIDER_ROTACAO-')],
					[self.sg.HSeparator()],
					[self.sg.Checkbox(text="Espelhamento", key="-CHECK_ESPELHAMENTO-", enable_events=True)],
					[self.sg.Radio('Horizontal', 'OPTION_ESPELHAMENTO', True, size=(30, 1), key="-H-")],
					[self.sg.Radio('Vertical', 'OPTION_ESPELHAMENTO', size=(30, 1), key="-V-")],
					[self.sg.Radio('Horizontal e Vertical', 'OPTION_ESPELHAMENTO', size=(30, 1), key="-HV-")],
					[self.sg.HSeparator()],
					[self.sg.Checkbox(text="Translação", key="-CHECK_TRANSLACAO-", enable_events=True)],
					[self.sg.Radio('Cima e esquerda', 'OPTION_TRANSLACAO', True, size=(30, 1), key="-CE-")],
					[self.sg.Radio('Baixo e direita', 'OPTION_TRANSLACAO', size=(30, 1), key="-BD-")]
				], scrollable=True, vertical_scroll_only=True, expand_y=True)
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