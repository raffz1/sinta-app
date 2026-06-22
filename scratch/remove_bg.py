import os
from rembg import remove
from PIL import Image

assets_dir = 'assets'
images = ['sinta_cemas.png', 'sinta_mengingatkan.png', 'sinta_senang.png']

for img_name in images:
    img_path = os.path.join(assets_dir, img_name)
    if os.path.exists(img_path):
        print(f"Processing {img_name}...")
        input_image = Image.open(img_path)
        output_image = remove(input_image)
        output_image.save(img_path)
        print(f"Saved {img_name}")
print("Done!")
