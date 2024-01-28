import random

import Speaker


class MathTeacher(object):
    def __init__(self) -> None:
        self.min_num = 1
        self.max_num = 20
        self.flags = ['+', '-']
        self.problems = {}

    def __get_problem(self):
        problem = ''
        answer = 0
        while True:
            num1 = random.randint(self.min_num, self.max_num)
            num2 = random.randint(self.min_num, self.max_num)
            flag_index = random.randint(0, len(self.flags) - 1)
            if self.flags[flag_index] == '+':
                problem = f'{num1} + {num2}'
                answer = num1 + num2
                self.problems[problem] = answer
                break
            else:
                if num1 < num2:
                    num1, num2 = num2, num1
                problem = f'{num1} - {num2}'
                answer = num1 - num2
                self.problems[problem] = answer
            # print(problem, answer)
            if problem in self.problems:
                continue
            break
        return problem, answer

    def get_problems(self, num):
        problems = {}
        for i in range(num):
            problem, answer = self.__get_problem()
            # print(problem, answer)
            problems[i] = (problem, answer)
        return problems


if __name__ == '__main__':
    speaker = Speaker.Speaker()
    teacher = MathTeacher()
    problems = teacher.get_problems(10)
    for i, (problem, answer) in problems.items():
        print(problem, answer)
        while True:
            problem_text = problem + '等于多少？'
            speaker.speak(problem_text)
            input_answer = input(problem_text + " 请输入答案: ")
            if (int(input_answer) == answer):
                speaker.speak('回答正确')
                break
            else:
                speaker.speak('不对哟，再试试吧')
