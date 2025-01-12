# Generated by Django 5.1.2 on 2024-10-17 18:15

import django.db.models.deletion
import upload.file_validation
import upload.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sirket_tipi', models.CharField(max_length=10)),
                ('Kurulus_sozlemesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Vergi_levhasi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Ticaret_sicil_gazetesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Imza_sirkuleri', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Oda_kayit_belgesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Yetki_belgesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Faaliyet_belgesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Calisma_ruhsati_izinler', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Sirketin_mali_bilgileri', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('Ticaret_sicil_tasdiknamesi', models.FileField(blank=True, upload_to=upload.models.upload_to_company_folder, validators=[upload.file_validation.validate_file_extension])),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('Sirket_adi', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
