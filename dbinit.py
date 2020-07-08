import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('DROP TABLE IF EXISTS `food_group`')

conn.execute('CREATE TABLE `food_group` (id int PRIMARY KEY NOT NULL,name text NOT NULL)')

data=[row.rstrip('\n').split('^') for row in open('data\FD_GROUP.txt','r').readlines()]

conn.executemany("INSERT INTO `food_group` (id,name) VALUES (?, ?);", data)

conn.commit()

conn.execute('DROP TABLE IF EXISTS `food`')

conn.execute('''CREATE TABLE `food` (
  id int PRIMARY KEY NOT NULL,
  food_group_id int REFERENCES food_group(id) NOT NULL,
  long_desc text NOT NULL DEFAULT '',
  short_desc text NOT NULL DEFAULT '',
  common_names text NOT NULL DEFAULT '',
  manufac_name text NOT NULL DEFAULT '',
  survey text NOT NULL DEFAULT '',
  ref_desc text NOT NULL DEFAULT '',
  refuse int NOT NULL,
  sci_name text NOT NULL DEFAULT '',
  nitrogen_factor float NOT NULL,
  protein_factor float NOT  NULL,
  fat_factor float NOT NULL,
  calorie_factor float NOT NULL
  )''')

data2=[row.rstrip('\n').split('^') for row in open('data\FOOD_DES.txt','r').readlines()]

conn.executemany("""INSERT INTO `food` (id,food_group_id,long_desc,short_desc,common_names,
  manufac_name,survey,ref_desc,refuse,sci_name,nitrogen_factor,protein_factor,fat_factor,
  calorie_factor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", data2)

conn.commit()

conn.execute('DROP TABLE IF EXISTS `nutrient`')

conn.execute('''CREATE TABLE `nutrient` (
  id int PRIMARY KEY NOT NULL,
  units text NOT NULL,
  tagname text NOT NULL DEFAULT '',
  name text NOT NULL,
  num_decimal_places text NOT NULL,
  sr_order int NOT NULL
  )''')

data3=[row.rstrip('\n').split('^') for row in open('data\\NUTR_DEF.txt','r').readlines()]

conn.executemany("""INSERT INTO `nutrient` (id,units,tagname,name,num_decimal_places,sr_order)
  VALUES (?, ?, ?, ?, ?, ?);""", data3)

conn.commit()

conn.execute('DROP TABLE IF EXISTS `nutrition`')

conn.execute('''CREATE TABLE `nutrition` (
  food_id int REFERENCES food(id) NOT NULL,
  nutrient_id int REFERENCES nutrient(id) NOT NULL,
  amount float NOT NULL,
  num_data_points int NOT NULL,
  std_error float,
  source_code text NOT NULL,
  derivation_code text,
  reference_food_id REFERENCES food(id),
  added_nutrient text,
  num_studients int,
  min float,
  max float,
  degrees_freedom int,
  lower_error_bound float,
  upper_error_bound float,
  comments text,
  modification_date text,
  confidence_code text,
  PRIMARY KEY(food_id, nutrient_id)
  )''')

data4=[row.rstrip('\n').split('^') for row in open('data\\NUT_DATA.txt','r').readlines()]

conn.executemany("""INSERT INTO `nutrition` (food_id,nutrient_id,amount,num_data_points,std_error,
  source_code,derivation_code,reference_food_id,added_nutrient,num_studients,min,max,degrees_freedom,
  lower_error_bound,upper_error_bound,comments,modification_date,confidence_code) 
  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);""", data4)

conn.commit()

conn.execute('DROP TABLE IF EXISTS `weight`')

conn.execute('''CREATE TABLE `weight` (
  food_id int REFERENCES food(id) NOT NULL,
  sequence_num int NOT NULL,
  amount float NOT NULL,
  description text NOT NULL,
  gm_weight float NOT NULL,
  num_data_pts int,
  std_dev float,
  PRIMARY KEY(food_id, sequence_num)
  )''')

data5=[row.rstrip('\n').split('^') for row in open('data\WEIGHT.txt','r').readlines()]

conn.executemany("""INSERT INTO `weight` (food_id,sequence_num,amount,description,
  gm_weight,num_data_pts,std_dev) VALUES (?, ?, ?, ?, ?, ?, ?);""", data5)

conn.commit()

conn.close()

