import boto3

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('proyectoTabla')

# Insertar
tabla.put_item(Item={'ID': '001', 'Nombre': 'Carlos'})
print("Insertado")

# Modificar
tabla.update_item(
    Key={'ID': '001'},
    UpdateExpression='SET Nombre = :val1',
    ExpressionAttributeValues={':val1': 'Carlos A.'}
)
print("Modificado")

# Eliminar
tabla.delete_item(Key={'ID': '001'})
print("Eliminado")
