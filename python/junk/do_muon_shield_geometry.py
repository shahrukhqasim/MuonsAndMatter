import uproot

# Open the ROOT file
file_path = '../../data/geofile_full.fe_0_n_events_1000.root'
file = uproot.open(file_path)

# List the contents of the ROOT file
file_content = file.keys()
print(file_content)

# Assuming you know the name of the tree or object you want to access,
# you can do something like this:
# tree = file['tree_name']
# tree.show()

# You can also iterate over the keys to inspect the contents more closely:
for key in file_content:
    print(key)
    obj = file[key]
    print(obj.classname)

# To convert the data to a pandas DataFrame (if it's a tree structure):
# df = tree.arrays(library='pd')
# print(df.head())