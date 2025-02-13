from flask import Flask, request, render_template, jsonify
from NNEpicContentInterLiga import paisPrimeraDivisionEsp, paisSegundaDivisionEsp, paisTerceraDivisionEsp, ligaPaisPrimera, ligaPaisSegunda, ligaPaisTercera
app = Flask(__name__)

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
    "México": {"Primera": {"min": 45600, "avg": 1122800, "max": 2200000},
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
                  "Tercera": {"min": 1116, "avg": 5580, "max": 11160}}
}

# Datos de ejemplo
countries = {
    
    "España": ["La Liga", "Segunda División", "Primera Federación", "Segunda Federación"],
    "Inglaterra": ["Primera División", "Segunda División", "Tercera División"],
    "Marruecos": ["Primera División", "Segunda División", "Tercera División"],
    "Francia": ["Primera División", "Segunda División", "Tercera División"],
    "China": ["Primera División", "Segunda División", "Tercera División"],
    "Portugal": ["Primera División", "Segunda División", "Tercera División"],
    "Costa Rica": ["Primera División", "Segunda División", "Tercera División"],
    "Brasil": ["Primera División", "Segunda División", "Tercera División"],
    "Argentina": ["Primera División", "Segunda División", "Tercera División"],
    "México": ["Primera División", "Segunda División", "Tercera División"],
    "Estados Unidos": ["Primera División", "Segunda División", "Tercera División"],
    "Sahara Occidental": ["Primera División", "Segunda División", "Tercera División"],
    "Arabia Saudita": ["Primera División", "Segunda División", "Tercera División"],
    "Bolivia": ["Primera División", "Segunda División", "Tercera División"],
    "Polonia": ["Primera División", "Segunda División", "Tercera División"],
    "Egipto": ["Primera División", "Segunda División", "Tercera División"],
    "Colombia": ["Primera División", "Segunda División", "Tercera División"],
    "Paraguay": ["Primera División", "Segunda División", "Tercera División"],
    "Latvia": ["Primera División", "Segunda División", "Tercera División"],
    "Italia": ["Primera División", "Segunda División", "Tercera División"],
    "Corea del Sur": ["Primera División", "Segunda División", "Tercera División"],
    "Panama": ["Primera División", "Segunda División", "Tercera División"],
    "Andorra": ["Primera División", "Segunda División", "Tercera División"],
    "Chile": ["Primera División", "Segunda División", "Tercera División"],
    "Noruega": ["Primera División", "Segunda División", "Tercera División"],
    "Luxemburgo": ["Primera División", "Segunda División", "Tercera División"],
    "Venezuela": ["Primera División", "Segunda División", "Tercera División"],
    "Ecuador": ["Primera División", "Segunda División", "Tercera División"],
}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        country1 = data.get("country1")
        league1 = data.get("league1")
        country2 = data.get("country2")
        
        if country1=="United States" or country1=="Estados Unidos":
            country=14
        elif country1=="United Kingdom" or country1=="Inglaterra":
            country=26
        elif country1=="Marocco" or country1=="Marruecos":
            country=19
        elif country1=="France" or country1=="Francia":
            country=15
        elif country1=="China" or country1=="China":
            country=7
        elif country1=="Portugal" or country1=="Portugal":
            country=25
        elif country1=="Argentina" or country1=="Argentina":
            country=3
        elif country1=="Costa Rica" or country1=="Costa Rica":
            country=10
        elif country1=="Sahara Occidental" or country1=="Sahara Occidental":
            country=27
        elif country1=="Mexico" or country1=="México":
            country=20
        elif country1=="Brazil" or country1=="Brasil":
            country=5
        elif country1=="Saudi Arabia" or country1=="Arabia Saudita":
            country=2
        elif country1=="Eslovenia" or country1=="Eslovenia":
            country=13
        elif country1=="Bolivia" or country1=="Bolivia":
            country=4
        elif country1=="Poland" or country1=="Polonia":
            country=24
        elif country1=="Egypt" or country1=="Egipto":
            country=12
        elif country1=="Colombia" or country1=="Colombia":
            country=8
        elif country1=="Paraguay" or country1=="Paraguay":
            country=23
        elif country1=="Latvia" or country1=="Latvia":
            country=17
        elif country1=="Italy" or country1=="Italia":
            country=16
        elif country1=="South Korea" or country1=="Corea del Sur":
            country=9
        elif country1=="Panama" or country1=="Panama":
            country=22
        elif country1=="Andorra" or country1=="Andorra":
            country=1
        elif country1=="Chile" or country1=="Chile":
            country=6
        elif country1=="Norway" or country1=="Noruega":
            country=21
        elif country1=="Luxembourg" or country1=="Luxemburgo":
            country=18
        elif country1=="Venezuela" or country1=="Venezuela":
            country=28
        elif country1=="Ecuador" or country1=="Ecuador":    
            country=11

        elif country1=="Spain" or country1=="España":
            if league1 =="La Liga":
                league=0
            elif league1 =="Segunda División":
                league=1
            elif league1 =="Primera Federación":
                league=2
            elif league1 =="Segunda Federación":
                league=3

       
        if league1=="Primera División":
             resultNum=paisPrimeraDivisionEsp(country)    
        elif league1=="Segunda División" and country2!="Spain":
             resultNum=paisSegundaDivisionEsp(country)
        elif league1=="Tercera División":
             resultNum=paisTerceraDivisionEsp(country)
        
        result_array=[]

        if country2=="Spain" or country2=="España":
            if resultNum==0:
                result="La Liga Española equivalente es: La Liga"
                predicted_league = "La Liga"
            elif resultNum==1:
                result="La Liga Española equivalente es: Segunda División"
                predicted_league = "Segunda División"
            elif resultNum==2:
                result="La Liga Española equivalente es: Primera Federación"
                predicted_league = "Primera Federación"
            elif resultNum==3:
                result="La Liga Española equivalente es: Segunda Federación"
                predicted_league = "Segunda Federación"
        else: 
                if country2=="United States" or country2=="Estados Unidos":
                    country2=13
                elif country2=="England" or country2=="Inglaterra":
                    country2=25
                elif country2=="England" or country2=="Inglaterra":
                    country2=25
                elif country2=="Marocco" or country2=="Marruecos":
                    country2=18
                elif country2=="France" or country2=="Francia":
                    country2=14
                elif country2=="China" or country2=="China":
                    country2=6
                elif country2=="Portugal" or country2=="Portugal":
                    country2=24
                elif country2=="Argentina" or country2=="Argentina":
                    country2=2
                elif country2=="Costa Rica" or country2=="Costa Rica":
                    country2=9
                elif country2=="Sahara Occidental" or country2=="Sahara Occidental":
                    country2=26
                elif country2=="Mexico" or country2=="México":
                    country2=19
                elif country2=="Brazil" or country2=="Brasil":
                    country2=4
                
                elif country2=="Saudi Arabia" or country2=="Arabia Saudita":
                    country2=1
                
                elif country2=="Bolivia" or country2=="Bolivia":
                    country2=3
                elif country2=="Poland" or country2=="Polonia":
                    country=23
                elif country2=="Egypt" or country2=="Egipto":
                    country2=11
                elif country2=="Colombia" or country2=="Colombia":
                    country2=7
                elif country2=="Paraguay" or country2=="Paraguay":
                    country2=22
                elif country2=="Latvia" or country2=="Latvia":
                    country2=16
                elif country2=="Italy" or country2=="Italia":
                    country2=15
                elif country2=="South Korea" or country2=="Corea del Sur":
                    country2=8
                elif country2=="Panama" or country2=="Panama":
                    country2=21
                elif country2=="Andorra" or country2=="Andorra":
                    country2=0
                elif country2=="Chile" or country2=="Chile":
                    country2=5
                elif country2=="Norway" or country2=="Noruega":
                    country2=20
                elif country2=="Luxembourg" or country2=="Luxemburgo":
                    country2=17
                elif country2=="Venezuela" or country2=="Venezuela":
                    country2=27
                elif country2=="Ecuador" or country2=="Ecuador":
                    country2=10
            

                resultNum21=ligaPaisPrimera(resultNum,country2)
                result_array.append(resultNum21)
                resultNum22=ligaPaisSegunda(resultNum,country2)
                result_array.append(resultNum22)
                resultNum23=ligaPaisTercera(resultNum,country2)
                result_array.append(resultNum23)
                print(result_array)
                indice=0
                for i in range(0,len(result_array)-1,1):
                    if result_array[i]>result_array[i+1] and i <len(result_array)-1:
                        indice=i
                        
                    
                if indice==0:
                    result="La Liga equivalente es: Primera División"
                    predicted_league = "Primera División"
                elif indice==1:
                    result="La Liga equivalente es: Segunda División"
                    predicted_league = "Segunda División"
                elif indice==2: 
                    result="La Liga equivalente es: Tercera División"
                    predicted_league = "Tercera División"
                
                
            
            
        
            
        
            
        # Lógica para la comparación
       
        # Add salary information to the response
        try:
            salary_info = {}
            
            # Get salary data for original league
            if country1 in salary_data:
                league_type = "Primera" if "Primera" in league1 else "Segunda" if "Segunda" in league1 else "Tercera"
                salary_info["original"] = {
                    "country": country1,
                    "league": league1,
                    "salaries": salary_data[country1][league_type]
                }
            
            # Get salary data for predicted league
            if country2 in salary_data:
                predicted_type = "Primera" if "Primera" in predicted_league else "Segunda" if "Segunda" in predicted_league else "Tercera"
                salary_info["predicted"] = {
                    "country": country2,
                    "league": predicted_league,
                    "salaries": salary_data[country2][predicted_type]
                }

            response = {
                "result": result,
                "original_league": league1,
                "predicted_league": predicted_league,
                "salary_info": salary_info
            }
        except Exception as e:
            # If there's any error getting salary data, return just the result
            response = {
                "result": result,
                "original_league": league1,
                "predicted_league": predicted_league
            }

        return jsonify(response)
    
    return render_template("index.html", countries=countries)

if __name__ == "__main__":
    app.run()
