from metadata import db


class Source(db.Model):
    __tablename__ = "SOURCE"
    __table_args__ = {'schema': 'BMAT'}

    source = db.Column(db.String(100), primary_key=True)
    id = db.Column(db.String(100), primary_key=True)
    iswc = db.Column(db.String(100), primary_key=True)

    def __init__(self, source, id, iswc):
        self.source = source
        self.id = id
        self.iswc = iswc