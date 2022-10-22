import faker

from users.models import CustomUser
from faker import Faker


class Test:

    def __init__(self):
        self.fake = Faker()

    def add_fake_users(self, n):
        for entry in range(n):
            first_name, last_name = self.fake.name().split()
            username = last_name + first_name
            fake_user, __ = CustomUser.objects.get_or_create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=self.fake.password(),
             )
            # fake_user.save()


if __name__ == "__main__":
    test = Test()
    test.add_fake_users(1)
