import tkinter
import ttk


def create_choicebox(root, choices_list, label_name, position_row):
    tkinter.Label(root, text=label_name).grid(row=position_row,column=0)
    combobox = ttk.Combobox(root, values=choices_list)
    combobox.grid(row=position_row, column=1)
    combobox.bind("<<ComboboxSelected>>", callBackFunc)


def read_movies():
    movies_names = {}
    with open("movies", 'r') as movies_file:
        movies_list = movies_file.readlines()
    for element in movies_list:
        key = element.strip().split("-")[0]
        val = element.strip().split("-")[1]
        movies_names[key] = val
    return movies_names


def callBackFunc(event):
    if event.widget._name == "!combobox2":
        price = (int(read_movies()[event.widget.get()]))
        print("Price: ",price)


def main():
    root = tkinter.Tk()
    root.geometry("400x200")
    create_choicebox(root, ["1", "2", "3"], "Hall:", 0)
    create_choicebox(root, list(read_movies().keys()), "Films:", 1)
    create_choicebox(root, ["10:00", "12:00", "14:00"], "Hour:", 2)
    create_choicebox(root, ["Child", "Adult"], "Ticket:", 3)
    tkinter.Button(root, text="Get price:").grid(row=6, column=0)
    root.mainloop()


if __name__ == "__main__":
    main()