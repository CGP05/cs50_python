class MP:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Backbencher:
    def __init__(self, name, party):
        self.name = name
        self.party = party

    ...


class PartyLeader:
    def __init__(self, name, leader_since):
        self.name = name
        self.leader_since = leader_since

    ...