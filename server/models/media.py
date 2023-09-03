from django.db import models


class Media(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="Inconnu")
    original_image = models.ImageField(upload_to='media/', null=True)
    converted_image = models.ImageField(
        upload_to='converted_media/', blank=True, null=True)
    conversion_type = models.CharField(max_length=255, blank=True)
    conversion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  # Utilisation du champ 'name' pour la représentation
        # sous forme de chaîne => admin django
