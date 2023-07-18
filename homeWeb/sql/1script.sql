use homeweb;
SELECT CURRENT_USER();
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';
-- Tables Section
-- _____________

create table AGENT_IMMOBILIER (
     ID_agent int not null auto_increment,
     Nom varchar(100) not null,
     Prenom varchar(100) not null,
     Adresse VARCHAR(100) not null,
     GSM varchar(100),
     Email varchar(100),
     constraint ID_AGENT_IMMOBILIER_ID primary key (ID_agent));


create table caracterise_1 (
     ID_PIE int not null,
     ID_Bien int not null,
     constraint ID_caracterise_1_1_ID primary key (ID_PIE, ID_Bien));

create table caracterise (
     ID_PIE int not null,
     ID_Bien int not null,
     constraint ID_caracterise_1_ID primary key (ID_PIE, ID_Bien));

create table CLIENT (
     ID_User int not null,
     constraint ID_CLIEN_UTILI_ID primary key (ID_User));

create table CONTRAT (
     ID_contrat int not null auto_increment,
     Date_du_contrat varchar(100) not null,
     ID_User int not null,
     CONTRAT_LOCATION boolean,
     CONTRAT_VENTE boolean ,
     ID_Bien int not null,
     constraint ID_CONTRAT_ID primary key (ID_contrat));

create table CONTRAT_LOCATION (
     ID_contrat int not null,
     Date_de_debut date not null,
     Date_de_fin date not null,
     Montant_mensuel int not null,
     Caution int not null,
     constraint ID_CONTR_CONTR_1_ID primary key (ID_contrat));

create table CONTRAT_VENTE (
     ID_contrat int not null,
     Prix_de_vente int not null,
     constraint ID_CONTR_CONTR_ID primary key (ID_contrat));

create table dispose (
     ID_agent int not null,
     ID_User int not null,
     constraint ID_dispose_ID primary key (ID_agent, ID_User));

create table FAVORI (
     ID_Bien int not null,
     ID_User  int not null,
     Date_d_ajout date not null,
     Note int,
     constraint ID_FAVORI_ID primary key (Date_d_ajout, ID_Bien, ID_User));

create table BIEN (
     ID_Bien int not null auto_increment,
     Prix int not null,
     ID_User int not null,
     ID_Region int not null,
     TERRAIN boolean not null ,
     MAISON boolean not null ,
     APPARTEMENT boolean not null ,
     caution int default null,
     constraint ID_BIEN_ID primary key (ID_Bien));

create table TERRAIN (
     ID_Bien int not null,
     Superficie float not null,
     constraint ID_TERRA_BIEN_ID primary key (ID_Bien));

create table MAISON (
     ID_Bien int not null,
     Surface_de_terrain float not null,
     Piscine boolean not null,
     Jardin boolean not null,
     constraint ID_MAISO_BIEN_ID primary key (ID_Bien));

create table APPARTEMENT (
     ID_Bien int not null auto_increment,
     Etage varchar(100) not null,
     Ascenseur boolean not null ,
     superficie float not null,
     constraint ID_APPAR_BIEN_ID primary key (ID_Bien));

create table PIECE (
     ID_PIE int not null auto_increment,
     Surface float not null,
     Evier boolean not null,
     constraint ID_PIECE_ID primary key (ID_PIE));

create table PLAINTE (
     ID_User int not null,
     ID_Bien int not null,
     Date date not null,
     Motif varchar(100) not null,
     Statut varchar(100) not null default 'en attente',
     constraint ID_PLAINTE_ID primary key (ID_User, ID_Bien, Date));

create table PROPRIETAIRE (
     ID_User int not null,
     constraint ID_PROPR_UTILI_ID primary key (ID_User));

create table REGION (
     ID_Region int not null auto_increment,
     Pays varchar(100) not null,
     Region varchar(100) not null,
     constraint ID_REGION_ID primary key (ID_Region));

create table REVIEW (
     ID_Review int not null auto_increment,
     Note int not null,
     Commentaire varchar(100) not null,
     Date date not null,
     REVIEW_UTILISATEUR int,
     REVIEW_AGENT int,
     RESPONSABLE_REVIEW_ int,
     RESPONSABLE_REVIEW__1 int,
     ID_Bien int not null,
     constraint ID_REVIEW_ID primary key (ID_Review));

