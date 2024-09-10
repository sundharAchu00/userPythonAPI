from models.user import User


class UserDAO:
    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def add_user(name, email):
        user = User(name=name, email=email)
        user.save()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.objects.filter(id=user_id).first()
        if user:
            user.delete()
            return True
        return False
