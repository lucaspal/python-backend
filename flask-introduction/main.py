from flask import Flask, request

app = Flask(__name__, static_folder="./static", static_url_path="")
app.debug = True


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name') or 'Stranger'
    return {'dataString': 'Hello {name} from Flask!!'.format(name=name)}


@app.route('/user-details/new', methods=['POST'])
def members():
    session_id = request.form.get('sessionId')
    username = request.form.get('username')
    content = request.form.get('content')

    save_to_file(session_id, username, content)
    return 'OK'


def save_to_file(file_name, first_param, second_param):
    full_name = f'./csv/{file_name}'
    with open(full_name, 'a+') as file:
        file.write(f'{first_param},{second_param}\n')


if __name__ == "__main__":
    app.run()
