import sys
import os
import shutil
import time
import psutil  # To check available disk space
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QProgressBar, QLabel, QLineEdit, QFileDialog
from PySide6.QtCore import Qt


class FolderSpeedTest(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up window
        self.setWindowTitle("Folder Speed Test")
        self.setGeometry(200, 200, 600, 400)

        # Main layout
        layout = QVBoxLayout()

        # Folder selection layout (text input + folder button)
        folder_layout = QHBoxLayout()
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Select a folder...")
        self.folder_button = QPushButton("Browse")
        self.folder_button.clicked.connect(self.open_folder_dialog)

        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.folder_button)
        layout.addLayout(folder_layout)

        # Start button
        self.start_button = QPushButton("Start Test")
        self.start_button.clicked.connect(self.start_test)
        layout.addWidget(self.start_button)

        # Create the layout for test progress bars (Read and Write)
        self.test_layout = QVBoxLayout()
        layout.addLayout(self.test_layout)

        # Set central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_folder_dialog(self):
        # Open folder dialog and set the selected folder to the input field
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_input.setText(folder)

    def start_test(self):
        # Get the folder path from the text input
        folder_path = self.folder_input.text()
        if folder_path and os.path.exists(folder_path):
            # Clear previous progress bars
            self.clear_progress_bars()

            # Check free space
            if not self.check_free_space(folder_path, 1024):  # 1GB
                print("Not enough free space for testing.")
                return

            # Perform the speed test in the selected folder
            self.perform_speed_test(folder_path)

            # Clean up test files after the speed test
            self.cleanup_test_files(folder_path)

    def clear_progress_bars(self):
        # Clear existing progress bars and labels
        for i in reversed(range(self.test_layout.count())):
            widget_to_remove = self.test_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

    def check_free_space(self, folder_path, required_space_mb):
        """Check if the folder has enough free space for the test."""
        disk_usage = psutil.disk_usage(folder_path)
        free_space_mb = disk_usage.free / (1024 * 1024)
        return free_space_mb >= required_space_mb

    def perform_speed_test(self, folder_path):
        # Single file tests (1MB, 100MB, 1GB)
        file_sizes = [1, 100, 1024]

        # Multiple file tests (10×1MB, 20×1MB, 100×1MB, 1000×1MB)
        multiple_file_tests = [(1, 10), (1, 20), (1, 100), (1, 1000)]

        # Run single file tests
        for size in file_sizes:
            self.create_progress_bar(folder_path, f"Single {size}MB File", size)

        # Run multiple file tests
        for size_mb, count in multiple_file_tests:
            self.create_progress_bar(folder_path, f"{count} × {size_mb}MB Files", size_mb, count)

    def create_progress_bar(self, folder_path, label, size_mb, file_count=1):
        # Add label for the test description
        test_label = QLabel(label)
        self.test_layout.addWidget(test_label)

        # Layout for Write and Read progress bars
        bar_layout = QHBoxLayout()

        # Write speed progress bar and label
        write_speed_bar = QProgressBar()
        write_speed_label = QLabel("0 MB/s")
        bar_layout.addWidget(QLabel("Write:"))
        bar_layout.addWidget(write_speed_bar)
        bar_layout.addWidget(write_speed_label)

        # Read speed progress bar and label
        read_speed_bar = QProgressBar()
        read_speed_label = QLabel("0 MB/s")
        bar_layout.addWidget(QLabel("Read:"))
        bar_layout.addWidget(read_speed_bar)
        bar_layout.addWidget(read_speed_label)

        # Add the bar layout to the main test layout
        self.test_layout.addLayout(bar_layout)

        # Perform the actual speed test for this set of files
        write_speed = self.write_test(folder_path, size_mb, file_count)
        read_speed = self.read_test(folder_path, size_mb, file_count)

        # Update progress bars and labels
        self.update_progress(write_speed_bar, write_speed_label, write_speed)
        self.update_progress(read_speed_bar, read_speed_label, read_speed)

    def write_test(self, folder_path, size_mb, count):
        start_time = time.time()

        # Writing multiple files or a single large file
        for i in range(count):
            file_path = os.path.join(folder_path, f"test_{i}_{size_mb}MB.bin")
            with open(file_path, 'wb') as f:
                f.write(os.urandom(size_mb * 1024 * 1024))  # Write random data

        duration = time.time() - start_time
        total_size = size_mb * count  # Total size in MB
        write_speed = total_size / duration  # MB/s
        return write_speed

    def read_test(self, folder_path, size_mb, count):
        start_time = time.time()

        # Reading multiple files or a single large file
        for i in range(count):
            file_path = os.path.join(folder_path, f"test_{i}_{size_mb}MB.bin")
            with open(file_path, 'rb') as f:
                f.read()

        duration = time.time() - start_time
        total_size = size_mb * count  # Total size in MB
        read_speed = total_size / duration  # MB/s
        return read_speed

    def update_progress(self, progress_bar, speed_label, speed):
        # Convert speeds to percentage (1GB/s = 100%)
        percentage = min((speed / 1024) * 100, 100)  # Max at 100%
        progress_bar.setValue(percentage)
        speed_label.setText(f"{speed:.2f} MB/s")

    def cleanup_test_files(self, folder_path):
        """Remove all test files created during the speed test."""
        for file_name in os.listdir(folder_path):
            if file_name.startswith("test_") and file_name.endswith(".bin"):
                try:
                    file_path = os.path.join(folder_path, file_name)
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error removing file {file_name}: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderSpeedTest()
    window.show()
    sys.exit(app.exec())
