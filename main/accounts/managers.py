from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self , phone , username , password):
        if not phone:
            raise ValueError('Phone is required...')
        if not username:
            raise ValueError('username is required...')
        
        user = self.model(
            phone = phone,
            username = username
        )

        user.set_password(password)

        user.save(using = self._db)
        return user
    
    def create_superuser(self , phone , username , password):
        user = self.create_user(phone , username , password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
