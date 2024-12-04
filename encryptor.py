import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import sys

load_dotenv()
fernet = Fernet(os.getenv('FERNET_KEY'))

day = sys.argv[1]
operation = sys.argv[2]

if operation == 'e':
    with open(f'input/input_day{day}.txt', 'r') as file:
        content = file.read()
    encMessage = fernet.encrypt(content.encode())
    # Write the encrypted content as raw bytes
    with open(f'input/public_input_day{day}.txt', 'wb') as file:
        file.write(encMessage)

elif operation == 'd':
    with open(f'input/public_input_day{day}.txt', 'rb') as file:
        encMessage = file.read()
    decMessage = fernet.decrypt(encMessage).decode()
    with open(f'input/input_day{day}.txt', 'w') as file:
        file.write(decMessage)

else:
    print("Invalid operation. Use 'e' for encrypt or 'd' for decrypt.")
