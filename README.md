# Amsterdam Airbnb Explorer

An interactive Streamlit dashboard for exploring Airbnb listings in Amsterdam by nightly price and distance from a selected point of interest.

The project turns an Airbnb listings dataset into a simple visual decision tool: choose a maximum nightly budget, inspect matching listings, and explore their locations on an interactive map.

> **Note:** This is an educational data-visualization project and is not affiliated with or endorsed by Airbnb.

## Features

- Interactive nightly-budget filter
- Summary metrics for matching listings
- Searchable and sortable listing table
- Interactive map of Airbnb listings and the selected point of interest
- Distance information for each listing
- Lightweight Streamlit interface that runs locally

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly

## Project Structure

```text
airbnb-project/
├── streamlit_app.py
├── WK1_Airbnb_Amsterdam_listings_proj_solution.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Dataset

The included CSV contains six fields used by the application:

| Column | Description |
| --- | --- |
| Airbnb Listing ID | Identifier of the listing |
| Price | Nightly price |
| Latitude | Listing latitude |
| Longitude | Listing longitude |
| Meters from chosen location | Distance from the selected point of interest |
| Location | Distinguishes listings from the selected point of interest |

The first row represents the selected point of interest, while the remaining rows represent Airbnb listings.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/HoosseinRahimi/airbnb-project.git
cd airbnb-project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run streamlit_app.py
```

Streamlit will print the local URL in the terminal, normally `http://localhost:8501`.

## How It Works

1. The CSV dataset is loaded with Pandas.
2. The selected point of interest is separated from the Airbnb listings.
3. The sidebar lets the user set a maximum nightly budget.
4. Listings above the selected budget are filtered out.
5. Streamlit displays summary statistics and the filtered table.
6. Plotly renders the matching listings and point of interest on an interactive map.

## Possible Improvements

- Add neighbourhood and room-type filters
- Add rating and review information
- Fetch newer listing data from a maintained source
- Add automated tests for the data-loading and filtering logic
- Deploy the dashboard publicly with Streamlit Community Cloud

## License

This repository includes a license file. See [LICENSE](LICENSE) for details.
