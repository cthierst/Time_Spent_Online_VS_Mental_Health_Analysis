# Purpose: The purpose of this code is to create the graphical visualizations for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024 

# Imports all of the necessary libraries
import pandas as pd
import plotly.express as px

# Imports the data clean and filtered data frame
df = pd.read_csv("filtered_clean_df.csv", low_memory=False)

## DEMOGRAPHICS ##

# Uses plotly to create a bar plot showing time spent using the internet vs. visible minority with facets for gender
fig = px.bar(df, x="Time spent using the internet", color= "Visible Minority", facet_col="Gender")

# Adjusts the layout of the graphs
fig.update_layout(
    font=dict(size=9), # Sets the font size faceted columns to prevent overlap
    margin=dict(t=50),  # Adjusts the top margin to help prevent overlap
)

# Renames the faceted columns for better readability
for i, label in enumerate(['Male', 'Female']):
    fig.layout.annotations[i]['text'] = label

fig.show() # Displays the graph in a separate interactive window

## PERCEIVED MENTAL HEALTH VS. TIME SPENT VS. LIFE SATISFACTION ##

# Uses plotly to create a bar plot showing time spent using the internet vs. life satisfaction with facets for perceived mental health
fig = px.bar(df, x="Time spent using the internet", color= "Life Satisfaction", facet_col="Perceived Mental Health")

# Adjusts the layout of the graphs
fig.update_layout(
    font=dict(size=9),  # Sets the font size faceted columns to prevent overlap
    margin=dict(t=50),  # Adjusts the top margin to help prevent overlap
)

# Renames the faceted columns for better readability
for i, label in enumerate(['Good', 'Very Good', 'Fair', 'Excellent', 'Poor']):
    fig.layout.annotations[i]['text'] = label

fig.show() # Displays the graph in a separate interactive window

## PERCEIVED MENTAL HEALTH VS. TIME SPENT VS. RELATIONSHIP SATISFACTION ##

# Uses plotly to create a bar plot showing time spent using the internet vs. relationship satisfaction with friends and relationship satisfaction with relatives 
fig = px.bar(df, 
             x="Time spent using the internet", 
             color="Relationship Sat: Friends", 
             facet_col="Relationship Sat: Relatives or family not living with")

# Adjusts the layout of the graphs
fig.update_layout(
    font=dict(size=9),  # Sets the font size faceted columns to prevent overlap
    margin=dict(t=50),  # Adjusts the top margin to help prevent overlap
    legend_title='Relationship Satisfaction: Friends', # Renames the legend for better readability
)

# Renames the faceted columns for better readability
for i, label in enumerate(['Completely satisfied', 'Somewhat satisfied', 'Neither satisfied nor dissatisfied', 'Completely dissatisfied', 'Somewhat dissatisfied']):
    fig.layout.annotations[i]['text'] = label

fig.show() # Displays the graph in a separate interactive window