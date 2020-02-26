import tkinter as tk
import logging
logging.basicConfig(filename='WhichKeyLog.log',level=logging.DEBUG,format='%(levelname)s:%(asctime)s:%(message)s')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.key = 'C'
        self.notes = 'C D E F G A B C'
        self.darkmode = False
        self.defaultbg = self.cget('bg')
        self.titlebar = True
        self.fullscreen = False
        self.defaultsize = root.geometry()
        self.create_buttons()

    def create_buttons(self):

        self.settings_button_img = tk.PhotoImage(file='button_settings.png')
        self.settings_button = tk.Button(self, image=self.settings_button_img)
        self.settings_button.grid(row=4,column=2)
        self.settings_button['border'] = '0'
        self.settings_button['command'] = self.showSettings
        self.settings_button.config(cursor='pencil')

        self.title = 'Find a key'
        self.winfo_toplevel().title(self.title)

        self.sharps_name = tk.Label(self)
        self.sharps_name['text'] = 'Sharps : '
        self.sharps_name.grid(row=2,column=1)

        self.sharps_input = tk.Entry(self)
        self.sharps_input.grid(row=2, column=2)
        self.sharps_input.bind('<Key-Return>', lambda event: self.findKey())

        self.flats_name = tk.Label(self)
        self.flats_name['text'] = 'Flats : '
        self.flats_name.grid(row=3, column=1)

        self.flats_input = tk.Entry(self)
        self.flats_input.grid(row=3, column=2)
        self.flats_input.bind('<Key-Return>', lambda event: self.findKey())

        self.submit_button_img = tk.PhotoImage(file='button_submit.png')
        self.submit_button = tk.Button(self, image=self.submit_button_img)
        self.submit_button['border'] = '0'
        self.submit_button['command'] = self.findKey
        self.submit_button.grid(row=4, column=1)

        self.answer_label = tk.Label(self)
        self.answer_label.grid(row=5,column=1)
        self.answer_label['text'] = 'You are in the key of : '

        self.answer_box = tk.Label(self)
        self.answer_box.grid(row=5,column=2)
        self.answer_box['text'] = self.key

        self.notes_label = tk.Label(self)
        self.notes_label.grid(row=6,column=1)
        self.notes_label['text'] = 'This key contains the notes : '

        self.notes_box = tk.Label(self)
        self.notes_box.grid(row=6,column=2)
        self.notes_box['text'] = self.notes

    def showSettings(self):
        self.settings_button.config(state='disabled')
        
        self.darkmode_button = tk.Button(self,width=20)
        self.darkmode_button['text'] = 'Dark mode (Experimental)'
        self.darkmode_button.grid(row=7,column=1)
        self.darkmode_button['command'] = self.toggleDarkMode

        self.hidesettings_button = tk.Button(self,width=16)
        self.hidesettings_button['text'] = 'Hide settings'
        self.hidesettings_button.grid(row=7,column=2)
        self.hidesettings_button['command'] = self.hideSettings
        self.hidesettings_button.config(cursor='x_cursor')

        self.quit_button = tk.Button(self,width=20)
        self.quit_button['text'] = 'Force quit'
        self.quit_button.grid(row=8,column=1)
        self.quit_button['command'] = self.master.destroy
        self.quit_button.config(cursor='x_cursor',fg='red')

        if self.titlebar == True:
            self.hidebar_button = tk.Button(self)
            self.hidebar_button.grid(row=8,column=2)
            self.hidebar_button['text'] = 'Hide top bar'
            self.hidebar_button['command'] = self.hideTopBar
            self.hidebar_button.config(width=16)

        if self.darkmode == True:
            self.darkmode_button.config(bg='black',fg='green')
            self.hidesettings_button.config(bg='black',fg='green')
            self.quit_button.config(bg='black',fg='green')
            self.hidebar_button.config(bg='black',fg='green')

    def hideTopBar(self):
        root.overrideredirect(True)
        self.hidebar_button.destroy()
        self.titlebar = False
        
        self.x_button = tk.Button(self)
        self.x_button.grid(row=1,column=3)
        self.x_button.config(fg='red')
        if self.darkmode == True:
            self.x_button.config(bg='black')
        elif self.darkmode == False:
            self.x_button.config(bg=self.defaultbg)
        else:
            print('Error: Could not decide if darkmode was true or false - it is set as ' + str(self.darkmode))
        self.x_button['command'] = self.master.destroy
        self.x_button['text'] = 'X'

        self.max_button_img = tk.PhotoImage(file='max_button_img.png')
        self.max_button = tk.Button(self, image=self.max_button_img,padx=100)
        self.max_button['command'] = self.toggleFullScreen
        self.max_button.grid(row=1,column=2)

    def toggleFullScreen(self):
        if self.fullscreen == False:
            root.geometry('1920x1080')
            self.fullscreen = True
        elif self.fullscreen == True:
            print('Could not exit fullscreen')
        else:
            print('Could not decide if fullscreen or not - self.fullscreen is ' + str(self.fullscreen))

    def hideSettings(self):
        self.darkmode_button.destroy()
        self.hidesettings_button.destroy()
        self.settings_button.config(state='normal')
        self.quit_button.destroy()
        self.hidebar_button.destroy()

    def toggleDarkMode(self):
        if self.darkmode == False:
            self.settings_button.config(state='disabled')
            self.darkmode = True
            self.config(bg='black')
            self.settings_button.config(bg='black',fg='green')
            self.sharps_name.config(bg='black', fg='green')
            self.sharps_input.config(bg='black', fg='green')
            self.flats_name.config(bg='black', fg='green')
            self.flats_input.config(bg='black', fg='green')
            self.answer_label.config(bg='black', fg='green')
            self.answer_box.config(bg='black', fg='green')
            self.notes_label.config(bg='black', fg='green')
            self.notes_box.config(bg='black', fg='green')
            self.hidesettings_button.config(bg='black', fg='green')
            self.darkmode_button['text'] = 'Light Mode'
            self.darkmode_button.config(bg='black', fg='green')
            self.quit_button.config(bg='black')
            self.darkmode_button.config(width=20)
            self.x_button.config(bg='black')
            try:
                self.hidebar_button.config(bg='black',fg='green')
            except:
                pass
        elif self.darkmode == True:
            self.darkmode = False
            self.x_button.config(bg=self.defaultbg)
            self.config(bg=self.defaultbg)
            self.darkmode_button['text'] = 'Dark Mode (Experimental)'
            self.darkmode_button.destroy()
            self.hidesettings_button.destroy()
            self.showSettings()
            self.create_buttons()
            self.settings_button.config(state='disabled')
            self.quit_button.config(bg=self.defaultbg)
            try:
                self.hidebar_button.config(bg=self.defaultbg,fg='black')
            except:
                pass
        else:
            pass

    def returnToNormal(self):
        self.sharps_input.config(state='normal')
        self.flats_input.config(state='normal')
        self.sharps_input.delete(first=0, last=100)
        self.flats_input.delete(first=0, last=100)

    def findKey(self):
        try:
            self.sharps = self.sharps_input.get()
            self.flats = self.flats_input.get()

            if self.sharps == '':
                self.sharps = 0
            else:
                pass

            if self.flats == '':
                self.flats = 0
            else:
                pass

            self.sharps = int(self.sharps)
            self.flats = int(self.flats)

            if self.sharps > 7 or self.sharps < 0:
                assert('Error')
                logging.info('Expected number of accidentals between 0 and 7, instead got {} sharps and {} flats'.format(self.sharps,self.flats))
                self.sharps_input.delete(first=0, last=100)
                self.flats_input.delete(first=0, last=100)
                self.sharps_input.insert(0, "You can't have more")
                self.flats_input.insert(0, "than 7 accidentals")
                self.sharps_input.config(state='disabled')
                self.flats_input.config(state='disabled')
                self.sharps_input.after(5000, lambda: self.returnToNormal())

            elif self.flats > 7 or self.sharps < 0:
                logging.info('Expected number of accidentals between 0 and 7, instead got {} sharps and {} flats'.format(self.sharps,self.flats))
                self.sharps_input.config(state='disabled')
                self.flats_input.config(state='disabled')
                self.sharps_input.delete(first=0, last=100)
                self.flats_input.delete(first=0, last=100)
                self.sharps_input.insert(0, "You can't have more")
                self.flats_input.insert(0, "than 7 accidentals")
                self.sharps_input.after(5000, lambda: self.returnToNormal())

            else:
                pass

            if self.sharps == 0 and self.flats == 0:
                self.key = 'Cmaj/Amin'
                self.notes = 'C D E F G A B C'
            elif self.sharps == 1 and self.flats == 0:
                self.key = 'Gmaj/Emin'
                self.notes = 'G A B C D E F# G'
            elif self.sharps == 2 and self.flats == 0:
                self.key = 'Dmaj/Bmin'
                self.notes = 'D E F# G A B C# D'
            elif self.sharps == 3 and self.flats == 0:
                self.key = 'Amaj/F#min'
                self.notes = 'A B C# D E F# G# A'
            elif self.sharps == 4 and self.flats == 0:
                self.key = 'Emaj/C#min'
                self.notes = 'E F# G# A B C# D# E'
            elif self.sharps == 5 and self.flats == 0:
                self.key = 'Bmaj/Abmin'
                self.notes = 'B Db Eb E Gb Ab Bb'
            elif self.sharps == 6 and self.flats == 0:
                self.key = 'F#maj/D#min'
                self.notes =  'F# G# A# B C# D# F F#'
            elif self.sharps == 7 and self.flats == 0:
                self.key = 'C#maj/Bbmin'
                self.notes = 'C# D# F F# G# A# C C#'
            elif self.sharps == 0 and self.flats == 1:
                self.key = 'Fmaj/Dmin'
                self.notes =  'F G A Bb C D E F'
            elif self.sharps == 0 and self.flats == 2:
                self.key = 'Bbmaj/Gmin'
                self.notes = 'Bb C D Eb F G A Bb'
            elif self.sharps == 0 and self.flats == 3:
                self.key = 'Ebmaj/Cmin'
                self.notes = 'Eb F G Ab Bb C D Eb'
            elif self.sharps == 0 and self.flats == 4:
                self.key = 'Abmaj/Fmin'
                self.notes = 'Ab Bb C Db Eb F G Ab'
            elif self.sharps == 0 and self.flats == 5:
                self.key = 'Dbmaj/Bbmin'
                self.notes = 'Db Eb F Gb Ab Bb C Db'
            elif self.sharps == 0 and self.flats == 6:
                self.key = 'Gbmaj/Ebmin'
                self.notes = 'Gb Ab Bb Cb Db Eb F Gb'
            elif self.sharps == 0 and self.flats == 7:
                self.key = 'Cbmaj/Abmin'
                self.notes = 'B Db Eb E Gb Ab Bb'
            else:
                self.answer_box['text'] = ''
                self.notes_box['text'] = ''
                print('Could not identify key.')
                self.key = 'UNKNOWN'
                self.notes = 'UNKNOWN'
                logging.info('Could not identify key')
            logging.info('Identified key as {}, notes are {}'.format(self.key,self.notes))

            self.keystr = self.key
            self.notesstr = self.notes
            self.answer_box['text'] = self.keystr
            self.notes_box['text'] = self.notesstr

            self.sharps_input.delete(first=0, last=100)
            self.flats_input.delete(first=0, last=100)
        except ValueError as value_error:
            print('ValueError : ' + str(value_error))
            logging.error('ValueError : {}'.format(str(value_error)))


root = tk.Tk()
logging.info('Started')
app = Application(master=root)
app.mainloop()
