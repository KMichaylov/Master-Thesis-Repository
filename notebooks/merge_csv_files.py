import os
import pandas as pd

# Function for merging multiple csv files into one, solely "Changes" and "General Category" are considered.
def merge_files(file_names, csv_destination_file_name):
    dfs = []
    path = "../resources/datasets"
    file_path = os.path.join(path, csv_destination_file_name)

    if not os.path.exists(path):
        os.makedirs(path)

    for file in file_names:
        pt = os.path.join(path, file)
        try:
            df = pd.read_csv(pt, sep=',', skip_blank_lines=True)
        except pd.errors.ParserError:
            df = pd.read_csv(pt, sep=';', skip_blank_lines=True)

        df.columns = df.columns.str.strip()

        dfs.append(df[["Changes", "General Category"]])

    if dfs:
        final_df = pd.concat(dfs, axis=0, ignore_index=True)

        final_df.to_csv(file_path, index=False, encoding="utf-8")
        print(final_df.head())


if __name__ == '__main__':
    all_file_names = ["Apache Commons IO.csv", "Apache Commons Lang and Commons Lang.csv", "Appcompat.csv", "JUnit.csv",
                      "Log4J.csv", "Project Lombok.csv"]
    subset_file_names = ["Apache Commons IO.csv", "JUnit.csv",
                         "Log4J.csv", "Project Lombok.csv"]
    merge_files(all_file_names, "Combined_csv_files.csv")
    merge_files(subset_file_names, "Subset_of_files.csv")