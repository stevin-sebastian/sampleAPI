import json, falcon

class objectReq:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = json.loads(req.stream.read())

        content = {
            'name': 'Stevin',
            'age': '22',
            'country': 'India'
        }
        output = {}

        if('method' not in data):
            resp.status = falcon.HTTP_501
            output['value'] = 'Error: No method found'
        else:
            if(data['method']=='get-name'):
                output['value'] = content['name']
            elif(data['method']=='get-age'):
                output['value'] = content['age']
            elif(data['method']=='get-country'):
                output['value'] = content['country']
            else:
                resp.status = falcon.HTTP_404
                output['value'] = None

        resp.text= json.dumps(output,ensure_ascii=False)


    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        sum = data['x'] + data['y']

        output = {
            "Message" : 'x: {x} + y: {y} is equal to {s}'.format(x=data['x'], y=data['y'], s=sum)
        }

        resp.text= json.dumps(output,ensure_ascii=False)

api = falcon.App()
api.add_route('/test', objectReq())
