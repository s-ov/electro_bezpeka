import tkinter as tk
from tkinter import Frame, Label, Button, StringVar
from typing import List
import settings as sett
# from auxiliary_module import AnswerButton, CheckLabel, TestButton, TurnPageButton, ScoreboardTitleLabel,\
#                              ScoreboardScores, questions, answers, tests
import auxiliary_module as am


class App(Frame):
    answers_values = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{sett.WIDTH}x{sett.HEIGHT}")
        self.root.title(sett.APP_NAME)
        self.root.resizable(0, 0)
        self.root.config(bg=sett.DARK_BLUE)

        self.answer_flag = True

        # CREATE ALL STRING VARS
        self.create_string_vars()
        # PUT LEFT SIDEBAR
        self.put_left_sidebar()
        # PUT TEST PAGE
        self.put_test_page_widgets()

        self.create_check_labels()

    def create_string_vars(self) -> None:
        """Creates all string vars"""
        self.title_var = StringVar()
        self.question_var = StringVar()
        self.answer_var_1 = StringVar()
        self.answer_var_2 = StringVar()
        self.answer_var_3 = StringVar()
        self.answer_var_4 = StringVar()
        self.answer_var_5 = StringVar()
        self.check_label_var_1 = StringVar()
        self.check_label_var_2 = StringVar()
        self.check_label_var_3 = StringVar()
        self.check_label_var_4 = StringVar()
        self.check_label_var_5 = StringVar()
        self.correct_answers_var = StringVar()
        self.wrong_answers_var = StringVar()

    def put_left_sidebar(self) -> None:
        """Puts left sidebar"""
        self.left_sidebar = self.create_left_sidebar()
        self.test_buttons = self.create_test_buttons(self.left_sidebar)

    def put_test_page_widgets(self) -> None:
        """Puts test page frames"""
        self.page_frame = self.create_page_frame()
        self.title_frame = self.create_title_frame(self.page_frame)
        self.question_frame = self.create_question_frame(self.page_frame)
        self.answer_frame = self.create_answer_frame(self.page_frame)
        self.answer_check_label_frame = self.create_answer_check_label_frame(self.page_frame)

        self.page_bottom_frame = self.create_page_bottom_frame(self.page_frame)
        self.title_label = Label(self.title_frame, width=int(sett.WIDTH * 0.8), textvariable=self.title_var,
                                 font=sett.SMALL_FONT_STYLE, bg=sett.LIGHT_BLUE, justify=tk.LEFT)
        self.question_label = Label(self.question_frame, width=int(sett.WIDTH * 0.7), textvariable=self.question_var,
                                    font=sett.SMALL_FONT_STYLE, bg=sett.LIGHT_BLUE, justify=tk.LEFT)
        self.next_button = self.create_next_button(self.page_bottom_frame)
        self.previous_button = self.create_previous_button(self.page_bottom_frame)
        self.score_board_labels = self.put_score_board_labels()

    def create_test_buttons(self, location) -> None:
        """Creates test buttons"""
        for item in range(len(am.tests)):
            am.TestButton(location, sett.TEST_TITLES[item], lambda btn_id=item: self.operate_test_btn(btn_id))

    def create_answer_buttons(self) -> None:
        """Creates answer buttons"""
        am.AnswerButton(self.answer_frame, self.answer_var_1, self.operate_answer_button_1).answer_button
        am.AnswerButton(self.answer_frame, self.answer_var_2, self.operate_answer_button_2).answer_button
        am.AnswerButton(self.answer_frame, self.answer_var_3, self.operate_answer_button_3).answer_button
        am.AnswerButton(self.answer_frame, self.answer_var_4, self.operate_answer_button_4).answer_button
        am.AnswerButton(self.answer_frame, self.answer_var_5, self.operate_answer_button_5).answer_button
        self.answer_flag = False

    def put_answer_button_text(self, test_id: int, question_id: int) -> None:
        """Puts text on answer buttons"""
        self.answer_var_1.set(am.answers[test_id][question_id][0][0])
        self.answer_var_2.set(am.answers[test_id][question_id][1][0])
        self.answer_var_3.set(am.answers[test_id][question_id][2][0])
        self.answer_var_4.set(am.answers[test_id][question_id][3][0])
        self.answer_var_5.set(am.answers[test_id][question_id][4][0])

    def create_check_labels(self) -> None:
        """Creates check labels"""
        self.check_label_1 = am.CheckLabel(self.answer_check_label_frame, self.check_label_var_1).check_label
        self.check_label_2 = am.CheckLabel(self.answer_check_label_frame, self.check_label_var_2).check_label
        self.check_label_3 = am.CheckLabel(self.answer_check_label_frame, self.check_label_var_3).check_label
        self.check_label_4 = am.CheckLabel(self.answer_check_label_frame, self.check_label_var_4).check_label
        self.check_label_5 = am.CheckLabel(self.answer_check_label_frame, self.check_label_var_5).check_label

    def refresh(self) -> None:
        """Destroys and creates again check"""
        self.check_label_1.destroy()
        self.check_label_2.destroy()
        self.check_label_3.destroy()
        self.check_label_4.destroy()
        self.check_label_5.destroy()
        self.create_check_labels()

    def set_check_label_text(self, test_id: int, question_id: int) -> None:
        """Creates check labels text"""
        self.check_label_var_1.set(am.answers[test_id][question_id][0][1])
        self.check_label_var_2.set(am.answers[test_id][question_id][1][1])
        self.check_label_var_3.set(am.answers[test_id][question_id][2][1])
        self.check_label_var_4.set(am.answers[test_id][question_id][3][1])
        self.check_label_var_5.set(am.answers[test_id][question_id][4][1])

    def operate_answer_button_1(self) -> None:
        """Sets first check label text"""
        self.check_label_1.place(x=0, y=12)
        self.get_answer_value(self.test_id, self.question_id, 0)
        self.set_correct_answer()
        self.set_wrong_answer()

    def operate_answer_button_2(self) -> None:
        """Sets second check label text"""
        self.check_label_2.place(x=0, y=85)
        self.get_answer_value(self.test_id, self.question_id, 1)
        self.set_correct_answer()
        self.set_wrong_answer()

    def operate_answer_button_3(self) -> None:
        """Sets third check label text"""
        self.check_label_3.place(x=0, y=155)
        self.get_answer_value(self.test_id, self.question_id, 2)
        self.set_correct_answer()
        self.set_wrong_answer()

    def operate_answer_button_4(self) -> None:
        """Sets forth check label text"""
        self.check_label_4.place(x=0, y=230)
        self.get_answer_value(self.test_id, self.question_id, 3)
        self.set_correct_answer()
        self.set_wrong_answer()

    def operate_answer_button_5(self) -> None:
        """Sets fifth check label text"""
        self.check_label_5.place(x=0, y=300)
        self.get_answer_value(self.test_id, self.question_id, 4)
        self.set_correct_answer()
        self.set_wrong_answer()

    def operate_test_btn(self, btn_id: int) -> None:
        """Puts test title, question text and answer buttons text of first question"""
        self.test_id = btn_id
        self.question_id = 0
        self.refresh()
        self.set_check_label_text(self.test_id, self.question_id)

        self.title_var.set(am.tests.get_data_set(btn_id))
        self.title_label.pack(expand=True)

        self.question_var.set(am.questions.get_data_set(btn_id)[self.question_id])
        self.question_label.pack(expand=True)

        if self.answer_flag:
            self.create_answer_buttons()
        self.flag = True
        self.put_answer_button_text(self.test_id, self.question_id)

    def operate_next_button(self) -> None:
        """Moves forward questions and answers of one test"""
        try:
            if self.flag:
                self.question_var.set(am.questions[self.test_id][self.question_id + 1])
                self.question_label.pack(expand=True)
                self.question_id += 1
                self.put_answer_button_text(self.test_id, self.question_id)
                self.set_check_label_text(self.test_id, self.question_id)
                self.refresh()
        except IndexError:
            print("IndexError")

    def operate_previous_button(self) -> None:
        """Moves back questions and answers of one test"""
        try:
            if self.flag:
                self.question_var.set(am.questions[self.test_id][self.question_id - 1])
                self.question_label.pack(expand=True)
                self.question_id -= 1
                self.put_answer_button_text(self.test_id, self.question_id)
                self.set_check_label_text(self.test_id, self.question_id)
                self.refresh()
        except IndexError:
            print("IndexError")

    def create_left_sidebar(self) -> Frame:
        """Creates test buttons frame"""
        left_sidebar = Frame(self.root, bg=sett.DARK_BLUE, width=int(sett.WIDTH * 0.10), height=sett.HEIGHT)
        left_sidebar.pack(side=tk.LEFT, expand=True, fill='both')
        return left_sidebar

    def create_page_frame(self) -> Frame:
        """Creates page frame"""
        right_frame = Frame(self.root, width=int(sett.WIDTH * 0.9), height=sett.HEIGHT, bg=sett.LIGHT_BLUE)
        right_frame.pack(side=tk.RIGHT, expand=True, fill='both', padx=5, pady=5)
        return right_frame

    @staticmethod
    def create_title_frame(location: Frame) -> Frame:
        """Creates title frame"""
        title_frame = Frame(location, bg=sett.LIGHT_BLUE)
        title_frame.place(x=0, y=1, relwidth=1, relheight=0.05)
        return title_frame

    @staticmethod
    def create_question_frame(location: Frame) -> Frame:
        """Creates question frame"""
        question_frame = Frame(location, bg=sett.LIGHT_BLUE)
        question_frame.place(x=0, y=20, relwidth=1, relheight=0.15)
        return question_frame

    @staticmethod
    def create_answer_frame(location: Frame) -> Frame:
        """Creates answer buttons frame"""
        answer_frame = Frame(location, bg=sett.LIGHT_BLUE)
        answer_frame.place(x=0, y=98, relwidth=0.94, relheight=0.75)
        return answer_frame

    @staticmethod
    def create_answer_check_label_frame(location: Frame) -> Frame:
        """Creates answer check label frame"""
        answer_label_frame = Frame(location, bg=sett.LIGHT_BLUE)
        answer_label_frame.place(x=795, y=98, relwidth=0.05, relheight=0.75)
        return answer_label_frame

    @staticmethod
    def create_page_bottom_frame(location: Frame) -> Frame:
        """Creates page bottom frame"""
        bottom_frame = Frame(location, bg=sett.LIGHT_BLUE)
        bottom_frame.place(x=0, y=463, relwidth=1, relheight=0.14)
        return bottom_frame

    def create_next_button(self, location: Frame) -> None:
        """Creates next button"""
        next_button = am.TurnPageButton(location, sett.PAGINATION_BUTTON_NAME[0], self.operate_next_button).turn_page_btn
        next_button.place(x=10, y=10)

    def create_previous_button(self, location: Frame) -> None:
        """Creates previous button"""
        previous_button = am.TurnPageButton(location, sett.PAGINATION_BUTTON_NAME[1],
                                            self.operate_previous_button).turn_page_btn
        previous_button.place(x=110, y=10)

    def put_score_board_labels(self) -> None:
        """Puts scoreboard labels"""
        am.ScoreboardTitleLabel(self.page_bottom_frame, sett.SCORE_BOARD_TITLES[0]).score_board_title.place(x=250, y=10)
        am.ScoreboardTitleLabel(self.page_bottom_frame, sett.SCORE_BOARD_TITLES[1]).score_board_title.place(x=250, y=40)
        am.ScoreboardScores(self.page_bottom_frame, self.correct_answers_var).scoreboard.place(x=435, y=10)
        am.ScoreboardScores(self.page_bottom_frame, self.wrong_answers_var).scoreboard.place(x=435, y=40)

    def get_answer_value(self, test_id: int, question_id: int, answer_id: int, value: int = 1) -> List[str]:
        """Appends list with answers values"""
        self.answers_values.append(am.answers[test_id][question_id][answer_id][value])
        return self.answers_values

    def get_correct_answers(self) -> int:
        """Creates a correct answers list and returns its length """
        correct_answers = [answer for answer in self.answers_values if answer == "Taк"]
        return len(correct_answers)

    def set_correct_answer(self) -> None:
        self.correct_answers_var.set(self.get_correct_answers())

    def get_wrong_answers(self) -> int:
        """Creates a wrong answers list and returns its length """
        wrong_answers = [answer for answer in self.answers_values if answer == "Hi"]
        return len(wrong_answers)

    def set_wrong_answer(self) -> None:
        self.wrong_answers_var.set(self.get_wrong_answers())

    def run(self) -> None:
        """Runs the program"""
        self.root.mainloop()
