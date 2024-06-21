# security.py

from flask import request, jsonify

def security_middleware():
    # Verificar el token de autorización en todas las solicitudes
    token = request.headers.get('Authorization')

    # Aquí deberías implementar tu lógica de verificación de token
    if not token or token != 'token_valido':
        return jsonify({'message': 'Acceso no autorizado'}), 401

    # Si el token es válido, la solicitud puede continuar
    return None
