
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_alter_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at']},
        ),
    ]
