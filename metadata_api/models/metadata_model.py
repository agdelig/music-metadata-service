from metadata import db


class Metadata(db.Model):
    __tablename__ = "METADATA"
    __table_args__ = {'schema': 'BMAT'}

    title = db.Column(db.String(100))
    iswc = db.Column(db.String(100), primary_key=True)

    def __init__(self, title, iswc):
        self.title = title
        self.iswc = iswc