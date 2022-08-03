wes_savings = 33800
ab_savings = 8000
equity = 26600
fees = 8000
mortgage = 297000
goal = 375000

class HousePurchase:
    def __init__(self, savings_1, savings_2, equity, fees, mortgage, goal):
        self.savings_1 = savings_1
        self.savings_2 = savings_2
        self.equity = equity
        self.fees = fees
        self.mortgage = mortgage
        self.goal = goal

    def get_house_budget(self):
        total = (self.savings_1 + self.savings_2 + self.equity + self.mortgage) - self.fees
        return f'House price you can afford = £{"{:,}".format(total)}'
    
    def get_deposit(self):
        deposit = self.savings_1 + self.savings_2 + self.equity
        return f'Total deposit = £{"{:,}".format(deposit)}'

    def left_to_save(self):
        current_budget = self.get_house_budget().replace(",",'')
        current_budget = int(current_budget[-6:])
        total_to_save = self.goal - current_budget
        if self.goal > current_budget:
            return f'Goal house purchase price = £{"{:,}".format(self.goal)} \n\nTotal to save = £{"{:,}".format(total_to_save)}'
        elif self.goal == 0:
            return "No goal set."
        elif self.goal < current_budget:
            return "Goal amount less than current house budget."
   
our_house = HousePurchase(wes_savings, ab_savings, equity, fees, mortgage, goal)

print(our_house.get_house_budget())
print("")
print(our_house.get_deposit())
print("")
print(our_house.left_to_save())
    

