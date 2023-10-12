import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "correct_option": 1,
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "correct_option": 1,
            },
        ]

        self.question_label = tk.Label(root, text="", wraplength=300)
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            option_button.pack()
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()

        self.update_question()

    def update_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            self.next_button.config(state="disabled")
        else:
            self.question_label.config(text="Quiz completed. Your score: {}/{}".format(self.score, len(self.questions)))
            for button in self.option_buttons:
                button.config(state="disabled")

    def check_answer(self, selected_option):
        current_question = self.questions[self.question_index]
        if selected_option == current_question["correct_option"]:
            self.score += 1
        self.next_button.config(state="active")

    def next_question(self):
        self.question_index += 1
        self.update_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
