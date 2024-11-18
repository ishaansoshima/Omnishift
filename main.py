#!/usr/bin/env python3
from PIL import Image
import os
import argparse

def convert_img(ip_path, op_format):
    if not os.path.isfile(ip_path):
        print(f"Error: the file {ip_path} does not exist.")
        return
    supported_format = {"png", "jpg", "jpeg", "bmp", "gif", "tiff"}
    if op_format.lower() not in supported_format:
        print(f"Error: Only supports: {supported_format}")
        return
    try:
        img = Image.open(ip_path)
        base = os.path.splitext(ip_path)[0]
        op_path = f"{base}.{op_format.lower()}"
        
        # Convert to RGB if saving as JPEG
        if op_format.lower() in ['jpg', 'jpeg']:
            img = img.convert('RGB')
        
        save_format = 'JPEG' if op_format.lower() == 'jpg' else op_format.upper()
        
        img.save(op_path, save_format)
        print(f"Image saved as {op_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Image conversion into specified format")
    parser.add_argument("input_path", type=str, help="Path of input image")
    parser.add_argument("output_format", type=str, help="Format to convert to")
    args = parser.parse_args()
    convert_img(args.input_path, args.output_format)

if __name__ == "__main__":
    main()