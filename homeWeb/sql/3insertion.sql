use homeweb;


insert into UTILISATEUR(prenom, nom, Password, adresse, gsm, email, PROPRIETAIRE, CLIENT,ADMIN)
values ('youssef', 'Fiher', 'Kosovo99', 'Rue de Bruxelles 61', '0426548721', 'youssef-fih@gmail.com',true, false,false),
       ('ayoub', 'elmansouri', 'elmansMadina11', 'Rue dames blanche121', '0487896514', 'ayoubelmns@gmail.com', false, true,false),
       ('sami', 'elouakli', 'RmaCr7', 'Rue de patenier 54', '041411578', 'sami@outlook.fr', false, true,false),
       ('omar', 'ametjaou', 'OmarAmet01', 'Rue salzinnes moulins', '048789854', 'omar@outlook.com', true, false,false),
       ('adnane', 'elmahi', 'AdnanZara99', 'rue bovresse 12', '0485454748', 'adnaneelmeh@gmail.fr', true, false,false),
       ('abdelali','Fiher','abdel1961','Lot naima n 104','0687838771',null,false,false,true);

insert into CLIENT(ID_User)
values (2),
       (3);

insert into PROPRIETAIRE(ID_User)
values (1),
       (4),
       (5);

insert into ADMIN (ID_User)
values (6);

insert into REGION(pays, region)
values ('MAROC','Rabat'),
       ('BELGIQUE','Bruxelles'),
       ('FRANCE','Paris'),
       ('ESPAGNE','Madrid'),
       ('HUNGARY','Budapest');

insert into BIEN(Prix, ID_User, ID_Region, TERRAIN, MAISON, APPARTEMENT,caution)
values (150000,1,1,false,false,true,null),
      (200000,4,3,true,false,false,null),
      (300000,5,2,false,true,false,1000),
      (400000, 1, 1, false, true, false, null),
      (250000, 4, 4, true, false, false, 500),
      (150000, 5, 3, false, false, true, null);

insert into MAISON (ID_Bien, Surface_de_terrain, Piscine, Jardin)
values (3,500,true,true),
       (4,1000,false,false);

insert into TERRAIN (ID_Bien, Superficie)
values (2,10000),
       (5,20000);

insert into APPARTEMENT(id_bien, etage, ascenseur,superficie)
values (1,2,true,250),
       (6,3,false,300);

INSERT INTO AGENT_IMMOBILIER (Nom, Prenom, Adresse, GSM, Email)
VALUES ('Rachid', 'Ali', '10 Rue Hassan II, Casablanca', '0612345678', 'rachid.ali@gmail.com'),
('louis', 'vanghal', '20 Avenue pascal V, toulouse', '0623456789', 'hafsa.benahmed@gmail.com'),
('thomas', 'chelby', '5 highway street, london', '0654321098', 'said.bouazzaoui@gmail.com'),
('Amina', 'El Kandoussi', '15 Rue Abdelkrim Al Khattabi, Fes', '0632109876', 'amina.elkandoussi@gmail.com'),
('Youssef', 'Sahli', '30 Avenue Hassan II, Agadir', '0667890123', 'youssef.sahli@gmail.com');

INSERT INTO AGENT_IMMOBILIER (Nom, Prenom, Adresse, GSM, Email)
VALUES('melvin','lombert','rue patenier 52 , Namur','','melvin-lombert@gmail.com');

insert into FAVORI (ID_Bien, ID_User, Date_d_ajout, Note)
values(1,2,'2022-11-12',5),
      (2,3,'2022-12-15',4);



insert PLAINTE (ID_User, ID_Bien, Date, Motif)
values (3,2,'2023-04-20','endroit non calme');

insert PLAINTE (id_user, id_bien, date, motif,Statut)
values (5,3,'2021-04-26','manque de repect','resolue');

-- Client to Owner --
insert into REVIEW(note, commentaire, date, review_utilisateur, RESPONSABLE_REVIEW_, id_bien)
values (4,'bruit','2023-01-01',5,3,1);

-- Client to Agent--
insert into REVIEW (Note, Commentaire, Date, REVIEW_AGENT,  RESPONSABLE_REVIEW_ , ID_Bien)
values (4,'nice work','2021-11-25', 2, 3, 1);

-- Owner to Client--
insert into REVIEW (Note, Commentaire, Date, REVIEW_UTILISATEUR,  RESPONSABLE_REVIEW_ , ID_Bien)
values (4,'nice work','2021-11-25', 3, 1, 1);


-- Owner to Agent--
insert into REVIEW(note, commentaire, date, REVIEW_AGENT, RESPONSABLE_REVIEW_, id_bien)
values (4,'bruit','2023-01-01',1,4,1);

-- Agent to Client--
insert into REVIEW (Note, Commentaire, Date, REVIEW_UTILISATEUR,  RESPONSABLE_REVIEW__1 , ID_Bien)
values (4,'nice work','2021-11-25', 2, 3, 1);

-- Agent to Owner--
insert into REVIEW (Note, Commentaire, Date, REVIEW_UTILISATEUR,  RESPONSABLE_REVIEW__1 , ID_Bien)
values (4,'nice work','2021-11-25', 4, 1, 1);

insert into CONTRAT(date_du_contrat, id_user, contrat_location, contrat_vente, id_bien)
values ('2022-12-16',3,true,false,2);

insert into CONTRAT (Date_du_contrat, ID_User, CONTRAT_LOCATION, CONTRAT_VENTE, ID_Bien)
values ('2021-10-17',3,false,true,1);

insert into CONTRAT_VENTE (id_contrat, prix_de_vente)
values (2,150000);

insert into CONTRAT_LOCATION(id_contrat, date_de_debut, date_de_fin, montant_mensuel, caution)
values (1,'2022-12-6','2023-12-6',5000,1000);


INSERT into TRANSACTION (ID_transaction,Transaction_date,Methode_de_Payement,Montant,ID_User)
VALUES(3,'2022-10-18','c','10000',4)