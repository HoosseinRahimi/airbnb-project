# Amsterdam Airbnb Explorer

[![App smoke test](https://github.com/HoosseinRahimi/airbnb-project/actions/workflows/app-smoke-test.yml/badge.svg)](https://github.com/HoosseinRahimi/airbnb-project/actions/workflows/app-smoke-test.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://amsterdam-airbnb-explorer.streamlit.app/)

**Live demo:** https://amsterdam-airbnb-explorer.streamlit.app/

An interactive Streamlit dashboard for exploring Airbnb listings in Amsterdam by nightly price and distance from a selected point of interest.

The project turns an Airbnb listings dataset into a simple visual decision tool: choose a maximum nightly budget, inspect matching listings, and explore their locations on an interactive map.

> **Note:** This is an educational data-visualization project and is not affiliated with or endorsed by Airbnb.

## Features

- Interactive nightly-budget filter
- Summary metrics for matching listings
- Searchable and sortable listing table
- Interactive MapLibre-based map of Airbnb listings and the selected point of interest
- Distance information for each listing
- Cached dataset loading
- Automated Streamlit boot/health smoke test in GitHub Actions
- Public Streamlit Community Cloud deployment

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly / MapLibre
- GitHub Actions

## Project Structure

```text
airbnb-project/
├── .github/
│   └── workflows/
│       └── app-smoke-test.yml
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

## Deployment

The app is deployed on Streamlit Community Cloud:

**https://amsterdam-airbnb-explorer.streamlit.app/**

The repository is organized for direct deployment: the Streamlit entrypoint, dependency file, and local CSV data are committed in the repository root.

## How It Works

1. The CSV dataset is loaded with Pandas using a path resolved relative to `streamlit_app.py`.
2. The selected point of interest is separated from the Airbnb listings.
3. The sidebar lets the user set a maximum nightly budget.
4. Listings above the selected budget are filtered out.
5. Streamlit displays summary statistics and the filtered table.
6. Plotly renders the matching listings and point of interest using its MapLibre-based map trace.

## Continuous Verification

On every push and pull request to `main`, GitHub Actions:

1. installs the dependencies from `requirements.txt`,
2. starts the Streamlit app in headless mode,
3. polls Streamlit's health endpoint,
4. fails the workflow if the app does not start successfully.

## Possible Improvements

- Add neighbourhood and room-type filters
- Add rating and review information
- Fetch newer listing data from a maintained source
- Separate data transformation from UI code and add unit tests around filtering logic

## License

This repository includes a license file. See [LICENSE](LICENSE) for details.
