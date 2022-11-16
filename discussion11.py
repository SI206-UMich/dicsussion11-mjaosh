import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    #this is how to set up our sql stuff
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    cur.execute('drop table if exists Patients')
    cur.execute('create table Patients (pet_id INTEGER PRIMARY KEY, name TEST, species_id NUMBER, age INTEGER, cuteness INTEGER, aggresiveness NUMBER)')
    conn.commit()

# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):

    cur.execute('insert into Patients (pet_id, name, species_id, age, cuteness, aggresiveness) values(?,?,?,?,?,?)', (0, "Fluffle", 0, 3, 90, 100))  
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    species_id_dict = {'Rabbit' : 0, 'Dog': 1, 'Cat': 2, 'Boa Constrictor': 3, 'Chinchilla': 4, 'Hamster': 5, 'Cobra': 6, 'Parrot': 7, 'Shark': 8, 'Goldfish': 9, 'Gerbil': 10, 'Llama': 11, 'Hare': 12}

    # THE REST IS UP TO YOU
    pet_id = 1
    for item in json_data: 
        conn.execute('insert into Patients (pet_id, name, species_id, age, cuteness, aggresiveness) values(?,?,?,?,?,?)', (pet_id, item['name'], species_id_dict[item['species']], item['age'], item['cuteness'], item['aggressiveness']))
        pet_id += 1
        conn.commit()
    


# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    cur.execute('select name from Patients where aggresiveness <= 10')
    names = cur.fetchall()
    conn.commit()
    return names



def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)

    create_patients_table(cur, conn)
    add_fluffle(cur, conn)
    add_pets_from_json('pets.json', cur, conn)
    ls = (non_aggressive_pets(10, cur, conn))
    print(ls)
    
    
if __name__ == "__main__":
    main()

