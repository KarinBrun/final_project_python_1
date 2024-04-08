from final_project.finalcharacter import Character
from final_project.finalrandom import *
from final_project.finalexceptions import *
import tkinter
from PIL import Image, ImageTk
import tkinter.font as font


def click_helm_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Choose a helm")
    new_window.geometry("300x150")

    def clicked_helm(helm_name):
        helm_label['text'] = helm_name
        canvas1.itemconfigure(helm_label_window, state='normal')
        character.update_helm(helm_name)
        new_window.destroy()

    for helm in VALID_HELMS:
        button = tkinter.Button(new_window, text=helm, command=lambda x=helm: clicked_helm(x))
        button.pack()


def click_weapon_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Choose a weapon")
    new_window.geometry("300x200")

    def clicked_weapon(weapon_name):
        weapon_label['text'] = weapon_name
        canvas1.itemconfigure(weapon_label_window, state='normal')
        character.update_weapon(weapon_name)
        new_window.destroy()

    for weapon in VALID_WEAPONS:
        button = tkinter.Button(new_window, text=weapon, command=lambda x=weapon: clicked_weapon(x))
        button.pack()


def click_chest_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Choose a chest")
    new_window.geometry("300x130")

    def clicked_chest(chest_name):
        chest_label['text'] = chest_name
        canvas1.itemconfigure(chest_label_window, state='normal')
        character.update_chest(chest_name)
        new_window.destroy()

    for chest in VALID_CHESTS:
        button = tkinter.Button(new_window, text=chest, command=lambda x=chest: clicked_chest(x))
        button.pack()


def click_gloves_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Choose gloves")
    new_window.geometry("300x130")

    def clicked_gloves(gloves_name):
        gloves_label['text'] = gloves_name
        canvas1.itemconfigure(gloves_label_window, state='normal')
        character.update_gloves(gloves_name)
        new_window.destroy()

    for gloves in VALID_GLOVES:
        button = tkinter.Button(new_window, text=gloves, command=lambda x=gloves: clicked_gloves(x))
        button.pack()


def click_boots_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Choose boots")
    new_window.geometry("300x130")

    def clicked_boots(boots_name):
        boots_label['text'] = boots_name
        canvas1.itemconfigure(boots_label_window, state='normal')
        character.update_boots(boots_name)
        new_window.destroy()

    for boots in VALID_BOOTS:
        button = tkinter.Button(new_window, text=boots, command=lambda x=boots: clicked_boots(x))
        button.pack()


def update_name_gui(event):
    try:
        character.update_name(name_text.get())
    except InvalidInputCharacters:
        name_text.set(" ")
        new_window = tkinter.Toplevel(m)
        new_window.title("Invalid Characters")
        new_window.geometry("500x45")
        label = tkinter.Label(new_window, text="Invalid Character Input in Name", font=myFont)
        label.pack()


def update_race_gui(event):
    try:
        character.update_race(race_text.get())
    except InvalidInputCharacters:
        race_text.set(" ")
        new_window = tkinter.Toplevel(m)
        new_window.title("Invalid Characters")
        new_window.geometry("500x45")
        label = tkinter.Label(new_window, text="Invalid Character Input in Race", font=myFont)
        label.pack()


def update_class_gui(event):
    try:
        character.update_char_class(class_text.get())
    except InvalidInputCharacters:
        class_text.set(" ")
        new_window = tkinter.Toplevel(m)
        new_window.title("Invalid Characters")
        new_window.geometry("500x45")
        label = tkinter.Label(new_window, text="Invalid Character Input in Class", font=myFont)
        label.pack()


def update_background_gui(event):
    new_background = background_textbox.get("1.0", tkinter.END).replace("\n", "")
    character.update_background(new_background)