create table REVIEW_AGENT (
     ID_Review int not null,
     ID_agent int not null,
     constraint ID_REVIE_REVIE_1_ID primary key (ID_Review));

create table REVIEW_UTILISATEUR (
     ID_Review int not null,
     ID_User int not null,
     constraint ID_REVIE_REVIE_ID primary key (ID_Review));

create table TRANSACTION (
     ID_transaction int not null auto_increment,
     Transaction_date date not null,
     Methode_de_Payement char not null,
     Montant int not null,
     ID_User int not null,
     constraint ID_TRANSACTION_ID primary key (ID_transaction));

create table UTILISATEUR (
     ID_User int not null auto_increment,
     Prenom varchar(100) not null,
     Nom varchar(100) not null,
     Password varchar(100) not null,
     Adresse varchar(100) not null,
     GSM varchar(100),
     Email varchar(100),
     PROPRIETAIRE boolean not null ,
     CLIENT boolean not null ,
     ADMIN boolean not null,
     constraint ID_UTILISATEUR_ID primary key (ID_User));

create table VISITE (
     ID_Bien int not null,
     Date date not null,
     Heure varchar(100) not null,
     ID_User int not null,
     RESPONSABLE_VISITE_ int,
     RESPONSABLE_VISITE__1 int,
     constraint ID_VISITE_ID primary key (ID_Bien, Date, Heure));

create table ADMIN (
    ID_User int ,
    constraint FK_ADMIN_UTILISATEUR  primary key (ID_User));

-- Constraints Section
-- ___________________

alter table AGENT_IMMOBILIER add constraint LSTONE_AGENT_IMMOBILIER
     check(GSM is not null or Email is not null);

-- not implemented :alter table MAISON add constraint ID_MAISO_BIEN_CHK
--     check((select count(*) from caracterise_1
--            where caracterise_1.ID_Bien = MAISON.ID_Bien) > 0);


alter table APPARTEMENT add constraint ID_APPAR_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien) ;

alter table BIEN add constraint EXTONE_BIEN
     check((MAISON is true and TERRAIN is false and APPARTEMENT is false)
           or (MAISON is false and TERRAIN is true and APPARTEMENT is false)
           or (MAISON is false and TERRAIN is false and APPARTEMENT is true));

alter table BIEN add constraint REF_BIEN_PROPR_FK
     foreign key (ID_User)
     references PROPRIETAIRE(ID_User);

alter table BIEN add constraint REF_BIEN_REGIO_FK
     foreign key (ID_Region)
     references REGION(ID_Region);

alter table caracterise_1 add constraint EQU_carac_MAISO_FK
     foreign key (ID_Bien)
     references MAISON(ID_Bien);

alter table caracterise_1 add constraint REF_carac_PIECE_1
     foreign key (ID_PIE)
     references PIECE(ID_PIE);

alter table caracterise add constraint EQU_carac_APPAR_FK
     foreign key (ID_Bien)
     references APPARTEMENT(ID_Bien);

alter table caracterise add constraint REF_carac_PIECE
     foreign key (ID_PIE)
     references PIECE(ID_PIE);

alter table CLIENT add constraint ID_CLIEN_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table CONTRAT add constraint EXTONE_CONTRAT
     check((CONTRAT_VENTE is true and CONTRAT_LOCATION is false)
           or (CONTRAT_VENTE is false and CONTRAT_LOCATION is true));

alter table CONTRAT add constraint REF_CONTR_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table CONTRAT add constraint REF_CONTR_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

alter table CONTRAT_LOCATION add constraint ID_CONTR_CONTR_1_FK
     foreign key (ID_contrat)
     references CONTRAT(ID_contrat);

alter table CONTRAT_VENTE add constraint ID_CONTR_CONTR_FK
     foreign key (ID_contrat)
     references CONTRAT(ID_contrat);

