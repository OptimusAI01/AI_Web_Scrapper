# AI-Powered Web Scraper & Parser

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

A Streamlit application that scrapes any website and uses a local Large Language Model (LLM) via Ollama to extract structured data based on natural language commands.

---

### The Problem it Solves

Traditional web scraping requires developers to write and maintain custom CSS selectors or XPath expressions for each website. This is time-consuming and breaks easily when a website's layout changes. This tool eliminates that process by leveraging an LLM to "understand" the page content and extract the desired information from a simple, plain-English description.

### Features

*   **Dynamic Scraping:** Scrapes single-page applications using Selenium.
*   **Intelligent Parsing:** Uses a local LLM (Llama 3.1 via Ollama) to parse and extract data.
*   **Natural Language Commands:** Simply describe the data you want (e.g., "Extract all the article titles and their authors").
*   **Simple UI:** Built with Streamlit for a clean and interactive user experience.
*   **Local First:** Runs entirely on your machine, ensuring data privacy and no API costs.

### Tech Stack

*   **Backend & App Logic:** Python
*   **AI/LLM Integration:** LangChain, Ollama
*   **Web Scraping:** Selenium, BeautifulSoup4
*   **Web Framework:** Streamlit
*   **LLM Model:** Llama 3.1 (or any other model supported by Ollama)

### Setup & Usage

Follow these steps to run the project locally.

**1. Prerequisites:**

*   Python 3.9+
*   Google Chrome installed
*   [Ollama](https://ollama.com/) installed and running.

**2. Clone the Repository:**

```bash
git clone https://github.com/OptimusAI01/AI-Web-Scraper.git
cd AI-Web-Scraper
```

**3. Set up a Virtual Environment:**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**4. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**5. Configure Ollama:**

Ensure Ollama is running. Pull the Llama 3.1 model if you haven't already:

```bash
ollama pull llama3.1
```

**6. Run the Application:**

```bash
streamlit run main.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

### How It Works

1.  **Input URL:** The user provides a URL to the Streamlit frontend.
2.  **Scraping:** Selenium launches a headless Chrome browser, loads the page, and extracts the raw HTML DOM.
3.  **Cleaning:** BeautifulSoup parses the HTML, removes all `<script>` and `<style>` tags, and extracts the clean, visible text content.
4.  **Parsing:** The user provides a natural language prompt (e.g., "list all product names"). The cleaned text is chunked and fed to the LLM via a LangChain prompt, instructing it to extract only the requested information.
5.  **Display:** The extracted data is displayed back to the user in the Streamlit interface.

---

Find me on [Linkedin!](https://www.linkedin.com/in/rashedmamdouh4233/)
