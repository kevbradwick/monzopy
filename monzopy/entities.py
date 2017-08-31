from datetime import datetime


class Account:

    def __init__(self, data):
        props = ('id', 'description', 'type')
        for keyword in props:
            setattr(self, keyword, data[keyword] if keyword in data else None)

        time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        self.created = datetime.strptime(data['created'], time_format)

    def __repr__(self):
        return '<Account {}>'.format(self.id)