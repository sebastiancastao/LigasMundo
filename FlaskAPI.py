from flask import Flask, request, render_template, jsonify, make_response
from NNEpicContentInterLiga import paisPrimeraDivisionEsp, paisSegundaDivisionEsp, paisTerceraDivisionEsp, ligaPaisPrimera, ligaPaisSegunda, ligaPaisTercera
import json
import logging
import traceback
import sys
import codecs
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

# Forzar codificación UTF-8 para stdout
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Update salary data with all countries from spreadsheet
salary_data = {
    "Portugal": {"Primera": {"min": 20000, "avg": 4811844, "max": 6920000},
                "Segunda": {"min": 17220, "avg": 77500, "max": 120000},
                "Tercera": {"min": 10000, "avg": 14760, "max": 50000}},
    "Inglaterra": {"Primera": {"min": 150800, "avg": 4831555, "max": 51272000},
                  "Segunda": {"min": 34800, "avg": 766113, "max": 2316400},
                  "Tercera": {"min": 62000, "avg": 92721, "max": 123442}},
    "Argentina": {"Primera": {"min": 5735, "avg": 28440, "max": 1380000},
                 "Segunda": {"min": 5640, "avg": 8700, "max": 11760},
                 "Tercera": {"min": 3720, "avg": 4032, "max": 4344}},
    "China": {"Primera": {"min": 47477, "avg": 190000, "max": 19900000},
             "Segunda": {"min": 19000, "avg": 104500, "max": 190000},
             "Tercera": {"min": 9500, "avg": 76250, "max": 143000}},
    "Mexico": {"Primera": {"min": 45600, "avg": 1122800, "max": 2200000},
              "Segunda": {"min": 9000, "avg": 19200, "max": 210000},
              "Tercera": {"min": 0, "avg": 5124, "max": 12000}},
    "Estados Unidos": {"Primera": {"min": 67000, "avg": 5733500, "max": 11400000},
                      "Segunda": {"min": 29400, "avg": 37500, "max": 45600},
                      "Tercera": {"min": 0, "avg": 0, "max": 0}},
    "Brasil": {"Primera": {"min": 2336, "avg": 403875, "max": 24126123},
              "Segunda": {"min": 3408, "avg": 38262, "max": 73116},
              "Tercera": {"min": 0, "avg": 2844, "max": 22800}},
    "Marruecos": {"Primera": {"min": 11400, "avg": 34200, "max": 57000},
                  "Segunda": {"min": 5640, "avg": 8520, "max": 11400},
                  "Tercera": {"min": 0, "avg": 0, "max": 0}},
    "Francia": {"Primera": {"min": 120000, "avg": 1769404, "max": 132000000},
               "Segunda": {"min": 56895, "avg": 157727, "max": 1589577},
               "Tercera": {"min": 18000, "avg": 39000, "max": 60000}},
    "Italia": {"Primera": {"min": 42000, "avg": 1904191, "max": 12960000},
              "Segunda": {"min": 11128, "avg": 358175, "max": 5798398},
              "Tercera": {"min": 6000, "avg": 15000, "max": 24000}},
    "Alemania": {"Primera": {"min": 120000, "avg": 2165033, "max": 25000000},
                "Segunda": {"min": 42504, "avg": 308350, "max": 1594292},
                "Tercera": {"min": 17000, "avg": 24648, "max": 100000}},
    "Colombia": {"Primera": {"min": 5688, "avg": 57000, "max": 74000},
                "Segunda": {"min": 2856, "avg": 8208, "max": 13560},
                "Tercera": {"min": 0, "avg": 0, "max": 0}},
    "Chile": {"Primera": {"min": 59244, "avg": 70644, "max": 110520},
             "Segunda": {"min": 3889, "avg": 13891, "max": 27778},
             "Tercera": {"min": 1667, "avg": 6389, "max": 11111}},
    "Perú": {"Primera": {"min": 11388, "avg": 227892, "max": 75964},
            "Segunda": {"min": 11388, "avg": 51270, "max": 91152},
            "Tercera": {"min": 0, "avg": 0, "max": 0}},
    "Arabia Saudita": {"Primera": {"min": 4570000, "avg": 13239245, "max": 200000000},
                      "Segunda": {"min": 3418404, "avg": 7406556, "max": 11394708},
                      "Tercera": {"min": 1139460, "avg": 1709196, "max": 2278932}},
    "Corea del Sur": {"Primera": {"min": 20000, "avg": 1000000, "max": 11560000},
                     "Segunda": {"min": 20000, "avg": 610000, "max": 1200000},
                     "Tercera": {"min": 10000, "avg": 20000, "max": 30000}},
    "Egipto": {"Primera": {"min": 28500, "avg": 95000, "max": 285176},
              "Segunda": {"min": 10000, "avg": 30000, "max": 100000},
              "Tercera": {"min": 2000, "avg": 10000, "max": 30000}},
    "Noruega": {"Primera": {"min": 50000, "avg": 406838, "max": 4650000},
               "Segunda": {"min": 33480, "avg": 78120, "max": 223200},
               "Tercera": {"min": 11160, "avg": 33480, "max": 78120}},
    "Bolivia": {"Primera": {"min": 8928, "avg": 27900, "max": 167400},
               "Segunda": {"min": 4464, "avg": 11160, "max": 22320},
               "Tercera": {"min": 1116, "avg": 5580, "max": 11160}},
    "Polonia": {"Primera": {"min": 55800, "avg": 133920, "max": 334800},
               "Segunda": {"min": 27900, "avg": 66960, "max": 167400},
               "Tercera": {"min": 5580, "avg": 16740, "max": 22320}},
    "Latvia": {"Primera": {"min": 8928, "avg": 27900, "max": 78120},
              "Segunda": {"min": 3348, "avg": 11160, "max": 22320},
              "Tercera": {"min": 1116, "avg": 5580, "max": 11160}},
    "Panama": {"Primera": {"min": 4464, "avg": 11160, "max": 33480},
              "Segunda": {"min": 2232, "avg": 5580, "max": 11160},
              "Tercera": {"min": 558, "avg": 2232, "max": 5580}},
    "Andorra": {"Primera": {"min": 5580, "avg": 13392, "max": 33480},
               "Segunda": {"min": 2232, "avg": 5580, "max": 11160},
               "Tercera": {"min": 558, "avg": 2232, "max": 5580}},
    "Costa Rica": {"Primera": {"min": 22320, "avg": 44640, "max": 111600},
                  "Segunda": {"min": 5580, "avg": 16740, "max": 33480},
                  "Tercera": {"min": 1116, "avg": 4464, "max": 11160}},
    "Eslovenia": {"Primera": {"min": 11160, "avg": 27900, "max": 89280},
                 "Segunda": {"min": 3348, "avg": 11160, "max": 27900},
                 "Tercera": {"min": 558, "avg": 2232, "max": 5580}},
    "Luxemburgo": {"Primera": {"min": 16740, "avg": 33480, "max": 66960},
                  "Segunda": {"min": 5580, "avg": 13392, "max": 27900},
                  "Tercera": {"min": 1116, "avg": 5580, "max": 11160}},
    "Espana": {"Primera": {"min": 150000, "avg": 2500000, "max": 33330000},
               "Segunda": {"min": 50000, "avg": 500000, "max": 2000000},
               "Tercera": {"min": 20000, "avg": 100000, "max": 500000}}
}

