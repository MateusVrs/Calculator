import configuration as conf


def makeButton(text, **place_option):
    btn = conf.tk.Button(conf.root, text=text, relief='groove',
                         height=2, width=8,
                         font=conf.fontGeral, bg=conf.colorGeral)
    if text == '=':
        btn['bg'] = 'tomato'
    btn['activebackground'] = 'gray60'
    btn.place(place_option)
    return btn


def makeEntry():
    entry = conf.tk.Entry(conf.root, font=(
        'Consolas', 20), bg=conf.backGround, width='31', justify='right')
    entry.focus()
    entry.place(x=5, y=30)
    return entry


def makeFrame():
    frame = conf.tk.Frame(conf.root)
    frame.pack(side='top', fill='x')
    return frame


def makeLabel(master=None):
    label = conf.tk.Label(master, text='', font=conf.fontGeral, padx=5)
    return label
