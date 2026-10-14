
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
project = Path(__file__).resolve().parent.parent
data_file = project / "03_Python" / "rfm_customer_segments.csv"
output_folder = project / "07_Screenshots"

output_folder.mkdir(exist_ok=True)

# Load customer segments
rfm = pd.read_csv(data_file)

# Count customers by segment
segment_counts = rfm["CustomerSegment"].value_counts()

# Create customer segmentation chart
plt.figure(figsize=(10, 6))

bars = plt.bar(
    segment_counts.index,
    segment_counts.values
)

plt.title("RFM Customer Segmentation Analysis")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")

plt.xticks(rotation=15)

# Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart
chart_path = output_folder / "rfm_segmentation.png"
plt.savefig(chart_path, dpi=300)
plt.show()

print("\nRFM visualization created successfully!")
print("Chart saved to:", chart_path)

print("\nCUSTOMER SEGMENT DISTRIBUTION")
print(segment_counts)
