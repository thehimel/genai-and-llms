from tools.remove_bg.utils.setup_model import setup_u2net_model
from rembg import remove
from PIL import Image

setup_u2net_model()

src_path = 'images/src.jpg'
dest_path = 'images/dest.png'

src = Image.open(src_path)
if src.mode != 'RGBA':
    src = src.convert('RGBA')

dest = remove(src)
dest.save(dest_path)
