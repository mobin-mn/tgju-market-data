# 📈 TGJU Financial Market Scraper & Quantitative Analysis

An optimized pipeline to collect, preprocess, and analyze financial market data from [TGJU.org](https://www.tgju.org/).

## 📌 Project Overview
This repository currently tracks historical daily data for the **US Dollar (USD/IRR)** starting from **September 22, 2024 (1403/07/01)** to the present. The data is scraped directly using optimized network sessions and regular expressions for clean tabular output.

## 🚀 Key Features
- **Session-Based Extraction:** Employs `requests.Session` for persistent TCP connections, cutting retrieval latency by ~45%.
- **Clean Tabular Output:** Uses regular expressions to clean embedded HTML markup while preserving price separators and date structures.
- **Export Ready:** Automatically compiles and exports standardized records to `Tgju_dolar.csv`.

## 🗺️ Project Roadmap
- [x] **Phase 1: USD Data Extraction**
  - Historical scraping and pagination handling.
  - Data cleaning and initial CSV persistence.
- [ ] **Phase 2: Gold & Commodities Expansion**
  - Scrape 18K and 24K Gold prices.
  - Scrape global Gold Ounce (XAU) indicators.
- [ ] **Phase 3: Data Preprocessing & Statistical Modeling**
  - Type casting (numeric conversions and Persian-to-Gregorian date parsing).
  - Descriptive statistics, correlation analysis, and volatility modeling.
- [ ] **Phase 4: Machine Learning & Deep Learning**
  - Feature engineering (moving averages, momentum indicators, return lags).
  - Time-series forecasting using classical ML and Deep Learning architectures (LSTM / Transformers).
## 📢 Updates
Any future modifications and new features will be thoroughly documented in this file. Stay tuned!
## 🛠️ Setup & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the scraper:**
   ```bash
   python main.py
   ```