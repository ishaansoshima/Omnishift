# Omnishift

Omnishift is a simple yet powerful command-line tool for converting images between different formats. It supports common image formats including PNG, JPG, JPEG, BMP, GIF, and TIFF.

## Installation

### From Source
1. Clone the repository:
```bash
git clone https://github.com/yourusername/omnishift.git
cd omnishift
```

2. Install using pip:
```bash
pip install .
```

### Dependencies
- Python 3.6 or higher
- Pillow (PIL) >= 9.0.0

## Usage

After installation, you can use Omnishift from the command line:

```bash
omnishift <input_image_path> <output_format>
```

### Arguments
- `input_image_path`: Path to the input image file
- `output_format`: Desired output format (png/jpg/jpeg/bmp/gif/tiff)

### Examples

Convert a PNG to JPG:
```bash
omnishift image.png jpg
```

Convert a JPEG to PNG:
```bash
omnishift photo.jpeg png
```

Convert a BMP to TIFF:
```bash
omnishift picture.bmp tiff
```

## Supported Formats

- PNG
- JPG/JPEG
- BMP
- GIF
- TIFF

## Error Handling

The tool will display appropriate error messages for:
- Non-existent input files
- Unsupported output formats
- Invalid image files
- General conversion errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Ishaan S. Oshima (ishaansoshima@gmail.com)

## Roadmap

Future plans include:
- Support for batch conversion
- Additional image formats
- Image optimization options
- Basic image editing features

## Bug Reports

If you discover any bugs, please create an issue on GitHub.