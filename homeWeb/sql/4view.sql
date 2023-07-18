CREATE VIEW BIENS_INFO AS
SELECT
    b.ID_Bien,
    b.Prix,
    r.Region,
    CASE
        WHEN b.TERRAIN = 1 THEN 'Terrain'
        WHEN b.MAISON = 1 THEN 'Maison'
        ELSE 'Appartement'
    END AS Type,
    CASE
        WHEN b.TERRAIN = 1 THEN t.Superficie
        WHEN b.MAISON = 1 THEN m.Surface_de_terrain
        ELSE a.Superficie
    END AS Superficie,
    CASE
        WHEN b.MAISON = 1 THEN m.Piscine
    END AS Piscine,
    CASE
        WHEN b.MAISON = 1 THEN m.Jardin
    END AS Jardin,
    CASE
        WHEN b.APPARTEMENT = 1 THEN a.Ascenseur
    END AS Ascenseur,
    u.ID_User AS ID_Proprietaire,
    u.Nom AS Nom_Proprietaire
FROM
    BIEN b
    INNER JOIN REGION r ON b.ID_Region = r.ID_Region
    LEFT JOIN TERRAIN t ON b.ID_Bien = t.ID_Bien
    LEFT JOIN MAISON m ON b.ID_Bien = m.ID_Bien
    LEFT JOIN APPARTEMENT a ON b.ID_Bien = a.ID_Bien
    LEFT JOIN UTILISATEUR u ON b.ID_User = u.ID_User
GROUP BY
    u.nom, b.ID_Bien, b.Prix, r.Region, u.ID_User;

CREATE VIEW VISITE_INFO AS
SELECT
    V.ID_Bien,
    U.Nom AS NomClient,
    (SELECT Adresse FROM UTILISATEUR WHERE ID_User = V.ID_User) AS RegionVisite,
    (SELECT CONCAT(Nom, ' ', Prenom) FROM UTILISATEUR WHERE UTILISATEUR.ID_User = V.RESPONSABLE_VISITE_) AS Responsable_proprietaire,
    (SELECT CONCAT(Nom, ' ', Prenom) FROM AGENT_IMMOBILIER WHERE ID_agent = V.RESPONSABLE_VISITE__1) AS Responsable_agent_immobiliers,
    B.ID_User,
    (SELECT Nom FROM UTILISATEUR WHERE ID_User = B.ID_User) AS nom_du_proprietaire
FROM
    VISITE V
    LEFT JOIN BIEN B ON V.ID_Bien = B.ID_Bien
    LEFT JOIN UTILISATEUR U ON V.ID_User = U.ID_User;

CREATE VIEW LOCATAIRE_INFO AS
SELECT cl.ID_contrat, U.Nom, U.Prenom, b.id_bien, c.Date_du_contrat, cl.Date_de_fin, ROUND((DATEDIFF(cl.Date_de_fin, CURDATE()) / 30)) AS duree_restante,SUM(ROUND((DATEDIFF(cl.Date_de_fin, CURDATE()) / 30)) * cl.Montant_mensuel) AS montant_restant
FROM CONTRAT c, CONTRAT_LOCATION cl, BIEN b, UTILISATEUR U
where c.ID_contrat = cl.ID_contrat and c.id_bien = b.id_bien and U.ID_User = c.ID_User
GROUP BY U.Nom, c.ID_contrat, b.id_bien;