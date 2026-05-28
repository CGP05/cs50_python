def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
REPORT
name: {spacecraft.get("name", "Unknown")}
distance: {spacecraft.get("distance", "Unknown"} AU
orbit: {spacecraft.get("orbit", "Unknown")}
"""
