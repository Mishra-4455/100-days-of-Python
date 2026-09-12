import json

website = "Replit"
email = "mishra@gmail.com"
password = "mish@2013"

new_data = {
    website : {
        "Email" : email,
        "Password" : password
    }
}

with open("data.json", "r") as data_file:
    #reading old data
    data = json.load(data_file)
    #Updating old data with new data
    data.update(data_file)

with open("data.json", "w") as data_file:
    #saving updated data 
    json.load(data, data_file, indent=4)

    # website_entry.delete(0, END)
    # password_entry.delete(0, END)