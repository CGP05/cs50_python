class Vault:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def __str__(self):
        return f"{self.gold} Gold, {self.silver} Silver, {self.bronze} Bronze"


bank_of_canada = Vault(100, 50, 25)
print(bank_of_canada)

bank_of_togo = Vault(25, 50, 100)
print(bank_of_togo)