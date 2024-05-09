from mfrc522 import SimpleMFRC522

#TODO: make exceptions when reading empty cards

reader = SimpleMFRC522()

id, text = reader.read()
print(f"card id: {id}")
print(f"written id: {text}")
