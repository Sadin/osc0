import gi
import random
import string
import math
#from wavegen import wavegen

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

def gen_random(chars, length):
    rnd_alphabet = ""
    for x in range(0, length):
        rnd_alphabet += random.choice(chars)	

    return rnd_alphabet

class MyWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="osc0")

        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("")
        self.entry.set_editable(False)
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=4)
        vbox.pack_start(hbox, True, True, 0)

        self.button = Gtk.Button(label="Gen Random")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):

        rnd_alphabet = gen_random(string.printable, 8)
        self.entry.set_text(rnd_alphabet)
        print(rnd_alphabet)


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
