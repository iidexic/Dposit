import tkinter as tk
#====Tkinter Widgets:=====
# (More info on widgets and options: https://tkdocs.com/tutorial/widgets.html)
# -Label - text display box. Can also display images
# -Button - standard pressable button
# -Entry - single line text entry box
# --Can add validation (restricts what can be typed)
# -Text - multi line text entry box
# -Frame - Rectangular region to group other widgets
# -Radiobutton - self-explanatory

window = tk.Tk()
title = tk.Label(text="Fart Calculator")
title.pack()

# Packs the widget (label) into the window

window.mainloop()
