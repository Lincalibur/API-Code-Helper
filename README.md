# API Code Helper

API Code Helper is a Python application built with CustomTkinter to generate JavaScript code snippets for connecting to various API endpoints using different authentication methods.

## Features

- **GUI Interface:** Allows users to input API details such as authentication method, endpoint URL, client credentials, and expected response type (JSON or XML).
- **Code Generation:** Automatically generates JavaScript code snippets based on user inputs.
- **Code Output:** Displays generated JavaScript code in a text area for easy viewing and copying.
- **File Saving:** Option to save the generated JavaScript code to a file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lincalibur/API-Code-Helper.git
   cd API-Code-Helper
   ```

2. Install dependencies:

   ```bash
   pip install customtkinter  # Ensure CustomTkinter is installed
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Launch the application using `python main.py`.
2. Fill in the API details in the GUI:
   - API Name
   - Authentication Method
   - Authentication Endpoint URL
   - Client ID
   - Client Secret
   - Expected Response Type (JSON or XML)
3. Click on "Generate JS Code" to generate the JavaScript code snippet.
4. The generated code will be displayed in the text area.
5. Optionally, click on "Save JS Code" to save the generated JavaScript code to a file.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using [CustomTkinter](https://github.com/pmgbergen/customtkinter)
- Inspired by the need to simplify API integration tasks