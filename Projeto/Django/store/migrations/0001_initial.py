# Generated by Django 3.1.4 on 2021-09-29 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(db_index=True, max_length=255)),
                ('slugCategoria', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=255)),
                ('autor', models.CharField(default='Administrador', max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('slug', models.SlugField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('em_estoque', models.BooleanField(default=True)),
                ('disponivel', models.BooleanField(default=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='store.categoria')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador_produto', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'ordering': ('-criado',),
            },
        ),
    ]
