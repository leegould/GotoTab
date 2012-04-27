import sublime, sublime_plugin

class GotoTabCommand(sublime_plugin.WindowCommand):
	
	def run(self, tab):
		try:
			views = self.window.views_in_group(self.window.active_group())
			if tab == 'last':
			    self.window.focus_view(views[len(views) - 1])
			else:
				tab = int(tab) - 1
				if tab < len(views):
					self.window.focus_view(views[tab])
		except ValueError:
			pass