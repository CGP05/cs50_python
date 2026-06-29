class Vault:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

bank_of_canada = Vault(100, 50, 25)
print(bank_of_canada)