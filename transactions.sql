-- Non Conflicting
START TRANSACTION;
UPDATE `Fruits` SET quantity = quantity - 50 WHERE fID = 1;
COMMIT;

START TRANSACTION;
INSERT INTO `Fruits` (name, price, quantity, addedDate, expiryDate) VALUES ('sushi', 400, 72, 2019-09-12, 2019-09-12), ('mizu', 100, 34, 2019-09-12, 2019-09-12);
COMMIT;

START TRANSACTION;
UPDATE `Fruits` SET price = price * 1.05 WHERE fID != 0;
COMMIT;

START TRANSACTION;
INSERT INTO `Customers` (first_name, email, phone, street) VALUES ('John Doe', 'johndoe@example.com', 1234567890,'123 Main St.');
COMMIT;

-- Conflicting
-- WRITE-WRITE
START TRANSACTION;
UPDATE `Fruits` SET quantity = quantity - 1 WHERE fID = 1;
COMMIT;

START TRANSACTION;
UPDATE `Fruits` SET quantity = quantity - 1 WHERE fID = 1;
COMMIT;
-- WRITE-READ
START TRANSACTION;
-- let this be out of stock
SELECT * FROM `Fruits` WHERE fID = 15 FOR UPDATE;
COMMIT;

START TRANSACTION;
UPDATE `Fruits` SET quantity = quantity - 1 WHERE fID = 15;
COMMIT;


