# package to index and search through articles, categories, and authors.
from django_elasticsearch_dsl import Document, fields
# registry of all the Document classes that will be used for indexing and searching.
from django_elasticsearch_dsl.registries import registry
from .models import Article, Category, Author

@registry.register_document
class AuthorDocument(Document):
    # id = fields.IntegerField()
    
    class Index:
        name = 'author'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Author
        fields = [
            'id',
            'name',
        ]
        
@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1, 
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'name',
            'description',
        ]
        
        
@registry.register_document
class ArticleDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    categories = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
        'description': fields.TextField(),
    })

    class Index:
        name = 'articles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Article
        fields = [
            'title',
            'content',
            'created_datetime',
            'updated_datetime',
        ]

