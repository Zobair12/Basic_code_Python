import pandas as pd
import plotly.express as px 

data = {
    "Category": ["USA", "Canada", "China", "India", "Germany", "Japan"],
    "GDP (Trillion $)": [12.4, 1.6, 14.3, 2.9, 3.8, 5.1]
}
df = pd.DataFrame(data)

fig = px.bar(df, 
             x="Category", 
             y="GDP (Trillion $)",
             title=" Top Countries by GDP",
             color="GDP (Trillion $)")

fig.show()