def clicked_random_button():
    name = random_name()
    name_text.set(name)
    character.update_name(name)
    race = random_race()
    race_text.set(race)
    character.update_race(race)
    char_class = random_class()
    class_text.set(char_class)
    character.update_char_class(char_class)
    background = random_background()
    background_textbox.delete("1.0", tkinter.END)
    background_textbox.insert("1.0", background)
    character.update_background(background)
    helm = random_helm()
    helm_label['text'] = helm
    canvas1.itemconfigure(helm_label_window, state='normal')
    character.update_helm(helm)
    weapon = random_weapon()
    weapon_label['text'] = weapon
    canvas1.itemconfigure(weapon_label_window, state='normal')
    character.update_weapon(weapon)
    chest = random_chest()
    chest_label['text'] = chest
    canvas1.itemconfigure(chest_label_window, state='normal')
    character.update_chest(chest)
    gloves = random_gloves()
    gloves_label['text'] = gloves
    canvas1.itemconfigure(gloves_label_window, state='normal')
    character.update_gloves(gloves)
    boots = random_boots()
    boots_label['text'] = boots
    canvas1.itemconfigure(boots_label_window, state='normal')
    character.update_boots(boots)


def clicked_create_button():
    global character
    character = Character("Diadem", "Staff", "Mail", "Cloth", "Leather", " ", " ", " ", " ")
    name_text.set(character.name)
    race_text.set(character.race)
    class_text.set(character.char_class)
    background_textbox.delete("1.0", tkinter.END)
    background_textbox.insert("1.0", character.background)
    canvas1.itemconfigure(helm_label_window, state='hidden')
    canvas1.itemconfigure(weapon_label_window, state='hidden')
    canvas1.itemconfigure(chest_label_window, state='hidden')
    canvas1.itemconfigure(gloves_label_window, state='hidden')
    canvas1.itemconfigure(boots_label_window, state='hidden')


def clicked_save_button():
    character.save_character()
    print(character.display())
    canvas1.itemconfigure(saved_label_window, state='normal')
    canvas1.after(3000, hide_saved_label)


def hide_saved_label():
    canvas1.itemconfigure(saved_label_window, state='hidden')


def clicked_load_button():
    new_window = tkinter.Toplevel(m)
    new_window.title("Load Character")
    new_window.geometry("500x400")
    characters = Character.all_characters()

    def clicked_char(char):
        global character
        character = Character(char[1], char[2], char[3], char[4], char[5], char[6], char[7], char[8], char[9], char[0])
        print(character.display())
        name_text.set(character.name)
        race_text.set(character.race)
        class_text.set(character.char_class)
        background_textbox.delete("1.0", tkinter.END)
        background_textbox.insert("1.0", character.background)
        helm_label['text'] = character.helm
        canvas1.itemconfigure(helm_label_window, state='normal')
        weapon_label['text'] = character.weapon
        canvas1.itemconfigure(weapon_label_window, state='normal')
        chest_label['text'] = character.chest
        canvas1.itemconfigure(chest_label_window, state='normal')
        gloves_label['text'] = character.gloves
        canvas1.itemconfigure(gloves_label_window, state='normal')
        boots_label['text'] = character.boots
        canvas1.itemconfigure(boots_label_window, state='normal')
        new_window.destroy()

    for char in characters:
        button = tkinter.Button(new_window, text=char[6], command=lambda x=char: clicked_char(x))
        button.pack()


m = tkinter.Tk()
m.title("Character Creator")
myFont = font.Font(size=20)

image = Image.open("146257.png")
img = image.resize((350, 700))
my_img = ImageTk.PhotoImage(img)
canvas1 = tkinter.Canvas(m, width=1100, height=750)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(70, 40, image=my_img, anchor="nw")

button_helm = tkinter.Button(m, text="Helm", font=myFont, command=click_helm_button)
button_helm_window = canvas1.create_window(200, 0, anchor='nw', window=button_helm)
helm_label = tkinter.Label(m, text="Null", font=myFont, fg="blue")
helm_label_window = canvas1.create_window(300, 5, anchor='nw', window=helm_label, state='hidden')

button_weapon = tkinter.Button(m, text="Weapon", font=myFont, command=click_weapon_button)
button_weapon_window = canvas1.create_window(15, 125, anchor='nw', window=button_weapon)
weapon_label = tkinter.Label(m, text="Null", font=myFont, fg="blue")
weapon_label_window = canvas1.create_window(15, 175, anchor='nw', window=weapon_label, state='hidden')

