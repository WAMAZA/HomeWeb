import hashlib
import comptabilite as comptabilite
from utiles import *
import mysql.connector
import datetime



def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
        database="homeweb"
    )
    return db

def display_menu():
    print("\n+------------------------------------+")
    print("| 1. Se connecter                    |")
    print("|------------------------------------|")
    print("| 2. S'inscrire                      |")
    print("|------------------------------------|")
    print("| 3. Quitter                         |")
    print("+------------------------------------+")
    choix = int(input('+ Que voulez-vous faire?: '))
    return choix

def display_client_menu():
    print("\n+------------------------------------+")
    print("| 1. Afficher mes données            |")
    print("|------------------------------------|")
    print("| 2. Afficher les biens              |")
    print("|------------------------------------|")
    print("| 3. Acheter                         |")
    print("|------------------------------------|")
    print("| 4. Louer                           |")
    print("|------------------------------------|")
    print("| 5. Faire une plainte               |")
    print("|------------------------------------|")
    print("| 6. Modifier mes données            |")
    print("|------------------------------------|")
    print("| 7. Se déconnecter                  |")
    print("|------------------------------------|")
    print("| 8. Se désinscrire définitivement   |")
    print("|------------------------------------|")
    choix = int(input('+ Que voulez-vous faire?: '))
    return choix

def display_owner_menu():
    print("\n+------------------------------------+")
    print("| 1. Afficher mes données            |")
    print("|------------------------------------|")
    print("| 2. Afficher mes biens              |")
    print("|------------------------------------|")
    print("| 3. Ajouter un BIEN                 |")
    print("|------------------------------------|")
    print("| 4. Faire une plainte               |")
    print("|------------------------------------|")
    print("| 5. Se déconnecter                  |")
    print("|------------------------------------|")
    print("| 6. Se désinscrire définitivement   |")
    print("|------------------------------------|")
    choix = int(input('+ Que voulez-vous faire?: '))
    return choix

def display_admin_menu():
    print("\n+------------------------------------+")
    print("| 1. Afficher mes données            |")
    print("|------------------------------------|")
    print("| 2. Afficher toutes les biens       |")
    print("|------------------------------------|")
    print("| 3. Voir le chiffre d'affaire       |")
    print("|------------------------------------|")
    print("| 4. Se déconnecter                  |")
    print("|------------------------------------|")
    choix = int(input('+ Que voulez-vous faire?: '))
    return choix

def handle_choice(choice):
    user_id = None
    user = None

    db = connect_to_database()
    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    if choice == 1:
        user_id = login()
        cursor.execute("SELECT ID_User FROM CLIENT WHERE ID_User = %s", (user_id,))
        clients = cursor.fetchall()
        for client in clients:
            if user_id in client:
                user = "client"

        cursor.execute("SELECT ID_User FROM PROPRIETAIRE WHERE ID_User = %s", (user_id,))
        owners = cursor.fetchall()
        for owner in owners:
            if user_id in owner:
                user = "owner"

        cursor.execute("SELECT ID_User FROM ADMIN WHERE ID_User = %s", (user_id,))
        admins = cursor.fetchall()
        for admin in admins:
            if user_id in admin:
                user = "admin"

    elif choice == 2:
        signup()
    elif choice == 3:
        print("Bye")
    else:
        print("--> Veuillez svp entrez un choix valide.")
    
    # Validation de la transaction
    db.commit()

    # Fermeture du curseur
    cursor.close()

    return user_id, user

def handle_client_choice(user_id, choice):
    if choice == 1:
        display_client_data(user_id)

    elif choice == 2:
        display_properties()

    elif choice == 3:
        buy_a_proprety(user_id)

    elif choice == 4:
        loan_a_proprety(user_id)

    elif choice == 5:
        fil_complaint(user_id)
    
    elif choice == 6:
        modify_client_data(user_id)

    elif choice == 7:
        print("--> Vous etes deconnecté")
        print("--> Bye")

    elif choice == 8:
        confirmation = input("--> Voulez-vous vraiment se désinscrire definitivement? (oui/non): ")
        if confirmation == "oui":
            delete_client(user_id)
            return None
        else:
            print("--> Veuillez svp entrez un choix valide.")
    else:
        print("--> Veuillez svp entrez un choix valide.")

    return user_id
        
