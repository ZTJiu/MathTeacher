from tkinter import *
from tkinter import messagebox
import Teacher
import Speaker
from functools import partial


class Application(object):
    def __init__(self, master=None):
        self.problem_num = 10
        self.teacher = Teacher.MathTeacher()
        self.speaker = Speaker.Speaker()
        self.problems = self.teacher.get_problems(self.problem_num)
        self.tk = Tk()
        self.tk.title("口算助手")
        self.tk.geometry('500x800')

        self.w = PanedWindow(self.tk, orient=HORIZONTAL)
        self.labels = []
        self.inputs = []
        self.asks = []
        self.answers = []
        for i, (ask, answer) in self.problems.items():
            index = i + 1
            lb = Label(self.w, text=f'问题{index}：{ask}')
            lb.grid(row=i, column=0, padx=10, pady=10, ipadx=10, ipady=10)
            self.labels.append(lb)

            on_play = partial(self.on_play, i)
            ask_button = Button(self.w, text=f'读题',
                                bg='green', command=on_play)
            ask_button.grid(row=i, column=1,
                            padx=10, pady=10, ipadx=10, ipady=10)
            self.asks.append(ask_button)

            input = Entry(self.w, bd=3, width=5)
            input.grid(row=i, column=2,
                       padx=10, pady=10, ipadx=10, ipady=10)
            self.inputs.append(input)

            on_answer = partial(self.on_submit, i)
            answer_button = Button(
                self.w, text=f'回答', bg='green', command=on_answer)
            answer_button.grid(row=i, column=3,
                               padx=10, pady=10, ipadx=10, ipady=10)
            self.answers.append(answer_button)
        self.w.pack(side=TOP)

        self.quit_button = Button(
            self.tk, text='退出', bg='green', command=self.on_quit).pack(padx=10, pady=10, ipadx=10, ipady=10)

        self.tk.mainloop()

    def on_play(self, i):
        ask = self.problems[i][0]
        self.speaker.speak(f'{ask} 等于多少？')

    def on_submit(self, i):
        input = self.inputs[i]
        answer_button = self.answers[i]
        answer = int(input.get())
        real_answer = self.problems[i][1]
        if answer == real_answer:
            self.speaker.speak(f'回答正确')
            input.config(state=DISABLED)
            answer_button["state"] = "disabled"
        else:
            self.speaker.speak(f'不对哦，请重新回答')

    def on_quit(self):
        result = messagebox.askquestion(title='Hi', message='要退出吗？')
        if result == 'yes':
            # messagebox.showinfo(title='Hi', message='Yes')
            self.tk.destroy()


if __name__ == '__main__':
    app = Application()
