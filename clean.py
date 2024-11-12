import pandas as pd
import plotly.express as px

df = pd.read_csv("Garmin_clean7.csv")

fig = px.line(df, x='Distance', y='Avg.Pace', title='Marathon Training Progress')
fig.show()
