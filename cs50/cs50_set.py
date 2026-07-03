mps = [
    {"name": "Yvan Baker", "party": "Liberal"},
    {"name": "Michael Chong", "party": "Conservative"},
    {"name": "Danielle Martin", "party": "Liberal"},
    {"name": "Elizabeth May", "party": "Green"},
    {"name": "Mark Carney", "party": "Liberal"},
    {"name": "Marylin Gladu", "party": "Liberal"},
]

parties = set()
for mp in mps:
    if mp["party"] not in mps:
        parties.append(mp["party"])

for party in sorted(parties):
    print(party)