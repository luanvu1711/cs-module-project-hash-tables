records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    {"Grace", "Marketing"}
]

def build_index(records):
    idx = {}
    for record in records:
        name = record[0]
        department = record[1]
        if department not in idx:
            idx[department] = [name]
        else:
            idx[department].append(name)
    return idx


# def print_department_using_index(dep_name):
#     return index_dict(dep_name)

index_direct = build_index(records)
print(index_direct)

