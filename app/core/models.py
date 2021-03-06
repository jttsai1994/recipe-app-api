from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self,email , password = None ,**extra_feilds): #extra_feilds: 將其他多傳遞的參數pass them into extra fields
        """ Creates and saves a new user"""
        if not email:
            raise ValueError("User must have email address")
        user = self.model(email = self.normalize_email(email),**extra_feilds)
        user.set_password(password)  #password be encrypted
        user.save( using = self._db)

        return user
    def create_superuser(self,email,password):
        """Create and saves a new super user"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
class User(AbstractBaseUser,PermissionsMixin): 
    """Custom user model that supports using email instead of username """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
