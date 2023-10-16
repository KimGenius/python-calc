import tkinter as tk

window = None
label_text = None
history = []
operators = ['+', '-', '/', '*', '%', '(', ')']


def quit():
    window.destroy()


def onClick(value):
    global history
    global label_text
    text = input_text.get(1.0, tk.END)
    last_text = text[len(text) - 2]
    if last_text in operators and value in operators:
        input_text.delete(1.0, tk.END)
        input_text.insert(1.0, text[0:len(text) - 2] + value)
        return
    if value == '=':
        # 결과를 눌렀는데 마지막이 연산자면 연산 안되게
        if last_text in operators:
            return
        input_text.delete(1.0, tk.END)
        result = eval(text)
        input_text.insert(1.0, result)
        history.append({'text': text, 'result': result})
        history_text = '계산 기록\n'
        for his in history:
            history_text += str(his['text']).strip() + ' = ' + str(his['result']).strip() + '\n'
        label_text.set(history_text)
        return
    if value == '<-':
        input_text.delete(1.0, tk.END)
        input_text.insert(1.0, text[0:len(text) - 2])
        return
    if value == 'C':
        input_text.delete(1.0, tk.END)
        return
    if value == '^2':
        is_operator = False
        for operator in operators:
            if operator in text:
                is_operator = True
                break
        if not is_operator:
            input_text.delete(1.0, tk.END)
            input_text.insert(1.0, str(int(text) ** 2))
            history_text = '계산 기록\n'
            history.append({'text': text.strip() + '^2', 'result': str(int(text) ** 2)})
            for his in history:
                history_text += str(his['text']).strip() + ' = ' + str(his['result']).strip() + '\n'
            label_text.set(history_text)
        return
    if value == '√':
        is_operator = False
        for operator in operators:
            if operator in text:
                is_operator = True
                break
        if not is_operator:
            input_text.delete(1.0, tk.END)
            input_text.insert(1.0, str(int(float(text.strip())) ** (1 / 2)))
            history_text = '계산 기록\n'
            history.append({'text': '√' + text.strip(), 'result': str(int(float(text.strip())) ** (1 / 2))})
            for his in history:
                history_text += str(his['text']).strip() + ' = ' + str(his['result']).strip() + '\n'
            label_text.set(history_text)
        return
    input_text.insert(tk.END, value)


def setupGUI():
    global window
    global label_text
    window = tk.Tk()
    window.title('계산기')
    frame = tk.Frame(window)
    frame.pack()
    global input_text
    input_text = tk.Text(frame, height=1, width=20)
    input_text.grid(row=0, column=0, rowspan=1, columnspan=4)

    elementList = [['', '(', ')', '√'], ['C', '<-', '^2', '%'], [1, 2, 3, '*'], [4, 5, 6, '-'], [7, 8, 9, '+'],
                   [0, '.', '/', '=']]

    for i in range(0, len(elementList)):
        for j in range(0, len(elementList[i])):
            text = str(elementList[i][j])
            if text != '':
                button0_1 = tk.Button(frame, text=text, command=lambda cmd=text: onClick(cmd))
                button0_1.grid(row=i + 2, column=j + 1, ipadx=20, ipady=20)

    label_text = tk.StringVar()
    label_text.set("계산 기록")
    label = tk.Label(frame, textvariable=label_text)
    label.grid(row=len(elementList) + 3, column=0, columnspan=len(elementList))


setupGUI()
window.mainloop()
