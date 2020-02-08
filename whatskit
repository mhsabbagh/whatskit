#!/usr/bin/env python
# M.Hanny Sabbagh <mhsabbagh@outlook.com>, 2020.

import gi, os, sys
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import WebKit2 as Webkit

# Load the interface file.
builder = Gtk.Builder()
possible_ui_file_locations = [
    "/usr/share/whatskit/ui.glade",
    "/usr/local/share/whatskit/ui.glade",
    os.path.dirname(os.path.realpath(__file__)) + "/ui/ui.glade"
]
for filename in possible_ui_file_locations:
  if os.path.exists(filename):
    builder.add_from_file(filename)
    break

# Initalize the WebKit view and its settings.
settings = Webkit.Settings.new()
settings.set_enable_webgl(True)
settings.set_enable_accelerated_2d_canvas(True)
settings.set_enable_encrypted_media(True)

webview = Webkit.WebView.new()
webview.set_settings(settings)

# Load WhatsApp.
webview.load_uri("https://web.whatsapp.com")



# Set some properties.
window = builder.get_object("window")
scrolledwindow = builder.get_object("scrolledwindow")
urlbar = builder.get_object("urlbar")
window.set_title("WhatsKit")
window.connect("delete-event", Gtk.main_quit)
urlbar.set_text(webview.get_uri())
urlbar.set_icon_activatable(Gtk.EntryIconPosition(1), True)
aboutwindow = builder.get_object("aboutwindow")

# Launch about window on icon click.
def iconclicked(self, icon, event):
  aboutwindow.run()
  aboutwindow.hide()
urlbar.connect("icon-press", iconclicked)

# Icon work.
possible_icon_paths = [
    "/usr/share/pixmaps/whatskit.png",
    os.path.dirname(os.path.realpath(__file__)) + "/data/whatskit.png"
]
for filename in possible_icon_paths:
  if os.path.exists(filename):
    window.set_icon_from_file(filename)
    aboutwindow.set_icon_from_file(filename)
    break

# Add the webview to GTK window.
scrolledwindow.add(webview)

if __name__ == "__main__": 
  window.show_all()
  Gtk.main()