def handle_owner_choice(user_id, choice):
    if choice == 1:
        display_client_data(user_id)

    elif choice == 2:
        display_owner_properties(user_id)

    elif choice == 3:
        add_bien(user_id)

    elif choice == 4:
        fil_complaint(user_id)

    elif choice == 5:
        print("--> Vous etes deconnecté")
        print("--> Bye")

    elif choice == 6:
        confirmation = input("--> Voulez-vous vraiment se désinscrire definitivement? (oui/non): ")
        if confirmation == "oui":
            delete_client(user_id)
            return None
        else:
            print("--> Veuillez svp entrez un choix valide.")

    else:
        print("--> Veuillez svp entrez un choix valide.")
    
    return user_id

def handle_admin_choice(user_id, choice):
    if choice == 1:
        display_client_data(user_id)

    elif choice == 2:
        display_properties()

    elif choice == 3:
        comptabilite.comptab()

    elif choice == 4:
        print("--> Vous etes deconnecté")
        print("--> Bye")

    else:
        print("--> Veuillez svp entrez un choix valide.")

    return user_id

def login():
    db = connect_to_database()
    cursor = db.cursor()

    mail_gsm = input("- Entrez votre mail ou GSM: ")
    password = input("- Entrez votre mot de passe: ")
    query = "SELECT ID_user FROM UTILISATEUR WHERE (email = %s OR GSM = %s) AND password = %s"
    values = (mail_gsm, mail_gsm, password)

    cursor.execute(query, values)
    
    result = cursor.fetchone()

    if result is None:
        print("--> Les données sont incorrects.")
        return None
    
    print("--> Vous êtes connecté !")
    return result[0]
    
    # # Hachez le mot de passe saisi par l'utilisateur
    # hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Comparez les deux versions hachées pour vérifier si le mot de passe est correct
    # if hashed_password == result[0]:
    #     print("Vous êtes connecté !")
    #     return True
    # else:
    #     print("Mot de passe incorrect.")
    #     return False

def signup():
    db = connect_to_database()
    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()
    
    while True:
        nom = input("Entrez votre nom: ")
        prenom = input("Entrez votre prénom: ")

        cursor.execute('SELECT * FROM UTILISATEUR WHERE nom = %s AND prenom = %s', (nom, prenom))
        resultat = cursor.fetchone()
        if not resultat:
            break
        print("Le client existe déjà dans la base de données.")

    adresse = input("Entrez votre adresse: ")

    while True:
        gsm = input("Entrez votre numéro de GSM (facultatif): ")
        email = input("Entrez votre adresse e-mail (facultatif): ")
        # Valider que au moins un des champs "GSM" et "Email" est rempli
        if not gsm and not email:
            print("Au moins un des champs 'GSM' et 'Email' doit être rempli !")
        elif not email_check(email):
            print("Format de mail invalid")
        else:
            cursor.execute('SELECT * FROM UTILISATEUR WHERE email = %s', (email,))
            resultat = cursor.fetchone()
            if not resultat:
                break
            print("Cette adresse e-mail a déjà été ajoutée.")

    while True:
        password = input("Entrez votre mot de passe : ")
        if not password_check(password):
            print("Le mot de passe doit contenir: \n  .au moins 5 caracteres\n  .au moins un nombre")
        else:
            break

    # # Hashage du mot de passe
    # hashed_password = hashlib.sha256(password.encode()).hexdigest()

    
    
    

    
    while True:
        user_type = input("Ajouter un type d'utilisateur? (1 = client, 2 = propriétaire): ")
        if user_type == "1":
            # Requête SQL en fonction des champs remplis par l'utilisateur
            if gsm and not email:
                sql = "INSERT INTO UTILISATEUR (nom, prenom, password, adresse, gsm, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, gsm, 0, 1, 0)
            elif email and not gsm:
                sql = "INSERT INTO UTILISATEUR (Nom, Prenom, password, adresse, email, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, email, 0, 1, 0)
            else:
                sql = "INSERT INTO UTILISATEUR (Nom, Prenom, password, adresse, gsm, email, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, gsm, email, 0, 1, 0)


            # Exécutez la requête SQL
            cursor.execute(sql, val)

            query = "SELECT ID_user FROM UTILISATEUR WHERE nom = %s AND prenom = %s AND password = %s"
            values = (nom, prenom, password)
            cursor.execute(query, values)
            resultat = cursor.fetchone()
            cursor.execute("INSERT INTO CLIENT (ID_User) values (%s)", (resultat[0],))
            break
        elif user_type == "2":
            # Requête SQL en fonction des champs remplis par l'utilisateur
            if gsm and not email:
                sql = "INSERT INTO UTILISATEUR (nom, prenom, password, adresse, gsm, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, gsm, 1, 0, 0)
            elif email and not gsm:
                sql = "INSERT INTO UTILISATEUR (Nom, Prenom, password, adresse, email, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, email, 1, 0, 0)
            else:
                sql = "INSERT INTO UTILISATEUR (Nom, Prenom, password, adresse, gsm, email, proprietaire, client, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (nom, prenom, password, adresse, gsm, email, 1, 0, 0)

            # Exécutez la requête SQL
            cursor.execute(sql, val)

            query = "SELECT ID_user FROM UTILISATEUR WHERE nom = %s AND prenom = %s AND password = %s"
            values = (nom, prenom, password)
            cursor.execute(query, values)
            resultat = cursor.fetchone()
            cursor.execute("INSERT INTO PROPRIETAIRE (ID_User) values (%s)", (resultat[0],))
            break
        else:
            print("--> Veuillez entrer un type d'utilisateur valide.")


    # Récupération du résultat de la requête
    resultat = cursor.fetchone()

    print("Vous êtes inscrit avec succès.")
        
    db.commit()

    db.close()

