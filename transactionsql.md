# CONFLICTING AND NON-CONFLICTING TRANSACTIONS

## CONFLICTING TRANSACTION QUERIES

### Query 1A:
```python
UPDATE `Salad` SET `price` = `price` * 1.1 WHERE `name` = 'Caesar Salad';
```
### Query 1B:
```python
DELETE FROM `Salad` WHERE `name` = 'Caesar Salad';
```
These queries conflict because one is trying to update the price of a specific salad while the other is trying to delete that same salad. If both queries are executed simultaneously, they may cause unpredictable behaviour.

Solution: You can use locks to ensure that both queries don't conflict.
```python
START TRANSACTION;
LOCK TABLES `Salad` WRITE;

UPDATE `Salad` SET `price` = `price` * 1.1 WHERE `name` = 'Caesar Salad';

UNLOCK TABLES;
COMMIT;

START TRANSACTION;
LOCK TABLES `Salad` WRITE;

DELETE FROM `Salad` WHERE `name` = 'Caesar Salad';

UNLOCK TABLES;
COMMIT;
```
### Query 2A:
```python
INSERT INTO `Smoothies` (`name`, `price`, `quantity`, `addedDate`, `expiryDate`)
VALUES ('Strawberry Smoothie', 5, 10, '2023-04-22', '2023-04-29');
```
### Query 2B:
```
UPDATE `Smoothies` SET `price` = `price` - 1 WHERE `name` = 'Strawberry Smoothie';
```
These queries conflict because one is trying to insert a new smoothie record while the other is trying to update the price of the same smoothie. If both queries are executed simultaneously, it might cause unpredictable behaviour or update failures.

Solution: You can use locks to ensure that both queries don't conflict.
```python
START TRANSACTION;
LOCK TABLES `Smoothies` WRITE;

INSERT INTO `Smoothies` (`name`, `price`, `quantity`, `addedDate`, `expiryDate`)
VALUES ('Strawberry Smoothie', 5, 10, '2023-04-22', '2023-04-29');

UNLOCK TABLES;
COMMIT;

START TRANSACTION;
LOCK TABLES `Smoothies` WRITE;

UPDATE `Smoothies` SET `price` = `price` - 1 WHERE `name` = 'Strawberry Smoothie';

UNLOCK TABLES;
COMMIT;
```
By locking the tables for writing and using transactions, we ensure that these queries are executed sequentially, preventing conflicts and maintaining data integrity.

## NON-CONFLICTING TRANSACTION QUERIES

### Query 1A:
```python
START TRANSACTION;

INSERT INTO `Salad` (`name`, `price`, `quantity`, `addedDate`, `expiryDate`)
VALUES ('Greek Salad', 8, 12, '2023-04-22', '2023-04-29');

COMMIT;
```
### Query 1B:
```python
START TRANSACTION;

SELECT `name`, `price` FROM `Salad` WHERE `expiryDate` >= '2023-04-29';

COMMIT;
```
These queries are not conflicting because one is inserting a new salad record, while the other is reading data from the table without modifying it. Both queries can be executed simultaneously without causing any data integrity issues.

### Query 2A:
```python
START TRANSACTION;

UPDATE `Smoothies` SET `quantity` = `quantity` - 1 WHERE `name` = 'Mango Smoothie';

COMMIT;
```
### Query 2B:
```python
START TRANSACTION;

SELECT `name`, `quantity` FROM `Smoothies` WHERE `price` >= 5;

COMMIT;
```
These queries are not conflicting because one is updating the quantity of a specific smoothie, while the other is reading data from the table without modifying it. Both queries can be executed simultaneously without causing any data integrity issues.

### Query 3A:
```python
START TRANSACTION;

INSERT INTO `Fruits` (`name`, `price`, `quantity`, `addedDate`, `expiryDate`)
VALUES ('Blueberries', 5, 20, '2023-04-22', '2023-04-30');

COMMIT;
```
### Query 3B:
```python
START TRANSACTION;

SELECT `name`, `quantity` FROM `Fruits` WHERE `expiryDate` < '2023-04-29';

COMMIT;
```
These queries are not conflicting because one is inserting a new fruit record, while the other is reading data from the table without modifying it. Both queries can be executed simultaneously without causing any data integrity issues.

### Query 4A:
```python
START TRANSACTION;

UPDATE `Fruits` SET `price` = `price` * 0.9 WHERE `quantity` > 10;

COMMIT;
```
### Query 4B:
```python
START TRANSACTION;

SELECT `name`, `price` FROM `Fruits` WHERE `expiryDate` >= '2023-04-29';

COMMIT;
```
These queries are not conflicting because one is updating the prices of specific fruits, while the other is reading data from the table without modifying it. Both queries can be executed simultaneously without causing any data integrity issues.

# SERIALIZABLE SCHEDULES

## TRANSACTION 1
```python
START TRANSACTION;

INSERT INTO Salad (name, price, quantity, addedDate, expiryDate)
VALUES ('Caesar Salad', 8, 20, '2023-04-22', '2023-04-30');

COMMIT;
```
## TRANSACTION 2
```python
START TRANSACTION;

UPDATE Salad
SET quantity = 10, expiryDate = '2023-05-05'
WHERE slID = 1;

COMMIT;
```
## CONFLICT SERIALIZABLE SCHEDULE

| T1                 | T2                 |
|--------------------|--------------------|
| START TRANSACTION; |                    |
| INSERT INTO Salad  |                    |
| COMMIT;            |                    |
|                    | START TRANSACTION; |
|                    | UPDATE Salad       |
|                    | COMMIT;            |


The above schedule is already conflict serializable, as there is no overlapping of read/write or write/write operations on the same data item.

## NON-CONFLICT SERIALIZABLE SCHEDULE

| T1                 | T2                 |
|--------------------|--------------------|
| START TRANSACTION; |                    |
| INSERT INTO Salad  |                    |
|                    | START TRANSACTION; |
|                    | UPDATE Salad       | 
| COMMIT;            |                    |
|                    | COMMIT;            |

In this schedule, the insert operation of T1 is performed first, followed by the update operation of T2, and then both transactions are committed. This schedule is non-conflict serializable because the operations of T1 and T2 are not conflicting with each other, since they are accessing different data items. However, this schedule may produce different intermediate results compared to the original schedule, because the update operation of T2 is performed before the commit operation of T1, which means that the data may be visible to other transactions before T1 commits. 