# Update the countries dictionary to use consistent league names
countries = {
    "Espana": ["Primera Division", "Segunda Division", "Primera Federacion", "Segunda Federacion"],
    "Inglaterra": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Marruecos": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Francia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "China": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Portugal": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Costa Rica": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Brasil": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Argentina": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Mexico": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Estados Unidos": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Sahara Occidental": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Arabia Saudita": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Bolivia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Polonia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Egipto": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Colombia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Paraguay": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Latvia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Italia": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Corea del Sur": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Panama": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Andorra": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Chile": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Noruega": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Luxemburgo": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Venezuela": ["Primera Division", "Segunda Division", "Tercera Division"],
    "Ecuador": ["Primera Division", "Segunda Division", "Tercera Division"],
}

# Country mapping with better error handling
country_mapping = {
    "Estados Unidos": 14,
    "Inglaterra": 26,
    "Marruecos": 19,
    "Francia": 15,
    "China": 7,
    "Portugal": 25,
    "Argentina": 3,
    "Costa Rica": 10,
    "Sahara Occidental": 27,
    "Mexico": 20,
    "Brasil": 5,
    "Arabia Saudita": 2,
    "Eslovenia": 13,
    "Bolivia": 4,
    "Polonia": 23,
    "Egipto": 12,
    "Colombia": 8,
    "Paraguay": 22,
    "Latvia": 17,
    "Italia": 16,
    "Corea del Sur": 9,
    "Panama": 22,
    "Andorra": 1,
    "Chile": 6,
    "Noruega": 21,
    "Luxemburgo": 18,
    "Venezuela": 27,
    "Ecuador": 10,
    "Espana": 0
}