def delete_client(user_id):
    db = connect_to_database()
    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la commande UPDATE pour anonymiser les informations du client
    cursor.execute("UPDATE UTILISATEUR SET Nom = %s, Prenom = %s, password = %s, email = %s, GSM = %s,Adresse=%s WHERE ID_User = %s", ("ANONYME", "ANONYME", "ANONYME", "ANONYME", "ANONYME","ANONYME", user_id))

    # Validation de la suppression
    if cursor.rowcount > 0:
        print("Le client a été supprimé avec succès.")
    else:
        print("Aucun client n'a été supprimé.")

    # Validation de la transaction
    db.commit()

    # Fermeture du curseur
    cursor.close()

def modify_client_data(user_id):
    db = connect_to_database()

    nouveau_nom = input("Entrez votre nouveau nom: ")
    nouveau_prenom = input("Entrez votre nouveau prenom: ")
    nouveau_email = input("Entrez votre nouveau email: ")
    nouvelle_adresse = input("Entrez votre nouvelle adresse: ")
    nouveau_gsm = input("Entrez votre nouveau gsm: ")
    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la commande UPDATE pour modifier les informations du client avec l'ID donné
    cursor.execute("UPDATE UTILISATEUR SET Nom = %s, Prenom = %s, email = %s, Adresse = %s, gsm = %s WHERE ID_User = %s",
                (nouveau_nom, nouveau_prenom, nouveau_email, nouvelle_adresse, nouveau_gsm, user_id))

    # Validation de la modification
    if cursor.rowcount > 0:
        print("Les informations du client ont été modifiées avec succès.")
        # Validation de la transaction
        db.commit()
    else:
        print("Aucun client n'a été modifié.")

    # Fermeture de la connexion à la base de données
    db.close()

def display_all_clients_data():
    db = connect_to_database()

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la commande SELECT pour récupérer les informations de tous les clients
    cursor.execute("SELECT * FROM UTILISATEUR")

    # Récupération des résultats et impression des informations de chaque client
    for row in cursor.fetchall():
        print("==========================================")
        print("= ID_User  :", row[0])
        print("= Prenom   :", row[1])
        print("= Nom      :", row[2])
        print("= Adresse  :", row[4])
        print("= GSM      :", row[5])
        print("= Email    :", row[6])
        print("==========================================")
    # Fermeture de la connexion à la base de données
    db.close()

