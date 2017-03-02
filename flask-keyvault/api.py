from flask import Flask
from azurekeyvault import AzureKeyVaultManager

app = Flask(__name__)

@app.route("/")
def hello():
    secret = kv.getSecretFromKeyVault('foo', 'df0505d64bdd401fb06cebe19c8ad2b3')
    return secret

if __name__ == "__main__":
    kv = AzureKeyVaultManager()
    kv.initialize()
    app.run()
