import requests
import json
from pathlib import Path

# Define output path
output_dir = Path('bike_share_data')
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / 'Toronto_bike_share_data.json'

base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
url = base_url + "/api/3/action/package_show"

params = { "id": "bike-share-toronto"}	
package = requests.get(url, params = params).json()

target_url = None

# To get resource data:	
for idx, resource in enumerate(package["result"]["resources"]):
    if resource['format'].lower() == 'json':
        target_url = resource['url']
        print(f"Found resource {[idx]}: {resource['name']}")
        break

if not target_url:
    print("No valid JSON resources found.")
    exit()

# fetch the payload data
print("Fetching dataset...")
data_response = requests.get(target_url).json()

# Save the readable json file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data_response, f, indent=4, ensure_ascii=False)

print(f"Successfully saved data to {output_file}.")
    
