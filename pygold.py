from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess
import webbrowser

window = Tk()

window.title("PyGold - Python IDE")
menu = Menu(window)
window.config(menu=menu)
 
editor = ScrolledText(window, font=("Futura"), wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
editor.insert(INSERT, "#Put Your Code Here! ")
file_path = ""


def gnosd():
    gbos = 'https://www.google.com/search?q=best+operating+systems&rlz=1C1CHBF_enUS728US728&sxsrf=APq-WBvfpNz4H9YssjaGFOGUGjBAguy3vw%3A1646095972190&ei=ZG4dYqXdCpedptQPxZe68AM&ved=0ahUKEwiln8Ct2aP2AhWXjokEHcWLDj4Q4dUDCA4&uact=5&oq=best+operating+systems&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABBDMgUIABCABDIFCAAQgAQ6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6EgguEMcBEKMCEMgDELADEEMYAToPCC4Q1AIQyAMQsAMQQxgBSgQIQRgASgQIRhgBULIHWLIHYJgLaAFwAXgAgAFliAFlkgEDMC4xmAEAoAEByAERwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz'

    webbrowser.open_new_tab(gbos)
    webbrowser.open_new(gbos)

def wirs():
    root = Tk()
    root.title("PyGold > Help > Window Size Too Big")
    root.geometry("400x100")

    rs = Label(root, text="Try Resizing The App")
    rs.pack()

    fs = Label(root, text="Try Fullscreening The App")
    fs.pack()

    gnos = Button(root, text="If None Of That Works, Get A Better Oparting System", command=gnosd)
    gnos.pack()

    root.mainloop()


def discord():
    url = 'https://discord.gg/R5vThQJQcs'

    webbrowser.open_new_tab(url)

    webbrowser.open_new(url)

def wcnr():
    root = Tk()
    root.title("PyGold > Help > Word Color Isn't Right")
    root.geometry("500x100")

    sol3 = Label(root, text="Try Going Through All The Themes Until It Is The Right Color")
    sol3.pack()

    sol4 = Label(root, text="Try Saving The File, Then Restart The App, Then Open The App Again")
    sol4.pack()

    sug2 = Button(root, text="If None Of That Works, Join Our Discord Server!", command=discord)
    sug2.pack()

    root.mainloop()

def DBU():
	DBUWIN = Tk()
	DBUWIN.title("PyGold > Discord > Discord Bots Used")
	Label(DBUWIN, text="Discord Bots Used: Dank Memer, Ticket Tool, Dyno").pack()
	Label(DBUWIN, text="Discord Buts Used With Mod Permissions: Dyno").pack()
	Label(DBUWIN, text="We May Have Put In More Bots Since Last Update Realeased Or Installed").pack()

def disable():
    window.attributes('-fullscreen', False)

def enable():
    window.attributes('-fullscreen', True)

def theme_settings():
    root = Tk()
    root.title("PyGold > Settings > Theme Settings")
    root.geometry("400x200")

    dark_theme_btn = Button(root, text="          Dark          ", command=dark)
    dark_theme_btn.pack()

    dark_theme_btn = Button(root, text="          Light          ", command=light)
    dark_theme_btn.pack()

    dark_theme_btn = Button(root, text="          PictureIt Creations          ", command=pic)
    dark_theme_btn.pack()

    dark_theme_btn = Button(root, text="          Extra Dark          ", command=exdark)
    dark_theme_btn.pack()

    root.mainloop()

def main_settings():
    root = Tk()
    root.title("Pygold > Settings")
    root.geometry("400x200")

    theme_button = Button(root, text="          Theme          ", command=theme_settings)
    theme_button.pack()

    root.mainloop()
    

def pirs():
    root = Tk()
    root.title("PyGold > Help > Program Isn't Running")
    root.geometry("400x100")

    sol = Label(root, text="Try Saving The File manually.")
    sol.pack()

    sol2 = Label(root, text="If That Does Not Work Try Restarting The App")
    sol2.pack()

    sug1 = Label(root, text="If None Of That Works, Join Our Discord Server")
    sug1.pack()
    
    root.mainloop()

def about():
    root = Tk()
    root.title("PyGold > About")
    root.geometry("400x200")
    
    date = Label(root, text="development started 1/22/2022")
    date.pack()

    imports = Label(root, text="Made With Tkinter And Subprocess")
    imports.pack()

    creator = Label(root, text="Made By Noah McCracken")
    creator.pack()

    programming = Label(root, text="Made 100% By Python")
    programming.pack()

    ver = Label(root, text="Version 1.0.0")

    influ = Label(root, text="Influenced By Python IDLE / Thonny Python IDE")
    influ.pack()

    ninflu = Label(root, text="Name Influenced By PyCharm")
    ninflu.pack()
    
    root.mainloop()

def helph():
    root = Tk()
    root.title("PyGold > Help")
    root.geometry("450x100")

    pir = Button(root, text="Program Isn't Running", command=pirs)
    pir.pack()

    wcnrf = Button(root, text="Text Is Wrong Color", command=wcnr)
    wcnrf.pack()

    wirsf = Button(root, text="Window Size Is Too Big", command=wirs)
    wirsf.pack()

    #Have The 'sug3' Variable At The End

    sug3 = Button(root, text="Can't Find The Problem Your Looking For? Join Our Discord!", command=discord)
    sug3.pack()

    

    root.mainloop()

def open_file(event=None):
    global code, file_path

    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
window.bind("<Control-o>", open_file)

def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-s>", save_file)

def save_as(event=None):
    global code, file_path
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
window.bind("<Control-S>", save_as)

def run(event=None):
    global code, file_path, code, file_path

    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 

    
    '''
    code = editor.get(1.0, END)
    exec(code)
    '''    
    cmd = f"python {file_path}"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error =  process.communicate()

    output_window.delete(1.0, END)

    output_window.insert(1.0, output)

    output_window.insert(1.0, error)
window.bind("<Control-s>", save_file)
window.bind("<F5>", run)

def close(event=None):
    window.destroy()
window.bind("<Control-q>", close)

def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))

