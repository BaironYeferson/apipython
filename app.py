from flask import Flask
from flask import jsonify,request,render_template,make_response 
from products import products
import pdfkit

app = Flask(__name__)

@app.route('/ping',methods=['GET'])

def ping():
    return jsonify({"mensaje":"pong"})


@app.route('/productos',methods=['GET'])

def getlistaProductos():
    return jsonify({"products":products,"mensaje":"lista de productos"})


#obtiene
@app.route('/producto/<string:product_name>',methods=['GET'])

def getproducto(product_name):
   ## print(product_name)
    productoFound = [product for product in products if product['name'] == product_name]

    if (len(productoFound)>0):

        return jsonify({"producto": productoFound[0]})
    else:
         return jsonify({"producto": "no existe"})



#envia datos 
@app.route('/productos/<string:product_name>',methods=['POST'])
def addProduct():
    #print(request.json)
    new_product={
        "name":request.json['name'],
        "prices":request.json['prices'],
        "quanty":request.json['quanty'],
    }
    products.append(new_product)

    return jsonify({"mensaje":"producto agregado","product":products})
   



#actualiza
@app.route('/productos/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    #print(request.json)
    
    productoFound = [product for product in products if product['name'] == product_name]
    if (len(productoFound)>0):

        productoFound[0]['name']=request.json['name']
        productoFound[0]['prices']=request.json['prices']
        productoFound[0]['quanty']=request.json['quanty']

        return jsonify({
            "mensaje": "producto actualizado",
            "product":productoFound[0]
        })

    else:
         return jsonify({"mensaje": "producto actualizado"})
    return jsonify({"mensaje":"producto agregado","product":products})



#elimina
@app.route('/productos/<string:product_name>',methods=['DELETE'])

def deleteProduct(product_name):
    productoFound = [product for product in products if product['name'] == product_name]
    if (len(productoFound)>0):

        products.remove(productoFound[0])

        return jsonify({
            "mensaje": "producto eliminado",
            "product":products
        })

    else:
        return jsonify({"mensaje": "producto actualizado"})
    return jsonify({"mensaje":"producto no encontrado"})
   

#genera pdf
@app.route('/pdf',methods=['GET'])
def generarPDF():


    #rendered = render_template('pdf_template.html')
    #pdf = pdfkit.from_string(rendered)

    response = make_response(pdf)
    respose.headers['Content-Type'] = 'aplication/pdf'
    respose.headers['Content-Disposition'] = 'inline; filename=output.pdf'


    return response
    
  




if __name__ == '__main__':
    app.run(debug=True, port=4000)