def display_client_data(user_id):
    db = connect_to_database()

    cursor = db.cursor()
    query = "SELECT * FROM UTILISATEUR WHERE ID_User = %s"
    values = (user_id,)

    cursor.execute(query, values)
    
    # Récupération des résultats et impression des informations de chaque client
    for row in cursor.fetchall():
        print("=====================================")
        print("=           Vos données             =")
        print("=====================================")
        # print("ID_User :", row[0])
        print("= Prenom  :", row[1])
        print("= Nom     :", row[2])
        print("= Password:", row[3])
        print("= Adresse :", row[4])
        print("= GSM     :", row[5])
        print("= EMAIL   :", row[6])
        print("=====================================")

def display_properties():
    db = connect_to_database()

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la commande SELECT pour récupérer les informations de tous les clients
    cursor.execute("SELECT * FROM BIEN where ID_User not in (SELECT ID_User FROM UTILISATEUR WHERE NOM LIKE '%ANONYME%')")

    print("=====================================")
    # Récupération des résultats et impression des informations de chaque client
    for row in cursor.fetchall():
        print("= ID_Bien         : ", row[0])
        cursor.execute("SELECT Nom FROM UTILISATEUR where ID_User = %s", (row[2],))
        owner_name = cursor.fetchone()
        print("= Proprietaire :", owner_name[0])


        if row[4] == 1:
            ## Terrain
            print("= Type         : Terrain")
            cursor.execute("SELECT * FROM TERRAIN where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Superficie   :", col[1])

        elif row[5] == 1:
            ## Maison
            print("= Type        : Maison")
            cursor.execute("SELECT * FROM MAISON where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Surface      :", col[1])
                if col[2] == 1:
                    print("= Piscine      : Oui")
                else:
                    print("= Piscine      : Non")
                if col[3] == 1:
                    print("= Jardin       : Oui")
                else:
                    print("= Jardin       : Non")

        elif row[6] == 1:
            ## Appartement
            print("= Type         : Appartement")
            cursor.execute("SELECT * FROM APPARTEMENT where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Etage        :", col[1])
                if col[2] == 1:
                    print("= Ascenceur    : Oui")
                else:
                    print("= Ascenceur    : Non")


        cursor.execute("SELECT * FROM REGION where ID_Region = %s", (row[3],))
        resultat = cursor.fetchall()
        print("= Pays         :", resultat[0][1])
        print("= Region       :", resultat[0][2])

        print("= Prix         :", row[1])
        print("=====================================")

    # Fermeture de la connexion à la base de données
    db.close()

def display_owner_properties(id_user):
    db = connect_to_database()

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la commande SELECT pour récupérer les informations de tous les clients
    cursor.execute("SELECT * FROM BIEN where ID_User = %s", (id_user,))

    print("=====================================")
    # Récupération des résultats et impression des informations de chaque client
    for row in cursor.fetchall():
        cursor.execute("SELECT Nom FROM UTILISATEUR where ID_User = %s", (row[2],))
        owner_name = cursor.fetchone()
        print("= Proprietaire :", owner_name[0])


        if row[4] == 1:
            ## Terrain
            print("= Type         : Terrain")
            cursor.execute("SELECT * FROM TERRAIN where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Superficie   :", col[1])

        elif row[5] == 1:
            ## Maison
            print("= Type        : Maison")
            cursor.execute("SELECT * FROM MAISON where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Surface      :", col[1])
                if col[2] == 1:
                    print("= Piscine      : Oui")
                else:
                    print("= Piscine      : Non")
                if col[3] == 1:
                    print("= Jardin       : Oui")
                else:
                    print("= Jardin       : Non")

        elif row[6] == 1:
            ## Appartement
            print("= Type         : Appartement")
            cursor.execute("SELECT * FROM APPARTEMENT where ID_Bien = %s", (row[0],))
            for col in cursor.fetchall():
                print("= Etage        :", col[1])
                if col[2] == 1:
                    print("= Ascenceur    : Oui")
                else:
                    print("= Ascenceur    : Non")


        cursor.execute("SELECT * FROM REGION where ID_Region = %s", (row[3],))
        resultat = cursor.fetchall()
        print("= Pays         :", resultat[0][1])
        print("= Region       :", resultat[0][2])

        print("= Prix         :", row[1])
        print("=====================================")

    # Fermeture de la connexion à la base de données
    db.close()

