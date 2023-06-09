# PDF_Merge

PDF Merger is a Python script that merges multiple PDF files into a single PDF file using the PyPDF2 library.

## Features

- Combines multiple PDF files into one.
- Simple and easy-to-use.
- Configurable input directory for PDF files.
- Outputs the merged PDF as 'result.pdf'.

## Requirements

- Python 3.x
- Listed in requirements.txt (install with `pip install -r requirements.txt`)

## Usage

1. Place the PDF files you want to merge in the 'input' directory.
2. Run the script by executing `python main.py`.
3. The script will merge the PDF files and create a file named 'result.pdf' in the same directory.
4. The merged PDF file can now be accessed and used as needed.

## Running in Docker

To run the PDF Merger program inside a Docker container, follow these steps:

### 1. Build the Docker Image

First, navigate to the directory containing the Dockerfile and execute the following command to build the Docker image:

```bash
docker build -t pdf-merger .
```

This command will build a Docker image named "pdf-merger" using the provided Dockerfile. Make sure you have Docker installed and running on your machine.

### 2. Run the Docker Container

After successfully building the Docker image, you can run the PDF Merger program inside a Docker container. Execute the following command:

```bash
docker run --rm -v <path_to_input_folder>:/app/input -v <path_to_output_folder>:/app -it pdf-merger
```

Replace <path_to_input_folder> with the absolute path to the directory containing the PDF files you want to merge. Replace <path_to_output_folder> with the absolute path to the directory where you want to save the merged PDF file.

The -v flag is used to mount volumes in the container, allowing access to the input and output folders from the host machine.

The --rm flag ensures that the container is automatically removed after the script finishes running. The -it flags enable an interactive terminal session within the container.

### 3. View the Merged PDF

Once the script completes its execution, the merged PDF file will be available in the specified output folder. You can access it on your host machine.

Note: The Docker image is based on Python 3.11.3 and automatically installs the required dependencies listed in the requirements.txt file.

## Configuration

The script uses the following configuration:

- `INPUT_DIR`: The directory where the input PDF files are stored. By default, it is set to the 'input' directory in the same location as the script. You can modify this variable in the script if needed.

## References

- Stack Overflow: Merge PDF files - https://stackoverflow.com/questions/3444645/merge-pdf-files
- PyPDF2 Documentation: PyPDF2 v3.0.0 - https://pypdf2.readthedocs.io/en/3.0.0/
- ChatGPT: OpenAI's ChatGPT - https://github.com/openai/chatgpt
