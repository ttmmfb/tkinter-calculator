from math import sqrt, factorial
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Калькулятор')
root.resizable(False, False) #запрещает тянуть окно по ширине и высоте

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=18, ipady=10)

# РАБОЧИЙ КОД

def validate_input(new_text):
    # Разрешаем цифры, точки, скобки, знаки операций
    allowed = "0123456789+-*/×÷^().Ans\u221A"
    return all(symbol in allowed for symbol in new_text)

# Регистрируем проверку и подключаем к полю ввода
vcmd = (root.register(validate_input), "%P")
# register переводит функцию на язык tkinter
# %P передает в validate_input измененную строку (подходящую)
entry.configure(validate="key", validatecommand=vcmd)
# validate='key' проверка при каждом нажатии клавиши
# validatecommand=vcmd привязывает команду vcmd к полю entry

def add_symbol(symbol):
    operators = "+-×÷^"
    current_text = entry.get()
    if current_text and symbol in operators and current_text[-1] in operators:
        entry.delete(len(current_text) - 1, tk.END)
    entry.insert(tk.END, symbol)

def backspace():
    current_text = entry.get()
    if current_text.endswith('Ans'):
        entry.delete(len(current_text) - 3, tk.END)
    else:
        entry.delete(len(current_text) - 1, tk.END)

last_answer = "0"
def calculate():
    global last_answer
    try:
        source = entry.get()
        source = source.replace('÷', '/').replace('×', '*').replace('fact(', 'factorial(')
        source = source.replace('^', '**').replace('\u221A(', 'sqrt(').replace('Ans', f'({last_answer})')
        result = eval(source)
        last_answer = str(result)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Ошибка вычисления", "На ноль делить нельзя!")
    except ValueError:
        messagebox.showerror("Ошибка вычисления", "Недопустимое значение (например, корень из отрицательного числа)!")
    except Exception:
        messagebox.showerror("Ошибка ввода", "Проверьте правильность выражения (возможно, не закрыта скобка).")

# СТИЛИЗАЦИЯ

bg_main = "#fff5f7"
root.configure(bg=bg_main)

btn_base = {"font": ("Segoe UI", 24), "bd": 0, "highlightthickness": 0}

s_eq = {
    **btn_base,
    "bd": 1, 
    "relief": "flat",
    "bg": "#e84393",
    "fg": "#ffffff",
    "activebackground": "#d6307d",
    "activeforeground": "#ffffff"
}

s_row1 = {
    **btn_base,
    "bd": 1, 
    "relief": "flat",
    "bg": "#f8a5c2",
    "fg": "#4a152b",
    "activebackground": "#f38bb0",
    "activeforeground": "#4a152b"
}

s_op = {
    **btn_base,
    "bd": 1, 
    "relief": "flat",
    "bg": "#fad2e1",
    "fg": "#5c1d36",
    "activebackground": "#f5bdd2",
    "activeforeground": "#5c1d36"
}

s_num = {
    **btn_base,
    "bd": 1, 
    "relief": "flat",
    "bg": "#fde8ef",
    "fg": "#5c1d36",
    "activebackground": "#f9d5e2",
    "activeforeground": "#5c1d36"
}

entry.configure(
    bg=bg_main,
    fg="#4a152b",
    insertbackground="#e84393",  # Цвет мигающего курсора
    font=("Segoe UI", 34),
    justify="right",
    bd=0
)

# КНОПКИ

b_lbracket = tk.Button(root, text='(', width=5, height=2, **s_row1, command=lambda: add_symbol('('))
b_rbracket = tk.Button(root, text=')', width=5, height=2, **s_row1, command=lambda: add_symbol(')'))
b_ac = tk.Button(root, text='AC', width=5, height=2, **s_row1, command=lambda: entry.delete(0, tk.END))
b_del = tk.Button(root, text='Del', width=5, height=2, **s_row1, command=lambda: backspace())

