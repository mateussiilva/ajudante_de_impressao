from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def pixel_for_cm(size, dpi):
    if len(size) == 2:
        return tuple(map(lambda x: 2.54 * (x / dpi), size))


def get_size_image_and_dpi(path_file):
    try:
        i = Image.open(path_file)
        return i.size, int(i.info["dpi"][0])
    except FileNotFoundError:
        print(f"O arquivo '{path_file}' não exite")
    except Exception as err:
        print(err)
