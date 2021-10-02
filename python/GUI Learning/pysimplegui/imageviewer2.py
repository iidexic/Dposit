import io # how used?
import os # filepath access
import PySimpleGUI as sg
from PIL import Image #Pillow (image lib)

# Setting file selection choices for browse button
file_types = [
    ("JPEG (*.jpg)","*.jpg"), 
    ("PNG (*.png)","*.png"), 
    ("All Files (*.*)", "*.*"),
]
    
def main():
    # Full GUI Layout
    sg.theme('Default')

    layout = [
        [sg.Image(key='-IMG-')],
        [
            sg.Text("Image File"),
            sg.Input(size=(25,1), key='-FILE-'),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
    ]

    window = sg.Window("Image Viewer", layout)

    # The Event Loop:
    while True:
        # Read Window object for events and values
        event, values = window.read()
        # Always check for exit event to exit event loop
        if event == "exit" or event == sg.WIN_CLOSED:
            break
        # On event button press of "Load Image" do the following:
        # Get user-input -FILE- value
        # Check that file exists
        # Using Pillow's Image object, load file
        # Update the image window
        if event == "Load Image":
            filename = values['-FILE-']
            if os.path.exists(filename):
                image = Image.open(values['-FILE-'])
                image.thumbnail((400,400))
                # This is used to conver the image
                # into a byte stream. This lets you
                # Save the image in memory.

                bio = io.BytesIO()
                # Now you can pull the byte data from
                # the in-memory file and pass it to
                # the sg.Image object
                image.save(bio, format="PNG")
                window["-IMG-"].update(data=bio.getvalue())
    
    window.close()

if __name__ == "__main__":
    main()