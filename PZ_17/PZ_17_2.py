# Дано целое положительное число. Проверить истинность высказывания: «Данное
# число является четным двузначным».

from tkinter import *

def window_deleted():
    root.destroy()
    print(u'Окно закрыто')
    root.quit()  # явное указание на выход из программы
def check_number():
    value = entry.get()
    try:
        number = int(value)
        if number < 0:
            result_label.configure(text="Ошибка: введите положительное число!", fg="red")
        elif 9 < number < 100 and number % 2 == 0:
            result_label.configure(text="True: число чётное двузначное", fg="green")
        elif 9 < number < 100 and number % 2 != 0:
            result_label.configure(text="False: число не чётное двузначное", fg="blue")
        elif number > 100 and number % 2 == 0:
            result_label.configure(text="False: число чётное не двузначное", fg="blue")
        elif number > 100 and number % 2 != 0:
            result_label.configure(text="False: число не чётное не двузначное", fg="blue")
    except ValueError:
        result_label.configure(text="Ошибка: введите целое число!", fg="red")

root = Tk()
root.title("Проверка числа")
root.geometry("350x180")
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)

label = Label(root, text="Введите целое положительное число:", font=("Arial", 12))
label.pack(pady=10)
entry = Entry(root, width=25, font=("Arial", 12))
entry.pack()
check_button = Button(root, text="Проверить", font=("Arial", 12), command=check_number)
check_button.pack(pady=10)
result_label = Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()