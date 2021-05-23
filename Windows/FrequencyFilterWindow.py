class FrequencyFilterWindow:
	def __init__(self):
		self.sg = __import__('PySimpleGUI')
		self.title = "Filtros no domínio da frequência"
		self.resolution = (250, 150)
		self.location = (1040, 175)
		self.window = []

	def start(self):
		layout = [
			[
				self.sg.Text(text="Filtros no domínio da frequência:", size=(30, 1))
			],
			[
				self.sg.Combo([
					'Nenhum',
					'Passa alta',
					'Passa baixa'
				], default_value='Nenhum', enable_events=True, size=(30, 1), key='-FREQUENCY_FILTERS-'),
			],
			[
				self.sg.Column([
					[self.sg.Radio('Ideal', 'OPTION_FREQ', True, size=(30, 1), key="-IDEAL-")],
					[self.sg.Radio('Butterworth', 'OPTION_FREQ', size=(30, 1), key="-BUTTERWORTH-")],
					[self.sg.Radio('Gaussiano', 'OPTION_FREQ', size=(30, 1), key="-GAUSSIANO-")]
				], key='-OPTIONS_FREQ-', visible=False),
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

	def showOptions(self):
		self.window['-OPTIONS_FREQ-'].update(visible=True)
	
	def hideOptions(self):
		self.window['-OPTIONS_FREQ-'].update(visible=False)