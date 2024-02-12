from core.http.models import User


class UserSeeder:
    def run(self):
        User.objects.create_user('998888112309', '2309')
