import dataclasses


@dataclasses.dataclass
class User:
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    id: str = ""

    def get_reg_data(self):
        return {
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'password': self.password
        }

    def get_credentials(self):
        return {
            'email': self.email,
            'password': self.password
        }

    def get_info(self):
        return {
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'id': self.id
        }

    def __repr__(self):
        return f'<User: id={self.id}; username={self.username}; email={self.email}>'
