# -*- coding: utf-8 -*-

from flask_restplus import Api, Resource
from flask import Flask

app = Flask(__name__)
api = Api(app, version='1.0', title=u'API超市', description=u'-- API Created by Allen',
          doc='/api', default='UserApi', default_label='')


@api.route('/resource/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {'name': 'rpj'}

    @api.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        api.abort(403)


if __name__ == '__main__':
    app.run()
