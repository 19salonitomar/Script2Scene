# Text-to-Image Generator

This project is a Text-to-Image Generator application built using Streamlit for a beautiful and interactive user interface. It leverages Stable Diffusion models and Hugging Face’s generative models to create images based on text descriptions. The application is designed to be easily run and modified using Visual Studio Code (VS Code).

## Features

- **User-Friendly Interface**: Developed with Streamlit to provide an intuitive and visually appealing web interface.
- **Advanced Text-to-Image Generation**: Uses Stable Diffusion and other generative models from Hugging Face for high-quality image generation.
- **Customizable**: Easy to adapt and expand with different models or additional features.

## Prerequisites

Before you get started, ensure you have the following installed:

- Python 3.8 or higher
- [VS Code](https://code.visualstudio.com/) with Python extension
- [Git](https://git-scm.com/)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/text-to-image-generator.git
    cd text-to-image-generator
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Download Model Weights**:
    - Ensure you have the necessary model weights and configurations. This may involve setting up Hugging Face credentials and downloading models.

## Running the Application

To start the Text-to-Image Generator application, run:
```bash
streamlit run app.py
```

## Usage

1. **Enter a Text Description**: Type a description of the image you want to generate in the input box.
2. **Generate Image**: Click the "Generate" button to create an image based on your description.
3. **View and Save**: The generated image will be displayed on the page. You can save it by right-clicking and selecting "Save image as...".

## Configuration

You can modify the configuration settings such as model paths and generation parameters by editing `config.py`.

## Troubleshooting

- **Model Download Issues**: Ensure you have a stable internet connection and a valid Hugging Face API token if required.
- **Environment Issues**: Make sure all dependencies are correctly installed and the virtual environment is activated.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For more details, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue on the GitHub repository or contact salonitomar5813@gmail.com.
