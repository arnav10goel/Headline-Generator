from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from textteaser import TextTeaser
import random
import markovgen

app = Tk()
app.title("LINGUA")
app.geometry("750x600")
app.configure(background = '#D1CF29')

class Markov(object):

    def __init__(self, open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()


    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words


    def triples(self):
        """ Generates triples from the given data string. So if our string were
                "What a lovely day", we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_headline(self, size=25):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words) 

def Headline_Generator():
    User_Txt = yourTxt.get()
    file_ = open(User_Txt,'r')
    markov = markovgen.Markov(file_)
    User_Headline = markov.generate_markov_headline()
    messagebox.showinfo("Here is a Possible Headline: ", User_Headline)
    return

def TextSummariser():
    title = yourTitle.get()
    text = yourText.get()
    tt = TextTeaser()
    sentences = tt.summarize(title, text)
    messagebox.showinfo("Here is the Summarised Text:   ", sentences)
    return

def Censor():
    a = yourWord.get()
    text = yourText2.get()
    word = a.lower()
    word1 = text.lower()
    words = word1.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)
    messagebox.showinfo("Here is the Censored Text:   ", result)
    return


Head_label1 = StringVar()
Head_label1.set("TEXT SUMMARISER")
Head_label = Label(app, textvariable = Head_label1, height = 3, font = 'sans_serif 15 bold', fg = '#193541', bg = '#D1CF29')
Head_label.pack()

labelText = StringVar()
labelText.set("Type in Your Text's Title Below:")
label = Label(app, textvariable = labelText, height = 2, font = 'sans_serif 13', fg = 'black', bg = '#D1CF29')
label.pack()

custText = StringVar(None)
yourTitle = Entry(app, textvariable = custText)
yourTitle.pack()

label_Text = StringVar()
label_Text.set("Type in Your Text Below and Click the Button Below for Summarisation:")
label1 = Label(app, textvariable = label_Text, height = 2, font = 'sans_serif 13', fg = 'black', bg = '#D1CF29')
label1.pack()

custText1 = StringVar(None)
yourText = Entry(app, textvariable = custText1, width = "100")
yourText.pack()

button1 = Button(app, text = "Click Here for Summarising your Text", width = "40", font = 'sans_serif 14 bold',fg = '#BBD3DF', bg = '#220900', command = TextSummariser)
button1.pack()

Head_label2 = StringVar()
Head_label2.set("CENSORER")
Head_label1 = Label(app, textvariable = Head_label2, height = 3, font = 'sans_serif 15 bold', fg = '#193541', bg = '#D1CF29')
Head_label1.pack()

labelText2 = StringVar()
labelText2.set("Type in the Word which you would like to get Censored:")
label2 = Label(app, textvariable = labelText2, height = 2, font = 'sans_serif 13', fg = 'black', bg = '#D1CF29')
label2.pack()

custText2 = StringVar(None)
yourWord = Entry(app, textvariable = custText2)
yourWord.pack()

labelText3 = StringVar()
labelText3.set("Type in Your Text Below and Click the Button Below for Censoring it:")
label1 = Label(app, textvariable = labelText3, height = 2, font = 'sans_serif 13', fg = 'black', bg = '#D1CF29')
label1.pack()

custText3 = StringVar(None)
yourText2 = Entry(app, textvariable = custText3, width = "100")
yourText2.pack()

button2 = Button(app, text = "Click Here for Censoring your Text", width = "40", font = 'sans_serif 14 bold',fg = '#BBD3DF', bg = '#220900', command = Censor)
button2.pack()

Head_label3 = StringVar()
Head_label3.set("HEADLINE GENERATOR")
Head_label2 = Label(app, textvariable = Head_label3, height = 3, font = 'sans_serif 15 bold', fg = '#193541', bg = '#D1CF29')
Head_label2.pack()

labelText4 = StringVar()
labelText4.set("Type in the Path of your Txt File:")
label2 = Label(app, textvariable = labelText4, height = 2, font = 'sans_serif 13', fg = 'black', bg = '#D1CF29')
label2.pack()

custText4 = StringVar(None)
yourTxt = Entry(app, textvariable = custText4, width = "100")
yourTxt.pack()

button3 = Button(app, text = "Click Here for Generating a Possible Headline", width = "40", font = 'sans_serif 14 bold',fg = '#BBD3DF', bg = '#220900', command = Headline_Generator )
button3.pack()

app.mainloop()
 
