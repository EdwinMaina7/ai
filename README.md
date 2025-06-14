# AI Crypto Bot

A Python-based AI chatbot that can provide cryptocurrency prices and general AI responses.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `config.py` file with your API keys:
   ```python
   OPENROUTER_API_KEY = "your-api-key"
   SITE_URL = "your-site-url"
   SITE_TITLE = "your-site-title"
   ```

## Usage

Run the bot:
```
python main.py
```

## Security Note

Never commit your `config.py` file or expose your API keys. The `.gitignore` file is set up to prevent accidental commits of sensitive information.