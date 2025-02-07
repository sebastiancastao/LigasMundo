from flask import Flask, request, render_template, jsonify
from NNEpicContentInterLiga import paisPrimeraDivisionEsp, paisSegundaDivisionEsp, paisTerceraDivisionEsp, ligaPaisPrimera, ligaPaisSegunda, ligaPaisTercera
app = Flask(__name__)

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
            elif resultNum==1:
                result="La Liga Española equivalente es: Segunda División"
            elif resultNum==2:
                result="La Liga Española equivalente es: Primera Federación"
            elif resultNum==3:
                result="La Liga Española equivalente es: Segunda Federación" 
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
                elif indice==1:
                    result="La Liga equivalente es: Segunda División"
                elif indice==2: 
                    result="La Liga equivalente es: Tercera División"
                
                
            
            
        
            
        
            
        # Lógica para la comparación
       
        return jsonify(result)
    
    return render_template("index.html", countries=countries)

if __name__ == "__main__":
    app.run()