def fil_complaint(user_id):
    db = connect_to_database()
    ID_contrat = int(input("Entrer l'ID de CONTRAT: "))
    Dat= datetime.date.today()
    cursor = db.cursor()

    cursor.execute("SELECT ID_contrat FROM CONTRAT")
    CONTRAT =[]
    for row in cursor.fetchall():
        CONTRAT.append(row[0])
    cursor.close()
    if ID_contrat in CONTRAT:
        cursor = db.cursor()
        cursor.execute("SELECT  ID_bien,CONTRAT_LOCATION,ID_User from CONTRAT where ID_contrat = %s", (ID_contrat,))
        contrat_loc = []
        for row in cursor.fetchall():
            contrat_loc.append(row[0])
            contrat_loc.append(row[1])
            contrat_loc.append(row[2])
        if contrat_loc[1] == 1 :
            print(contrat_loc) 
            ID_bien = contrat_loc[0]
            print(ID_bien)
            Motif = input("veuillez remplir votre plainte:")
            while not verifier_motif(Motif):
                Motif = input("expliquer encore plus votre probléme")
            sql="INSERT into PLAINTE (ID_User, ID_bien, Date ,Motif) VALUES (%s, %s, %s, %s)"
            val=(user_id, ID_bien, Dat , Motif)
            cursor.execute(sql, val)
        else:
            
            print("cette CONTRAT ce n'est pas un CONTRAT de location")
    else:
        print("Contrat introuvable")
    db.commit()
    db.close()

def buy_a_proprety(client):
    # Connexion à la base de données
    db = connect_to_database()

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la requête SELECT pour récupérer toutes les données de la table BIENS_INFO
    cursor.execute("SELECT ID_BIEN, PRIX, REGION, TYPE, SUPERFICIE, PISCINE, JARDIN, ASCENSEUR, ID_PROPRIETAIRE, NOM_PROPRIETAIRE FROM BIENS_INFO WHERE ID_BIEN IN (SELECT ID_BIEN FROM BIEN WHERE CAUTION IS NULL AND ID_User not in (SELECT ID_User FROM UTILISATEUR WHERE NOM LIKE '%ANONYME%'))")


    # Affichage des résultats
    for row in cursor.fetchall():
        print("==========================================")
        print("= ID_Bien     :", row[0])
        print("= Prix        :", row[1])
        print("= Region      :", row[2])
        print("= Type        :", row[3])
        print("= Superficie  :", row[4])
        print("= Piscine     :", row[5])
        print("= Jardin      :", row[6])
        print("= Ascenceur   :", row[7])
        print("= Nom du proprietaire :", row[9])
        print("==========================================")

    # Fermeture de la connexion à la base de données
    db.close()

    ID_Bien = int(input("Entrer l'ID du BIEN: "))
    Dat = datetime.date.today()
    
    prop = []
    db = connect_to_database()
    cursor = db.cursor()

    cursor.execute("SELECT Nom FROM UTILISATEUR where ID_user in (SELECT ID_user FROM BIEN where ID_BIEN = %s)", (ID_Bien,))
    proprietaire = cursor.fetchone()[0]

    cursor.execute("SELECT Nom FROM UTILISATEUR where proprietaire = 1")
    
    # les propriétaire qui existent
    for row in cursor.fetchall() :
        prop.append(row[0])

    cursor.execute("SELECT* from CONTRAT ")
    CONTRAT =[]
    # les biens qui sont sous CONTRAT
    for row in cursor.fetchall():
        CONTRAT.append(row[5])
    
    # les prix du BIEN
    cursor.execute("SELECT prix  from BIEN where BIEN.ID_Bien = %s",(ID_Bien,))
    prix = cursor.fetchone()[0]

    if proprietaire in prop : 
        if ID_Bien not in CONTRAT : 
            sql="INSERT into CONTRAT (Date_du_contrat, ID_User, CONTRAT_LOCATION, CONTRAT_VENTE, ID_Bien)  VALUES (%s, %s, %s, %s,%s)"
            val=(Dat,client,False,True,ID_Bien)
            cursor.execute(sql, val) 
            
            cursor.execute("SELECT ID_contrat from CONTRAT where ID_User = %s and Date_du_contrat = %s", (client, Dat))
            id_contrat = cursor.fetchone()[0]

            cursor.execute("INSERT into CONTRAT_VENTE (id_contrat, prix_de_vente)  VALUES (%s, %s)", (id_contrat,prix))
            
        else : 
            print("le BIEN est sous CONTRAT")
    else : 
        print("le propriétaire n'existe pas")
    
    db.commit()
    db.close()
    
