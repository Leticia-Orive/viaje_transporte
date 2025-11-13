from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'viajes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ruta raíz
@app.route('/')
def home():
    return jsonify({
        'message': 'API de Sistema de Viajes y Transporte',
        'version': '1.0',
        'endpoints': {
            'transportes': '/api/transportes',
            'viajes': '/api/viajes',
            'reservas': '/api/reservas',
            'inicializar_db': '/api/init-db (POST)'
        }
    })

# Modelos de la base de datos
class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # Bus, Tren, Avión, etc.
    nombre = db.Column(db.String(100), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean, default=True)
    viajes = db.relationship('Viaje', backref='transporte', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'nombre': self.nombre,
            'capacidad': self.capacidad,
            'activo': self.activo
        }

class Viaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False)
    fecha_llegada = db.Column(db.DateTime, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    asientos_disponibles = db.Column(db.Integer, nullable=False)
    transporte_id = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=False)
    reservas = db.relationship('Reserva', backref='viaje', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'origen': self.origen,
            'destino': self.destino,
            'fecha_salida': self.fecha_salida.isoformat(),
            'fecha_llegada': self.fecha_llegada.isoformat(),
            'precio': self.precio,
            'asientos_disponibles': self.asientos_disponibles,
            'transporte_id': self.transporte_id,
            'transporte': self.transporte.to_dict() if self.transporte else None
        }

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_pasajero = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    numero_asientos = db.Column(db.Integer, nullable=False)
    fecha_reserva = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(20), default='confirmada')  # confirmada, cancelada, pendiente
    viaje_id = db.Column(db.Integer, db.ForeignKey('viaje.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_pasajero': self.nombre_pasajero,
            'email': self.email,
            'telefono': self.telefono,
            'numero_asientos': self.numero_asientos,
            'fecha_reserva': self.fecha_reserva.isoformat(),
            'estado': self.estado,
            'viaje_id': self.viaje_id
        }

# Rutas - Transportes
@app.route('/api/transportes', methods=['GET'])
def get_transportes():
    transportes = Transporte.query.filter_by(activo=True).all()
    return jsonify([t.to_dict() for t in transportes])

@app.route('/api/transportes/<int:id>', methods=['GET'])
def get_transporte(id):
    transporte = Transporte.query.get_or_404(id)
    return jsonify(transporte.to_dict())

@app.route('/api/transportes', methods=['POST'])
def create_transporte():
    data = request.json
    transporte = Transporte(
        tipo=data['tipo'],
        nombre=data['nombre'],
        capacidad=data['capacidad']
    )
    db.session.add(transporte)
    db.session.commit()
    return jsonify(transporte.to_dict()), 201

@app.route('/api/transportes/<int:id>', methods=['PUT'])
def update_transporte(id):
    transporte = Transporte.query.get_or_404(id)
    data = request.json
    transporte.tipo = data.get('tipo', transporte.tipo)
    transporte.nombre = data.get('nombre', transporte.nombre)
    transporte.capacidad = data.get('capacidad', transporte.capacidad)
    transporte.activo = data.get('activo', transporte.activo)
    db.session.commit()
    return jsonify(transporte.to_dict())

@app.route('/api/transportes/<int:id>', methods=['DELETE'])
def delete_transporte(id):
    transporte = Transporte.query.get_or_404(id)
    transporte.activo = False
    db.session.commit()
    return jsonify({'message': 'Transporte desactivado'}), 200

# Rutas - Viajes
@app.route('/api/viajes', methods=['GET'])
def get_viajes():
    viajes = Viaje.query.all()
    return jsonify([v.to_dict() for v in viajes])

@app.route('/api/viajes/<int:id>', methods=['GET'])
def get_viaje(id):
    viaje = Viaje.query.get_or_404(id)
    return jsonify(viaje.to_dict())

@app.route('/api/viajes/buscar', methods=['GET'])
def buscar_viajes():
    origen = request.args.get('origen')
    destino = request.args.get('destino')
    fecha = request.args.get('fecha')
    
    query = Viaje.query
    if origen:
        query = query.filter(Viaje.origen.ilike(f'%{origen}%'))
    if destino:
        query = query.filter(Viaje.destino.ilike(f'%{destino}%'))
    if fecha:
        fecha_obj = datetime.fromisoformat(fecha)
        query = query.filter(db.func.date(Viaje.fecha_salida) == fecha_obj.date())
    
    viajes = query.all()
    return jsonify([v.to_dict() for v in viajes])

@app.route('/api/viajes', methods=['POST'])
def create_viaje():
    data = request.json
    viaje = Viaje(
        origen=data['origen'],
        destino=data['destino'],
        fecha_salida=datetime.fromisoformat(data['fecha_salida']),
        fecha_llegada=datetime.fromisoformat(data['fecha_llegada']),
        precio=data['precio'],
        asientos_disponibles=data['asientos_disponibles'],
        transporte_id=data['transporte_id']
    )
    db.session.add(viaje)
    db.session.commit()
    return jsonify(viaje.to_dict()), 201

@app.route('/api/viajes/<int:id>', methods=['PUT'])
def update_viaje(id):
    viaje = Viaje.query.get_or_404(id)
    data = request.json
    viaje.origen = data.get('origen', viaje.origen)
    viaje.destino = data.get('destino', viaje.destino)
    if 'fecha_salida' in data:
        viaje.fecha_salida = datetime.fromisoformat(data['fecha_salida'])
    if 'fecha_llegada' in data:
        viaje.fecha_llegada = datetime.fromisoformat(data['fecha_llegada'])
    viaje.precio = data.get('precio', viaje.precio)
    viaje.asientos_disponibles = data.get('asientos_disponibles', viaje.asientos_disponibles)
    db.session.commit()
    return jsonify(viaje.to_dict())

@app.route('/api/viajes/<int:id>', methods=['DELETE'])
def delete_viaje(id):
    viaje = Viaje.query.get_or_404(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify({'message': 'Viaje eliminado'}), 200

# Rutas - Reservas
@app.route('/api/reservas', methods=['GET'])
def get_reservas():
    reservas = Reserva.query.all()
    return jsonify([r.to_dict() for r in reservas])

@app.route('/api/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    return jsonify(reserva.to_dict())

@app.route('/api/reservas', methods=['POST'])
def create_reserva():
    data = request.json
    viaje = Viaje.query.get_or_404(data['viaje_id'])
    
    if viaje.asientos_disponibles < data['numero_asientos']:
        return jsonify({'error': 'No hay suficientes asientos disponibles'}), 400
    
    reserva = Reserva(
        nombre_pasajero=data['nombre_pasajero'],
        email=data['email'],
        telefono=data.get('telefono'),
        numero_asientos=data['numero_asientos'],
        viaje_id=data['viaje_id']
    )
    
    viaje.asientos_disponibles -= data['numero_asientos']
    
    db.session.add(reserva)
    db.session.commit()
    return jsonify(reserva.to_dict()), 201

@app.route('/api/reservas/<int:id>', methods=['PUT'])
def update_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    data = request.json
    reserva.estado = data.get('estado', reserva.estado)
    
    if reserva.estado == 'cancelada':
        viaje = Viaje.query.get(reserva.viaje_id)
        viaje.asientos_disponibles += reserva.numero_asientos
    
    db.session.commit()
    return jsonify(reserva.to_dict())

@app.route('/api/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    viaje = Viaje.query.get(reserva.viaje_id)
    viaje.asientos_disponibles += reserva.numero_asientos
    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva eliminada'}), 200

# Inicializar la base de datos
@app.route('/api/init-db', methods=['POST'])
def init_db():
    db.create_all()
    
    # Datos de ejemplo
    if Transporte.query.count() == 0:
        transportes = [
            Transporte(tipo='Autobús', nombre='Express Madrid', capacidad=50),
            Transporte(tipo='Tren', nombre='AVE Barcelona', capacidad=300),
            Transporte(tipo='Avión', nombre='Iberia A320', capacidad=180),
            Transporte(tipo='Autobús', nombre='Alsa Premium', capacidad=40)
        ]
        db.session.add_all(transportes)
        db.session.commit()
        
        viajes = [
            Viaje(
                origen='Madrid',
                destino='Barcelona',
                fecha_salida=datetime(2025, 11, 15, 8, 0),
                fecha_llegada=datetime(2025, 11, 15, 11, 0),
                precio=45.50,
                asientos_disponibles=300,
                transporte_id=2
            ),
            Viaje(
                origen='Madrid',
                destino='Valencia',
                fecha_salida=datetime(2025, 11, 16, 9, 0),
                fecha_llegada=datetime(2025, 11, 16, 13, 0),
                precio=25.00,
                asientos_disponibles=50,
                transporte_id=1
            ),
            Viaje(
                origen='Barcelona',
                destino='Madrid',
                fecha_salida=datetime(2025, 11, 17, 14, 0),
                fecha_llegada=datetime(2025, 11, 17, 15, 30),
                precio=120.00,
                asientos_disponibles=180,
                transporte_id=3
            )
        ]
        db.session.add_all(viajes)
        db.session.commit()
    
    return jsonify({'message': 'Base de datos inicializada'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
