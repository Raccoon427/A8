#https://github.com/Raccoon427/A8
#Max Skinner u1600635
#Eliana Fisher u1492743
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
        self.frame_count = 0
        self.fps = 1
        self.is_playing = False
        self.sprite = QLabel()
        self.frames_per_display = QLabel("Frames Per Second: ")
        self.frame_display = QLabel(str(self.fps))
        # Make the GUI in the setupUI method
        self.setupUI()

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.
        self.sprite.setPixmap((self.frames[0]))

        #menu code
        menubar = self.menuBar()
        file_menu = QMenu("&File", self)
        menubar.addMenu(file_menu)
        exit = QAction("&Exit", self)
        exit.triggered.connect(self.app_close)
        pause = QAction("&Pause", self)
        pause.triggered.connect(self.app_pause)
        file_menu.addAction(exit)
        file_menu.addAction(pause)

        #layout
        main_layout = QVBoxLayout()
        sprite_layout = QHBoxLayout()
        sprite_layout.addWidget(self.sprite)

        # add slider
        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setRange(1, 100)
        self.slider.setValue(self.fps)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        sprite_layout.addWidget(self.slider)
        main_layout.addLayout(sprite_layout)

        #slider value change
        self.slider.valueChanged.connect(self.slider_fps_change)

        #fps text layout
        fps_layout = QHBoxLayout()
        fps_layout.addWidget(self.frames_per_display)
        fps_layout.addWidget(self.frame_display)
        main_layout.addLayout(fps_layout)

        # main_frame
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        # add start button
        self.start_button = QPushButton("START")
        main_layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.change_is_playing)

        # add timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)

    # You will need methods in the class to act as slots to connect to signals

    # animate method
    def animate(self):
        if self.is_playing:
            if self.frame_count == self.num_frames:
                self.frame_count = 0
            self.sprite.setPixmap(self.frames[self.frame_count])
            self.frame_count += 1
            self.repaint()

    # slider fps change method
    def slider_fps_change(self):
        self.fps = self.slider.value()
        delay_in_ms = int(1000/self.fps)
        self.timer.start(delay_in_ms)
        self.frame_display.setText(str(self.fps))

    # is_playing method
    def change_is_playing(self):
        if self.is_playing:
            self.is_playing = False
            self.start_button.setText("START")

        else:
            self.is_playing = True
            self.slider_fps_change()
            self.start_button.setText("STOP")

    #menu methods
    def app_pause(self):
        self.is_playing = False
        self.start_button.setText("START")

    def app_close(self):
        self.close()

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
