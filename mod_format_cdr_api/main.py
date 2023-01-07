from flask import Flask, request, jsonify, json
import json

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/cdr', methods=['GET', 'POST'])
@app.route('/cdr/<uuid>', methods=['GET', 'POST'])
def get_cdrs():
    data = request.form
    data = dict(data)
    cdr = data['cdr']
    data = json.loads(cdr)

    '''
    print("---------------------------- START -------------------------------\n\n")
    print("keys ===> ", data.keys(), "\n\n")
    print("core-uuid ---> ", data['core-uuid'], "\n\n")
    print("switchname  ---> ", data['switchname'], "\n\n")
    print("channel_data ---> ", data['channel_data'],"\n\n")
    print("callStats ---> ", data['callStats'], "\n\n")
    print("variables ---> ", data['variables'], "\n\n")
    print("callflow ---> ", data['callflow'],  "\n\n")
    print("---------------------------- STOP -------------------------------\n\n")
    '''

    variables = data['variables']
    print('uuid: ', variables['uuid'])
    print('sip_from_user: ', variables['sip_from_user'])
    print('domain_name: "', variables['domain_name'])
    print('tenant_id: ', variables['tenant_id'])
    print('start_stamp: ', variables['start_stamp'])
    print('profile_start_stamp: ', variables['profile_start_stamp'])
    try:
        print('answer_stamp: ', variables['answer_stamp'])
    except KeyError:
        print('answer_stamp: ' + ": " + "missing")
    try:
        print('progress_media_stamp: ', variables['progress_media_stamp'])
    except KeyError:
        print('progress_media_stamp: ' + ": " + "missing")
    print('end_stamp: ', variables['end_stamp'])
    print('start_epoch: ', variables['start_epoch'])
    print('profile_start_epoch: ', variables['profile_start_epoch'])
    print('answer_epoch: ', variables['answer_epoch'])
    print('progress_media_epoch: ', variables['progress_media_epoch'])
    print('end_epoch: ', variables['end_epoch'])
    print('duration: ', variables['duration'])
    print('billsec: ', variables['billsec'])
    print('\n\n')

    items = ['uuid', 'sip_from_user', 'domain_name', 'tenant_id', 'start_stamp',
            'profile_start_stamp', 'answer_stamp', 'progress_media_stamp', 'end_stamp',
            'start_epoch', 'profile_start_epoch', 'answer_epoch', 'progress_media_epoch',
            'end_epoch', 'duration', 'billsec']

    with open('/app/cdr.txt', 'a') as f:
        for item in items:
            try:
                f.write(item + ": " +  str(variables[item]) + "\n")
            except KeyError:
                f.write(item + ": " + "missing \n")
        f.write('\n\n')

        f.write("FULL CDR: \n\n")

        for k, v in data.items():
            if type(v) is dict:
                for a, b in v.items():
                    #print(a,": ",  b)
                    f.write(str(a) + ": " +  str(b) + "\n")
        f.write('\n\n')

    return "ok\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