b_stepen = tk.Button(root, text='^', width=5, height=2, **s_op, command=lambda: add_symbol('^'))
b_sqrt = tk.Button(root, text="\u221A", width=5, height=2, **s_op, command=lambda: add_symbol('\u221A('))
b_ans = tk.Button(root, text='Ans', width=5, height=2, **s_op, command=lambda: add_symbol('Ans'))
b_delenie = tk.Button(root, text='÷', width=5, height=2, **s_op, command=lambda: add_symbol('÷'))

b_7 = tk.Button(root, text='7', width=5, height=2, **s_num, command=lambda: add_symbol('7'))
b_8 = tk.Button(root, text='8', width=5, height=2, **s_num, command=lambda: add_symbol('8'))
b_9 = tk.Button(root, text='9', width=5, height=2, **s_num, command=lambda: add_symbol('9'))
b_umnozhenie = tk.Button(root, text='×', width=5, height=2, **s_op, command=lambda: add_symbol('×'))

b_4 = tk.Button(root, text='4', width=5, height=2, **s_num, command=lambda: add_symbol('4'))
b_5 = tk.Button(root, text='5', width=5, height=2, **s_num, command=lambda: add_symbol('5'))
b_6 = tk.Button(root, text='6', width=5, height=2, **s_num, command=lambda: add_symbol('6'))
b_minus = tk.Button(root, text='-', width=5, height=2, **s_op, command=lambda: add_symbol('-'))

b_1 = tk.Button(root, text='1', width=5, height=2, **s_num, command=lambda: add_symbol('1'))
b_2 = tk.Button(root, text='2', width=5, height=2, **s_num, command=lambda: add_symbol('2'))
b_3 = tk.Button(root, text='3', width=5, height=2, **s_num, command=lambda: add_symbol('3'))
b_plus = tk.Button(root, text='+', width=5, height=2, **s_op, command=lambda: add_symbol('+'))

b_dot = tk.Button(root, text='.', width=5, height=2, **s_num, command=lambda: add_symbol('.'))
b_0 = tk.Button(root, text='0', width=5, height=2, **s_num, command=lambda: add_symbol('0'))
b_ravno = tk.Button(root, text='=', height=2, **s_eq, command=lambda: calculate())

# РАСПОЛОЖЕНИЕ

b_lbracket.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
b_rbracket.grid(row = 1, column=1, sticky="nsew", padx=4, pady=4)
b_ac.grid(row=1, column=2, sticky="nsew", padx=4, pady=4)
b_del.grid(row=1, column=3, sticky="nsew", padx=4, pady=4)

b_stepen.grid(row=2, column=2, sticky="nsew", padx=4, pady=4)
b_sqrt.grid(row=2, column=1, sticky="nsew", padx=4, pady=4)
b_ans.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
b_delenie.grid(row=2, column=3, sticky="nsew", padx=4, pady=4)

b_7.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)
b_8.grid(row = 3, column=1, sticky="nsew", padx=4, pady=4)
b_9.grid(row=3, column=2, sticky="nsew", padx=4, pady=4)
b_umnozhenie.grid(row=3, column=3, sticky="nsew", padx=4, pady=4)

b_4.grid(row=4, column=0, sticky="nsew", padx=4, pady=4)
b_5.grid(row=4, column=1, sticky="nsew", padx=4, pady=4)
b_6.grid(row=4, column=2, sticky="nsew", padx=4, pady=4)
b_minus.grid(row=4, column=3, sticky="nsew", padx=4, pady=4)

b_1.grid(row=5, column=0, sticky="nsew", padx=4, pady=4)
b_2.grid(row=5, column=1, sticky="nsew", padx=4, pady=4)
b_3.grid(row=5, column=2, sticky="nsew", padx=4, pady=4)
b_plus.grid(row=5, column=3, sticky="nsew", padx=4, pady=4)

b_dot.grid(row=6, column=0, sticky="nsew", padx=4, pady=4)
b_0.grid(row=6, column=1, sticky="nsew", padx=4, pady=4)
b_ravno.grid(row=6, column=2, columnspan=2, sticky="nsew", padx=4, pady=4)

# Нажатие Enter запускает подсчет
root.bind("<Return>", lambda event: calculate())
root.bind("<KP_Enter>", lambda event: calculate())

# Ставим курсор в поле ввода сразу при запуске программы
entry.focus_set()

root.mainloop()