# Screenshot to PDF

This project allows users to take multiple screenshots and save them as a single PDF file. It utilizes the `pyautogui` library for capturing screenshots and the `Pillow` library for image processing.

## Features

- Take a specified number of screenshots.
- Automatically saves screenshots in a designated folder on the Desktop.
- Combines all screenshots into a single PDF file.

## Requirements

To run this project, you need to have Python installed along with the following dependencies:

- `pyautogui`
- `Pillow`

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/screenshot-to-pdf.git
   ```

2. Navigate to the project directory:

   ```
   cd screenshot-to-pdf
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```
   python src/screenshot_to_pdf.py
   ```

2. Enter the number of screenshots you want to take when prompted.
3. You will have 10 seconds to prepare your screen before the screenshots are taken.
4. The script will automatically capture the specified number of screenshots and save them as a PDF on your Desktop.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.