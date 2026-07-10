mps = [
    {"name": "Yvan Baker", "party": "Conservative"},
    {"name": "Michael Chong", "party": "Conservative"},
    {"name": "Danielle Martin", "party": "Liberal"},
    {"name": "Elizabeth May", "party": "Green"},
    {"name": "Mark Carney", "party": "Liberal"},
    {"name": "Marylin Gladu", "party": "Liberal"},
]

conservatives = [
    mp["name"] for mp in mps if mp["party"] =="Conservative"
]

for conservative in sorted(conservatives):
    print(conservative)