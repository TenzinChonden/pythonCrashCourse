from pathlib import Path
import pandas as pd
import plotly.express as px
import json

file_path = Path('hn_data/hn_discussions.json')

if not file_path.exists():
    raise FileNotFoundError(
        f"Could not find {file_path}. Run hn_submissions.py first!"
    )

with open(file_path, 'r', encoding='utf-8') as f:
    submission_dicts = json.load(f)

hover_texts, discussion_links, comments = [], [], []
for submission_dict in submission_dicts:
    try:
        title = submission_dict['title']
        link = submission_dict['hn_link']
        comment_count = submission_dict['comments']
    except KeyError:
        continue
    else:
         # Create a clickable html anchor tag for x-axis label
         discussion_link = f"<a href='{link}'>{title[:30]}...</a>" if len(title) > 30 else f"<a href='{link}'>{title}</a>"

         discussion_links.append(discussion_link)
         comments.append(comment_count)
         hover_texts.append(f"{title}<br>Comments: {comment_count}")

if not discussion_links:
    print("No valid submission data found in JSON file.")
else:
    # Option A: Convert directly to a DataFrame for cleanest Plotly integration
    df = pd.DataFrame({
        'discussion_link': discussion_links,
        'comments': comments,
        'hover_text': hover_texts
    })

    fig = px.bar(
        df,
        x='discussion_link', 
        y='comments', 
        title="Most Active Hacker News Discussions", 
        labels={'discussion_link': 'Discussion Title (click to open)', 'comments': 'Number of Comments'}, 
        hover_name='hover_text'
    )

    fig.update_layout(
        title_font_size=24, 
        xaxis_title_font_size=16, 
        yaxis_title_font_size=16, 
        xaxis_tickangle=-45
    )

    fig.show()
