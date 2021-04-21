# GUI-File-Login-System

This Python program is an advancement from the text based File-Login-System that I made earlier.

This one utilizes tKinter, Fernet from Cryptography, and CSV to create a GUI based login system that will store data with symmetric key encryption in a CSV file. 

If you want to use this program, you must install Cryptography as it is not a default library. To do this on Windows, do "py -m pip install cryptography". Also, place the vaultLogo.png, vaultLargeLogo.png, key.txt, and secret_data.csv in the same directory as the python program itself. 

You should be all good to go after that and if you want to test the login feature, there is already one user in the data file which has the following credentials and message:

Username: admin
Password: 1234
Message: This is a test
