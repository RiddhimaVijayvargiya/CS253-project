# Generated by Django 5.1.7 on 2025-03-24 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostNFound', '0003_remove_lostitem_image_chat_message'),
        ('marketplace', '0002_alter_itemcategory_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='started_at',
            new_name='created_at',
        ),
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lostnfound_received_chats', to='marketplace.profile'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lostnfound_sent_chats', to='marketplace.profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lostnfound_messages', to='marketplace.profile'),
        ),
        migrations.RemoveField(
            model_name='chat',
            name='last_message_time',
        ),
    ]
