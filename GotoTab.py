import sublime, sublime_plugin

class GotoTabCommand(sublime_plugin.WindowCommand):
	
	def run(self, tab):
		try:
			tab = int(tab) - 1
			if tab < len(self.window.views()):
				self.window.focus_view(self.window.views()[tab])
		except ValueError:
			pass