# Generated by Django 5.1.2 on 2024-10-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_blog_updated_at_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('TECH', 'Technology'), ('LIFE', 'Lifestyle'), ('TRVL', 'Travel'), ('EDU', 'Education'), ('FIN', 'Finance'), ('FOOD', 'Food'), ('STORY', 'Story'), ('OTH', 'Other')], max_length=10),
        ),
    ]
