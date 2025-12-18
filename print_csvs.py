#!/usr/bin/env python3

import argparse
from pathlib import Path
import pandas as pd

def print_csvs(directory, head):
    directory = Path(directory)

    if not directory.exists():
        print(f"❌ Directory not found: {directory}")
        return

    csv_files = sorted(directory.glob("*.csv"))

    if not csv_files:
        print(f"⚠️ No CSV files found in {directory}")
        return

    for csv_file in csv_files:
        print("\n" + "=" * 80)
        print(f"📄 FILE: {csv_file.name}")
        print("=" * 80)

        try:
            df = pd.read_csv(csv_file)

            if head:
                print(df.head(head))
                print(f"\n... showing first {head} rows "
                      f"(total rows: {len(df)})")
            else:
                print(df)

        except Exception as e:
            print(f"❌ Failed to read {csv_file.name}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Print all CSV files in a directory"
    )
    parser.add_argument(
        "directory",
        help="Directory containing CSV files"
    )
    parser.add_argument(
        "--head",
        type=int,
        default=0,
        help="Print only first N rows of each CSV"
    )

    args = parser.parse_args()
    print_csvs(args.directory, args.head)

if __name__ == "__main__":
    main()
