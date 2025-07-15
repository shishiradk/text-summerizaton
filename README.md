# text-summerizaton

## Overview

**text-summerizaton** is a Python project for automatic text summarization, focusing on speeches and documents such as APJ Abdul Kalam's farewell speech. It leverages modern NLP techniques and large language models to generate concise summaries.

## Features

- Summarizes long speeches and documents into concise points
- Supports PDF input (e.g., `apjspeech.pdf`)
- Interactive Jupyter notebook for experimentation (`text_summerization.ipynb`)
- Customizable prompts for summary generation
- Integrates with OpenAI and HuggingFace APIs

## Project Structure

```
.env                      # Environment variables (API keys, etc.)
.gitignore                # Git ignore rules
apjspeech.pdf             # Example input PDF (APJ Abdul Kalam's speech)
app.py, app2.py           # Python scripts for summarization
LICENSE                   # MIT License
README.md                 # Project documentation
requirements.txt          # Python dependencies
text_summerization.ipynb  # Jupyter notebook for summarization workflow
```

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd text-summerizaton
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   - Copy `.env.example` to `.env` (if available) or create a `.env` file.
   - Add your OpenAI, LangChain, and HuggingFace API keys.

4. **Run the notebook**
   - Open `text_summerization.ipynb` in Jupyter or VS Code and follow the cells.

5. **Or run the script**
   ```sh
   python app.py
   ```

## Usage

- Place your input document (PDF or text) in the project directory.
- Update the script or notebook to point to your input file.
- Run the summarization process to generate a summary.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- APJ Abdul Kalam's speeches for sample data
- OpenAI, HuggingFace, and LangChain for NLP