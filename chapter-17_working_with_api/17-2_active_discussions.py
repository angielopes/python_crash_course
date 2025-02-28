"""Using the data from hn_submissions.py, make a bar chart showing the most
active discussions currently happening on Hacker News.
- The height of each bar should correspond to the number of comments each submission has.
- The label for each bar should include the submission's title and act
as a link to the discussion page for that submission.
- If you get a KeyError when creating a chart, use a try-except block 
o skip over the promotional posts."""

import requests
import plotly.express as px
from operator import itemgetter

# API call to get the IDs of the top stories.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# "Checks if the API call was successful.
if r.status_code != 200:
    raise Exception(f"Error accessing the API. Status code: {r.status_code}")
else:
    print(f"Status code: {r.status_code}")

# Processes the information of each submission.
submission_ids = r.json()
submission_links, comments, hover_texts = [], [], []

# Iterates over the submission IDs.
for submission_id in submission_ids[:10]:
    # Makes a new API call to get the details of each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Checks if the submission is of type 'story' and has the required fields.
    if (
        response_dict.get("type") == "story"
        and "title" in response_dict
        and "descendants" in response_dict
    ):
        try:
            # Extracts the relevant data.
            title = response_dict["title"]
            hn_link = f"https://news.ycombinator.com/item?id={submission_id}"
            num_comments = response_dict["descendants"]
            author = response_dict.get("by")

            # Creates a clickable link for the submission.
            submission_link = f"<a href='{hn_link}'>{title}</a>"
            submission_links.append(submission_link)

            # Adiciona o número de comentários
            comments.append(num_comments)

            # Cria o texto de hover
            hover_text = f"Author: {author}<br>Comments: {num_comments}"
            hover_texts.append(hover_text)
        except KeyError as ke:
            print(f"Error processing the submission {submission_id}: {ke}")

# Verifica se há dados suficientes para criar o gráfico
if not submission_links:
    raise Exception("No valid submissions found.")

# Cria o gráfico de barras
title = "The most active discussions currently happening on Hacker News"
labels = {"x": "Submission's title", "y": "Number of comments"}
fig = px.bar(
    x=submission_links, y=comments, title=title, labels=labels, hover_name=hover_texts
)
fig.update_traces(marker_color="lightblue")
fig.update_layout(
    xaxis_title="Submission", yaxis_title="Number os comments", showlegend=False
)
fig.show()
