import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Define age distribution data for Asia, Europe, and Africa
age_distribution = {
    "Asia": [20, 15, 15, 14, 12, 10],
    "Europe": [10, 10, 12, 13, 15, 20],
    "Africa": [25, 20, 18, 15, 12, 10]
}

# Regions and age ranges
regions = list(age_distribution.keys())
age_ranges = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60']

# Set up bar positions
x = np.arange(len(age_ranges))
width = 0.25  # width of bars

# Create a grouped bar chart
plt.figure(figsize=(12, 6))
for i, region in enumerate(regions):
    plt.bar(x + i * width, age_distribution[region], width, label=region)

# Labeling
plt.xlabel('Age Ranges')
plt.ylabel('Percentage of Population')
plt.title('Age Distribution by Region (Approximate)')
plt.xticks(x + width, age_ranges)
plt.legend(title="Regions")

plt.show()


