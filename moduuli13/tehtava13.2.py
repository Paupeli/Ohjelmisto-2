from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pauliina',
    password='tikru123!',
    autocommit=True,
    collation='utf8mb4_unicode_ci'
)

def get_airport_by_icao(icao_code):
    sql = f"SELECT name FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql,(icao_code.upper(),))
    row = cursor.fetchone()
    cursor.close()
    if row:
        return {
            "ICAO": icao_code.upper(),
            "Name": row[0],
        }
    else:
        return None

@app.route('/airport/<icao_code>', methods = ['GET'])
def airport_info(icao_code):
    result = get_airport_by_icao(icao_code)
    if result:
        return jsonify(result)
    else:
        abort(404, message= "Airport not found.")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)




