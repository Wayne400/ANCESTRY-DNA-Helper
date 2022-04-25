fn = 'Wayne_A.txt'
sorted_fn = 'sorted_Wayne_A.txt'
file_path = '/mnt/c/Users/Wayne/DNA/'
fn = file_path + fn
sorted_fn = file_path + sorted_fn

with open(fn, 'r') as first_file:
    rows = first_file.readlines()
    sorted_rows = sorted(rows, key=lambda x: int(x.split()[0]), reverse=False)
    with open(sorted_fn,'w') as second_file:
        for row in sorted_rows:
            second_file.write(row)