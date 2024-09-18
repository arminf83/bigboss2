from django.contrib.auth.models import UserManager

class CustomUsermanager(UserManager):
    
    
    def _create_user(self,email,password,**extra_fields):
    
    
        if not email:
            raise ValueError('email must be provided')

        user = self.model(email= email , **extra_fields)
        user.set_password(password)
        user.save(using=self.db)



    def create_user(self, email=None , password=None , **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)
    
    
    def create_superuser(self, email=None , password=None , **extra_fields ):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password , **extra_fields)