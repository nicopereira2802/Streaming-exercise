import csv

def save_data(episodes,path):

    headers = ['series_name','season_number','episode_number','episode_title','air_date']

    with open(path,mode='w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for ep in episodes:
            writer.writerow({
                'series_name': ep.series,
                'season_number': ep.season,
                'episode_number': ep.number,
                'episode_title': ep.title,
                'air_date': ep.date
            })
    print(f"Archive saved in: {path}")


def save_report(input_episodes, output_episodes, report_path):

    total_input = len(input_episodes)
    total_output = len(output_episodes)

    discarded = len([e for e in input_episodes if not e.is_valid])
    corrected = len([e for e in input_episodes if e.errors and e.is_valid])

    valid = [e for e in input_episodes if e.is_valid]
    duplicates = len(valid) - total_output

    report_explanation = """
Deduplication Strategy

Data normalization:
Before comparing, all text fields are stripped of extra spaces and converted to lowercase.

Multikey matching:
To identify duplicates even with missing data, the system generates three keys for each entry:
key1: series name + season + episode number
key2: series name + episode number + episode title
key3: series name + season + episode title

If two rows match any of these combinations, they are flagged as the same entity.

Scoring system:
Then, the system calculates a quality score:
100 points if it has a valid air date
50 points if it has a real episode title
25 points if season and episode numbers are greater than 0

Tie breaking and final output:
The record with the highest score is kept. If there is a tie, the system follows the "first in file" rule.
"""

    with open(report_path, mode="w", encoding="utf-8") as f:

        f.write("== DATA REPORT ==\n\n")

        f.write(f"Total input records: {total_input}\n")
        f.write(f"Total output records: {total_output}\n")
        f.write(f"Corrected entries: {corrected}\n")
        f.write(f"Discarded entries: {discarded}\n")
        f.write(f"Duplicates detected: {duplicates}\n\n")

        f.write("-" * 60 + "\n\n")
        f.write(report_explanation)

    print(f"Report generated in {report_path}")
