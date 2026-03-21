#hello this is a test to see if the repo clone worked
#practicing classes


class Player:
    def __init__(self,name,team,goals,assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def summary(self):
        return f"{self.name} ({self.team}) - {self.goals} goals, {self.assists} assists"
        
    def goal_contribution(self):
        return(self.goals + self.assists)
    
    def is_top_performer(self):
        if self.goal_contribution() > 20:
            return True
        else:
            return False
        

Haaland = Player("Erling Haaland", "Man City", 28, 5)
print(Haaland.summary())

