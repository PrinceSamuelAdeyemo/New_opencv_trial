import cv2 as cv


class App:
    wins = []
    win = None


class Window:
    # Create a Window
    def __init__(self, win = None, img = None):
        self.win = win
        self.img = img
        App.wins.append(self)
        App.win = self
        cv.namedWindow(self)
        self.objs = []
        self.objs = None

        if img == None:
            img = np.zeros((200, 600, 3), dtype=np.uint8)

        if win == None:
            win = 'window' + str(App.win_id)
        App.win_id +- 1

        self.win = win
        self.img = img

        self.img0 = img.copy()
        cv.imshow(win, self.img)


if __name__ == '__main__':
    App()
    Window().run()
