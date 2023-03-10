from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from riddles import qslist, answerlist


class GameScreen(GridLayout):

	def __init__(self, **kwargs):
		super(GameScreen, self).__init__(**kwargs)
		self.cols = 4

		self.add_widget(Label(text='Welcome to this Capture the flag!!! \n \nState the riddle number and\nyour answer and confirm it\nin the respective boxes of the row: \n \nIn order for a new riddle to \nappear you have to answer correctly \nthe previous.'))

		self.rn = TextInput( multiline=False)
		self.add_widget(self.rn)

		self.answer = TextInput( multiline=False)
		self.add_widget(self.answer)

		self.confirm_button = Button(text='Confirm Answer', font_size=32)
		self.confirm_button.bind(on_press=self.confirm)
		self.add_widget(self.confirm_button)

		self.add_widget(Label(text='Riddle 1. What is the \nsnake that made the flag?'))

	def confirm(self, instance):
		no = self.rn.text
		answer = self.answer.text
		if answer==answerlist[int(no)-1]:
			self.add_widget(Label(text=qslist[int(no)-1]))



