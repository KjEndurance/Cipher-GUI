import CaesarCipher as cp
from tkinter import Tk, Frame, Label, Text, Button, Menu


class caesarCipherGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.constructGUI()

    def constructGUI(self):
        self.parent.title("Encryption Software")
        self.parent.geometry("700x700+100+100")
        encryptLabel = Label(self.parent, text="Message to Encrypt")
        encryptLabel.place(x=10, y=10)

        decryptLabel = Label(self.parent, text="Message to Decrypt")
        decryptLabel.place(x=570, y=10)

        #Encrypt/Decrypt Text Boxes
        self.encryptText = Text(self.parent, width=40, height=20, wrap='word')
        self.encryptText.place(x=10, y=40)

        self.resultText = Text(self.parent, width=40, height=20, wrap='word')
        self.resultText.place(x=360, y=40)

        #Encrypt/Decrypt Buttons
        self.encryptButton = Button(self.parent, text='Encrypt Message', command=self.encryptPressed)
        self.encryptButton.place(x=80, y=400)

        self.decryptButton = Button(self.parent, text='Decrypt Message', command=self.decryptPressed)
        self.decryptButton.place(x=500, y=400)

        #Keypad
        self.button1 = Button(self.parent, text='1')
        self.button1.config(command= lambda: self.numberPressed(self.button1.cget('text')))
        self.button1.place(x=325, y=530)

        self.button2 = Button(self.parent, text='2')
        self.button2.config(command= lambda: self.numberPressed(self.button2.cget('text')))
        self.button2.place(x=350, y=530)

        self.button3 = Button(self.parent, text='3')
        self.button3.config(command= lambda: self.numberPressed(self.button3.cget('text')))
        self.button3.place(x=375, y=530)

        self.button4 = Button(self.parent, text='4')
        self.button4.config(command= lambda: self.numberPressed(self.button4.cget('text')))
        self.button4.place(x=325, y=565)

        self.button5 = Button(self.parent, text='5')
        self.button5.config(command= lambda: self.numberPressed(self.button5.cget('text')))
        self.button5.place(x=350, y=565)

        self.button6 = Button(self.parent, text='6')
        self.button6.config(command= lambda: self.numberPressed(self.button6.cget('text')))
        self.button6.place(x=375, y=565)

        self.button7 = Button(self.parent, text='7')
        self.button7.config(command= lambda: self.numberPressed(self.button7.cget('text')))
        self.button7.place(x=325, y=600)

        self.button8 = Button(self.parent, text='8')
        self.button8.config(command= lambda: self.numberPressed(self.button8.cget('text')))
        self.button8.place(x=350, y=600)

        self.button9 = Button(self.parent, text='9')
        self.button9.config(command= lambda: self.numberPressed(self.button9.cget('text')))
        self.button9.place(x=375, y=600)

        self.button0 = Button(self.parent, text='0')
        self.button0.config(command= lambda: self.numberPressed(self.button0.cget('text')))
        self.button0.place(x=350, y=635)

        self.numpadBackspace = Button(self.parent, text='<--', command=self.backspacePressed)
        self.numpadBackspace.place(x=300, y=635)

        self.numpadClear = Button(self.parent, text='CLR', command=self.clearPressed)
        self.numpadClear.place(x=380, y=635)

        self.numpadDisplay = Text(self.parent, width=12, height=1, state='disabled')
        self.numpadDisplay.place(x=310, y=490)

        numpadLabel = Label(self.parent, text='Enter key for Encryption and Decryption')
        numpadLabel.place(x=260, y=460)

    def encryptPressed(self):
        PIN = self.numpadDisplay.get('1.0', 'end-1c')
        if len(PIN) > 0:
            message = self.encryptText.get('1.0', 'end-1c')
            encrypted = cp.encrypt(message, int(PIN))
            self.resultText.delete('1.0', 'end')
            self.resultText.insert('1.0', encrypted)

    def decryptPressed(self):
        PIN = self.numpadDisplay.get('1.0', 'end-1c')
        if len(PIN) > 0:
            message = self.resultText.get('1.0', 'end-1c')
            decrypted = cp.decrypt(message, int(PIN))
            self.encryptText.delete('1.0', 'end')
            self.encryptText.insert('1.0', decrypted)

    def numberPressed(self, num):
        PIN = self.numpadDisplay.get('1.0', 'end-1c')
        if len(PIN) < 12:
            self.numpadDisplay.config(state='normal')
            self.numpadDisplay.insert('end', num)
            print(int(num))
            self.numpadDisplay.config(state='disabled')

    def backspacePressed(self):
        PIN = self.numpadDisplay.get('1.0', 'end-1c')
        if len(PIN) > 0:
            self.numpadDisplay.config(state='normal')
            self.numpadDisplay.delete('1.0', 'end-1c')
            self.numpadDisplay.insert('1.0', PIN[:-1])
            self.numpadDisplay.config(state='disabled')

    def clearPressed(self):
        self.numpadDisplay.config(state='normal')
        self.numpadDisplay.delete('1.0', 'end-1c')
        self.numpadDisplay.config(state='disabled')




root = Tk()
GUI = caesarCipherGUI(root)
root.mainloop()