

from haystack import indexes
from dobby.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    siteName = indexes.CharField(model_attr='sitename')


    def get_model(self):
        return Product