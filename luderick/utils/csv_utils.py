import csv

def findCsvRowsByImageID(image_id, csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            if int(row['image_id']) == image_id:
                rows.append(row)
        return rows
def findCsvRowsByFilename(filename,csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            if row['image'] == filename:
                rows.append(row)
        return rows

def getBoundingBoxesFromRows(rows):
    filtered = []
    for row in rows:
        filtered.append(getBoundingBoxFromRow(row))
    return filtered
def getBoundingBoxFromRow(row):
    return { "x":row['bbox_x',"y":row["bbox_y"],"w",row["bbox_w"],"h":row["bbox_h"]]}

