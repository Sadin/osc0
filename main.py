import gi
import random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

alphabet = "abcdefghijklmnopqrstuvwxyz"

def gen_random(chars, length):
    rnd_alphabet = ""
    for x in range(0, length):
        rnd_alphabet += random.choice(alphabet)	

    return rnd_alphabet

class MyWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):

        rnd_alphabet = gen_random('abcdefghijklmnopqrstuvwxyz', 8)
        print(rnd_alphabet)


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