def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))

def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
     

file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
help_menu = Menu(menu, tearoff=0)
settings_menu = Menu(menu, tearoff=0)
discord_menu = Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label="View", menu=view_menu)
menu.add_cascade(label="Help", menu=help_menu)
menu.add_cascade(label="Settings", menu=settings_menu)
menu.add_cascade(label="Discord", menu=discord_menu)


file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)

edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

run_menu.add_command(label="Run", accelerator="F5", command=run)

discord_menu.add_command(label="Discord Invite (Never Expires!)", command=discord)
discord_menu.add_separator()
discord_menu.add_command(label="Discord Bots Used", command=DBU)

help_menu.add_command(label="About Pygold", command=about)
help_menu.add_separator()
help_menu.add_command(label="PyGold Help", command=helph)


show_status_bar = BooleanVar()
show_status_bar.set(True)
def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=BOTTOM)
        show_status_bar = True
        
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = 0,variable = show_status_bar , command = hide_statusbar)

status_bars = ttk.Label(window,text = " \t\t\t\t\t\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)

text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text = f"\t\t\t\t\t\t characters: {chararcter} words: {word}")
    editor.edit_modified(False)
editor.bind("<<Modified>>",change_word)

def pic():
    editor.config(bg="teal", fg="white")
    output_window.config(bg="teal", fg="white")

def exdark():
    editor.config(bg="black", fg="white")
    output_window.config(bg="black", fg="white")

def light():
    editor.config(bg="white")
    output_window.config(bg="white")

def dark():
    editor.config(fg="black", bg="dark grey")
    output_window.config(fg="black", bg="dark grey")

def disable():
    window.attributes('-fullscreen', False)

def enable():
    window.attributes('-fullscreen', True)


output_window = ScrolledText(window, height=10)
output_window.pack(fill=BOTH, expand=1)
window.mainloop()

