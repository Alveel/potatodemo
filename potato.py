import os
from flask import Flask, render_template
from markupsafe import escape
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Potato World!\n<br>\nヽ(･∀･)ﾉ'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/potato')
def potato():
    return render_template('potato.html')


@app.route('/tomato')
def tomato():
    return render_template('tomato.html')


@app.route('/vault')
def vault():
    key_vault_name = os.getenv("KEY_VAULT_NAME", "tst-ocp2-temp")

    kv_uri = f"https://{key_vault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)
    secret_name = "secret"
    # secret_name = input("Input a name for your secret > ")
    # secretValue = input("Input a value for your secret > ")
    # print(f"Creating a secret in {key_vault_name} called '{secret_name}' with the value '{secretValue}' ...")
    # client.set_secret(secret_name, secretValue)
    # print(f"Retrieving your secret from {key_vault_name}.")
    retrieved_secret = client.get_secret(secret_name)
    # print(f"Deleting your secret from {key_vault_name} ...")
    # poller = client.begin_delete_secret(secret_name)
    # deleted_secret = poller.result()
    return f"Your secret is '{retrieved_secret.value}'."


if __name__ == '__main__':
    app.run()
