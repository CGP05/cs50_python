class MP:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Backbencher(MP):
    def __init__(self, name, party):
        super().__init__(name)
        self.party = party

    ...


class PartyLeader(MP):
    def __init__(self, name, leader_since):
        super().__init__(name)
        self.leader_since = leader_since

    ...

backbencher = Backbencher("Baker", "Liberal")
party_leader = PartyLeader("Carney", "2025")