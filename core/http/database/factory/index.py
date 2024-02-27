from core.http.models import User, Post
from core.utils.factory import BaseFaker


class UserFactory(BaseFaker):
    model = User

    def handle(self):
        """Factory method"""

        return {
            "first_name": self.faker.first_name(),  # First name
            "username": self.faker.user_name(),  # User name
            "phone": self.faker.phone_number()  # phone
        }


class PostFactory(BaseFaker):
    model = Post

    def handle(self):
        return {
            "title": self.faker.name(),
            "desc": self.faker.text(),
            "image": self.faker.image_url()
        }
