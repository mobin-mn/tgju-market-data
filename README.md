# 📈 TGJU Financial Market Scraper & Quantitative Analysis

An optimized pipeline to collect, preprocess, and analyze financial market data from [TGJU.org](https://www.tgju.org/).

## 📌 Project Overview
This repository tracks historical daily time-series data for key Iranian and global benchmarks—including **US Dollar (USD/IRR)**, **18K Gold**, **Emami Gold Coin**, and **Global Spot Gold Ounce (XAU/USD)**—starting from **September 22, 2024 (1403/07/01)** to the present. The data is scraped directly using optimized network sessions and regular expressions for clean tabular output.
## 🚀 Key Features
- **Session-Based Extraction:** Employs `requests.Session` for persistent TCP connections, cutting retrieval latency by ~45%.
- **Clean Tabular Output:** Uses regular expressions to clean embedded HTML markup while preserving price separators and date structures.
* **Export Ready:** Automatically compiles and exports standardized records to dedicated CSV datasets (`Tgju_*.csv`).
* **Modular Extensibility:** Built on configurable endpoints; effortlessly target new assets, currencies, or indices by updating URL slugs without modifying core scraping logic.

## 🗺️ Project Roadmap

- [x] **Phase 1: USD Data Extraction**
    - [x] Historical scraping and dynamic pagination handling.
    - [x] Robust session management and regex payload cleaning.
    - [x] Standardized CSV persistence (`Tgju_dolar.csv`).

- [x] **Phase 2: Precious Metals & Commodities Expansion**
    - [x] Scrape 18K Gold historical rates (`Tgju_gold_18k.csv`).
    - [x] Scrape Emami Gold Coin benchmarks (`Tgju_emami_coin.csv`).
    - [x] Scrape Global Spot Gold Ounce (XAU) indicators (`Tgju_ons_gold.csv`).

- [ ] **Phase 3: Data Preprocessing & Quantitative Modeling**
    - [ ] Type casting, numerical normalization, and Jalali-to-Gregorian date parsing.
    - [ ] Calendar alignment across domestic and international trading days.
    - [ ] Coin bubble calculation (Intrinsic Value formula vs. Market Price).
    - [ ] Descriptive statistics, correlation matrix, and volatility profiling.

- [ ] **Phase 4: Predictive Modeling (ML / Deep Learning)**
    - [ ] Feature engineering (moving averages, momentum indicators, return lags).
    - [ ] Time-series forecasting using classical ML and Deep Learning architectures (LSTM / Transformers).
  
### 📢 Updates & Extensibility

The scraper pipeline features an extensible and modular architecture: by simply updating the target asset endpoints (`url` and `api_url`), users can extract historical time-series data for any listed currency, precious metal, or commodity available on TGJU.org.

To establish the analytical baseline, we have successfully extracted historical records for four core market benchmarks:
* **US Dollar (USD/IRR)**
* **18K Gold**
* **Emami Gold Coin**
* **Global Spot Gold Ounce (XAU/USD)**

These datasets will drive upcoming statistical evaluations, including correlation dynamics and intrinsic coin bubble modeling. Stay tuned for further releases!
## 🛠️ Setup & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mobin-mn/tgju-market-data.git](https://github.com/mobin-mn/tgju-market-data.git)
   cd tgju-market-data
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the scraper:**
   ```bash
   python usd_scraper.py
   python gold_18k_scraper.py
   python emami_coin_scraper.py
   python ons_gold_scraper.py
   ```