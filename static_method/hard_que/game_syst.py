'''Create class Player:
name
score
rank ("Bronze" initially)
Methods:
update_rank()
Bronze → Silver if score ≥ 100
Silver → Gold if score ≥ 200
Create class GameSystem:
static method add_score(player, points)
Add points
Call update_rank()
Print new rank'''

class Player:
	def __init__(self,name:str,score:int):
		self.name=name
		self.score=score
		self.rank="Bronze"
		
	def update_rank(self):
		if self.score>=200:
			self.rank= "Gold"
			return self.rank
		elif self.score>100:
			self.rank= "Silver"
			return self.rank
		else:
			return self.rank
class GameSystem:
	def add_score(p:Player,points):
		p.score+=points
		p.update_rank()
		print(f"Player {p.name} has score {p.score} and rank {p.rank}")
		return p.score
		
p1=Player("Ashutosh",200)
GameSystem.add_score(p1,100)
