import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set(style="whitegrid")
plt.rcParams["figure.dpi"] = 150  # Better resolution for all plots

# -------------------------------
# LOAD DATA
# -------------------------------
def load_data():
    df = pd.read_csv("athlete_events.csv")
    df_countries = pd.read_csv("noc_regions.csv")
    return df, df_countries

# -------------------------------
# MERGE AND CLEAN
# -------------------------------
def preprocess_data(df, df_countries):
    total = df.merge(df_countries, on="NOC", how="left")
    return total

# -------------------------------
# PLOT HELPERS
# -------------------------------
def plot_countplot(data, x, title, rotation=45, hue=None, figsize=(20, 6)):
    plt.figure(figsize=figsize)
    sns.countplot(data=data, x=x, hue=hue)
    plt.title(title)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()

def plot_barplot(data, x, y, title="", xlabel="", ylabel="", rotation=45, figsize=(20, 6)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()

# -------------------------------
# ANALYSIS FUNCTIONS
# -------------------------------

def analyze_gold_medal_age(total):
    gold = total[(total["Medal"] == "Gold") & (np.isfinite(total["Age"]))]
    plot_countplot(gold, "Age", "Distribution of Gold Medalists' Ages", rotation=90, figsize=(20, 8))
    
    print("Mean Age:", gold["Age"].mean())
    print("Median Age:", gold["Age"].median())

    # Elder athletes
    aged = gold[gold["Age"] > 50]
    print("Number of gold medalists over 50:", len(aged))
    plot_countplot(aged, "Sport", "Sports with Older Gold Medalists", rotation=90, figsize=(20, 8))

def analyze_gender_evolution(total):
    women = total[(total["Sex"] == "F") & (total["Season"] == "Summer")]
    plot_countplot(women, "Year", "Women Participation Over Time", rotation=90, figsize=(20, 8))
    
    total_women = total[total["Sex"] == "F"].groupby("Year")["Sex"].count()
    total_participants = total.groupby("Year")["Sex"].count()
    ratio = (total_women / total_participants * 100).reset_index(name="Women_Participation_Ratio")

    sns.lineplot(data=ratio, x="Year", y="Women_Participation_Ratio")
    plt.title("Female Participation Ratio Over Time")
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.show()

def analyze_medals_by_country(total):
    medals = total[total["Medal"].isin(["Gold", "Silver", "Bronze"])]
    top_countries = medals["region"].value_counts().head(10).reset_index()
    top_countries.columns = ["Country", "Total_Medals"]
    plot_barplot(top_countries, "Country", "Total_Medals", title="Top 10 Countries by Total Medals")

    # Gender-wise
    by_gender = medals.groupby(["region", "Sex"]).size().reset_index(name="Medals")
    top_male = by_gender[by_gender["Sex"] == "M"].sort_values("Medals", ascending=False).head(10)
    top_female = by_gender[by_gender["Sex"] == "F"].sort_values("Medals", ascending=False).head(10)

    plot_barplot(top_male, "region", "Medals", title="Top 10 Countries by Male Medals")
    plot_barplot(top_female, "region", "Medals", title="Top 10 Countries by Female Medals")

def analyze_us_discipline_dominance(total):
    medals = total[total["Medal"].isin(["Gold", "Silver", "Bronze"])]
    usa = medals[medals["NOC"] == "USA"]
    top_discipline = usa["Event"].value_counts().head(1)
    print("Most Awarded Discipline for USA:", top_discipline)

    basketball_usa = usa[(usa["Sport"] == "Basketball") & (usa["Sex"] == "M")].drop_duplicates(subset=["Year"])
    gold_ratio = (basketball_usa["Medal"] == "Gold").sum() / len(basketball_usa)
    print("USA Men's Basketball Gold Medal Ratio:", round(gold_ratio, 2))

def analyze_height_weight_correlation(total):
    medals = total[total["Medal"].notna()].copy()

    # Fill missing Height/Weight
    for feature in ["Height", "Weight"]:
        median_per_event = medals.groupby("Event")[feature].median()
        medals[feature] = medals.apply(
            lambda row: median_per_event[row["Event"]] if pd.isna(row[feature]) else row[feature], axis=1
        )

    sns.scatterplot(data=medals, x="Weight", y="Height")
    plt.title("Height vs Weight (Medalists)")
    plt.tight_layout()
    plt.show()

    corr = medals["Height"].corr(medals["Weight"])
    print("Correlation (all):", corr)

    # Outlier Detection using BMI
    medals["BMI"] = medals["Weight"] / ((medals["Height"] / 100) ** 2)
    q1, q3 = medals["BMI"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = medals[(medals["BMI"] < lower) | (medals["BMI"] > upper)]

    print("Outliers based on BMI:", len(outliers))

    # Scatterplot without outliers
    clean_medals = medals[~medals.index.isin(outliers.index)]
    sns.scatterplot(data=clean_medals, x="Weight", y="Height")
    plt.title("Height vs Weight (No Outliers)")
    plt.tight_layout()
    plt.show()

    print("Correlation (no outliers):", clean_medals["Height"].corr(clean_medals["Weight"]))

def analyze_tunisian_athletes(total):
    tunisian = total[total["region"] == "Tunisia"]
    medals_tun = tunisian[tunisian["Medal"].notna()]
    print("Tunisian Athletes with Medals:\n", medals_tun)

    sns.boxplot(data=tunisian, y="Age", x="Year")
    plt.title("Age Distribution of Tunisian Athletes Over Time")
    plt.tight_layout()
    plt.show()

    print("Tunisian Medal Ratio:", len(medals_tun) / len(tunisian))

def analyze_gymnastics_physical_traits(total):
    gym = total[total["Sport"] == "Gymnastics"]
    for feature in ["Height", "Weight"]:
        plt.figure(figsize=(20, 8))
        sns.boxplot(data=gym, x="Year", y=feature, hue="Sex", palette="Set2")
        plt.title(f"{feature} Variation Over Time (Gymnastics)")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

# -------------------------------
# MAIN EXECUTION
# -------------------------------
def main():
    df, df_countries = load_data()
    total = preprocess_data(df, df_countries)

    analyze_gold_medal_age(total)
    analyze_gender_evolution(total)
    analyze_medals_by_country(total)
    analyze_us_discipline_dominance(total)
    analyze_height_weight_correlation(total)
    analyze_tunisian_athletes(total)
    analyze_gymnastics_physical_traits(total)

if __name__ == "__main__":
    main()