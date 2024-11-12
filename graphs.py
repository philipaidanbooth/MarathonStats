import csv
import plotly.graph_objects as go

# Read the CSV file
x = []
y = []
with open('Activities (1).csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        x.append(row['date'])
        y.append(float(row['distance']))

# Create a scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Distance'))

# Customize the graph
fig.update_layout(title='Running Distance Over Time', xaxis_title='Date', yaxis_title='Distance (mi)')

# Show the graph
fig.show()