import pandas as pd
from datetime import datetime

def create_sample_dataset():
    data = {
        "date": [
            "2026-06-01",
            "2026-06-02",
            "2026-06-03",
            "2026-06-04",
            "2026-06-05"
        ],
        "close_price": [2650, 2675, 2640, 2690, 2715],
        "volume": [120000, 135000, 110000, 150000, 165000]
    }

    df = pd.DataFrame(data)

    output_path = "data/raw/nepse_sample.csv"

    df.to_csv(output_path, index=False)

    print(f"Dataset saved to {output_path}")
    print(df)

if __name__ == "__main__":
    create_sample_dataset()