alter table dispose add constraint REF_dispo_PROPR_FK
     foreign key (ID_User)
     references PROPRIETAIRE(ID_User);

alter table dispose add constraint REF_dispo_AGENT
     foreign key (ID_agent)
     references AGENT_IMMOBILIER(ID_agent);

alter table FAVORI add constraint REF_FAVOR_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table FAVORI add constraint REF_FAVOR_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

-- not implemented : alter table APPARTEMENT add constraint ID_APPAR_BIEN_CHK
--     check((select count(*) from caracterise
--                  where caracterise.ID_Bien = ID_Bien) > 0);

alter table MAISON add constraint ID_MAISO_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

alter table PLAINTE add constraint REF_PLAIN_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);


alter table PLAINTE add constraint REF_PLAIN_UTILI
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table PROPRIETAIRE add constraint ID_PROPR_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table PLAINTE add constraint CHECK_STATUT
check ( Statut in ('en attente','en cours','resolue'));

alter table REVIEW add constraint EXTONE_REVIEW_1
     check((REVIEW_AGENT is not null and REVIEW_UTILISATEUR is null)
           or (REVIEW_AGENT is null and REVIEW_UTILISATEUR is not null));

alter table REVIEW add constraint EXTONE_REVIEW
     check((RESPONSABLE_REVIEW__1 is not null and RESPONSABLE_REVIEW_ is null)
           or (RESPONSABLE_REVIEW__1 is null and RESPONSABLE_REVIEW_ is not null));

alter table REVIEW add constraint REF_REVIE_UTILI_1_FK
     foreign key (RESPONSABLE_REVIEW_)
     references UTILISATEUR(id_user);

alter table REVIEW add constraint REF_REVIE_AGENT_1_FK
     foreign key (RESPONSABLE_REVIEW__1)
     references AGENT_IMMOBILIER(ID_agent);

alter table REVIEW add constraint REF_REVIE_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

alter table REVIEW_AGENT add constraint ID_REVIE_REVIE_1_FK
     foreign key (ID_Review)
     references REVIEW(ID_Review);

alter table REVIEW_AGENT add constraint REF_REVIE_AGENT_FK
     foreign key (ID_agent)
     references AGENT_IMMOBILIER(ID_agent);

alter table REVIEW_UTILISATEUR add constraint REF_REVIE_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table REVIEW_UTILISATEUR add constraint ID_REVIE_REVIE_FK
     foreign key (ID_Review)
     references REVIEW(ID_Review);

alter table TERRAIN add constraint ID_TERRA_BIEN_FK
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

alter table TRANSACTION add constraint REF_TRANS_UTILI_FK
     foreign key (ID_User)
     references UTILISATEUR(ID_User);

alter table UTILISATEUR add constraint LSTONE_UTILISATEUR
     check(GSM is not null or Email is not null);

alter table UTILISATEUR add constraint EXTONE_UTILISATEUR
     check(( ADMIN is true and CLIENT is false and PROPRIETAIRE is false)
         or ( ADMIN is false and CLIENT is true and PROPRIETAIRE is false)
         or ( ADMIN is false and CLIENT is false and PROPRIETAIRE is true));


alter table VISITE add constraint EXTONE_VISITE
     check((RESPONSABLE_VISITE__1 is not null and RESPONSABLE_VISITE_ is null)
           or (RESPONSABLE_VISITE__1 is null and RESPONSABLE_VISITE_ is not null));

alter table VISITE add constraint REF_VISIT_CLIEN_FK
     foreign key (ID_User)
     references CLIENT(ID_User);

alter table VISITE add constraint REF_VISIT_PROPR_FK
     foreign key (RESPONSABLE_VISITE_)
     references PROPRIETAIRE(ID_User);

alter table VISITE add constraint REF_VISIT_AGENT_FK
     foreign key (RESPONSABLE_VISITE__1)
     references AGENT_IMMOBILIER(ID_agent);

alter table VISITE add constraint REF_VISIT_BIEN
     foreign key (ID_Bien)
     references BIEN(ID_Bien);

ALTER TABLE ADMIN
ADD CONSTRAINT FK_ADMIN_UTILISATEUR
FOREIGN KEY (ID_User)
REFERENCES UTILISATEUR(ID_User);


