import unittest
class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if  self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    def strikeScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		
class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()
  
    def testAllStrikes(self):
        for i in range(12):  
         self.game.roll(10)
        assert self.game.score() == 300

    def testAllSpares(self):
        for i in range(21):  
         self.game.roll(5)
        assert self.game.score() == 150
        
if __name__ == '__main__':
    unittest.main()