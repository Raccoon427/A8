#https://github.com/Raccoon427/A8
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.label = QLabel()
        self.frame_count = 0
        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.label.setPixmap(QPixmap.fromImage(QImage(self.frames[0])))

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)

        # main_frame = QFrame()

        frame.setLayout(main_layout)

        self.setCentralWidget(frame)

        # add slider
        slider = QSlider(Qt.Orientation.Vertical, self)
        slider.setRange(0,100)
        slider.setValue(100)

        slider.setTickPosition(QSlider.TickPosition.TicksBothSides)

        main_layout.addWidget(slider)

        # add timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(100)

    # animate method
    def animate(self):
        if self.frame_count == self.num_frames:
            self.frame_count = 0
        self.label.setPixmap(self.frames[self.frame_count])
        self.frame_count += 1
        self.repaint()

    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
