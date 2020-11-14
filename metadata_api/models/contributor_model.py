from metadata import db


class Contributor(db.Model):
    __tablename__ = "CONTRIBUTOR"
    __table_args__ = {'schema': 'BMAT'}

    contributor = db.Column(db.String(100), primary_key=True)
    iswc = db.Column(db.String(100), primary_key=True)

    def __init__(self, contributor, iswc):
        self.contributor = contributor
        self.iswc = iswc