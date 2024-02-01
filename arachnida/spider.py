import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

import argparse

def config_download_path(download_path):
    """
        create directory if not exist download_path
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)

def is_valid_image_url(url):
    return url.startswith('http')

def download_image(url, path):
    print(f"\t[{url[:25]}] ... ", end='')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                    file.write(response.content)
            print("✅")
        else:
            print("❌")
    except Exception as e:
        print(f"❌ : {e}")

def extract_images_from_page(url, path):
    print(f"Extract from {url}", end=' : ')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print()
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url and is_valid_image_url(img_url):
                    img_url = urljoin(url, img_url)
                    img_name = os.path.basename(urlparse(img_url).path)
                    img_path = os.path.join(path, img_name)
                    download_image(img_url, img_path)
        else:
            print(f"Bad response -> {response}")
    except Exception as e:
        print(f"Error in request : {e}")

def spider(url, recursion_depth, download_path):
    if recursion_depth == 0:
        return
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    extract_images_from_page(url, download_path)

    # Recursively follow links and download images
    try:
        responses = requests.get(url)
        if responses.status_code == 200:
            soup = BeautifulSoup(responses.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and href.startswith('http'):
                    spider(href, recursion_depth - 1, download_path)
        else:
            print(f"Bad response -> {responses}")
    except Exception as e:
        print(f"Error in request : {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spider program to extract images from a website.")
    parser.add_argument("url", help="URL of the website")
    parser.add_argument("-r", action="store_true", help="Recursively download images")
    parser.add_argument("-l", type=int, default=5, help="Maximum depth level for recursive download")
    parser.add_argument("-p", type=str, default="./data/", help="Path to save downloaded files")

    args = parser.parse_args()
    print(f"args = {args.p}")
    config_download_path(args.p)
    if args.r:
        spider(args.url, args.l, args.p)
    else:
        extract_images_from_page(args.url, args.p)
