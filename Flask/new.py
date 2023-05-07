import os
import pandas
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="uwu123",
    port=3306,
    database="FastFruits"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM `Salads`")
result = mycursor.fetchall()

df = pandas.DataFrame(result, columns=['S.No', 'Salads', 'Price', 'Quantity', 'Added Date', 'Expiry Date'])

# Add a new column for the button with the cart symbol and a hidden form with fruit name and price data
df['Cart'] = '''
<form method="post" action="/add-to-cart">
    <input type="hidden" name="fruit" value="{}">
    <input type="hidden" name="price" value="{}">
    <button type="submit" class="btn btn-success"><i class="fas fa-shopping-cart"></i></button>
</form>
'''.format(df['Fruit'], df['Price'])

# Convert the dataframe to HTML, including the new column for the button and form
table_html = df.to_html(index=False, classes='table table-striped', escape=False)

# Define the HTML template
html_template = f"""
<!DOCTYPE html>
<html>
<head>
  <title>My Website</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://kit.fontawesome.com/yourkitfontawesomekey.js" crossorigin="anonymous"></script>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">
      <img src="#" height="30" alt="My Website">
    </a>
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Contact</a>
      </li>
    </ul>
  </nav>
  <div class="container-fluid mt-3">
    <form method="post" action="/checkout">
        {table_html}
        <button type="submit" class="btn btn-primary">Checkout</button>
    </form>
  </div>
</body>
</html>
"""

# Write the HTML template to a file
with open('templates/index.html', 'w') as f:
    f.write(html_template)
