import csv
import sqlite3
import time
from collections import Counter
POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}
def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0
    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i > 0 and words[i - 1] in NEGATORS:
            value = -value
        total += value
    return total
def label(text):
    s = score(text)
    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    return "neutral"
complaints = []
human_labels = []
with open("complaints.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        complaints.append(row["complaint"])
        human_labels.append(row["human_label"].lower())
        agree = 0
for complaint, human in zip(complaints, human_labels):
    predicted = label(complaint)
    if predicted == human:
        agree +=1
    print(predicted, "|", complaint)
print("Total complaints:", len(complaints))
print("Labels agreed:", agree)
stop_words = {"the", "is", "and", "are", "was", "a", "from", "to"}
words = []
for complaint in complaints:
    for word in complaint.lower().split():
        word = word.strip(".,!?")
        if word not in stop_words:
            words.append(word)
frequency = Counter(words)
print("Important words:", frequency.most_common(5))
con = sqlite3.connect(":memory:")
con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")
data = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]
con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)", data
)
con.commit()
query = """
SELECT AVG(pm25)
FROM readings
WHERE station = ? AND day = ?
"""
start = time.perf_counter()
con.execute(query, ("Adyar", "2026-10-01")).fetchone()
before = time.perf_counter() - start
con.execute(
    "CREATE INDEX idx_station_day ON readings(station, day)"
)
start = time.perf_counter()
con.execute(query, ("Adyar", "2026-10-01")).fetchone()
after = time.perf_counter() - start
print("Query time before index:", before)
print("Query time after index:", after)
con.close()
