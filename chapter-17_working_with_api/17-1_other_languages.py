"""Modify the API call in python_repos.py so it generates a chart showing
the most popular projects in other languages. Try languages such as
JavaScript, Ruby, C, Java, Perl, Haskell, and Go."""

import requests
import plotly.express as px

# API call
url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overal results.
response_dicts = r.json()
print(f"Complete results: {not response_dicts['incomplete_results']}")

# Process repository information.
repo_dicts = response_dicts["items"]
repo_links, stars, hover_texts = [], [], []
for repo in repo_dicts:
    # Turn repo names into actives links.
    repo_name = repo["name"]
    repo_url = repo["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>'"
    repo_links.append(repo_link)

    stars.append(repo["stargazers_count"])

    # Build hover text.
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Visualization.
title = "Most-Starred Java Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Styiling visualization.
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
fig.update_traces(marker_color="DarkSlateGrey", marker_opacity=0.8)

fig.show()
