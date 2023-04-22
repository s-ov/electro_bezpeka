import tkinter as tk
import settings as sett


class DataHandler:
    def __init__(self, collection):
        self.collection = collection

    def __getitem__(self, item):
        return self.collection[item]

    def __len__(self):
        return len(self.collection)

    def get_data_set(self, index_=0):
        return self.collection[index_]


class TestButton(tk.Button):
    def __init__(self, parent, btn_text, btn_command):
        super().__init__()
        self.parent = parent
        self.btn_text = btn_text
        self.btn_command = btn_command
        self.test_button = self.create_test_button()

    def create_test_button(self):
        test_btn = tk.Button(self.parent,
                             text=self.btn_text,
                             width=11, height=1,
                             font=15, bd=2,
                             bg=sett.LIGHT_BLUE,
                             activebackground=sett.MIDDLE_BLUE,
                             command=self.btn_command)
        test_btn.pack(anchor=tk.NW, pady=1)
        return test_btn


class AnswerButton(tk.Button):
    def __init__(self, parent, btn_text, btn_command):
        super().__init__()
        self.parent = parent
        self.btn_text = btn_text
        self.btn_command = btn_command
        self.answer_button = self.create_answer_button()

    def create_answer_button(self):
        answer_button = tk.Button(self.parent,
                                  textvariable=self.btn_text,
                                  font=sett.SMALL_FONT_STYLE,
                                  bg=sett.LIGHT_BLUE, bd=1,
                                  activebackground=sett.MIDDLE_BLUE,
                                  width=int(sett.WIDTH * 0.8),
                                  height=int(sett.HEIGHT * 0.0058),
                                  command=self.btn_command)
        answer_button.pack(pady=2)
        return answer_button


class CheckLabel(tk.Label):
    def __init__(self, parent, text):
        super().__init__()
        self.parent = parent
        self.text = text
        self.check_label = self.create_check_label()

    def create_check_label(self):
        check_label = tk.Label(self.parent,
                               textvariable=self.text,
                               font=sett.SMALL_FONT_STYLE,
                               bg=sett.LIGHT_BLUE,
                               width=4, height=2, bd=4,
                               relief=tk.RIDGE)
        return check_label


class TurnPageButton(tk.Button):
    def __init__(self, parent, btn_text, btn_command):
        super().__init__()
        self.parent = parent
        self.btn_text = btn_text
        self.btn_command = btn_command
        self.turn_page_btn = self.create_turn_page_btn()

    def create_turn_page_btn(self):
        turn_page_btn = tk.Button(self.parent,
                                  text=self.btn_text,
                                  bg=sett.DARK_BLUE,
                                  activebackground=sett.MIDDLE_BLUE,
                                  command=self.btn_command)
        return turn_page_btn


class ScoreboardTitleLabel:
    def __init__(self, parent, text_):
        self.parent = parent
        self.text_ = text_
        self.score_board_title = self.create_score_board_title()

    def create_score_board_title(self):
        score_board_title_label = tk.Label(self.parent, text=self.text_,
                                           bg=sett.LIGHT_BLUE,
                                           font=sett.SMALL_FONT_STYLE,
                                           width=22, height=1, relief=tk.RIDGE)
        return score_board_title_label


class ScoreboardScores:
    def __init__(self, parent, text_):
        self.parent = parent
        self.text_ = text_
        self.scoreboard = self.create_scoreboard()

    def create_scoreboard(self):
        scoreboard = tk.Label(self.parent, textvariable=self.text_,
                              bg=sett.LIGHT_BLUE,
                              font=sett.SMALL_FONT_STYLE,
                              width=5, height=1, relief=tk.RIDGE)
        return scoreboard


questions = DataHandler(sett.QUESTIONS_SET)
answers = DataHandler(sett.ANSWERS_SET)
tests = DataHandler(sett.TEST_TITLES)
