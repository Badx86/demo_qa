# Elements -> Check Box

expected_elements = [
    "Home", "Desktop", "Notes", "Commands", "Documents",
    "WorkSpace", "React", "Angular", "Veu", "Office",
    "Public", "Private", "Classified", "General", "Downloads",
    "Word File.doc", "Excel File.doc"
]

data1 = ["Desktop", "Notes", "Commands", "Angular", "Veu", "Downloads", "Word File.doc", "Excel File.doc"]
data2 = ["desktop", "notes", "commands", "angular", "veu", "downloads", "wordFile", "excelFile"]

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()
assert data1 == data2