button_chest = tkinter.Button(m, text="Chest", font=myFont, command=click_chest_button)
button_chest_window = canvas1.create_window(345, 225, anchor='nw', window=button_chest)
chest_label = tkinter.Label(m, text="Null", font=myFont, fg="blue")
chest_label_window = canvas1.create_window(450, 230, anchor='nw', window=chest_label, state='hidden')

button_gloves = tkinter.Button(m, text="Gloves", font=myFont, command=click_gloves_button)
button_gloves_window = canvas1.create_window(5, 400, anchor='nw', window=button_gloves)
gloves_label = tkinter.Label(m, text="Null", font=myFont, fg="blue")
gloves_label_window = canvas1.create_window(10, 450, anchor='nw', window=gloves_label, state='hidden')

button_boots = tkinter.Button(m, text="Boots", font=myFont, command=click_boots_button)
button_boots_window = canvas1.create_window(355, 650, anchor='nw', window=button_boots)
boots_label = tkinter.Label(m, text="Null", font=myFont, fg="blue")
boots_label_window = canvas1.create_window(460, 655, anchor='nw', window=boots_label, state='hidden')

name_label = tkinter.Label(m, text="Name:", font=myFont)
name_label_window = canvas1.create_window(600, 10, anchor='nw', window=name_label)

name_text = tkinter.StringVar()
name_entry = tkinter.Entry(m, fg='black', bg='white', font=myFont, textvariable=name_text)
name_entry.bind('<Leave>', update_name_gui)
name_entry.bind('<FocusOut>', update_name_gui)
name_entry_window = canvas1.create_window(690, 10, anchor='nw', window=name_entry)

race_label = tkinter.Label(m, text="Race:", font=myFont)
race_label_window = canvas1.create_window(600, 60, anchor='nw', window=race_label)

race_text = tkinter.StringVar()
race_entry = tkinter.Entry(m, fg='black', bg='white', font=myFont, textvariable=race_text)
race_entry.bind('<Leave>', update_race_gui)
race_entry.bind('<FocusOut>', update_race_gui)
race_entry_window = canvas1.create_window(690, 60, anchor='nw', window=race_entry)

class_label = tkinter.Label(m, text="Class:", font=myFont)
class_label_window = canvas1.create_window(600, 110, anchor='nw', window=class_label)

class_text = tkinter.StringVar()
class_entry = tkinter.Entry(m, fg='black', bg='white', font=myFont, textvariable=class_text)
class_entry.bind('<Leave>', update_class_gui)
class_entry.bind('<FocusOut>', update_class_gui)
class_entry_window = canvas1.create_window(690, 110, anchor='nw', window=class_entry)

background_label = tkinter.Label(m, text="Background:", font=myFont)
background_label_window = canvas1.create_window(600, 160, anchor='nw', window=background_label)

background_textbox = tkinter.Text(m, fg='black', bg='white', font=myFont, height=10, width=26, wrap=tkinter.WORD)
background_textbox.bind('<Leave>', update_background_gui)
background_textbox.bind('<FocusOut>', update_background_gui)
background_textbox_window = canvas1.create_window(600, 200, anchor='nw', window=background_textbox)

image2 = Image.open("dice.jpg")
img2 = image2.resize((50, 35))
my_img2 = ImageTk.PhotoImage(img2)

button_random = tkinter.Button(m, image=my_img2, command=clicked_random_button)
button_random_window = canvas1.create_window(800, 550, anchor='nw', window=button_random)

button_create = tkinter.Button(m, text="Create New Character", font=myFont, command=clicked_create_button)
button_create_window = canvas1.create_window(660, 600, anchor='nw', window=button_create)

button_save = tkinter.Button(m, text="Save", font=myFont, command=clicked_save_button)
button_save_window = canvas1.create_window(700, 650, anchor='nw', window=button_save)

saved_label = tkinter.Label(m, text="Saved!", font=myFont, fg="red")
saved_label_window = canvas1.create_window(700, 700, anchor='nw', window=saved_label, state='hidden')

button_load = tkinter.Button(m, text="Load", font=myFont, command=clicked_load_button)
button_load_window = canvas1.create_window(850, 650, anchor='nw', window=button_load)

clicked_create_button()
m.mainloop()
