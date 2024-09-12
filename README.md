# Folder Speed Test

`Folder Speed Test` is a simple PySide6-based GUI tool to benchmark the read and write speeds of a selected folder on your system. It simulates the behavior of tools like CrystalDiskMark but allows users to select any folder for testing, making it convenient for checking specific directories.

This tool performs the following tests:

- Single file speed tests for 1MB, 100MB, and 1GB files.
- Multiple small file tests for 10×1MB, 20×1MB, 100×1MB, and 1000×1MB files.
- Displays both read and write speeds in MB/s.
- Uses a progress bar (with a maximum value set at 1GB/s) to display speed graphically.
- Automatically cleans up test files after each test is completed.

---

## Features

- **Folder Selection**: Choose any folder on your system to perform the speed tests.
- **Custom File Sizes**: Tests the speed of both small and large files (1MB to 1GB).
- **Multiple File Testing**: Tests for large numbers of small files, ideal for stress testing.
- **Free Space Check**: Ensures the selected folder has enough free space before starting the test.
- **Auto Cleanup**: All test files are deleted after the speed tests are completed.
- **User-Friendly Interface**: Simple GUI with real-time progress updates.

---

## Installation

To use `Folder Speed Test`, you need to have **Python 3.8+** installed, along with the required dependencies such as `PySide6` and `psutil`.

### Step 1: Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/folder-speed-test.git
cd folder-speed-test
```

### Step 2: Create a Virtual Environment (optional but recommended)

Creating a virtual environment is highly recommended to keep your dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Required Dependencies

Install the required Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not created, you can manually install the required packages:

```bash
pip install PySide6 psutil
```

### Step 4: Run the Application

After installing the dependencies, you can run the application using:

```bash
python folder_speed_test.py
```

---

## Usage

Once the program is running, follow these steps to test the speed of a folder:

1. **Select Folder**: Use the "Browse" button to open a folder dialog, and choose the folder where you want to test the speed.
2. **Start Test**: Click the "Start Test" button to run the write/read speed tests.
3. **Progress Display**: The tool will display the write and read speeds in real-time for various file sizes, using progress bars and speed labels.
4. **Results**: After the tests are completed, all test files will be automatically removed from the folder.

### Test Cases

- **Single File Tests**: The application will perform tests for:
  - 1MB file
  - 100MB file
  - 1GB file

- **Multiple File Tests**:
  - 10×1MB files
  - 20×1MB files
  - 100×1MB files
  - 1000×1MB files

---

## Project Structure

The project has a simple structure:

```
folder-speed-test/
│
├── folder_speed_test.py   # Main application file
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## Requirements

- **Python**: Version 3.8 or higher
- **PySide6**: For creating the GUI (Install via `pip install PySide6`)
- **psutil**: For checking available disk space (Install via `pip install psutil`)

---

## Screenshots

### Folder Selection:
![Folder Selection](https://example.com/folder-selection.png)

### Speed Test in Progress:
![Speed Test](https://example.com/speed-test.png)

### Results with Read and Write Speed:
![Results](https://example.com/results.png)

---

## Contributing

Contributions are welcome! If you have ideas for improving the application or want to fix bugs, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- Inspired by CrystalDiskMark.
- Built using the PySide6 library for the GUI.
- Thanks to [psutil](https://github.com/giampaolo/psutil) for the disk space utilities.

---

### Additional Notes

- **Cross-Platform Compatibility**: This tool works on Linux and Windows (since it's based on Python), but make sure the folder you test has appropriate permissions.
- **Performance**: The tool is not designed for super-fast enterprise storage but can give a good estimate of read/write performance for typical folders and drives.

---

### How to Get Help

If you encounter any issues while installing or using the application, feel free to [open an issue](https://github.com/YOUR_USERNAME/folder-speed-test/issues) on GitHub.

---

Feel free to replace placeholder URLs and `YOUR_USERNAME` with your actual GitHub username and the URLs of images/screenshots you might want to include.

### Summary:
- This `README.md` gives detailed instructions on how to set up the project, run it, and contribute. It's formatted for ease of use and provides clear guidelines for anyone interested in trying or contributing to your project! Let me know if you need anything else! 😄
