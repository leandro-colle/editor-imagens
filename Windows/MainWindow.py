class MainWindow:
	def __init__(self):
		self.sg = __import__('PySimpleGUI')
		self.title = "Editor de imagens"
		self.importFileTypes = [
			("PNG (*.png)", "*.png"),
			("JPEG (*.jpg)", "*.jpg"),
			("All files (*.*)", "*.*")
		]
		self.resolution = (980, 640)
		self.window = []

	def start(self):
		layout = [
			[
				self.sg.Text("Arquivo de imagem:")
			],
			[
				self.sg.Input(size=(20, 1), enable_events=True, key="-FILE-"),
				self.sg.FileBrowse(button_text="Buscar imagem", file_types=self.importFileTypes),
				self.sg.Checkbox(text="Mostrar original", key="-SHOW_ORIGINAL-", enable_events=True),
			],
			[
				self.sg.HSeparator()
			],
			[	
				self.sg.Column([
					[self.sg.Image(key="-IMAGE-", tooltip="Imagem")]
				])
			]
		]
		self.window = self.sg.Window(
			title=self.title,
			layout=layout,
			size=self.resolution,
			finalize=True,
			location=(50,50)
		)
		return self.window