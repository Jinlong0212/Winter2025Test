#
import json


#Create the data dictionary

data1= {

    'name': 'Jinlong Luo',
    'age':25,
    'city':'Seattle,WA',
    'interests': ['Music','Hiking','videogames'],
    'is_student':True
}



#
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file.
    json.dump(data1,json_file,indent=4)

print("You have successfully written to data1.json")