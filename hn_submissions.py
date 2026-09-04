from operator import itemgetter
from pathlib import Path

import json
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

output_dir = Path('hn_data')
output_dir.mkdir(parents=True, exist_ok=True)
file_path = output_dir / 'hn_discussions.json'

# Proces information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict.get('title', 'No title available'), 
        'hn_link': f"https://hacker-news.firebaseio.com/v0/topstories", 
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

with open (file_path, 'w', encoding='utf-8') as f:
    json.dump(submission_dicts, f, indent=4)
