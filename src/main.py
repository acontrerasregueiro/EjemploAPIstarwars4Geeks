"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os  #Porder acceder a carpetas
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate  #
from flask_swagger import swagger
from flask_cors import CORS # Para evitar un error al consumir APIs
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Fav_people, Fav_planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods = ['GET'])
def get_people():
    allpeople = People.query.all() #Es un methodo de Sql Alchemy que devuelve la totalidad de la info
    #Guarda en allpeople la info una vez realizado el serialice , que es un metodo para mostrar mas "bonito"
    #Itera en cada una de las class y almacena el resultado de la funcion serialice
    #Estructura de Map (quiero hacer esto, en que array)
    allpeople = list(map(lambda elementoArray: elementoArray.serialize(),allpeople))
    print(allpeople)
    return jsonify({"Array all People : ": allpeople})

"""
@app.route('/people/<int:id>', methods=['GET'])
def get_one_people(id):
    #bajo un parametro especifico
    #onepeople = People.query.filter_by(id=id).first()
    #buscar SOLO por el id
    onepeople = People.query.get(id).serialize()
    return jsonify({"resultado": onepeople})

"""
@app.route('/people/<int:id>', methods =['GET'])
def get_one_people(id):
    #pedimos informacion con un parametro especificio
    oneperson= People.query.filter_by(id=id).first() #el .first solamente muestra un resultado
    print(oneperson)
    #return ('RESULTADO .FIRST')
    oneperson= People.query.filter_by(id=id) # sin el first mostraria todos los resultado0s
    print(oneperson)
    #resultado con serialice
    oneperson = People.query.get(id).serialize()
    return jsonify({"resultado": oneperson})
    """
    if oneperson:
        return jsonify({'Resultado :',oneperson})
    else:
        return jsonify({'NO EXISTE EL PERSONAJE'})
 
   """
@app.route("/favorite/people/<int:people_id>", methods=['POST'])
def add_fav_people(people_id):
    return({"resultado : "  + ' estamos en POST'})
    """
    if onepeople:
        new = Fav_people() #instanciamos una clase
        new.user_id = 1   # anadimos los datos
        new_people_id = people_id
        db.session.add(new) #agreo el registro a la BBDD
        db.session.commit() #guardamos los resultados en la BBDD

        return jsonify({"AÑADIDO A LA BBDD"})
    else:
        return jsonify({' Ha ocurrido un error'})
    """
@app.route('/planets/<int:id>', methods=['GET'])
def get_one_planet(id):
    #bajo un parametro especifico
    #onepeople = People.query.filter_by(id=id).first()
    #buscar SOLO por el id
    unplanet = Planets.query.get(id).serialize()
    return jsonify({"resultado": unplanet})

@app.route('/favpeople', methods = ['GET'])
def get_favpeople():
    favpeople = Fav_people.query.all() #Es un methodo de Sql Alchemy que devuelve la totalidad de la info
    #Guarda en allpeople la info una vez realizado el serialice , que es un metodo para mostrar mas "bonito"
    #Itera en cada una de las class y almacena el resultado de la funcion serialice
    #Estructura de Map (quiero hacer esto, en que array)
    favpeople = list(map(lambda elementoArray: elementoArray.serialize(),favpeople))
    print(favpeople)
    return jsonify({"Array all People : ": allpeople})

@app.route('/planets', methods = ['GET'])
def get_planets():
    allplanets = Planets.query.all() #Es un methodo de Sql Alchemy que devuelve la totalidad de la info
    #Guarda en allpeople la info una vez realizado el serialice , que es un metodo para mostrar mas "bonito"
    #Itera en cada una de las class y almacena el resultado de la funcion serialice
    #Estructura de Map (quiero hacer esto, en que array)
    allplanets = list(map(lambda elementoArray: elementoArray.serialize(),allplanets))
    print(allplanets)
    return jsonify({"Array all planets : ": allplanets})



@app.route('/favpeople', methods = ['GET'])
def get_favplanets():
    favplanets = Fav_planets.query.all() #Es un methodo de Sql Alchemy que devuelve la totalidad de la info
    favplanets = list(map(lambda elementoArray: elementoArray.serialize(),favplanets))
    print(favplanets)
    return jsonify({"Array all People : ": allpeople})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
