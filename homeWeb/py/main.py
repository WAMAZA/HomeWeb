from functions import *


def run_app():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+-+-+-+-+ Bienvenue dans HomeWeb (Application de location et de vente immobilière)  +-+-+-+-+")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    user_id = None
    user = None

    while True:

        if user == None:
            choix = 0
            choix = display_menu()
            user_id, user = handle_choice(choix)
            if choix == 3:
                break

        elif user == 'client':
            choix = 0
            while choix != 7 and user_id != None:
                choix = display_client_menu()
                user_id = handle_client_choice(user_id, choix)
            user = None
            user_id = None

        elif user == 'owner':
            choix = 0
            while choix != 5 and user_id != None:
                choix = display_owner_menu()
                user_id = handle_owner_choice(user_id, choix)
            user = None
            user_id = None

        elif user == 'admin':
            choix = 0
            while choix != 4 and user_id != None:
                choix = display_admin_menu()
                user_id = handle_admin_choice(user_id, choix)
            user = None
            user_id = None

run_app()