-- Index Section
-- _____________

create unique index ID_AGENT_IMMOBILIER_IND
     on AGENT_IMMOBILIER (ID_agent);

create unique index ID_APPAR_BIEN_IND
     on APPARTEMENT (ID_Bien);

create unique index ID_BIEN_IND
     on BIEN (ID_Bien);

create index REF_BIEN_PROPR_IND
     on BIEN (ID_User);

create index REF_BIEN_REGIO_IND
     on BIEN (ID_Region);

create unique index ID_caracterise_1_1_IND
     on caracterise_1 (ID_PIE, ID_Bien);

create index EQU_carac_MAISO_IND
     on caracterise_1 (ID_Bien);

create unique index ID_caracterise_1_IND
     on caracterise (ID_PIE, ID_Bien);

create index EQU_carac_APPAR_IND
     on caracterise (ID_Bien);

create unique index ID_CLIEN_UTILI_IND
     on CLIENT (ID_User);

create unique index ID_CONTRAT_IND
     on CONTRAT (ID_contrat);

create index REF_CONTR_UTILI_IND
     on CONTRAT (ID_User);

create index REF_CONTR_BIEN_IND
     on CONTRAT (ID_Bien);

create unique index ID_CONTR_CONTR_1_IND
     on CONTRAT_LOCATION (ID_contrat);

create unique index ID_CONTR_CONTR_IND
     on CONTRAT_VENTE (ID_contrat);

create unique index ID_dispose_IND
     on dispose (ID_agent, ID_User);

create index REF_dispo_PROPR_IND
     on dispose (ID_User);

create unique index ID_FAVORI_IND
     on FAVORI (Date_d_ajout, ID_Bien, ID_User);

create index REF_FAVOR_UTILI_IND
     on FAVORI (ID_User);

create index REF_FAVOR_BIEN_IND
     on FAVORI (ID_Bien);

create unique index ID_MAISO_BIEN_IND
     on MAISON (ID_Bien);

create unique index ID_PIECE_IND
     on PIECE (ID_PIE);

create unique index ID_PLAINTE_IND
     on PLAINTE (ID_User, ID_Bien, Date);

create index REF_PLAIN_BIEN_IND
     on PLAINTE (ID_Bien);

create unique index ID_PROPR_UTILI_IND
     on PROPRIETAIRE (ID_User);

create unique index ID_REGION_IND
     on REGION (ID_Region);

create unique index ID_REVIEW_IND
     on REVIEW (ID_Review);

create index REF_REVIE_UTILI_1_IND
     on REVIEW (RESPONSABLE_REVIEW_);

create index REF_REVIE_AGENT_1_IND
     on REVIEW (RESPONSABLE_REVIEW__1);

create index REF_REVIE_BIEN_IND
     on REVIEW (ID_Bien);

create unique index ID_REVIE_REVIE_1_IND
     on REVIEW_AGENT (ID_Review);

create index REF_REVIE_AGENT_IND
     on REVIEW_AGENT (ID_agent);

create index REF_REVIE_UTILI_IND
     on REVIEW_UTILISATEUR (ID_User);

create unique index ID_REVIE_REVIE_IND
     on REVIEW_UTILISATEUR (ID_Review);

create unique index ID_TERRA_BIEN_IND
     on TERRAIN (ID_Bien);

create unique index ID_TRANSACTION_IND
     on TRANSACTION (ID_transaction);

create index REF_TRANS_UTILI_IND
     on TRANSACTION (ID_User);

create unique index ID_UTILISATEUR_IND
     on UTILISATEUR (ID_User);

create unique index ID_VISITE_IND
     on VISITE (ID_Bien, Date, Heure);

create index REF_VISIT_CLIEN_IND
     on VISITE (ID_User);

create index REF_VISIT_PROPR_IND
     on VISITE (RESPONSABLE_VISITE_);

create index REF_VISIT_AGENT_IND
     on VISITE (RESPONSABLE_VISITE__1);

create unique index ID_ADMIN_UTILI_IND
     on ADMIN (ID_User);



