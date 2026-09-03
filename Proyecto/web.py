# Alternativa Web para actividades del proyecto

from flask import Flask, jsonify, request
import areas.circulo
import areas.cuadrado
import areas.triangulo

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    pagina = "<html> <head><title>Fundamentos Web</title></head><body>"
    pagina += "<H2 style='color:Navy;'>Hello, World! Bienvenidos al curso de: </h2> <p> <h1>Fundamentos de Programación</h1>"
    pagina += "<H2> Elija la opción de acuerdo a los tipos de problemas a resolver</H2>"
    pagina += "<ul> <li><a href='localhost:5000/areas'>Areas</a></li> "
    pagina += "<li><a href='localhost:5000/ohm'>Ley de Ohm</a></li>"
    pagina += "<li><a href='localhost:5000/fisica'>Física</a></li></ul>"
    pagina += "</body> </html>" 
    return pagina

@app.route('/areas')
def area():
    pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
    pagina += "<H2> Área de círculo: </H2>"
    pagina += "<form action='localhost:5000/areas/circulo' method='post'>"
    pagina += "<label>Proporcione el radio del cìrculo</label><p>"
    pagina += "<input type='text' name='radio'><p>"
    pagina += "<input type='submit' value='Enviar'>"
    pagina += "</form>"
    pagina += "</body></html>"
    return pagina


@app.route('/areas/<figura>', methods=['POST'])
def calcular_areas(figura):
    if figura =="circulo":
        resultado = areas.circulo(request.post('radio'))
        pagina = "<html> <head><title>Cálculo de áreas</title></head><body>"
        pagina += "<H2> Área de círculo: </H2>"
        pagina += f"<p> El resultado es: {resultado}</p>"    
        pagina += "</body></html>"           
    return pagina,200

# 3. A POST route that accepts and returns JSON data
@app.route('/api/data', methods=['POST'])
def handle_post():
    data = request.get_json()  # Extract JSON data sent in the request
    
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request body"}), 400
        
    response_message = f"Data received successfully for {data['name']}!"
    return jsonify({"status": "success", "message": response_message}), 200

# Run the app locally if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)