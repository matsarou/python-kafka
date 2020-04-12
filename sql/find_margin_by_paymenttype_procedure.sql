DELIMITER $$
DROP PROCEDURE if exists margin_by_payment_type_procedure$$
CREATE PROCEDURE margin_by_payment_type_procedure (IN FROM_DATETIME varchar(25), IN TO_DATETIME VARCHAR(25))
BEGIN
	INSERT INTO Margin_info
    SELECT
        'payment_type',payment_type,FROM_DATETIME,TO_DATETIME,SUM(margin_func(price, payment_cost))
    FROM Classifieds
    WHERE created_at BETWEEN FROM_DATETIME AND TO_DATETIME
    GROUP BY payment_type;
END$$
DELIMITER ;
