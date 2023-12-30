class R(object):

    def success(msg=None, data=None):
        result = {
            'code': 200,
            'msg': msg,
            'data': data
        }
        return result

    def fail(msg=None, data=None):
        result = {
            'code': 201,
            'msg': msg,
            'data': data
        }
        return result