import kivy
from kivy.app import App

from screen import GameScreen


class CapTF(App):
	def build(self):
		return GameScreen()


if __name__=='__main__':
	CapTF().run()