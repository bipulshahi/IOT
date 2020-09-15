import boto3

def lambda_handler(event, context):
    
    client = boto3.client('dynamodb')
    
    tf = event['T']*(9/5) + 32
    
    response = client.put_item(
        TableName='dbtable',
        Item = {'time': { 'S' : event['time']},
                'temperature(C)' : {'N' : str(event['T'])},
                'temperature(F)' : {'N' : str(tf)}
        }
    
    )
    print("Temperature:",tf)
    return 0
