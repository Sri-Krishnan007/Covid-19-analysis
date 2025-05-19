# COVID-19 Data Analysis

A Streamlit web application for interactive analysis and visualization of COVID-19 data in India, supporting raw data exploration, basic statistics, time series analysis, geographical visualization, state/UT-wise analysis, and comparisons.

## Features

- **Raw Data View**: Explore the raw COVID-19 dataset.
- **Basic Statistics**: Analyze the data by date range or by state/UT, including descriptive statistics and percentage calculations (deaths and recoveries).
- **Time Series Analysis**: Visualize the progression of confirmed cases, deaths, and recoveries over time.
- **Geographical Visualization**: Interactive map showing confirmed cases geographically (requires latitude and longitude data).
- **State/UT-wise Analysis**: Detailed breakdown by individual state or union territory.
- **State/UT Comparison**: Compare confirmed cases between multiple states/UTs over time.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sri-Krishnan007/Covid-19-analysis.git
   cd Covid-19-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pandas matplotlib plotly
   ```

3. **Prepare the data:**
   - Place your `covid.csv` file in a location accessible to your script.
   - Update the file path in your code if needed. The current code expects the file at:
     ```
     C:\Users\srikr\Desktop\COLLEGE\Extra\Projects\covid.csv
     ```
   - For portability, you may want to move the CSV into the project folder and update the path:
     ```python
     data = pd.read_csv('covid.csv')
     ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run <your_script_name>.py
   ```
   Replace `<your_script_name>.py` with the filename containing your Streamlit code.

2. **Navigate the app:**
   - Use the sidebar to select different analysis pages.
   - Filter and explore the data interactively.

## Notes

- The CSV file should contain at least the following columns:
  - `Date`
  - `Name of State / UT`
  - `Total Confirmed cases`
  - `Death`
  - `Cured/Discharged/Migrated`
  - `Latitude` and `Longitude` (for geographical visualization)
- If you encounter issues with data types, ensure columns are formatted correctly in the CSV.


## License

This project is licensed under the MIT License.

---

*Created by [Sri-Krishnan007](https://github.com/Sri-Krishnan007)*
