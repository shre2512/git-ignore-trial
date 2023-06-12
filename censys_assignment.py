import csv
from censys.search import CensysCertificates

c = CensysCertificates()
field_names = ['parsed.validity.start', 'parsed.validity.end', 'parsed.fingerprint_sha256']

fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end"
]

pages = []

for page in c.search("parsed.names: censys.io and tags: trusted", fields):
    pages.append(page)

with open('fingerprint_start_end.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(pages)

