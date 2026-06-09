# COVID-19 Analysis and Visualization using Plotly Express

This project is inspired by the [GeeksforGeeks tutorial](https://www.geeksforgeeks.org/data-visualization/covid-19-analysis-and-visualization-using-plotly-express/) on COVID-19 data visualization.

## Project Structure
- `data/`: Contains the datasets.
    - `covid.csv`: Country-aggregated data.
    - `covid_grouped.csv`: Time-series combined data.
    - `coviddeath.csv`: Detailed global data from Our World in Data.
- `analysis.py`: Python script using Plotly Express for visualizations.
- `requirements.txt`: Python dependencies.
- `images/`: Folder where generated visualizations are saved.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the analysis:
   ```bash
   python analysis.py
   ```

## Visualizations Included
- Top 15 Countries by Confirmed Cases (Bar Chart).
- Confirmed vs Deaths Bubble Chart.
- US Confirmed Cases Over Time (Line Plot).
- Global Confirmed Cases Choropleth Map.
- Word Cloud of locations in the dataset.
