# CSV Data Analytics

A simple Python project to load, clean, and analyze CSV files using Pandas, Matplotlib, and Seaborn.  
An example dataset (`sales_data.csv`) demonstrates a full workflow: data cleaning, aggregation, summary statistics, and plotting.

## Features
- Load any CSV file (with date parsing)
- Clean data: remove duplicates, drop missing/invalid entries
- Compute derived metrics (e.g. `total = quantity × price`)
- Print row counts and descriptive statistics
- Aggregate sales by date and by customer
- Generate charts:
  - Line plot of total sales over time
  - Bar plot of top 10 products by sales

## Prerequisites
- Python 3.7+
- (Optional) Virtual environment tool (`venv`, `virtualenv`)

## Installation

```bash
# Clone the repo
git clone <repo-url>
cd cursor_data_analytics

# Create & activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install pandas matplotlib seaborn
```

*Tip:* You can freeze exact versions with:
```bash
pip freeze > requirements.txt
```

## Usage

```bash
# Analyze the built-in sales_data.csv:
python analyze.py

# Or point to your own CSV file:
python analyze.py path/to/your_file.csv
```

- If no path is provided, the script defaults to `sales_data.csv` in its directory.
- Output includes:
  - Rows before & after cleaning
  - Descriptive stats for `quantity`, `price`, and `total`
  - Aggregated sales by date and top customers
  - Inline display of two charts

## Project Structure

```
cursor_data_analytics/
├── analyze.py # Main analysis script
├── sales_data.csv # Sample data (replaceable)
├── README.md # This guide
└── venv/ # Virtual environment (after setup)
```


## Extending This Project
- Add new cleaning or validation rules in `analyze.py`
- Build out additional plots (e.g., histograms, scatter plots)
- Incorporate CLI flags (argparse) for fine-grained control
- Write unit tests under a `tests/` directory
- Export reports to CSV/JSON/Excel or integrate with dashboards

## License
This project is open-source and available under the MIT License.  