def loan_a_proprety(client):
    # Connexion à la base de données
    db = connect_to_database()

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()

    # Exécution de la requête SELECT pour récupérer toutes les données de la table BIENS_INFO
    cursor.execute("SELECT ID_BIEN, PRIX, REGION, TYPE, SUPERFICIE, PISCINE, JARDIN, ASCENSEUR, ID_PROPRIETAIRE, NOM_PROPRIETAIRE FROM BIENS_INFO WHERE ID_BIEN IN (SELECT ID_BIEN FROM BIEN WHERE CAUTION IS NOT NULL AND ID_User NOT IN (SELECT ID_User FROM UTILISATEUR WHERE NOM LIKE '%ANONYME%'))")

    # Affichage des résultats
    for row in cursor.fetchall():
        print("==========================================")
        print("= ID_Bien     :", row[0])
        print("= Prix        :", row[1])
        print("= Region      :", row[2])
        print("= Type        :", row[3])
        print("= Superficie  :", row[4])
        print("= Piscine     :", row[5])
        print("= Jardin      :", row[6])
        print("= Ascenceur   :", row[7])
        print("= Nom du proprietaire :", row[9])
        print("==========================================")

    # Fermeture de la connexion à la base de données
    db.close()

    ID_Bien = int(input("Entrer l'ID du BIEN: "))
    Dat = datetime.date.today()
    Dat_fin = Dat + datetime.timedelta(days=6 * 30)

    prop = []
    db = connect_to_database()
    cursor = db.cursor()

    cursor.execute("SELECT Nom FROM UTILISATEUR WHERE ID_user IN (SELECT ID_user FROM BIEN WHERE ID_BIEN = %s)", (ID_Bien,))
    proprietaire = cursor.fetchone()[0]
    cursor.execute("SELECT Nom FROM UTILISATEUR WHERE proprietaire = 1")

    # les propriétaires qui existent
    for row in cursor.fetchall():
        prop.append(row[0])

    cursor.execute("SELECT * FROM CONTRAT ")
    CONTRAT = []
    # les biens qui sont sous CONTRAT
    for row in cursor.fetchall():
        CONTRAT.append(row[5])

    # le prix du BIEN
    cursor.execute("SELECT PRIX FROM BIEN WHERE BIEN.ID_Bien = %s", (ID_Bien,))
    prix = cursor.fetchone()[0]
    cursor.fetchall()

    # la caution du BIEN
    cursor.execute("SELECT CAUTION FROM BIEN WHERE BIEN.ID_Bien = %s", (ID_Bien,))
    caution = cursor.fetchone()[0]
    cursor.fetchall()

    if proprietaire in prop:
        if ID_Bien not in CONTRAT:
            sql = "INSERT INTO CONTRAT (Date_du_contrat, ID_User, CONTRAT_LOCATION, CONTRAT_VENTE, ID_Bien)  VALUES (%s, %s, %s, %s, %s)"
            val = (Dat, client, False, True, ID_Bien)
            cursor.execute(sql, val)
            cursor.fetchall()

            cursor.execute("SELECT ID_contrat FROM CONTRAT WHERE ID_User = %s AND Date_du_contrat = %s", (client, Dat))
            id_contrat = cursor.fetchone()[0]
            cursor.fetchall()

            cursor.execute("INSERT INTO CONTRAT_LOCATION (id_contrat, date_de_debut, date_de_fin, montant_mensuel, caution)  VALUES (%s, %s, %s, %s, %s)", (id_contrat, Dat, Dat_fin, prix, caution))
            cursor.fetchall()

        else:
            print("Le BIEN est sous CONTRAT")
    else:
        print("Le propriétaire n'existe pas")

    db.commit()
    db.close()

