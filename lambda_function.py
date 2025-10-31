import json
import boto3

def lambda_handler(event, context):
    # Captura o registro do evento do S3
    record = event['Records'][0]
    
    # Extrai nome do bucket de origem e do arquivo
    bucket_name = record['s3']['bucket']['name']
    object_key = record['s3']['object']['key']
    
    # Define o nome do bucket de destino
    bucket_destino = 'bucketdestinoprocessamentocamila'
    
    # Inicializa o cliente S3
    s3_client = boto3.client('s3')
    copy_source = {
        'Bucket': bucket_name,
        'Key': object_key
    }
    try:
        # Copia o objeto para o bucket de destino
        s3_client.copy(copy_source, bucket_destino, object_key)
        print("Arquivo copiado para bucket destino!")
    except Exception as e:
        print(f"Erro ao copiar arquivo: {e}")
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído e arquivo copiado com sucesso!')
    }

