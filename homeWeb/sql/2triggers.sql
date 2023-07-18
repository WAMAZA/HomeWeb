use homeweb;
DELIMITER //

CREATE TRIGGER check_review BEFORE INSERT ON REVIEW FOR EACH ROW BEGIN
  IF NEW.responsable_review__1 IS NOT NULL AND NEW.review_agent IS NOT NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Agents are not allowed to leave reviews to an agent.';
  ELSEIF EXISTS (SELECT 1 FROM REVIEW WHERE NEW.responsable_review_ IN (SELECT ID_User FROM CLIENT) AND NEW.review_utilisateur IN (SELECT ID_User FROM CLIENT)) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Clients are not allowed to leave reviews to a client.';
  ELSEIF EXISTS (SELECT 1 FROM REVIEW WHERE NEW.responsable_review_ IN (SELECT ID_User FROM PROPRIETAIRE) AND NEW.review_utilisateur IN (SELECT ID_User FROM PROPRIETAIRE)) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Owners are not allowed to leave reviews to another owner.';
  END IF;
END//
DELIMITER //
CREATE TRIGGER check_plainte_responsable BEFORE INSERT ON PLAINTE
FOR EACH ROW
BEGIN
    IF EXISTS(SELECT 1 FROM PLAINTE, BIEN WHERE NEW.ID_User = BIEN.ID_User AND BIEN.ID_Bien = PLAINTE.ID_Bien) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Owner cannot make a complaint about their own properties.';
    ELSEIF EXISTS(SELECT 1 FROM PLAINTE, CONTRAT WHERE NEW.ID_User = PLAINTE.ID_User AND PLAINTE.ID_User = CONTRAT.ID_User AND contrat_location = false) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The property must be rented so that you can file a complaint to its owner.';
    END IF;
END//
DELIMITER //
CREATE TRIGGER check_contrat BEFORE INSERT ON CONTRAT
FOR EACH ROW
BEGIN
    IF EXISTS(SELECT 1 FROM CONTRAT WHERE NEW.ID_User IN (SELECT ID_User FROM BIEN WHERE BIEN.ID_User IN (SELECT ID_User FROM PROPRIETAIRE))) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The person who owns the contract property cannot be the same person who rents/buys the property.';
    END IF;
END//

-- -- Client to Client ERROR --
-- INSERT INTO REVIEW (Note, Commentaire, Date, review_utilisateur, responsable_review_, ID_Bien)
-- VALUES (5, 'mauvaise transaction', '2022-10-15', 2, 3, 2);

-- -- Owner to Owner ERROR --
-- INSERT INTO REVIEW (Note, Commentaire, Date, review_utilisateur, responsable_review_, ID_Bien)
-- VALUES (5, 'mauvaise transaction', '2022-10-15', 5, 5, 2);

-- -- Agent to Agent ERROR --
-- INSERT INTO REVIEW (Note, Commentaire, Date, review_agent, responsable_review__1, ID_Bien)
-- VALUES (4, 'nice work', '2021-11-25', 4, 1, 1);

-- -- Trigger lancé ('Owner cannot make a complaint about their own properties')
-- INSERT INTO PLAINTE(ID_User, ID_Bien, Date, Motif)
-- VALUES (4, 2, '2023-04-30', 'dar mouskha');

-- -- Trigger lancé ('The property must be rented so that you can file a complaint to its owner.')
-- INSERT INTO PLAINTE(ID_User, ID_Bien, Date, Motif)
-- VALUES (3, 1, '2022-10-11', 'khkhkhk');

-- -- Trigger lancé ('The person who owns the contract property cannot be the same person who rents/buys the property.')
-- INSERT INTO CONTRAT(Date_du_contrat, ID_User, contrat_location, contrat_vente, ID_Bien)
-- VALUES ('2022-12-11', 1, TRUE, FALSE, 1);
