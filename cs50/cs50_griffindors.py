mps = [
    {"name": "Yvan Baker", "party": "Liberal"},
    {"name": "Roman Baber", "party": "Conservative"},
    {"name": "Michael Chong", "party": "Conservative"},
    {"name": "Danielle Martin", "party": "Liberal"},
    {"name": "Elizabeth May", "party": "Green"},
    {"name": "Mark Carney", "party": "Liberal"},
    {"name": "Marylin Gladu", "party": "Liberal"},
]

def is_conservative(s):
    return s["party"] =="Conservative"

conservatives = filter(is_conservative, mps)

for conservative in sorted(conservatives, key=lambda m: m["name"]):
    print(conservative["name"])