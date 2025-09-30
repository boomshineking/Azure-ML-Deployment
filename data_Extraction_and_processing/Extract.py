"""
Renewed climate data scraper
"""

import os
import time
import requests
from pathlib import Path


def retrieve_html(start_year=2013, end_year=2018, station="421820"):
    base_url = "http://en.tutiempo.net/climate/{month:02d}-{year}/ws-{station}.html"

    for year in range(start_year, end_year + 1):
        year_dir = Path(f"Data/Html_Data/{year}")
        year_dir.mkdir(parents=True, exist_ok=True)

        for month in range(1, 13):
            url = base_url.format(year=year, month=month, station=station)
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f" Failed to fetch {url}: {e}")
                continue

            file_path = year_dir / f"{month:02d}.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f" Saved {file_path}")


if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    elapsed = time.time() - start_time
    print(f"\n⏱ Time taken: {elapsed:.2f} seconds")
