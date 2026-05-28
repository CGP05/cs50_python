from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open(r"C:\Users\chris\Pictures\shimmer the vim.png") as img:
        img.filter(ImageFilter.FIND_EDGES)
        img.save("out_edge_vim.png")

main()