from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self,email , password = None ,**extra_feilds): #extra_feilds: 將其他多傳遞的參數pass them into extra fields
        """ Creates and saves a new user"""
        user = self.model(email = self.normalize_email(email),**extra_feilds)
        user.set_password(password)  #password be encrypted
        user.save( using = self._db)

        return user
class User(AbstractBaseUser,PermissionsMixin): 
    """Custom user model that supports using email instead of username """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
