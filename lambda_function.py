import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Hello DevOps Pro Lambda Function
    Returns a friendly greeting with request information
    """
    try:
        # Log the incoming event
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Extract information from the event
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        user_agent = event.get('headers', {}).get('User-Agent', 'Unknown')
        
        # Prepare response
        response_body = {
            "message": "Hello DevOps Pro!",
            "status": "success",
            "request_details": {
                "http_method": http_method,
                "path": path,
                "user_agent": user_agent
            },
            "deployment_info": {
                "pipeline": "AWS CodePipeline",
                "build_system": "AWS CodeBuild",
                "function": "hello-devops-pro-lambda"
            }
        }
        
        # Return successful response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_body)
        }
        
    except Exception as e:
        # Log the error
        logger.error(f"Error processing request: {str(e)}")
        
        # Return error response
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                "message": "Internal server error",
                "error": str(e)
            })
        }

# Additional utility function for testing
def test_handler():
    """Test function for local development"""
    test_event = {
        'httpMethod': 'GET',
        'path': '/hello',
        'headers': {
            'User-Agent': 'TestClient/1.0'
        }
    }
    
    result = lambda_handler(test_event, None)
    print("Test result:", result)
    return result

if __name__ == "__main__":
    # Run test when executed locally
    test_handler()
