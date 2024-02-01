#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tldextract
import argparse
from quo import echo


DEPTH = 5

def config_download_path(download_path):
    """
        create directory if not exist download_path
    """
    if not os.path.exists(download_path):
        os.makedirs(download_path)

def is_valid_image_url(url):
    url_with_http_scheme = urlparse(url)._replace(scheme='http').geturl()
    return url_with_http_scheme.startswith('http')

def download_image(url, path):
    print(f"\t[{url[:50]}] ... ", end='')
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

def extract_images_from_page(url, path, downloaded_img):
    echo(f"Extract from {url} : ",underline=True, fg="blue",nl = False)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print()
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img') + soup.find_all('picture')
            for img_tag in img_tags:
                if img_tag.name == 'picture':
                    # If the tag is a <picture>, extract the source from the <source> tag
                    source_tag = img_tag.find('source')
                    if source_tag:
                        img_url = source_tag.get('srcset', '').split()[0]
                    else:
                        # If no <source> tag, use the <img> tag
                        img_url = img_tag.get('src')
                else:
                    img_url = img_tag.get('src')
                
                if img_url and is_valid_image_url(img_url):
                    img_url = urljoin(url, img_url)
                    img_url = urlparse(img_url)._replace(scheme='http').geturl()
                    img_name = os.path.basename(urlparse(img_url).path)
                    img_path = os.path.join(path, img_name)
                    if img_url not in downloaded_img:
                        download_image(img_url, img_path)
                        downloaded_img.add(img_url)
        else:
            print(f"Bad response -> {response}")
    except Exception as e:
        print(f"Error in request : {e}")

def spider(url, recursion_depth, download_path, base_domain, visited_urls, downloaded_img):
    if recursion_depth == 0 or url in visited_urls:
        return
    visited_urls.add(urljoin(base_domain, url))
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    link_domain = tldextract.extract(url).domain
    # print(f"link_domain = {link_domain}")
    if link_domain == base_domain:
        extract_images_from_page(url, download_path, downloaded_img)
    
    # Recursively follow links and download images
    try:
        responses = requests.get(url)
        if responses.status_code == 200:
            soup = BeautifulSoup(responses.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                # print(f"{DEPTH - recursion_depth} - href = {href}")
                tabs = '\t' * (DEPTH - recursion_depth + 1)
                print(f"\n{tabs}|\n{tabs}└> [{href}]", end= '')
                if href:
                    link_url = urljoin(url, href)
    
                    # Ajouter le schéma 'http' si l'URL relative ne contient pas de schéma
                    if urlparse(link_url).scheme == '':
                        link_url = urlparse(link_url)._replace(scheme='http').geturl()

                    link_domain = tldextract.extract(link_url).domain
                    if link_domain == base_domain:
                        spider(link_url, recursion_depth - 1, download_path, base_domain, visited_urls, downloaded_img)
                    else:
                        print()
                else:
                    print()
        else:
            print(f"Bad response -> {responses}")
    except Exception as e:
        print(f"Error in request : {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spider program to extract images from a website.")
    parser.add_argument("url", help="URL of the website")
    parser.add_argument("-r", action="store_true", help="Recursively download images")
    parser.add_argument("-l", type=int, default=DEPTH, help="Maximum depth level for recursive download")
    parser.add_argument("-p", type=str, default="./data/", help="Path to save downloaded files")

    args = parser.parse_args()
    base_domain = tldextract.extract(args.url).domain
    DEPTH = args.l
    print(f"base_domaine = {base_domain}")
    config_download_path(args.p)
    if args.r:
        spider(args.url, args.l, args.p, base_domain, set(), set())
    else:
        extract_images_from_page(args.url, args.p, base_domain, set())