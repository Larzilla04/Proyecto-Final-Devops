import boto3

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('proyectoTabla')

# Insertar
tabla.put_item(Item={'proyecto1': '001', 'Nombre': 'Carlos'})
tabla.put_item(Item={'proyecto1': '002', 'Nombre': 'Lars'})
print("Insertado")

# Modificar
tabla.update_item(
    Key={'proyecto1': '001'},
    UpdateExpression='SET Nombre = :val1',
    ExpressionAttributeValues={':val1': 'Carlos A.'}
)
print("Modificado")

# Eliminar
tabla.delete_item(Key={'proyecto1': '001'})
print("Eliminado")
