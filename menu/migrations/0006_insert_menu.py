import django.db.models.deletion
from django.db import migrations, models


def insert_initial_products(apps, schema_editor):
    Product = apps.get_model('menu', 'Product')
    Category = apps.get_model('menu', 'Category')

    # Add initial categories
    bebidas = Category.objects.create(name='Bebidas', available=True)
    salgados = Category.objects.create(name='Salgados', available=True)
    pratos = Category.objects.create(name='Pratos', available=True)
    sobremesas = Category.objects.create(name='Sobremesas', available=True)

    # Define your initial product data
    products = [
        # Bebidas
        {
            'name': 'Coca Cola 300ml',
            'description': 'Latinha de coca normal',
            'category': bebidas,
            'price': '3.50',
            'image_url': 'https://maissabor.pt/cdn/shop/products/3200000216_COCA-COLA_LATA_33CL_1f1313f6-ef7c-4df0-ad1f-48058002b580_1080x.jpg?v=1641402470',
            'available': True,
        },
        {
            'name': 'Agua 400ml',
            'description': 'Garrafa de agua fresquinha',
            'category': bebidas,
            'price': '3',
            'image_url': 'https://carrefourbrfood.vtexassets.com/arquivos/ids/201123/8229260_1.jpg?v=637272447931570000',
            'available': True,
        },
        {
            'name': 'Suco de Laranja Natural 300ml',
            'description': 'Suco de laranja espremido na hora',
            'category': bebidas,
            'price': '4.50',
            'image_url': 'https://storage.googleapis.com/domain-images/06c5ca84-e308-4cad-8b0a-ece554dd990c/products/gallery_ffd2e63a-a707-4c47-9380-55f375e97df1.jpg',
            'available': True,
        },
        # Salgados
        {
            'name': 'Coxinha de frango',
            'description': 'Coxinha de frango recheado e catupiry',
            'category': salgados,
            'price': '5',
            'image_url': 'https://lh6.googleusercontent.com/proxy/EeEwfLnrCxMI0I4zL7tCSXEkbzRWFpIXD-wsB7nFcQQPVRVe9y9tLxXy3VszaUuwImiAhihPvAvZXcEYZWolD_B-MNmdRX0r5uecfxuGVdNI_DC7lgJunwzFToQTAr0GsBZyThZ51sCL_H2wtAZtSw',
            'available': True,
        },
        {
            'name': 'Empada de Calabresa',
            'description': 'Empadinha de frango feita na casa, com recheio de calabresa',
            'category': salgados,
            'price': '5.50',
            'image_url': 'https://www.massottisalgados.com.br/wp-content/uploads/2017/05/empada-calabresa-assado-massotti.jpg',
            'available': True,
        },
        {
            'name': 'Esfiha de Carne com queijo',
            'description': 'Esfiha árabe com recheio de carne e queijo mussarela',
            'category': salgados,
            'price': '5',
            'image_url': 'https://www.inglesescongelados.com.br/wp-content/uploads/2021/08/Ficha-T%C2%AEcnica-Esfirra-de-Carne_03.09.18-.png',
            'available': True,
        },
        # Pratos
        {
            'name': 'Filé de frango',
            'description': 'Arroz, feijão, batata frita, filé de frango grelhado e salada.',
            'category': pratos,
            'price': '32',
            'image_url': 'https://as1.ftcdn.net/v2/jpg/04/52/02/32/1000_F_452023294_GGha6a7JWrCz6pIJ8uAvtCa8VpiaySGy.jpg',
            'available': True,
        },
        {
            'name': 'Filé de frango a parmegiana',
            'description': 'File de frango aparmegiana com muzzarela, fritas e arroz.',
            'category': pratos,
            'price': '35',
            'image_url': 'https://www.zappas.com.br/image/cache/catalog/produtos/Pratos/Prato%202%20-%20Fil%C3%A9%20de%20Frango%20%C3%A0%20Parmegiana-800x800.jpg',
            'available': True,
        },
        {
            'name': 'Feijoada Completa p/ 2 pessoas',
            'description': 'Feijoada completa com pratos separados feita idealmente para 2 pessoas',
            'category': pratos,
            'price': '50',
            'image_url': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOGCt4Tv91eCVR3h9TqkbN_ne_4jhrel_Jf8PZq2Rh0OgL2BODgqolInArJc9MkheYlJXPn3znImyzm0xqYF06iRXPO7lZRT0NrGSgiHQNct7Uaa8jQutuZOdjCgkoYc_uliyukz_w3dFl/s1600/feij+table.jpg',
            'available': True,
        },
        # Sobremesas
        {
            'name': 'Pudim de leite',
            'description': 'Pudim de leite condensado',
            'category': sobremesas,
            'price': '15',
            'image_url': 'https://s2-receitas.glbimg.com/jK-kMTPr3Yzex9P93zqt4DSsFXo=/0x0:1366x768/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_1f540e0b94d8437dbbc39d567a1dee68/internal_photos/bs/2023/z/0/RsipkzTEu0Y1PGiavCpA/pudim-de-leite-condensado.jpg',
            'available': True,
        },
        {
            'name': 'Bolo de brigadeiro',
            'description': 'Description for Product 2',
            'category': sobremesas,
            'price': '10',
            'image_url': 'https://conteudo.imguol.com.br/2015/03/04/bolo-de-brigadeiro-da-carole-crema-1425505346330_1920x1292.jpg',
            'available': True,
        },
        {
            'name': 'Doce de figo em calda',
            'description': 'Description for Product 2',
            'category': sobremesas,
            'price': '15.50',
            'image_url': 'https://www.atacadaodascastanhas.com.br/icontrole/files/1687363260957_doce-de-figo-em-calda.webp',
            'available': True,
        },

    ]

    # Insert products into the Product table
    for product_data in products:
        Product.objects.create(**product_data)


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0005_order_orderitem"),
    ]

    operations = [
        migrations.RunPython(insert_initial_products),
    ]

