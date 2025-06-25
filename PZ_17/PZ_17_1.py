# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

from tkinter import *

def send_action():
    print(u'Отправить')

def window_deleted():
    root.destroy()
    print(u'Окно закрыто')
    root.quit()  # явное указание на выход из программы

root = Tk()
root.title("Testform")
root.geometry("800x470")
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)

header_frame = Frame(root, bg="#ededed", bd=1, relief="solid")
header_frame.grid(row=0, column=0, columnspan=3, sticky="we")
header_label = Label(header_frame, text="Testform", font=("Arial", 16, "bold"), bg="#ededed")
header_label.pack(anchor="w", padx=8, pady=4)

Label(root, text="Name", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=14, pady=10)
entry_name = Entry(root, width=32)
entry_name.grid(row=1, column=1, sticky="w", pady=10)

Label(root, text="Password", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=14, pady=10)
entry_pass = Entry(root, width=32, show="*")
entry_pass.grid(row=2, column=1, sticky="w", pady=10)

Label(root, text="Gender", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=14)
gender_var = StringVar()
Radiobutton(root, text="Male", variable=gender_var, value="male").grid(row=3, column=1, sticky="w")
Radiobutton(root, text="Female", variable=gender_var, value="female").grid(row=4, column=1, sticky="w")

Label(root, text="Continent", font=("Arial", 12)).grid(row=5, column=0, sticky="e", padx=14, pady=10)
continent_frame = Frame(root)
continent_frame.grid(row=5, column=1, sticky="w", pady=10)
continent_listbox = Listbox(continent_frame, height=1, width=28, exportselection=0)
continents = ["Please select...", "Europe", "Asia", "Africa", "North America", "South America", "Australia", "Antarctica"]
for item in continents:
    continent_listbox.insert(END, item)
continent_listbox.select_set(0)
continent_listbox.grid(row=0, column=0, sticky="ns")

scrollbar = Scrollbar(continent_frame, orient="vertical", command=continent_listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
continent_listbox.config(yscrollcommand=scrollbar.set)

Label(root, text="Meals", font=("Arial", 12)).grid(row=6, column=0, sticky="e", padx=14)
meal_vars = [IntVar(), IntVar(), IntVar()]
Checkbutton(root, text="breakfast", variable=meal_vars[0]).grid(row=6, column=1, sticky="w")
Checkbutton(root, text="lunch", variable=meal_vars[1]).grid(row=7, column=1, sticky="w")
Checkbutton(root, text="dinner", variable=meal_vars[2]).grid(row=8, column=1, sticky="w")

Label(root, text="Remark", font=("Arial", 12)).grid(row=9, column=0, sticky="ne", padx=14, pady=10)
remark_text = Text(root, width=45, height=5)
remark_text.grid(row=9, column=1, pady=10, sticky="w")

footer_frame = Frame(root, bg="#ededed", bd=1, relief="solid")
footer_frame.grid(row=10, column=0, columnspan=3, sticky="we")
footer_frame.grid_columnconfigure(0, weight=1)
button_frame = Frame(footer_frame, bd=0)
button_frame.grid(row=0, column=1, sticky="e", pady=8)
send_btn = Button(button_frame, text="Send", width=10, command=send_action)
send_btn.pack(side="left", padx=5)
cancel_btn = Button(button_frame, text="Cancel", width=10, command=window_deleted)
cancel_btn.pack(side="left", padx=5)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)

root.mainloop()
