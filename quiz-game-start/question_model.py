from email.encoders import encode_quopri


class QuizGameModel:
    
    def __init__(self, list):
        self.list = list
        self.question = []
        self.answer = []
        
    def questions(self):
        
        for e, c in enumerate(self.list):            
            self.question.append(f'Q.{e+1}: {c["question"]}')
            
        return self.question
            
    def answers(self):
        
        for c in self.list:
            self.answer.append(c["correct_answer"])
            
        return self.answer