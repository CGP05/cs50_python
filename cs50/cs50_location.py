import sys

def main():
    coordinate_tuple = (43.654, -79.562)
    coordinate_list = [43.654, -79.562]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()
