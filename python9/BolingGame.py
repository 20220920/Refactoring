import unittest
class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_index=0
        for frame_index in range(10):
            if  self.is_strike(roll_index):
                result += self.strike_score(roll_index)
                roll_index +=1
            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index +=2
            else:
                result += self.frame_score(roll_index)
                roll_index +=2
        return result

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10
    def is_spare(self, roll_index):
        return self.rolls[roll_index]+ self.rolls[roll_index+1]==10
    def strike_score(self,roll_index):
        return  10+ self.rolls[roll_index+1]+ self.rolls[roll_index+2]

    def spare_score(self,roll_index):
        return  10+ self.rolls[roll_index+2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
		
class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()
  
    def test_all_strikes(self):
        for i in range(12):  
         self.game.roll(10)
        assert self.game.score() == 300

    def test_all_spares(self):
        for i in range(21):  
         self.game.roll(5)
        assert self.game.score() == 150
        
if __name__ == '__main__':
    unittest.main()