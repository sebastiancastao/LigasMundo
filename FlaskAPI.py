from flask import Flask, request, render_template, jsonify
from NNEpicContentInterLiga import paisPrimeraDivisionEsp, paisSegundaDivisionEsp, paisTerceraDivisionEsp, ligaPaisPrimera, ligaPaisSegunda, ligaPaisTercera
app = Flask(__name__)

# Datos de ejemplo
countries = {
    "Spain": ["La Liga", "Segunda División", "Primera Federación", "Segunda Federación"],
    "England": ["Primera División", "Segunda División", "Tercera División"],
    "Italy": ["Primera División", "Segunda División", "Tercera División"],
    "Germany": ["Primera División", "Segunda División", "Tercera División"],
    "France": ["Primera División", "Segunda División", "Tercera División"],
    "Portugal": ["Primera División", "Segunda División", "Tercera División"],
    "Netherlands": ["Primera División", "Segunda División", "Tercera División"],
    "Brazil": ["Primera División", "Segunda División", "Tercera División"],
    "Argentina": ["Primera División", "Segunda División", "Tercera División"],
    "Mexico": ["Primera División", "Segunda División", "Tercera División"],
    "United States": ["Primera División", "Segunda División", "Tercera División"],
    "Canada": ["Primera División", "Segunda División", "Tercera División"],
    "Japan": ["Primera División", "Segunda División", "Tercera División"],
    "South Korea": ["Primera División", "Segunda División", "Tercera División"],
    "Australia": ["Primera División", "Segunda División", "Tercera División"],
    "China": ["Primera División", "Segunda División", "Tercera División"],
    "Russia": ["Primera División", "Segunda División", "Tercera División"],
    "Turkey": ["Primera División", "Segunda División", "Tercera División"],
    "Greece": ["Primera División", "Segunda División", "Tercera División"],
    "Belgium": ["Primera División", "Segunda División", "Tercera División"]
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
        elif country1=="United Kingdom" or country1=="Reino Unido":
            country=26
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
                elif country2=="England" or country2=="Ingleterra":
                    country2=25
            

                resultNum21=ligaPaisPrimera(resultNum,country2)
                result_array.append(resultNum21)
                resultNum22=ligaPaisSegunda(resultNum,country2)
                result_array.append(resultNum22)
                resultNum23=ligaPaisTercera(resultNum,country2)
                result_array.append(resultNum23)
                
                for i in range(0,len(result_array)-1,1):
                    if result_array[i]>result_array[i+1]and i <len(result_array)-1:
                        indice=i
                        break
                    else:
                        result="No hay equivalencia"
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
    app.run(debug=True)
