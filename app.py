import threading
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import *
import easygui

import os
import charts


class ChartsApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("Chart Downloader")
        self.geometry('600x200+500+300')
        self.data_file_path = easygui.diropenbox()
        self.btn = Button(self, text='Download', command=self.download)
        self.btn.grid(row=0, column=2)
        self.progress = Progressbar(self, orient=HORIZONTAL, length=185, mode='determinate')
        self.lbl = Label(self, text="Separate ICAOs by spaces")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self, width=30)
        self.txt.grid(column=1, row=0)
        self.airport_text = Label(self, text="")
        self.airport_text.grid(row=2, column=0)
        self.chart_text = Label(self, text="")
        self.chart_text.grid(row=2, column=1)

    def download(self):
        def start_download():
            print(self.data_file_path)
            self.btn['state'] = 'disabled'
            self.txt.grid_remove()
            self.progress.grid(row=0, column=1)
            charts.start_download(self, user_list, self.data_file_path)
            self.btn.grid_remove()
            self.lbl['text'] = 'Done'
            self.progress.grid_forget()

        user_input = self.txt.get().strip()
        user_list = user_input.split(' ')
        res = list_checks(user_list)
        if res[0]:
            threading.Thread(target=start_download).start()
        else:
            messagebox.showerror("Error", res[1])


def list_checks(raw_list):
    if raw_list[0] != '':
        if all(len(x) == len(raw_list[0]) for x in raw_list):
            return True, None
        return False, "Not all items are the same length"
    return False, "List is empty"


if __name__ == "__main__":
    app = ChartsApp()
    app.mainloop()
