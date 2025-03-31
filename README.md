# AfroMessage SDK

A Python wrapper for the AfroMessage SMS service API that allows you to easily integrate SMS capabilities into your applications.

## About This Project

AfroMessage SDK is a lightweight Python library that provides an easy-to-use interface for the AfroMessage SMS API. With this SDK, you can:

- Send single SMS messages
- Send bulk SMS messages
- Generate and send security codes (OTPs)
- Verify security codes

The library handles authentication, request formatting, and error handling to streamline your integration with AfroMessage's services.

## Installation

You can install the AfroMessage SDK using pip:

```bash
pip install afromessage-service
```

## Requirements

- Python 3.6+
- httpx

## Getting Started

### Authentication

To use the AfroMessage SDK, you'll need:
- Your AfroMessage Identifier ID
- Your sender name
- Your authentication token
- Optional callback URL

### Basic Usage

```python
from afromessage_service import AfroMessage

# Initialize the AfroMessage client
afro_client = AfroMessage(
    IdentifierId='your-identifier-id',
    senderName='YourCompany',
    auth_token='your-auth-token',
    callbackUrl='https://your-callback-url.com/webhook'
)
```

## Examples

### Sending a Single SMS

```python
# Send a single SMS message
response = afro_client.sendMessage(
    to='+251912345678',
    message='Hello from AfroMessage SDK!'
)

# Check response
if response.status_code == 200:
    print("Message sent successfully!")
    print(response.json())
else:
    print(f"Failed to send message: {response.text}")
```

### Sending Bulk SMS Messages

```python
# Method 1: Different messages to different recipients
response = afro_client.sendBulkMessage(
    messageList=[
        {
            'to': '+251912345678',
            'message': 'Hello User 1!'
        },
        {
            'to': '+251987654321',
            'message': 'Hello User 2!'
        }
    ],
    campaignTitle='Welcome Campaign',
    createCallback="https://your-domain.com/create-callback",
    statusCallback="https://your-domain.com/status-callback"
)

# Method 2: Same message to multiple recipients
response = afro_client.sendBulkMessage(
    messageList=[
        {'to': '+251912345678'},
        {'to': '+251987654321'}
    ],
    campaignMessage='Same message to everyone!',
    campaignTitle='Announcement Campaign'
)

# Check response
print(response.json())
```

### Generating and Sending Security Codes (OTP)

```python
# Generate and send a security code
response = afro_client.sendSecurityCode(
    to='+251912345678',
    codeLength=4,  # Length of the security code
    codeType=0,    # Type of code (0 = numeric, 1 = alphanumeric)
    expires_after=300  # Expiry time in seconds
)

if response.status_code == 200:
    verification_code = response.json().get('vc')
    print(f"Security code sent successfully. Verification code: {verification_code}")
else:
    print(f"Failed to send security code: {response.text}")
```

### Verifying Security Codes

```python
# Verify a security code
response = afro_client.verifyCode(
    to='+251912345678',
    vc='verification-code-from-sendSecurityCode',
    code='1234'  # The code the user entered
)

if response.status_code == 200:
    result = response.json()
    if result.get('success'):
        print("Code verified successfully!")
    else:
        print("Invalid code or verification failed.")
else:
    print(f"Error during verification: {response.text}")
```

## API Reference

### AfroMessage Class

```python
AfroMessage(IdentifierId, senderName, auth_token, callbackUrl)
```

#### Parameters:
- `IdentifierId` (str): Your AfroMessage identifier ID
- `senderName` (str): The name that will appear as the sender
- `auth_token` (str): Your AfroMessage authentication token
- `callbackUrl` (str): URL for delivery status callbacks

### Methods

#### `sendMessage(to, message)`
Send a single SMS message.

#### `sendBulkMessage(messageList, campaignTitle="", campaignMessage="", createCallback="", statusCallback="")`
Send bulk SMS messages.

#### `sendSecurityCode(to, codeLength=4, codeType=0, expires_after=0, pr="", ps="", sb=0, sa=0)`
Generate and send a security code.

#### `verifyCode(to, vc, code)`
Verify a security code.

## Error Handling

The SDK returns httpx Response objects that include status codes and response content. You should always check the status code to ensure successful API calls:

```python
response = afro_client.sendMessage(to='+251912345678', message='Hello!')
if response.status_code == 200:
    # Success
    print(response.json())
else:
    # Error
    print(f"Error: {response.status_code} - {response.text}")
```

## Contributing

Contributions to the AfroMessage SDK are welcome! If you'd like to contribute, please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/p4ndish/afromessage_service.git
cd afromessage_service

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Links

- [AfroMessage Official Website](https://afromessage.com)
- [GitHub Repository](https://github.com/p4ndish/afromessage_service) 
