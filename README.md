# Screenshot to PDF

This project allows users to take multiple screenshots and save them as a single PDF file. It utilizes the `pyautogui` library for capturing screenshots and the `Pillow` library for image processing.

## Features

- Take a specified number of screenshots.
- Simulates pressing the right arrow key between screenshots (useful for flipping pages in viewers).
- Automatically saves screenshots in a designated folder on the Desktop.
- Combines all screenshots into a single PDF file.
- Opens the output folder automatically when done.

## Why use this tool?

Some PDF files are embedded in web pages or applications in a way that prevents direct downloading or extraction. For example, certain eBook readers, online course platforms, or document viewers may disable download options or use custom rendering that blocks copy/paste and extraction tools.

**Screenshot to PDF** provides a practical workaround by automating the process of capturing each visible page as a screenshot and then compiling those images into a single PDF. This is especially useful when:

- The PDF is embedded in a viewer that blocks downloads.
- Extraction tools (like browser extensions or PDF utilities) do not work.
- You need a quick, reliable way to archive or print the content for offline use.

> **Note:** Please respect copyright and terms of service when using this tool.

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
   Or install manually:
   ```
   pip install pyautogui pillow
   ```

## Usage

1. **Prepare your screen:**  
   Open the embedded PDF or document you want to capture. Make sure the first page is visible and ready.

2. **Run the script:**

   ```
   python src/screenshot_to_pdf.py
   ```

3. **Follow the prompts:**
   - Enter the number of screenshots/pages you want to capture.
   - You will have 10 seconds to prepare your screen before the screenshots start.
   - The script will automatically take screenshots, pressing the right arrow key between each one (to flip pages).

4. **Result:**
   - Screenshots and the combined PDF will be saved in a `ScreenshotToPDF` folder on your Desktop.
   - The folder will open automatically when done.

## Example Use Case

Suppose you are viewing a PDF in an online course platform that does not allow downloading or copying. You can use this tool to:
- Set the viewer to full screen for best quality.
- Run the script and specify the number of pages.
- Let the tool flip through each page, capturing screenshots and compiling them into a PDF for your personal offline use.

## Limitations

- The quality of the resulting PDF depends on your screen resolution and the size of the viewer window.
- This tool does not bypass any DRM or security restrictions; it simply automates what you could do manually.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
