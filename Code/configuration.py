import tkinter as tk
import calculate as calc
import functions as func

fontGeral = ('Consolas', '14')
colorGeral = 'gray87'
backGround = 'gray95'

strButtons = [['7', '8', '9', '/', '*'], ['4', '5', '6', '-', '+'],
              ['1', '2', '3', '(', ')'], ['C', '0', '.', '^', '=']]
buttonPosx = [5, 100, 195, 290, 385]
buttonPosy = [80, 150, 220, 290]
listButton = []


class Application():

    def __init__(self, master=None):
        for sList, py in zip(strButtons, buttonPosy):
            for string, px in zip(sList, buttonPosx):
                listButton.append(func.makeButton(string, x=px, y=py))
        self.oldExp = func.makeEntry()
        self.oldExp.bind('<Return>', self.entryResult)
        self.oldExp.bind('<Key>', self.entryReturn)

        self.configButton()
        self.configFrame()
        self.janelaConfig()

    def janelaConfig(self):
        img = tk.PhotoImage(file='Images/calculator.png')
        root.iconphoto(False, img)
        root.title('Calculator')
        root.configure(bg=backGround)
        # root.overrideredirect(True) -> Without menu bar
        root.geometry('480x380+450+200')
        root.resizable(False, False)

    def configButton(self):
        for button in listButton:
            if button['text'] == 'C':
                button.bind('<Button-1>', self.entryDelete)
            elif button['text'] == '=':
                button.bind('<Button-1>', self.entryResult)
            else:
                button.bind('<Button-1>', self.entryReturn)

    def configFrame(self):
        returnFrame = func.makeFrame()
        self.returnExp = func.makeLabel(returnFrame)
        self.returnExp.pack(side='right')

    def entryReturn(self, event=None):
        if self.oldExp.get().isalpha():
            self.entryDelete()
        self.oldExp.insert('end', event.widget['text'])

    def entryDelete(self, event=None):
        self.oldExp.delete(0, 'end')

    def entryResult(self, event=None):
        result = calc.returnResult(self.oldExp.get())
        self.returnExp['text'] = self.oldExp.get(
        ) + ' =' if result != 'Erro' else ''
        self.entryDelete()
        self.oldExp.insert('end', result)


root = tk.Tk()
Application(root)
