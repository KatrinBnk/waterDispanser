import sys
import tkinter
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

class consT:
    W_app = 1000
    H_app = 700
    font_app = '#D9D9D9'
    font_market = '#FFFFFF'
    font_button = '#6B5F5F'

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.img()
        self.title('Water Market')
        self.geometry("1000x700")
        self.resizable(False, False)
        self.canvas = Canvas(self,
                             width=consT.W_app, height=consT.H_app,
                             bg=consT.font_app)
        self.canvas.pack()

        self.canvas.create_rectangle(100, 20, 100 + 320, 40 + 640, fill=consT.font_market, outline='')
        self.canvas.create_image(100, 20, anchor=NW, image=self.water)

        square_center_x = (100 + 100 + 320) / 2

        self.canvas.create_text(square_center_x, 155,
                                font=("Arial", 15, "bold"), fill="black", anchor=tkinter.CENTER,
                                text="Дыхание родника\n Water dispanser")
        self.canvas.create_rectangle(square_center_x-90, 200, square_center_x +150, 240, fill=consT.font_app, outline='')


        self.canvas.create_rectangle(120-10, 300-20, 300-10, 520, fill=consT.font_app, outline='')
        self.canvas.create_rectangle(300, 300-20, 410, 520, fill=consT.font_app, outline='')

        self.canvas.create_text((300+410)/2, (300-20+520)/2-20,
                                font=("Arial", 12, "bold"), fill="black", anchor=tkinter.CENTER,
                                text=" Информация\n 1л — 5р\n 5л — 20р\n 9л — 35p")

        self.canvas.create_rectangle(200, 600, 415, 675, fill=consT.font_app, outline='')
        self.canvas.create_text((200 + 415) / 2, (600 + 675) / 2,
                                font=("Arial", 12, "bold"), fill="black", anchor=tkinter.CENTER,
                                text="Приложите карту")

        self.canvas.create_image(100, 600-20, anchor=NW, image=self.bottle_2)

        self.button_start = tkinter.Button(self.canvas, text="пуск/старт", width=14, height=2,
                                           command=self.button_clicked)
        self.button_start.place(x=300, y=480)

        # Кнопка 1
        self.button1 = tkinter.Button(self.canvas, text="Кнопка 1", width=80, height=80,
                                      command=self.button_clicked, relief=tkinter.SOLID, bg="red")
        self.button1.place(x=300, y=440)

        # Кнопка 2
        self.button2 = tkinter.Button(self.canvas, text="Кнопка 2", width=80, height=80,
                                      command=self.button_clicked, relief=tkinter.SOLID, bg="green")
        self.button2.place(x=400, y=440)

        # Кнопка 3
        self.button3 = tkinter.Button(self.canvas, text="Кнопка 3", width=80, height=80,
                                      command=self.button_clicked, relief=tkinter.SOLID, bg="blue")
        self.button3.place(x=500, y=440)

    def button_clicked(self):
        print("Кнопка нажата")

    def img(self):
        self.bottle = Image.open('bottle.png')
        self.bottle_2 = Image.open('BottlTwo.png')
        self.bottle_2 = self.bottle_2.resize((90, 100))
        self.bottle_2 = ImageTk.PhotoImage(self.bottle_2)
        self.water = Image.open('water.png')
        self.water = self.water.resize((320, 100))
        self.water = ImageTk.PhotoImage(self.water)



def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()