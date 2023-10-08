class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def has_question(self):
        """Compares between two attributes & returns a boolean value"""
        return self.q_number < len(self.q_list)

    def next_ques(self):
        """Picks a single question from question list, asks user input for Quiz answer after presenting the Question"""
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_input = input(f"Q{self.q_number}: {current_question.text} (True/False): ").lower()
        self.process(user_input, current_question.answer)

    def process(self, user_input, correct_answer):
        if user_input == correct_answer.lower():
            self.score += 1
            print(f"Correct Answer!")
        else:
            print(f"Wrong Answer!")
        print(f"Your score is {self.score}/{self.q_number}")
