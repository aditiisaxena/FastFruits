USE FastFruits;
-- 1. top 10 orders that had the highest amount
SELECT c.first_name, c.last_name, o.amount, o.orderDate
FROM Customers c
JOIN Orders o ON c.cID = o.cID
GROUP BY c.cID, c.first_name, c.last_name, o.oID, o.amount, o.orderDate
ORDER BY o.amount DESC
LIMIT 10;
-- 2. customers who have subscribed to all three ie raw fruits, smoothies and salads
SELECT c.cID, c.first_name, c.last_name
FROM Customers c
JOIN subscription s ON c.cID = s.cID
WHERE s.rID = 1 AND s.smID = 1 AND s.slID = 1
GROUP BY c.cID, c.first_name, c.last_name;
-- 3. Last 10 purchases
SELECT c.first_name, c.last_name, o.amount, o.orderDate
FROM Customers c
JOIN Orders o ON c.cID = o.cID
GROUP BY c.cID, c.first_name, c.last_name, o.oID, o.amount, o.orderDate
ORDER BY o.orderDate DESC
LIMIT 10;
-- 4. names and prices of all fruits in the store, as well as the names and prices of all smoothies that contain those fruits as ingredients.
SELECT DISTINCT Fruits.name AS fruit_name, Fruits.price AS fruit_price, Smoothies.name AS smoothie_name, Smoothies.price AS smoothie_price
FROM Fruits
JOIN Smoothies_Ingredients ON Fruits.fID = Smoothies_Ingredients.fID
JOIN Smoothies ON Smoothies_Ingredients.smID = Smoothies.smID
ORDER BY Fruits.name, Smoothies.name;
-- 5. 50 fruits that are nearing expiry
SELECT f.fID, f.name, f.expiryDate
FROM Fruits f
ORDER BY f.expiryDate DESC
LIMIT 50;
-- 6. Union of prices in ascending order with fruits closing to expiry date
SELECT name, price, expiryDate
FROM fruits
WHERE expiryDate < DATE_ADD(NOW(), INTERVAL 7 YEAR)
UNION
SELECT name, price, expiryDate
FROM fruits
ORDER BY price ASC;
-- 7. intersection of customers with the amount they've paid
SELECT c.first_name, o.oID, o.orderDate, o.amount
FROM customers AS c
INNER JOIN orders AS o ON c.cID = o.cID
ORDER BY o.orderDate DESC;
-- 8. product for customers and their respective orders
SELECT *
FROM customers
CROSS JOIN orders;
-- 9. name and price of all fruits that are not used as ingredients in any smoothies.
SELECT Fruits.name, Fruits.price
FROM Fruits
LEFT JOIN Smoothies_Ingredients ON Fruits.fID = Smoothies_Ingredients.fID
WHERE Smoothies_Ingredients.fID IS NULL;
-- 10. Retrieve the smoothies that contain all fruits of the salad named "Hazelnut and Plum Salad"
SELECT sm.name 
FROM Smoothies sm 
WHERE NOT EXISTS 
(SELECT f.fID FROM Fruits f WHERE f.name IN 
(SELECT f2.name FROM Salad s 
JOIN Fruits f2 ON s.slID = f2.fID 
WHERE s.name = 'Hazelnut and Plum Salad') 
AND NOT EXISTS 
(SELECT si.fID FROM Smoothies_Ingredients si 
WHERE si.smID = sm.smID AND si.fID = f.fID));






