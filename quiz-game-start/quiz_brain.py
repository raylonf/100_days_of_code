class QuizBrain:
    
    def __init__(self):
        
        self.score = 0
        self.games = 0
        
    def game(self, game):
        
        game.questions()
        game.answers()
        
        for c in game.question:
            resp = input(f'{c} (True/False) ').capitalize()
            
            if resp == game.answer[self.games]:
                self.score += 1
                print("That's right")
                
            else:
                print("That's wrong.")
                print(f"The correct answer : {game.answer[self.games]}")
            
            self.games += 1
            print(f"Your current score is : {self.score}/{self.games}\n")
            
        print("You've completed the quiz")    
        print(f"Your final score is : {self.score}/{self.games}\n")

            
    