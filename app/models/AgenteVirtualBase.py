from app import db 

class AgenteVirtualMain(db.Model):
    __tablename__ = 'agente_virtual'
    id_agenVitual = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_agent = db.Column(db.String(60), unique=True, nullable=False)
    level_access = db.Column(db.String(60), unique=True, nullable=False)
    status_agent = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f'<user {self.type_agent}>'