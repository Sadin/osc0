import gi, random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

alphabet = "abcdefghijklmnopqrstuvwxyz"

def genRandom(chars, length):
	rndAlphabet = ""
	for x in range(1, length):
		rndAlphabet = rndAlphabet + random.choice(alphabet)	
		
	return rndAlphabet

class MyWindow(Gtk.Window):


	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")

		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):

		rndAlphabet = genRandom('abcdefghijklmnopqrstuvwxyz', 8)
#		print(len(alphabet)) # just to check
		print(rndAlphabet)
#		print("Hello World")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
