import re

def password_check(password):
    # Vérifie si le mot de passe contient au moins 5 caractères et un chiffre
    if len(password) < 5:
        return False
    if re.search('[0-9]', password) is None:
        return False
    return True

def email_check(email):
    # Vérifie si l'adresse e-mail est au format valide
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) or email == '':
        return True
    else:
        return False

def verifier_motif(motif):
    if motif.strip() == "":
        print("Le motif ne peut pas être vide.")
        return False
    elif len(motif) < 10 :
        return False
    else:
        return True