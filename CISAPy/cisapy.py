import requests
import json
import argparse
from collections import defaultdict

def get_vulnerabilities(year=None):
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    # Fetch JSON data
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data. Status code:", response.status_code)
        return []

    json_data = response.json()

    # Check if "properties" key exists or not
    if "properties" in json_data and "vulnerabilities" in json_data["properties"]:
        vulnerabilities = json_data["properties"]["vulnerabilities"]
    elif "vulnerabilities" in json_data:
        # If "properties" key is absent but "vulnerabilities" key exists at the root level
        vulnerabilities = json_data["vulnerabilities"]
    else:
        print("JSON structure doesn't match the expected format.")
        return []

    # Filter vulnerabilities based on the specified year
    if year:
        filtered_vulnerabilities = [vuln for vuln in vulnerabilities if vuln.get("dateAdded", "").startswith(year) or vuln.get("dateAdded", "") > year]
        return filtered_vulnerabilities
    else:
        return vulnerabilities

def get_vulnerability_stats():
    vulnerabilities = get_vulnerabilities()

    if vulnerabilities:
        stats = defaultdict(int)
        for vuln in vulnerabilities:
            year = vuln.get("dateAdded", "")[:4]
            stats[year] += 1
        
        return stats
    else:
        return {}

def export_vulnerabilities():
    vulnerabilities = get_vulnerabilities()

    if vulnerabilities:
        with open("exported_cisa_vulnerabilities.json", "w") as export_file:
            json.dump(vulnerabilities, export_file, indent=2)
        print("Exported vulnerabilities to 'exported_cisa_vulnerabilities.json'")
    else:
        print("No vulnerabilities found to export.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch known exploited vulnerabilities JSON and perform operations.")
    parser.add_argument("-s", "--stats", help="Show statistics of vulnerabilities added for each year", action="store_true")
    parser.add_argument("-e", "--export", help="Export vulnerabilities to a JSON file", action="store_true")
    parser.add_argument("-y", "--year", help="Filter entries equal to or newer than the specified YEAR (format: YYYY)", type=str)
    args = parser.parse_args()

    if args.stats:
        vulnerability_stats = get_vulnerability_stats()
        if vulnerability_stats:
            print("Vulnerabilities added in")
            print(json.dumps(vulnerability_stats, indent=2))
        else:
            print("No vulnerability statistics found.")
    
    if args.export:
        export_vulnerabilities()
    
    if not args.stats and not args.export:
        vulnerabilities = get_vulnerabilities(args.year)
        if vulnerabilities:
            print(json.dumps(vulnerabilities, indent=2))
