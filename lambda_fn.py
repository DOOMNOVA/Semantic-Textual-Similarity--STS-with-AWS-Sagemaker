import boto3
import json

def lambda_handler(event, context):

    # Create a Boto3 client for SageMaker
    client = boto3.client('sagemaker-runtime')

    # Set the name of the SageMaker endpoint to invoke
    endpoint_name = ENDPOINTNAME #  endpoint name 

    # Set the content type of the input data
    content_type = 'application/json'

    # Extract the input data from the incoming API Gateway event
      # Extract the input data from the incoming API Gateway event
    input_data = json.dumps(event, indent=2)

    # Convert the input data to JSON format
    payload = input_data.encode()

    # Invoke the SageMaker endpoint
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=payload
    )

    # Get the response from the SageMaker endpoint
    result = response['Body'].read().decode()
  

    # Return the result
    return result
