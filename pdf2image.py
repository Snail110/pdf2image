import os
from pdf2image import convert_from_path
import zipfile

def pdf_to_images(pdf_path, output_folder, dpi=300):
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path, dpi=dpi)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
    return image_paths

def zip_images(image_paths, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for img_path in image_paths:
            arcname = os.path.basename(img_path)
            zipf.write(img_path, arcname)

def process_all_pdfs(input_dir):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            pdf_name = os.path.splitext(filename)[0]
            output_img_dir = os.path.join(input_dir, f'{pdf_name}_images')
            zip_output = os.path.join(input_dir, f'{pdf_name}.zip')

            print(f"Processing {filename}...")
            image_paths = pdf_to_images(pdf_path, output_img_dir)
            zip_images(image_paths, zip_output)
            print(f"Saved zip: {zip_output}")

if __name__ == "__main__":
    input_pdf_dir = '/ICML2025/'  # 替换为你的实际路径
    process_all_pdfs(input_pdf_dir)