class TennisGame:
    def __init__(self, player1, player2):
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]
        self.player1 = player1
        self.player1_score = 0
        self.player2 = player2
        self.player2_score = 0

    def won_point(self, player):
        if player == self.player1:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def individual_score(self, score):
        return self.scores[score]

    def advantage(self):
        difference = self.player1_score - self.player2_score

        if difference == 1:
            return "Advantage " + self.player1
        if difference == -1:
            return "Advantage " + self.player2
        if difference > 1:
            return "Win for " + self.player1
        return "Win for " + self.player2
        
    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score <= 3:
                return self.individual_score(self.player1_score)+"-All"
            return "Deuce"
            
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage()
        
        return self.individual_score(self.player1_score) + "-" + self.individual_score(self.player2_score)