def add_bien(ID_User):
    db = connect_to_database()
    # Création d'un curseur pour exécuter des commandes SQL
    cursor = db.cursor()
    
    # Exécution de la commande INSERT pour ajouter un BIEN avec l'ID donné
    type_bien = input("Donnez le type de BIEN : ")
    while type_bien != "terrain" and type_bien != "maison" and type_bien != "appartement":
        print("--> Veuillez entrer un type de BIEN valide.")
        type_bien = input("Donnez le type de BIEN : ")

    a = input("Ce bien est pour l'achat ou la location? (A/L): ")

    while a != "A" and a != "L":
        print("--> Veuillez entrer un choix valide : ")
        a = input("Ce bien est pour l'achat ou la location? (A/L): ")

    if a == "A":
        prix = input("Donnez le prix du BIEN : ")
    else:
        prix = input("Donnez le prix mensuelle du BIEN : ")
        caution = input("Entrer la caution du BIEN : ")

    maison = 0
    terrain = 0
    appartement = 0
    
    pays = input("Donnez le pays du BIEN : ")
    ville = input("Donnez la ville du BIEN : ")

    if type_bien == "terrain":
        Superficie = float(input("Entrer la superficie de terrain : "))
        terrain = 1
    elif type_bien == "maison":
        surface_de_terrain = float(input("Entrer la surface de terrain : "))
        while True:
            piscine = input("Piscine (Y/N): ")
            if piscine == "Y":
                piscine = 1
                break
            elif piscine == "N":
                piscine = 0
                break
            print("Entrer un valide choix.")
        while True:
            jardin = input("Jardin (Y/N): ")
            if jardin == "Y":
                jardin = 1
                break
            elif jardin == "N":
                jardin = 0
                break
            print("Entrer un valide choix.")
        maison = 1

    elif type_bien == "appartement":
        etage = int(input("Etage: "))
        superficie = float(input("Entrer la superficie d'appartement : "))
        while True:
            ascenceur = input("Ascenceur (Y/N): ")
            if ascenceur == "Y":
                ascenceur = 1
                break
            elif ascenceur == "N":
                ascenceur = 0
                break
            print("Entrer un valide choix.")
        appartement = 1
    
    sql1 = "INSERT INTO REGION (pays, Region) VALUES (%s, %s)"
    val1 = (pays, ville)
    cursor.execute(sql1, val1)
    
    cursor.execute("SELECT pays, Region FROM REGION WHERE pays = %s AND Region = %s", (pays, ville))
    result = cursor.fetchone()
    
    if not result:
        cursor.execute(sql1, val1)
    
    cursor.execute("SELECT ID_Region FROM REGION WHERE pays = %s AND Region = %s", (pays, ville))
    REGION = cursor.fetchone()[0]
    
    if a == "A":
        sql = "INSERT INTO BIEN (Prix, ID_User, ID_Region, TERRAIN, MAISON, APPARTEMENT) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (prix, ID_User, REGION, terrain, maison, appartement)
        cursor.execute(sql, val)
    else:
        sql = "INSERT INTO BIEN (Prix, ID_User, ID_Region, TERRAIN, MAISON, APPARTEMENT, CAUTION) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (prix, ID_User, REGION, terrain, maison, appartement, caution)
        cursor.execute(sql, val)

    sql = "SELECT ID_bien FROM BIEN WHERE Prix = %s AND ID_User = %s AND ID_Region = %s AND TERRAIN = %s AND MAISON = %s AND APPARTEMENT = %s"
    val = (prix, ID_User, REGION, terrain, maison, appartement)
    cursor.execute(sql, val)

    id_bien = cursor.fetchone()[0]

    if type_bien == "terrain":
        cursor.execute("INSERT INTO TERRAIN (ID_Bien, Superficie) values (%s, %s)", (id_bien, Superficie))
    elif type_bien == "maison":
        cursor.execute("INSERT INTO MAISON (ID_Bien, Surface_de_terrain ,Piscine, Jardin) values (%s, %s, %s, %s)", (id_bien, surface_de_terrain, piscine, jardin))
    elif type_bien == "appartement":
        cursor.execute("INSERT INTO APPARTEMENT (ID_Bien, Etage, Ascenceur, superficie) values (%s, %s, %s, %s)", (id_bien, etage, ascenceur, superficie))
    
    # Validation de la transaction
    if cursor.rowcount > 0:
        print("Bien ajouté avec succès.")
    else:
        print("Aucun BIEN n'a été ajouté.")

    db.commit()

    # Fermeture de la connexion à la base de données
    db.close()