# Crear el reverse_mapping
reverse_mapping = {v: k for k, v in country_mapping.items()}

# Mensajes en español sin caracteres especiales
MESSAGES = {
    'primera_esp': "La liga equivalente es: Primera Division",
    'segunda_esp': "La liga equivalente es: Segunda Division",
    'tercera_esp': "La liga equivalente es: Tercera Division",
    'primera_fed': "La liga equivalente es: Primera Federacion",
    'segunda_fed': "La liga equivalente es: Segunda Federacion"
}

def calculate_salary_differences(original_salaries, predicted_salaries):
    """
    Calcula las diferencias porcentuales entre salarios
    Retorna el promedio de las diferencias y las diferencias individuales
    """
    try:
        differences = {
            "min_diff": ((predicted_salaries["min"] - original_salaries["min"]) / original_salaries["min"]) * 100,
            "avg_diff": ((predicted_salaries["avg"] - original_salaries["avg"]) / original_salaries["avg"]) * 100,
            "max_diff": ((predicted_salaries["max"] - original_salaries["max"]) / original_salaries["max"]) * 100
        }
        
        # Calcular el promedio de las diferencias
        avg_total_diff = sum(differences.values()) / len(differences)
        
        # Redondear todos los valores a 2 decimales
        differences = {k: round(v, 2) for k, v in differences.items()}
        avg_total_diff = round(avg_total_diff, 2)
        
        return {
            "differences": differences,
            "average_difference": avg_total_diff
        }
    except ZeroDivisionError:
        return {
            "differences": {"min_diff": 0, "avg_diff": 0, "max_diff": 0},
            "average_difference": 0
        }

# Definir los países de élite (solo los principales)
elite_countries = ["Espana", "Francia", "Italia", "Portugal", "Inglaterra"]

