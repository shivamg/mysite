from django.db import models
from djorm_pgarray.fields import ArrayField
#from djorm_expressions.models import ExpressionManager

class Product(models.Model):

    #created = models.DateTimeField(auto_now_add=True) #For REST interface
    prodid = models.CharField(max_length=255, primary_key=True, db_column='prodId') # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, db_column="name")
    sitename = models.CharField(max_length=255, blank=True, db_column= 'siteName') # Field name made lowercase.
    sku = models.CharField(max_length=255, blank=True, db_column = "sku")
    desc = models.CharField(max_length=255, blank=True, db_column = "desc")
    href = models.CharField(max_length=255, blank=True, db_column = "href")
    imghref = ArrayField(dbtype="varchar(255)", blank=True, db_column = "imgHref") # Field name made lowercase. This field type is a guess.
    origprice = models.FloatField(blank=True, db_column = "origPrice") # Field name made lowercase.
    price = models.FloatField(blank=True, db_column = "price")
    category = ArrayField(dbtype="varchar(255)", blank=True, db_column = "category") # This field type is a guess.
    tag = ArrayField(dbtype="varchar(255)", blank=True, db_column = "tag") # This field type is a guess.
    landingpage = models.CharField(max_length=255, db_column='landingPage', blank=True) # Field name made lowercase.
    landingroot = models.CharField(max_length=255, db_column='landingRoot', blank=True) # Field name made lowercase.
    landingcount = models.IntegerField(max_length=255, db_column='landingCount', blank=True) # Field name made lowercase.
    features = ArrayField(dbtype="varchar(255)", blank=True, db_column = "features") # This field type is a guess.
    delivery = ArrayField(dbtype="varchar(255)",  db_column = "delivery",blank=True) # This field type is a guess.
    emi = ArrayField(dbtype="varchar(255)", db_column = "emi", blank=True) # This field type is a guess.
    sizes = ArrayField(dbtype="varchar(255)", db_column = "sizes", blank=True) # This field type is a guess.
    brand = ArrayField(dbtype="varchar(255)", db_column = "brand", blank=True) # This field type is a guess.
    color = ArrayField(dbtype="varchar(255)", db_column = "color", blank=True) # This field type is a guess.
    owncat = ArrayField(dbtype="varchar(255)", db_column = "ownCat", blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'dirtydb'
        ordering = ('prodid',)
