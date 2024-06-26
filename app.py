from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contacts.db'
db=SQLAlchemy(app)


# Crear modelo de la base de datos

class Contact(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    phone=db.Column(db.String(11), nullable=False)

    # Serializa el objeto, se convierte el objeto en un diccionario
    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'phone':self.phone
        }
    
# Crea las tablas en la base de datos
with app.app_context():
    db.create_all()




# Get contactos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts=Contact.query.all()
    return jsonify({'contacts':[contact.serialize() for contact in contacts]})


# Crear Contacto
@app.route('/contacts', methods=['POST'])
def create_contact():
    #obtener los datos del json
    data=request.get_json()
    contact=Contact(name=data['name'], email=data['email'],phone=data['phone'])
    db.session.add(contact)
    db.session.commit()

    return jsonify({'message':'Contacto creado con exito','contact':contact.serialize()}), 201 #201 estado creado


# Get Contacto por ID
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact=Contact.query.get(id)
    if not contact:
        return jsonify({'message':'El contacto no se encuentra'}), 404

    return jsonify(contact.serialize())

# Editar Contacto
@app.route('/contacts/<int:id>', methods=['PUT','PATCH'])
def edit_contact(id):
    contact=Contact.query.get_or_404(id)

    data=request.get_json()

    if 'name' in data:
        contact.name=data['name']
    if 'email' in data:
        contact.email=data['email']
    if 'phone' in data:
        contact.phone=data['phone']   
    
    # Guardar cambios en la base
    db.session.commit()
    return jsonify({'message':'Contacto actualizado con exito','contact':contact.serialize()}), 201 #201 estado creado


# Eliminar Contacto
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact=Contact.query.get(id)
    if not contact:
        return jsonify({'message':'El contacto no se encuentra'}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message':'Contacto eliminado con exito'})


if __name__ == '__main__':
    app.run(debug=True)