@app.route("/api/compare", methods=["POST"])
def compare_leagues_api():
    """Endpoint separado para la API JSON"""
    try:
        if not request.is_json:
            return jsonify({
                "error": "Invalid request",
                "message": "Request must be JSON"
            }), 400
            
        data = request.json
        logger.debug(f"Received data: {data}")
        
        country1 = data.get("country1", "").replace("España", "Espana")
        league1 = data.get("league1", "")
        country2 = data.get("country2", "").replace("España", "Espana")
        
        logger.debug(f"Processing request for: {country1}, {league1}, {country2}")

        # Validate input
        if not all([country1, league1, country2]):
            logger.error("Missing required fields")
            return jsonify({
                "error": "Missing data",
                "message": "Please provide all required fields"
            }), 400

        # Determinar el tipo de liga
        league_type = None
        if "Primera" in league1:
            league_type = "Primera"
        elif "Segunda" in league1:
            league_type = "Segunda"
        else:
            league_type = "Tercera"

        # Verificar si AMBOS países son de élite
        is_elite_case = (country1 in elite_countries and country2 in elite_countries) and "Primera" in league1

        # Si es un caso de élite, forzar Primera División
        if is_elite_case:
            logger.debug(f"Caso especial de élite detectado: {country1} -> {country2}")
            resultNum = 0  # Primera División
        else:
            # Usar el método anterior para países no élite
            country = None
            if country1 in country_mapping:
                country = country_mapping[country1]
            else:
                logger.error(f"Unknown country1: {country1}")
                return jsonify({
                    "error": "Invalid country",
                    "message": f"Country not supported: {country1}"
                }), 400
            
            try:
                if league1 == "Primera Division" and country2 != "Spain":
                    resultNum = int(paisPrimeraDivisionEsp(country))
                elif league1 == "Segunda Division" and country2 != "Spain":
                    resultNum = int(paisSegundaDivisionEsp(country))
                elif league1 == "Tercera Division":
                    resultNum = int(paisTerceraDivisionEsp(country))
                else:
                    resultNum = 0
            except Exception as e:
                logger.error(f"Error in prediction: {str(e)}")
                return jsonify({
                    "error": "Prediction error",
                    "message": f"Error processing prediction: {str(e)}"
                }), 500

        # Determinar la liga equivalente basada en resultNum
        predicted_league = ""
        result = ""
        
        if country2 == "Espana" or country2 == "España":
            if resultNum == 0:
                result = "La liga equivalente es: La Liga"
                predicted_league = "La Liga"
            elif resultNum == 1:
                result = "La liga equivalente es: Segunda Division"
                predicted_league = "Segunda Division"
            elif resultNum == 2:
                result = "La liga equivalente es: Primera Federacion"
                predicted_league = "Primera Federacion"
            elif resultNum == 3:
                result = "La liga equivalente es: Segunda Federacion"
                predicted_league = "Segunda Federacion"
        else:
            # Manejar otros países
            if resultNum == 0:
                result = f"La liga equivalente es: Primera Division de {country2}"
                predicted_league = "Primera Division"
            elif resultNum == 1:
                result = f"La liga equivalente es: Segunda Division de {country2}"
                predicted_league = "Segunda Division"
            else:
                result = f"La liga equivalente es: Tercera Division de {country2}"
                predicted_league = "Tercera Division"
        
        # Crear información de salarios
        salary_info = {}
        
        # Información del país de origen
        if country1 in salary_data and league_type in salary_data[country1]:
            salary_info["original"] = {
                "country": country1,
                "league": league1,
                "salaries": salary_data[country1][league_type]
            }
        
        # Información del país de destino
        predicted_type = "Primera" if resultNum == 0 else "Segunda" if resultNum == 1 else "Tercera"
        if country2 in salary_data and predicted_type in salary_data[country2]:
            salary_info["predicted"] = {
                "country": country2,
                "league": predicted_league,
                "salaries": salary_data[country2][predicted_type]
            }
            
            # Calcular diferencias si tenemos ambos datos
            if "original" in salary_info and "predicted" in salary_info:
                salary_info["differences"] = calculate_salary_differences(
                    salary_info["original"]["salaries"],
                    salary_info["predicted"]["salaries"]
                )
                
                # Añadir mensaje interpretativo
                diff = salary_info["differences"]["average_difference"]
                if diff > 0:
                    salary_info["comparison_message"] = f"Los salarios en la liga equivalente son en promedio {abs(diff)}% mayores"
                elif diff < 0:
                    salary_info["comparison_message"] = f"Los salarios en la liga equivalente son en promedio {abs(diff)}% menores"
                else:
                    salary_info["comparison_message"] = "Los salarios son similares en ambas ligas"
        
        # Devolver la respuesta JSON
        response = make_response(jsonify({
            "result": result,
            "original_league": league1,
            "predicted_league": predicted_league,
            "salary_info": salary_info
        }))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
        
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        logger.error(traceback.format_exc())
        response = make_response(jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

@app.route("/", methods=["GET"])
def home():
    """Endpoint para la página principal"""
    return render_template("index.html", countries=countries)

if __name__ == '__main__':
    app.run(debug=True)
