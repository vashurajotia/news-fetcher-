# 📰 News Fetcher using Python & NewsAPI

This is a simple Python command-line application that fetches the latest news articles based on the user's search query. It uses the [NewsAPI](https://newsapi.org/) to retrieve real-time headlines and article links.

## 💡 Features

- Get real-time news from trusted sources
- Search any topic of interest (e.g., technology, health, sports, etc.)
- Display titles and URLs of articles in a clean format
- Easy to use and extend for beginners

## 📌 Requirements

- Python 3.x
- `requests` library

Install dependencies (if not already installed):
```bash
pip install requests
```
## 🚀 How to Run
```bash
python news_fetcher.py
```
You'll be prompted to enter a topic:
```
What type of news are you interested in today? : technology
```
The script will then display a list of recent articles with clickable URLs.

## 🔐 API Key
This project uses the NewsAPI. To get your free API key:

1. Visit https://newsapi.org/register
2. Sign up and generate your API key
3. Replace the existing api_key variable in the script with your key
```python
api_key = "your_api_key_here"
```
## 📷 Sample Output
```bash
1. AI is revolutionizing education across the globe
https://example.com/article1

******************************************************************************************

2. Python 3.13: What's new in the next release?
https://example.com/article2
```
## 📁 Project Structure
```
news_fetcher.py
README.md
```
## 📜 License
This project is open source and available under the MIT License.

