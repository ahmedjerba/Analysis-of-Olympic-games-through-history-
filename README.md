🏅 Olympic Games Data Analysis (1896 - 2016)
📌 Project Overview
This project performs an in-depth Exploratory Data Analysis (EDA) on the modern Olympic Games dataset. By merging athlete performance records with regional data, the analysis uncovers historical trends in gender participation, physical attributes of athletes across different sports, and country-specific dominance.

🛠️ Technical Stack
Language: Python

Data Manipulation: Pandas, NumPy

Visualization: Seaborn, Matplotlib

🔍 Key Analysis Features
The Python script provides a modular approach to data exploration:

Medalist Demographics: * Distribution of gold medalist ages.

Identification of "Elder Athletes" (50+) and the sports where they excel.

Gender Evolution: * Tracking the rise of female participation in the Summer Olympics.

Calculating the ratio of female to male participants over time.

Global Performance: * Top 10 countries by total medal count.

Gender-stratified medal rankings for top-performing nations.

Physical Attribute Correlation: * BMI Outlier Detection: Filtering physical outliers using Interquartile Range (IQR) to find the "true" correlation between Height and Weight.

Gymnastics Deep-Dive: Tracking how the physical profiles (Height/Weight) of gymnasts have changed over decades.

National Insight (Tunisia): * Specific analysis of Tunisian athletes’ age distributions and historical medal success ratios.

📈 Data Insights Examples
Data Cleaning: Imputed missing physical traits (Height/Weight) using the median values specific to each Olympic event to maintain data integrity.

USA Dominance: Specific logic to calculate the Gold Medal ratio for iconic teams, such as USA Men's Basketball.

Physical Trends: Statistical boxplots showing the variation of traits in specialized sports like Gymnastics.

🚀 How to Use
Datasets: Ensure you have athlete_events.csv and noc_regions.csv in your project directory.

Install Dependencies:

Bash
pip install pandas numpy seaborn matplotlib
Run the Analysis:

Bash
python olympic_analysis.py
