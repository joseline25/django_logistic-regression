
# pip install pandas
# pip install seaborn
# pip install sklearn


import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

# to work with the database
import sqlite3

connexion = sqlite3.connect("trash_logis_reg/db.sqlite3")

# to query from our connexion established

cursor = connexion.cursor()

# get all the entries of the table trash_trashbooking

sql = pd.read_sql_query("SELECT * FROM trash_trashbooking", connexion)
data = pd.DataFrame(sql, columns=["id", "day_of_week", "previous_requests",
                    "public_holiday", "resident_id", "weather", "date", "trash_pickup_request"])

print(data)