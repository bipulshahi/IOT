def lambda_handler(event,context):
    tf = event['T']*9/5 + 32
    print('Temperature:',tf)
    return 0
