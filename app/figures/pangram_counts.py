import pandas as pd

colors = {
    "background" : "white",
    "plot_background" : "#bfc9ea",
    "font" : "black"
}

pangram_counts_df = pd.read_csv("data/example_data", header=None, sep=";")

pangram_counts_df = pangram_counts_df.rename(columns={0 : "Date", 1 : "Counts"})

pangram_counts_barplot = {
    "data" : [
        {"x" : pangram_counts_df["Date"], "y" : pangram_counts_df["Counts"], "type" : "bar", "name" : "Pangrams"},
    ],
    "layout" : {
        "plot_bgcolor" : colors["plot_background"],
        "paper_bgcolor" : colors["background"],
        "font" : {
            "color" : colors["font"]
        }
    }
}