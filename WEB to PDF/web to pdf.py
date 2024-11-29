import os
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from urllib.parse import urljoin

def get_images_from_webpage(url):
    """Fetch all image URLs from a webpage."""
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        image_urls = []
        
        for img in img_tags:
            if 'src' in img.attrs:
                img_url = urljoin(url, img['src'])
                if any(img_url.lower().endswith(ext) for ext in valid_extensions):
                    image_urls.append(img_url)
        
        return image_urls
    except Exception as e:
        print(f"Error fetching images: {e}")
        return []

def download_image(image_url, save_path):
    """Download an image from a URL."""
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False

def images_to_pdf(image_files, output_pdf):
    """Convert a list of image files to a single PDF."""
    pdf = FPDF()
    for image_file in image_files:
        try:
            pdf.add_page()
            pdf.image(image_file, x=10, y=10, w=190)
        except Exception as e:
            print(f"Error adding {image_file} to PDF: {e}")
    pdf.output(output_pdf)
    print(f"PDF generated: {output_pdf}")

def main(webpage_url, output_pdf):
    """Main function to fetch images from a webpage and convert them to a PDF."""
    print("Fetching images...")
    image_urls = get_images_from_webpage(webpage_url)
    
    if not image_urls:
        print("No images found on the webpage.")
        return

    os.makedirs("images", exist_ok=True)
    image_files = []
    for idx, img_url in enumerate(image_urls):
        save_path = os.path.join("images", f"image_{idx + 1}.jpg")
        if download_image(img_url, save_path):
            image_files.append(save_path)

    if image_files:
        print("Converting images to PDF...")
        images_to_pdf(image_files, output_pdf)

        # Cleanup downloaded images
        for file in image_files:
            os.remove(file)
        os.rmdir("images")
    else:
        print("No images were successfully downloaded.")

if __name__ == "__main__":
    # Replace with the webpage URL and desired PDF output filename
    webpage_url = input("Enter the webpage URL: ")
    output_pdf = "output.pdf"
    main(webpage_url, output_pdf)