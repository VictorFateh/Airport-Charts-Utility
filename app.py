import threading
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import charts


class ChartsApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("Chart Downloader")
        self.geometry('600x200+500+300')
        self.btn = Button(self, text='Download', command=self.download)
        self.btn.grid(row=0, column=2)
        self.progress = Progressbar(self, orient=HORIZONTAL, length=185, mode='indeterminate')
        self.lbl = Label(self, text="Separate ICAOs by spaces")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(self, width=30)
        self.txt.grid(column=1, row=0)

    def download(self):
        def start_download():
            self.btn['state'] = 'disabled'
            self.txt.grid_remove()
            self.progress.grid(row=0, column=1)
            self.progress.start()
            charts.start_download(user_list)
            self.progress.stop()
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
