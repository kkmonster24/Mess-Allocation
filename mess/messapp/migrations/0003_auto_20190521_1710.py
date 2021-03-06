# Generated by Django 2.0.2 on 2019-05-21 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messapp', '0002_student_authent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniform_and_punctuality', models.IntegerField()),
                ('cleanliness_and_hygiene', models.IntegerField()),
                ('waste_disposal', models.IntegerField()),
                ('quality_of_ingredients', models.IntegerField()),
                ('overall_satisfaction_of_breakfast', models.IntegerField()),
                ('overall_satisfaction_of_lunch', models.IntegerField()),
                ('overall_satisfaction_of_dinner', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='feedback',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_student', to='messapp.Feedback'),
        ),
    ]
