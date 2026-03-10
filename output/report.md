== DATA REPORT ==

Total input records: 42
Total output records: 23
Corrected entries: 8
Discarded entries: 1
Duplicates detected: 18

------------------------------------------------------------


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
