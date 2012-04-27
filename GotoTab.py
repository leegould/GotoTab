import sublime, sublime_plugin

class GotoTabCommand(sublime_plugin.WindowCommand):
	
	def run(self, tab):
		try:
<<<<<<< HEAD
			views = self.window.views_in_group(self.window.active_group())
			if tab == 'last':
			    self.window.focus_view(views[len(views) - 1])
			else:
				tab = int(tab) - 1
				if tab < len(views):
					self.window.focus_view(views[tab])
=======
			if tab == 'last':
			    self.window.focus_view(self.window.views()[len(self.window.views()) - 1])
			else:
				tab = int(tab) - 1
				if tab < len(self.window.views()):
					self.window.focus_view(self.window.views()[tab])
>>>>>>> a52d97352b5c439b43c7d4179f7ab2e37d3dcf33
		except ValueError:
			pass