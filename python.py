import random
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
a = "INSERT INTO `Orders` VALUES (1,71,45,'1981-04-02','1978-07-22',4796,'quia'),(2,12,29,'1979-01-20','2020-12-28',29830,'dolore'),(3,3,84,'1994-06-03','2020-01-01',4812,'aut'),(4,45,54,'2014-06-11','1981-11-20',4766,'ut'),(5,97,96,'1971-03-15','2013-05-21',3323,'dolores'),(6,52,89,'2016-05-30','1970-12-21',3265,'dolorem'),(7,49,87,'1996-03-27','2016-10-30',1642,'consectetur'),(8,47,54,'1979-02-24','1992-10-21',3658,'nostrum'),(9,5,83,'1990-10-06','2005-01-01',4741,'totam'),(10,2,14,'1996-03-06','2015-12-26',2033648,'error'),(11,87,77,'2005-08-23','1995-03-24',54557,'consequatur'),(12,26,36,'2020-12-22','1977-04-15',3682,'ducimus'),(13,18,3,'2015-08-05','1975-10-11',96578,'aperiam'),(14,48,34,'1982-07-06','2007-03-30',2522,'laborum'),(15,70,27,'2014-10-25','2012-08-28',2586309,'sed'),(16,94,74,'2000-03-26','2014-04-11',34767185,'corrupti'),(17,77,1,'2005-03-24','2022-06-17',3625,'beatae'),(18,78,89,'2021-09-04','2012-10-31',103598612,'rerum'),(19,54,19,'2017-11-16','2004-03-10',19068,'dolor'),(20,21,4,'2004-08-13','2005-03-28',2150,'quia'),(21,73,85,'2011-07-25','2014-11-05',284710,'voluptas'),(22,82,61,'2009-11-28','2016-05-01',426535138,'sint'),(23,58,52,'1996-05-05','2005-10-16',4016,'omnis'),(24,7,4,'2017-06-22','1992-07-03',4632,'nemo'),(25,30,6,'1980-05-06','2017-11-27',12071,'corrupti'),(26,40,96,'1979-04-08','2002-08-10',806423346,'est'),(27,61,77,'2015-10-17','1976-11-13',4425,'dolores'),(28,75,60,'1992-11-11','2021-02-03',5710,'a'),(29,1,84,'2013-10-01','2021-11-24',90638476,'velit'),(30,76,29,'1984-12-14','1999-06-06',8949791,'amet'),(31,60,65,'1973-04-03','1994-10-21',52381481,'sit'),(32,50,1,'1993-09-08','2009-01-21',420454,'qui'),(33,66,42,'2011-05-28','1971-12-10',18418370,'est'),(34,83,71,'1982-05-02','1985-11-01',5520,'quaerat'),(35,99,50,'2009-06-11','1973-05-28',3326801,'adipisci'),(36,34,98,'2003-12-20','1975-03-02',1895,'totam'),(37,74,40,'2020-05-06','2016-06-20',78909224,'suscipit'),(38,42,58,'1986-05-23','2022-09-29',5802,'exercitationem'),(39,15,54,'1982-02-21','2018-09-06',571818389,'incidunt'),(40,65,28,'1994-12-23','2018-10-22',2783,'in'),(41,43,24,'1973-07-18','1986-11-29',556395,'natus'),(42,93,100,'2008-02-28','1974-12-27',42101953,'ducimus'),(43,28,83,'1980-05-19','2005-04-13',4572423,'non'),(44,69,98,'2021-06-22','1991-02-28',23025,'eum'),(45,39,28,'2009-12-19','1988-12-24',7499,'fugiat'),(46,24,49,'2000-10-15','2002-05-08',34809,'ut'),(47,84,4,'1974-10-11','2010-11-25',1046349,'laborum'),(48,53,76,'2002-10-27','1989-04-27',597,'eaque'),(49,20,88,'1973-07-23','2004-09-01',2113,'voluptatum'),(50,16,7,'1981-02-21','1979-11-09',262620,'non'),(51,31,76,'1979-10-26','2021-05-26',29994533,'voluptatem'),(52,51,54,'2019-05-11','2012-04-24',3728,'amet'),(53,91,14,'1986-11-30','1974-02-06',41980,'et'),(54,56,77,'1980-05-08','1992-04-08',4726,'non'),(55,67,76,'1998-04-07','1992-05-11',2216,'non'),(56,63,100,'1985-07-19','2004-06-22',3224,'ipsam'),(57,13,1,'1986-02-13','2008-12-05',382400,'placeat'),(58,38,100,'1974-08-29','2008-12-23',781926,'officia'),(59,8,74,'1976-05-05','1990-01-10',181512,'voluptatem'),(60,19,71,'1991-03-29','2015-09-24',852450,'distinctio'),(61,88,32,'2002-08-15','1991-02-11',1737,'at'),(62,64,96,'1979-02-03','2018-03-26',53541517,'sit'),(63,27,74,'1988-10-24','2017-09-08',21157,'quibusdam'),(64,32,75,'2020-01-30','1989-07-14',5514,'nisi'),(65,81,41,'1978-05-12','1983-02-24',61821,'maxime'),(66,36,35,'1979-05-17','2016-04-14',4065,'ex'),(67,35,47,'1989-01-15','1979-04-17',289372,'voluptas'),(68,57,54,'2015-04-04','2003-12-19',1702419,'amet'),(69,41,17,'2006-12-10','1992-09-17',17010250,'voluptas'),(70,95,37,'1993-07-15','1992-10-19',32464606,'quod'),(71,23,55,'2006-06-21','2022-06-02',1951,'et'),(72,62,33,'2020-01-08','1979-04-07',43234918,'eum'),(73,10,95,'2010-07-22','1994-10-03',36810,'ex'),(74,29,37,'2019-07-12','1986-05-09',5500,'facilis'),(75,98,56,'2008-08-01','2019-09-09',59429,'mollitia'),(76,46,31,'2018-02-09','2001-07-12',1610294,'consequatur'),(77,89,35,'1986-06-23','1982-09-19',2591,'aliquid'),(78,80,79,'1976-08-30','2002-11-04',4056,'et'),(79,86,35,'1998-04-02','2011-08-29',150432,'et'),(80,100,84,'1975-03-06','2013-07-05',3129,'quis'),(81,85,60,'2022-04-28','1990-05-28',315706,'vitae'),(82,17,85,'2018-06-16','1987-05-20',3851,'eos'),(83,33,45,'1971-10-17','1986-04-07',11856,'saepe'),(84,37,59,'2015-02-04','1972-02-18',4026,'eveniet'),(85,22,92,'1980-02-07','1987-05-08',5398,'et'),(86,4,42,'2020-01-09','2014-08-05',5529,'delectus'),(87,79,26,'2021-08-31','2002-05-03',469963,'dolorem'),(88,68,10,'2010-07-17','1988-07-27',2876,'hic'),(89,96,75,'2012-05-01','2011-02-15',4842,'repellat'),(90,44,84,'2001-11-11','2004-04-29',4187,'ut'),(91,92,6,'1984-09-26','2022-02-03',14252,'modi'),(92,90,24,'1986-11-10','1981-08-26',1438,'a'),(93,55,94,'2005-06-19','1982-02-26',393584,'debitis'),(94,59,96,'2021-11-18','1979-10-24',2233,'eum'),(95,11,57,'1986-06-01','2013-05-29',7800,'veniam'),(96,9,81,'2001-11-08','1994-09-08',7043,'vero'),(97,25,73,'2018-11-06','2010-09-09',242537,'nemo'),(98,6,26,'1978-08-02','2006-11-29',1324,'sed'),(99,14,34,'2021-03-01','1998-08-13',4915,'et'),(100,72,82,'2013-11-11','2005-03-11',2664,'illo');"
l = a.split(",")
fruits = ["Apple", "Banana", "Cherry", "Blueberry", "Grape", "Raspberry", "Strawberry", "Blackberry", "Peach", "Plum", "Mango", "Papaya", "Watermelon", "Cantaloupe", "Kiwi", "Honeydew", "Apricot", "Grapefruit", "Lemon", "Lime", "Orange", "Tangerine", "Pineapple", "Coconut", "Avocado", "Guava", "Pomegranate", "Stark-fruit", "Dragon-fruit", "Jackfruit", "Durian", "Breadfruit", "Loquat", "Star-apple", "Passion-fruit", "Fig", "Date", "Raisin", "Currant", "Gooseberry", "Black-currant", "Redcurrant", "Cranberry", "Bilberry", "Lingonberry", "Elderberry", "Barberry", "Goji-berry", "Boysenberry", "Olive", "Cherry-tomato", "Tomato", "Green-pepper", "Red-pepper", "Yellow-pepper", "Bell-pepper", "Habanero-pepper", "Jalapeno-pepper", "Poblano-pepper", "Chipotle-pepper", "Pumpkin", "Butternut-squash", "Zucchini", "Yellow-squash", "Acorn-squash", "Spaghetti-squash", "Delicata-squash", "Kabocha-squash", "Cucumber", "Eggplant", "Lettuce", "Arugula", "Spinach", "Kale", "Chard", "Mustard-greens", "Beet-greens", "Collard-greens", "Turnip-greens", "Bok-choy", "Radicchio", "Endive", "Escarole", "Frisee", "Radish", "Carrot", "Turnip", "Rutabaga", "Parsnip", "Sweet-potato", "Yam", "Potato", "Garlic", "Onion", "Shallot", "Leek", "Chive", "Scallion", "Fennel", "Parsley", "Cilantro", "Basil", "Thyme", "Oregano", "Rosemary", "Mint", "Lavender"]
gender = ["male", "female", "other", "prefer not to say"]
smoothies = ["Strawberry Banana", "Mango Madness", "Peach Perfection", "Tropical Twist", "Green Goddess", "Berry Blast", "Citrus Sensation", "Apple Pie", "Pineapple Paradise", "Coconut Craze", "Raspberry Ripple", "Banana Split", "Carrot Crush", "Orange Julius", "Papaya Punch", "Blueberry Bash", "Strawberry Shortcake", "Mango Tango", "Peach Fuzz", "Tropical Treat", "Green Machine", "Berry Burst", "Citrus Cooler", "Apple Cider", "Pineapple Power", "Coconut Cream", "Raspberry Rhapsody", "Banana Boat", "Carrot Dream", "Orange Oasis", "Papaya Passion", "Blueberry Bites", "Strawberry Swirl", "Mango Magic", "Peach Perfect", "Tropical Temptation", "Green Gourmet", "Berry Bliss", "Citrus Crush", "Apple Ambrosia", "Pineapple Punch", "Coconut Crush", "Raspberry Rush", "Banana Boogie", "Carrot Craze", "Orange Overload", "Papaya Puree", "Blueberry Blastoff", "Strawberry Sensation", "Mango Marvel", "Peach Pleasure", "Tropical Tornado", "Green Galaxy", "Berry Boost", "Citrus Craze", "Apple Aromatics", "Pineapple Paradise", "Coconut Cool", "Raspberry Rainbow", "Banana Bliss", "Carrot Coconut", "Orange Oasis", "Papaya Paradise", "Blueberry Bliss", "Strawberry Sorbet", "Mango Mingle", "Peach Pizzazz", "Tropical Thrill", "Green Goodness", "Berry Bites", "Citrus Chill", "Apple Adventure", "Pineapple Punch", "Coconut Crush", "Raspberry Refresher", "Banana Beats", "Carrot Charisma", "Orange Orchard", "Papaya Pure", "Blueberry Burst", 'Green Energy', 'Tropical Sunset', 'Berry Blast', 'Mango Madness', 'Peach Paradise', 'Strawberry Sensation', 'Pineapple Punch', 'Citrus Crush', 'Banana Bliss', 'Coconut Craze', 'Blackberry Boost', 'Kiwi Kick', 'Raspberry Ripple', 'Apple Adrenaline', 'Pomegranate Power', 'Lemon Lift', 'Watermelon Wow', 'Blueberry Boost', 'Grape Glee', 'Cherry Charge']
salad = [
'Greek Salad',
'Caesar Salad',
'Tomato and Mozzarella Salad',
'Taco Salad',
'Spinach Salad',
'Wedge Salad',
'Cobb Salad',
'Nicoise Salad',
'Beet Salad',
'Quinoa Salad',
'Kale Salad',
'Broccoli Salad',
'Pear and Blue Cheese Salad',
'Arugula Salad',
'Apple and Walnut Salad',
'Roasted Carrot Salad',
'Cucumber Salad',
'Pesto Pasta Salad',
'Strawberry Salad',
'Caprese Salad',
'Fruit Salad',
'Southwestern Salad',
'Chopped Salad',
'Potato Salad',
'Rainbow Salad',
'Watermelon Salad',
'Coleslaw',
'Balsamic Salad',
'Roasted Beet Salad',
'Crab Salad',
'Shrimp Salad',
'Tuna Salad',
'Chicken Salad',
'Egg Salad',
'Greek Pasta Salad',
'Feta Salad',
'Zucchini Salad',
'Mango Salad',
'Cherry Salad',
'Pecan Salad',
'Avocado Salad',
'Lemon Salad',
'Peach Salad',
'Cantaloupe Salad',
'Raspberry Salad',
'Honeydew Salad',
'Papaya Salad',
'Plum Salad',
'Blueberry Salad',
'Strawberry and Spinach Salad',
'Blackberry Salad',
'Raisin Salad',
'Grape Salad',
'Mandarin Orange Salad',
'Pineapple Salad',
'Cranberry Salad',
'Coconut Salad',
'Banana Salad',
'Melon Salad',
'Peanut Salad',
'Almond Salad',
'Walnut Salad',
'Pumpkin Seed Salad',
'Sunflower Seed Salad',
'Hazelnut Salad',
'Cashew Salad',
'Pecan and Apple Salad',
'Macadamia Salad',
'Peanut and Grape Salad',
'Almond and Cherry Salad',
'Walnut and Raspberry Salad',
'Pumpkin Seed and Mango Salad',
'Sunflower Seed and Peach Salad',
'Hazelnut and Plum Salad',
'Cashew and Papaya Salad',
'Pecan and Pineapple Salad',
'Macadamia and Cantaloupe Salad', "Tomato Cucumber Salad", "Fruit Salad", "Spinach Berry Salad", "Greek Salad", "Roasted Vegetable Salad", "Caprese Salad", "Carrot Raisin Salad", "Quinoa Salad", "Potato Salad", "Coleslaw", "Pasta Salad", "Lentil Salad", "Watermelon Feta Salad", "Avocado Salad", "Cobb Salad", "Fennel Salad", "Kale Salad", "Orzo Salad", "Mixed Greens Salad", "Artichoke Salad", "Beet Salad", "Chickpea Salad", "Raspberry Salad"]
status = ['shipped', 'delivered', 'returned', 'cancelled', 'pending']
print(len(salad))
j = 0
for i in range(6, len(l), 7):
    l[i] = "'"+random.choice(status)+"')"
m = ', '.join(l)
print(m)