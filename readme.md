# Data Science Assignment

A comprehensive data science project covering exploratory data analysis, data cleaning, feature engineering, machine learning, and web scraping.

## Project Overview

This project demonstrates a complete data science workflow including:
- Exploratory Data Analysis (EDA)
- Data Cleaning (missing values, duplicates)
- Feature Engineering & Encoding
- Data Visualization
- Statistical Analysis
- Machine Learning Models
- Web Scraping & Automation

## Project Structure

```
assignment/
├── data/
│   └── loan_data.csv                 # Main dataset
├── notebooks/
│   ├── 01_eda.ipynb                  # Exploratory Data Analysis
│   ├── 02_missing_values.ipynb       # Handle missing data
│   ├── 03_duplicates.ipynb           # Remove duplicates
│   ├── 04_label_one_hot_encoding.ipynb # Categorical encoding
│   ├── 05_visualizations.ipynb       # Data visualizations
│   ├── 06_outliers.ipynb             # Outlier detection & treatment
│   ├── 07_feature_engineering.ipynb  # Create new features
│   ├── 08_scaling.ipynb              # Normalize/standardize features
│   ├── 09_train_test_split.ipynb     # Data splitting
│   ├── 10_logistic_regression.ipynb  # Classification model
│   ├── 11_decision_tree.ipynb        # Tree-based model
│   ├── 12_kmeans.ipynb               # Clustering model
│   ├── 13_fastapi.ipynb              # API development
│   ├── 14_scraping.ipynb             # Web scraping
│   ├── 15_selenium.ipynb             # Selenium automation

├── app.py                             # FastAPI application
├── ekantipur_articles_20260426_170237.csv  # Scraped articles data
└── README.md                          # This file
```

## Notebooks Description

### Data Exploration & Cleaning
1. **01_eda.ipynb** - Initial exploration of the loan dataset
2. **02_missing_values.ipynb** - Identify and handle missing values
3. **03_duplicates.ipynb** - Detect and remove duplicate records
4. **06_outliers.ipynb** - Identify and treat outliers

### Data Preprocessing
4. **04_label_one_hot_encoding.ipynb** - Encode categorical variables
5. **07_feature_engineering.ipynb** - Create and transform features
6. **08_scaling.ipynb** - Normalize and standardize numerical features
7. **09_train_test_split.ipynb** - Split data for training and testing

### Visualization & Analysis
5. **05_visualizations.ipynb** - Create meaningful visualizations

### Machine Learning Models
10. **10_logistic_regression.ipynb** - Binary classification model
11. **11_decision_tree.ipynb** - Decision tree classifier
12. **12_kmeans.ipynb** - Unsupervised clustering

### API & Web Automation
13. **13_fastapi.ipynb** - Build REST API with FastAPI
14. **14_scraping.ipynb** - Web scraping with BeautifulSoup/Requests
15. **15_selenium.ipynb** - Browser automation basics
(login, form filling, multi-page scraping)

## Requirements

### Python Libraries
```
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
requests
beautifulsoup4
selenium
webdriver-manager
fastapi
uvicorn
```

### Installation

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn plotly requests beautifulsoup4 selenium webdriver-manager fastapi uvicorn
```

## Usage

### Running Notebooks
```bash
jupyter notebook
```
Then open any `.ipynb` file to explore the analysis.

### Running the FastAPI Application
```bash
python app.py
```
or
```bash
uvicorn app:app --reload
```

Access the API at `http://localhost:8000`

### Selenium Automation
Run the selenium automation notebook to:
- Automate login on practice websites
- Extract quotes and book data
- Navigate multiple pages
- Take screenshots
- Save scraped data to CSV

## Dataset

**loan_data.csv** - Loan application dataset containing:
- Applicant demographics
- Loan details
- Credit information
- Approval status

## Key Learnings

- **Data Cleaning**: Handling missing values and duplicates
- **Feature Engineering**: Creating meaningful features from raw data
- **Encoding**: Converting categorical to numerical data
- **Scaling**: Normalizing features for machine learning
- **Model Selection**: Comparing different algorithms
- **Web Scraping**: Extracting data from websites
- **API Development**: Building REST APIs with FastAPI
- **Automation**: Browser automation with Selenium

## Results

The project demonstrates:
- Complete data preprocessing pipeline
- Multiple machine learning approaches
- Model evaluation and comparison
- Data extraction from web sources
- REST API implementation

## Notes

- All notebooks are designed to be run sequentially
- Ensure all dependencies are installed before running
- Selenium requires ChromeDriver (automatically handled by webdriver-manager)
- Some notebooks may take time depending on data size and model complexity

## Author

Assignment Project | April 2026

## License

MIT License
