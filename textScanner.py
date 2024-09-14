import boto3

# Initialize the AWS Textract client with credentials
textract = boto3.client(
    'textract',
    region_name='us-west-2',  # Replace with your region
    aws_access_key_id='your_aws_access_key_id',
    aws_secret_access_key='your_aws_secret_access_key'
)

def analyze_document(image_path):
    """
    Analyze the document using AWS Textract to detect text and numeric data.
    
    :param image_path: Path to the image file.
    """
    with open(image_path, 'rb') as document:
        response = textract.detect_document_text(
            Document={'Bytes': document.read()}
        )
    
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            print(f"Detected text: {block['Text']}")
        elif block['BlockType'] == 'WORD':
            print(f"Detected word: {block['Text']}")
            if is_numeric(block['Text']):
                print(f"Numeric data found: {block['Text']}")

def is_numeric(value):
    """
    Check if a string represents a numeric value.
    
    :param value: String to check.
    :return: True if the string is numeric, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    image_path = 'image.jpg'  # Replace with your image file path
    analyze_document(image_path)
