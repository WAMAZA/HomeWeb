import mysql.connector
import functions
from datetime import datetime, timedelta


def comptab():
    year = int(input("Entrer l'année : "))
    month = int(input("Entrer le mois : "))
        
    compta(year, month)

def compta(year, month):
    db = functions.connect_to_database()
    date_actuelle = datetime.now()
    annee_passee = date_actuelle.year - year
    date_annee_passee = date_actuelle.replace(year=annee_passee)
    date_annee_passee_str = date_annee_passee.strftime("%d-%m-%Y")
    
    cursor = db.cursor()
    cursor.execute("SELECT Montant FROM TRANSACTION WHERE Transaction_date like '%s%' ", (year,))
    
    results = cursor.fetchall()
    SUM = 0
    for row in results:
        SUM += row[0]
    
    print(f"Le rapport de comptabilité de l'année {year} est de : {SUM}")
    cursor.close()
    
    cursor = db.cursor()
    for month in range(1, month+1):
        start_date = datetime(year, month, 1)
        end_date = start_date.replace(day=1, month=month+1) if month < 12 else start_date.replace(day=1, month=1, year=year+1)
        
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")
        
        cursor.execute("SELECT SUM(Montant) FROM TRANSACTION WHERE Transaction_date >= %(start_date)s AND Transaction_date < %(end_date)s",
                    {'start_date': start_date_str, 'end_date': end_date_str})
        
        result = cursor.fetchone()
        monthly_sum = result[0] if result[0] is not None else 0
        
    print(f"Le rapport de comptabilité pour le mois {month} de l'année {year} est : {monthly_sum}")

    cursor.close()
    db.close()

