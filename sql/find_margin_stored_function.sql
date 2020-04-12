DELIMITER $$
drop function if exists margin_func$$
CREATE FUNCTION margin_func(
    price DECIMAL(7,3),
    payment_cost DECIMAL(7,3)
)
RETURNS DECIMAL(7,3)
DETERMINISTIC
BEGIN
    DECLARE margin DECIMAL(7,3);

    SET margin = (price - payment_cost) / price;

    -- return the margin
    RETURN (margin);
END$$
DELIMITER ;