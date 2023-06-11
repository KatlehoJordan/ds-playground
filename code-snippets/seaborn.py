import plotly.express as px
import seaborn as sns

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a scatter plot using Seaborn
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", style="time")

# Convert the Seaborn plot to Plotly
fig = px.scatter(tips, x="total_bill", y="tip", color="sex", symbol="time")

# Display the interactive Plotly plot
fig.show()
