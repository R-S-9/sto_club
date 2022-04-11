class SetNewPassword:
    @staticmethod
    def set_new_password(user, new_password):
        user.set_password(new_password)
        user.save()

        return True
