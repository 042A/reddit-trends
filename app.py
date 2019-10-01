import json

# Function to write a dict as json to file.json
def write_json_file ( pet_name ) :
    my_dict = {
        "name": pet_name,
        "species": "Doggo",
        "age": 8,
        "angry": False,
        "other_names": ["doggen", "good boy", "byracka"]
    }
    f = open("file.json", "w")
    json.dump(my_dict, f, indent=3) 

# Function to read file.json into a dict, and then print it.
def read_json_file ():
    f = open('file.json', 'r')
    my_dict = json.load(f)
    print(my_dict)

# Choice of reading or writing to the JSON-file
val = input("Read(r) or write(w)?: ") 
if val == "r" :
    print("Let's read the json data.")
    read_json_file ()
    "Thanks for using the pet database."
if val == "w" :
    print("Let's write the json data.")
    mypet = input("Name of pet: ") 
    write_json_file ( mypet )
    "Adding that name."
    "Thanks for using the pet database."
else :
    print("Please choose read(r) or write(w). Exiting.")
