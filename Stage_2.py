import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset (handling potential errors)
try:
    data = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv", sep='\t') #load the tsv file, and specify the seperator.
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Function to determine the time to reach 80% of the maximum growth (carrying capacity)
def time_to_carrying_capacity(growth_curve, time_points):
    if not growth_curve or not time_points:
        return None
    max_growth = max(growth_curve)
    target_growth = 0.8 * max_growth
    for i, growth in enumerate(growth_curve):
        if growth >= target_growth:
            return time_points[i]
    return None

# Unique strains
strains = data['Strain'].unique()

# Store the time to carrying capacity for each strain/mutant
carrying_capacity_times = []

# Loop through each strain
for strain in strains:
    strain_data = data[data['Strain'] == strain]
    knock_out_data = strain_data[strain_data['Mutant'] == '-']
    knock_in_data = strain_data[strain_data['Mutant'] == '+']
    time_points = knock_out_data['Time'].values.tolist()
    knock_out_od600 = knock_out_data['OD600'].values.tolist()
    knock_in_od600 = knock_in_data['OD600'].values.tolist()

    plt.figure()
    plt.plot(time_points, knock_out_od600, label=f"{strain} Knock-out (-)")
    plt.plot(time_points, knock_in_od600, label=f"{strain} Knock-in (+)")
    plt.xlabel("Time")
    plt.ylabel("OD600")
    plt.title(f"Growth Curves for {strain}")
    plt.legend()
    plt.show()

    knock_out_time = time_to_carrying_capacity(knock_out_od600, time_points)
    knock_in_time = time_to_carrying_capacity(knock_in_od600, time_points)

    carrying_capacity_times.append({'Strain': strain, 'Mutant': '-', 'Time_to_Carrying_Capacity': knock_out_time})
    carrying_capacity_times.append({'Strain': strain, 'Mutant': '+', 'Time_to_Carrying_Capacity': knock_in_time})

carrying_capacity_df = pd.DataFrame(carrying_capacity_times)
carrying_capacity_df = carrying_capacity_df.dropna(subset=['Time_to_Carrying_Capacity'])#remove none values

plt.figure()
sns.scatterplot(data=carrying_capacity_df, x='Mutant', y='Time_to_Carrying_Capacity', hue='Strain')
plt.xlabel("Mutant")
plt.ylabel("Time to Carrying Capacity")
plt.title("Scatter Plot of Time to Carrying Capacity")
plt.show()

plt.figure()
sns.boxplot(data=carrying_capacity_df, x='Mutant', y='Time_to_Carrying_Capacity')
plt.xlabel("Mutant")
plt.ylabel("Time to Carrying Capacity")
plt.title("Box Plot of Time to Carrying Capacity")
plt.show()

knock_out_times = carrying_capacity_df[carrying_capacity_df['Mutant'] == '-']['Time_to_Carrying_Capacity']
knock_in_times = carrying_capacity_df[carrying_capacity_df['Mutant'] == '+']['Time_to_Carrying_Capacity']

t_stat, p_value = stats.ttest_ind(knock_out_times, knock_in_times)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
