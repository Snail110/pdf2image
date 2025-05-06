import os
from PIL import Image

# 设置参数
IMAGE_ROOT_DIR = 'ICML2025/'  # 替换为你的实际目录
GRID_SIZE = (4, 4)  # 4x4 网格

def get_all_page1_images(image_dir):
    images = []
    for folder in sorted(os.listdir(image_dir)):
        folder_path = os.path.join(image_dir, folder)
        if os.path.isdir(folder_path) and folder.endswith("_images"):
            page1_path = os.path.join(folder_path, "page_1.png")
            if os.path.exists(page1_path):
                img = Image.open(page1_path).convert("RGB")
                images.append(img)
    return images

def create_image_grid(images, grid_size, save_path):
    rows, cols = grid_size
    img_width, img_height = images[0].size

    grid_img = Image.new('RGB', (cols * img_width, rows * img_height), color=(255, 255, 255))

    for idx, img in enumerate(images):
        row = idx // cols
        col = idx % cols
        grid_img.paste(img, (col * img_width, row * img_height))

    grid_img.save(save_path)
    print(f"保存拼图：{save_path}")

def main():
    images = get_all_page1_images(IMAGE_ROOT_DIR)
    total = len(images)
    batch_size = GRID_SIZE[0] * GRID_SIZE[1]
    num_grids = (total + batch_size - 1) // batch_size

    for i in range(num_grids):
        batch_images = images[i * batch_size:(i + 1) * batch_size]

        # 如果不足 16 张，用空白图填充，保持尺寸一致
        while len(batch_images) < batch_size:
            blank_img = Image.new('RGB', batch_images[0].size, color=(255, 255, 255))
            batch_images.append(blank_img)

        output_path = os.path.join(IMAGE_ROOT_DIR, f'grid_{i + 1}.png')
        create_image_grid(batch_images, GRID_SIZE, output_path)

if __name__ == "__main__":
    main()