class MP:
    def __init__(self)

class Backbencher:
    def __init__(self, name, party):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.party = party

    ...


class PartyLeader:
    def __init__(self, name, leader_since):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.leader_since = leader_since

    ...