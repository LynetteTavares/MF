import mysql.connector
cnx = mysql.connector.connect(user="CloudCrafters", password="ABL@FdmMvpS$", host="movie-findr.mysql.database.azure.com", port=3306, database="moviefindr", ssl_ca="https://github.com/LynetteTavares/MF/blob/main/DigiCertGlobalRootG2.crt.pem", ssl_disabled=False)

try:
    cursor=cnx.cursor()
    print("Connection established")
except mysql.connector.Error as err:
    print(err)
