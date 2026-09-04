from flask import Flask, jsonify, request
import areas.circulo
import areas.cuadrado
import areas.triangulo

app = Flask(__name__)

@app.route('/')
def home():
    pagina = "<html> <head><title>Fundamentos Web</title></head><body>"
    pagina += "<H2 style='color:Navy;'>Hello, World! Bienvenidos al curso de: </h2> <p> <h1>Fundamentos de Programación</h1>"
    pagina += "<H2> Elija la opción de acuerdo a los tipos de problemas a resolver</H2>"
    pagina += "<ul> <li><a href='http://localhost:5000/areas'>Areas</a></li> "
    pagina += "<li><a href='http://localhost:5000/ohm'>Ley de Ohm</a></li>"
    pagina += "<li><a href='http://localhost:5000/fisica'>Física</a></li></ul>"
    pagina += "</body> </html>" 
    return pagina

@app.route('/areas')
def area():
    pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
    pagina += "<H2> Área de círculo: </H2>"
    pagina += "<label>Proporcione el radio del cìrculo</label><p>"
    pagina += "<form action='http://localhost:5000/areas/circulo' method='POST'>"
    pagina += "<input type='text' name='radio'><p>"
    pagina += "<input type='submit' value='Enviar'>"
    pagina += "</form>"
    pagina += "<hr>"
    pagina += "<H2> Área de Triángulo: </H2>"
    pagina += "<form action='http://localhost:5000/areas/triangulo' method='POST'>"
    pagina += "<label>Proporcione la base del triángulo</label><p>"
    pagina += "<input type='text' name='base'><p>"
    pagina += "<label>Proporcione la altura del triángulo</label><p>"
    pagina += "<input type='text' name='altura'><p>"
    pagina += "<input type='submit' value='Enviar'>"
    pagina += "</form>"
    pagina += "<hr>"
    pagina += "<H2> Área de Cuadrado: </H2>"
    pagina += "<label>Proporcione el lado del cuadrado</label><p>"
    pagina += "<form action='http://localhost:5000/areas/cuadrado' method='POST'>"
    pagina += "<input type='text' name='lado'><p>"
    pagina += "<input type='submit' value='Enviar'>"
    pagina += "</form>"
    pagina += "<hr>"
    pagina += "</form>"
    pagina += "</body></html>"
    return pagina


@app.route('/areas/<figura>', methods=['POST'])
def calcular_areas(figura):
    if figura =="circulo":
        radio = float(request.form.get('radio', 0))  
        resultado = areas.circulo.area_circulo(radio)
        pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
        pagina += "<H2> Área de círculo: </H2>"
        pagina += f"<p> El resultado es: {resultado}</p>"    
        pagina += "</body></html>" 
    elif figura == "triangulo": 
        base = float(request.form.get('base'))
        altura = float(request.form.get('altura'))
        resultado = areas.triangulo.area_triangulo(base, altura)
        pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
        pagina += "<H2> Área de triangulo: </H2>"
        pagina += f"<p> El resultado es: {resultado}</p>"    
        pagina += "</body></html>"
    elif figura == "cuadrado":
        lado = float(request.form.get('lado', 0))  
        resultado = areas.cuadrado.area_cuadrado(lado)
        pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
        pagina += "<H2> Área de cuadrado: </H2>"
        pagina += f"<p> El resultado es: {resultado}</p>"    
        pagina += "</body></html>"                 
    return pagina,200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)