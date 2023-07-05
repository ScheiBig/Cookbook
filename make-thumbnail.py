from PIL import Image
import sys

def main():
    img_path = sys.argv[1]

    img_path_s = img_path.rsplit(".", 1)
    img_out_path = img_path_s[0] + ".thumbnail." + img_path_s[1]

    img = Image.open(img_path)

    w, h = img.size
    nh = 128
    nw = int(nh / h * w)

    img_thumb = img.resize((nw, nh))
    img_thumb.save(img_out_path)


if __name__ == "__main__": main()
