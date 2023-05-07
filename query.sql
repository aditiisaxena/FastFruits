USE `FastFruits`;

-- Triggers

DELIMITER $$
DROP TRIGGER IF EXISTS check_order_amount $$
CREATE TRIGGER check_order_amount 
BEFORE INSERT ON `Orders`
FOR EACH ROW
BEGIN
    IF NEW.amount < 100 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Order amount cannot be less than 100.';
    END IF;
END $$
DELIMITER ;

DELIMITER $$
DROP TRIGGER IF EXISTS `check_fruit_exists` $$
CREATE TRIGGER `check_fruit_exists`
BEFORE INSERT ON `Smoothies_Ingredients`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `Fruits` WHERE `fID` = NEW.`fID`) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Fruit with fID ';
    END IF;
END$$
DELIMITER ;

-- Embedded

SELECT first_name, last_name, (SELECT COUNT(*) FROM `Orders` WHERE cID = Customers.cID) AS NumOrders
FROM Customers;

SELECT *
FROM `Salad`
WHERE slID IN (SELECT slID FROM `Cart` GROUP BY slID HAVING COUNT(*) > 2);

-- OLAP

SELECT cID, dID, SUM(amount) as total
FROM `Orders`
GROUP BY cID, dID WITH ROLLUP;

SELECT SUM(price) as total_smoothies
FROM Fruits
WHERE addedDate >= '2022-01-01' AND addedDate <= '2022-03-31';

SELECT supID,
       SUM(CASE WHEN states = 'California' THEN dues ELSE 0 END) AS CA_dues,
       SUM(CASE WHEN states = 'Calfornia' THEN listing_fee ELSE 0 END) AS CA_listing_fee,
       SUM(CASE WHEN states = 'NewYork' THEN dues ELSE 0 END) AS NY_dues,
       SUM(CASE WHEN states = 'NewYork' THEN listing_fee ELSE 0 END) AS NY_listing_fee,
       SUM(CASE WHEN states = 'Nevada' THEN dues ELSE 0 END) AS TX_dues,
       SUM(CASE WHEN states = 'Nevada' THEN listing_fee ELSE 0 END) AS TX_listing_fee
FROM Suppliers
GROUP BY supID;

SELECT DATE_FORMAT(orderDate, '%Y-%m-%d') AS day, status, SUM(amount) AS total_sales
FROM Orders
GROUP BY day, status;