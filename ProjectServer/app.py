from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []


@app.route('/')
def hello():
    return '''Messenger Flask is running! 
            <br> <a href="/status">Check Status</a>'''


@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }


@app.route('/api/Messanger', methods=['POST'])
def sendmessage():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)
    print(msg)
    print(type(msg))
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение {msg['MessageText']}")
    return f"Сообщение отправлено успешно. Всего сообщений: {len(ListOfMessages)}", 200


@app.route('/api/Messanger/<int:id>')
def getmessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400



if __name__ == '__main__':
    app.run()
