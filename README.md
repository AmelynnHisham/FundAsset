# FundAsset

This project is developed using Python and Django Framework as back-end. Basic CSS, HTML5 and JavaScript, on top of Bootstrap and JQuery for front-end.

### Installation
Below are the steps to run this code:
1. Install Python
2. Create a virtual environment on your machine (either run ```mkvirtualenv [env-name]``` or ```py -m venv [env-name]```)
3. Activate the virtual environment (either run ```workon [env-name]``` or ```.\[env-name]\Scripts\activate```)
4. Change directory to **"FundAsset/AHAM/"**
5. Install the requirements.txt file using ```pip install -r requirements.txt```
6. Run server using ```python manage.py runserver```
7. Open the web application on a browser

_Please note that this project uses JSON file to store data. All graphs are for illustration purposes only._ 

### Functionalities
1. **Dashboard**: An overview of the investor's portfolio and funds
2. **My Funds**: A table displaying information of each fund. Click on a row to view fund details, transaction history or add investments
3. **Funds**: A menu showcasing other available funds
4. **Performance History**: A menu displaying the Net Asset Value (NAV) of all funds listed in **"My Funds"**
5. **All Transactions**: A menu listing all investment transactions made
