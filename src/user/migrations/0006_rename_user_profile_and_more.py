# Generated by Django 4.0.6 on 2022-11-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_author_alter_comment_blog_user_id_and_more'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('order', '0002_alter_card_user_id_alter_wish_list_user_id'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0005_delete_profile_user_groups_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
        migrations.RemoveIndex(
            model_name='profile',
            name='user_user_first_n_45e159_idx',
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['first_name'], name='user_profil_first_n_3b622f_idx'),
        ),
    ]