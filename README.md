# LaTeX Delimiter Converter and Renderer

![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

A simple Streamlit application designed to convert non-standard LaTeX delimiters from OpenAI API outputs to standard LaTeX symbols, enabling accurate rendering of mathematical formulas alongside markdown content.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Delimiter Conversion**: Automatically replaces non-standard LaTeX delimiters `\[` `\]` and `\(` `\)` with standard `$` and `$$` symbols.
- **Markdown Rendering**: Supports rendering of standard markdown alongside LaTeX mathematical expressions.
- **User-Friendly Interface**: Provides an intuitive text area for input and real-time rendering of processed content.

## Installation

### Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Clone the Repository

```bash
git clone https://github.com/yourusername/latex-delimiter-converter.git
cd latex-delimiter-converter
```

### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

*If `requirements.txt` is not provided, you can install Streamlit directly:*

```bash
pip install streamlit
```

## Usage

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501` in your browser.

## Example

### Input Text

```markdown
Here is an inline equation: \( E = mc^2 \).

And here is a display equation:
\[
\int_{a}^{b} f(x) \, dx
\]

This is a regular markdown text with **bold** and _italic_ formatting.
```

### Processed Output

Here is an inline equation: $E = mc^2$.

And here is a display equation:
$$\int_{a}^{b} f(x) \, dx$$

This is a regular markdown text with **bold** and _italic_ formatting.

*The Streamlit app will render the equations properly alongside the markdown text.*

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit your changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Developed with ❤️ using [Streamlit](https://streamlit.io/) and Python.*