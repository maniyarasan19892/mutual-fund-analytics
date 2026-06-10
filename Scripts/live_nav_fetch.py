import pandas as pd
import requests
from pathlib import Path

schemes = {
    125497: "HDFC_Top_100",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

output_path = Path("data/raw")

for scheme_code, scheme_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = output_path / f"{scheme_name}_live_nav.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    else:
        print(f"Failed: {scheme_name}")