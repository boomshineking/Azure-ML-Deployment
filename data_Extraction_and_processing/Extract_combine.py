import os
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

from Plot_AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016


def met_data(month, year):
    """Extract monthly meteorological data from saved HTML."""
    file_path = Path(f"Data/Html_Data/{year}/{month:02d}.html")
    if not file_path.exists():
        print(f"Missing file: {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    table = soup.find("table", {"class": "medias mensuales numspan"})
    if not table:
        print(f" No table found for {month}-{year}")
        return []

    df = pd.read_html(str(table))[0]

    # Print original columns for debugging
    print(f"Original columns for {month:02d}-{year}: {list(df.columns)}")

    # Drop unnecessary columns safely
    drop_cols = ["Day", "Insolation", "WindGust", "Snowfall", "Precip", "Rain", "Thunderstorm"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")

    # Clean missing values
    df = df.replace(["-", ""], pd.NA).dropna()

    return df.values.tolist()


def data_combine(year, chunk_size=600):
    """Read CSV in chunks and return as list of lists."""
    csv_path = Path(f"Data/Real-Data/real_{year}.csv")
    all_rows = []
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
        all_rows.extend(chunk.values.tolist())
    return all_rows


if __name__ == "__main__":
    Path("Data/Real-Data").mkdir(parents=True, exist_ok=True)

    for year, pm_func in zip(
        range(2013, 2017), 
        [avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016]
    ):
        all_data = []
        for month in range(1, 13):
            all_data.extend(met_data(month, year))

        # Remove summary rows
        all_data = [row for row in all_data if row and row[0] != 'Monthly means and totals:']

        pm = pm_func()
        if len(pm) == 364:  # adjust leap year issue
            pm.insert(364, "-")

        # insert PM2.5 values
        for i, row in enumerate(all_data):
            if i < len(pm):
                row.append(pm[i])

        # Debug: print the length and content of the first row to check columns
        if all_data:
            print(f"Year {year} sample row length: {len(all_data[0])}")
            print(f"Year {year} sample row: {all_data[0]}")

        # Save yearly data (columns list may need to be updated after inspecting output)
        df_year = pd.DataFrame(all_data, columns=['Day', 'T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG', 'PM 2.5'])
        df_year.to_csv(f"Data/Real-Data/real_{year}.csv", index=False)

    # Combine all years
    dfs = [pd.read_csv(f"Data/Real-Data/real_{y}.csv") for y in range(2013, 2017)]
    df_all = pd.concat(dfs, ignore_index=True)
    df_all.to_csv("Data/Real-Data/Real_Combine.csv", index=False)

    print("Data combined and saved to Data/Real-Data/Real_Combine.csv")
