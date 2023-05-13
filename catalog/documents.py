from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from catalog.models import Product, SubCategory, Category


@registry.register_document
class ProductDocument(Document):
    brand = fields.TextField(
        attr="brand",
        fields={
            "raw": fields.TextField(),
            "suggest": fields.CompletionField(),
        },
    )
    title = fields.TextField(
        attr="title",
        fields={
            "raw": fields.TextField(),
            "suggest": fields.CompletionField(),
        },
    )
    sub_category = fields.ObjectField(
        attr="sub_category",
        properties={
            "title": fields.TextField(
                attr="title",
                fields={
                    "raw": fields.KeywordField(),
                },
            )
        },
    )

    class Index:
        name = "products"

    class Django:
        model = Product
