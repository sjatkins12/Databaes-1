from django.db import models


# Create your models here.

class Category(models.Model):
    """
    Fields-
    1. category_name- Name of the category
    2. Foreign Keys:
    Relationships-
    1. One to Many with Subcategory                         --In 'Subcategory' Model
    """
    category_name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    """
    1. subcategory_name- Name of the subcategory
    2. category_name- Name of the category that holds this subcategory
    3. Foreign Keys:
    Relationships-
    1. One to Many with Category                            --In This Model
    2. One to Many with Interest Group                      --In This Model
    """
    subcategory_name = models.CharField(max_length=30, primary_key=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name


class InterestGroup(models.Model):
    """
    Fields-
    1. interest_id- Primary key (Identifier) of Interest Group
    2. interest_group_name- Name of the interest_group
    3. subscription_cost- Monthly price of a box
    4. subcategory_name- Name of subcategory that holds this interest_group
    5. Foreign Keys:
    Relationships-
    1. Many to Many with User                           --In 'User' Model
    2. One to Many with Discussion                      --In 'Discussion' Model
    3. One to Many with Subcategory                     --In This Model
    4. Many to Many with Item                           --In this Model
    5. Many to One with Box                             --In 'Box' Model
    """
    # TODO: Potentially Change Relationship #5 to Many to One
    interest_id = models.IntegerField(primary_key=True)
    interest_group_name = models.CharField(max_length=30)
    subscription_cost = models.DecimalField(max_digits=6, decimal_places=2)
    subcategory_name = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    have = models.ManyToManyField('Crate.Item')

    def __str__(self):
        return '{} {}'.format(self.interest_id, self.interest_group_name)


class Votes(models.Model):
    """
    Fields-
    1. item_id- Identifier of item which is being voted on
    2. selling_cycle- Identifier of which cycle the item is being sold in
    3. vote_score- Number of votes for the give item in the given cycle
    4. Foreign Keys:
    Relationships-
    1. One to Many with Item                        --In This Model
    2. One to Many with Selling Cycle               --In This Model
    """
    item_id = models.ForeignKey('Crate.Item', on_delete=models.CASCADE)
    selling_cycle = models.ForeignKey('Crate.SellingCycle', on_delete=models.CASCADE)
    vote_score = models.IntegerField(default=0)

    # Gives guarantee that an item in two selling cycles can be voted on
    class Meta:
        unique_together = ('item_id', 'selling_cycle')

    def __str__(self):
        return '{} {} {}'.format(self.item_id, self.selling_cycle, self.vote_score)


class SellingCycle(models.Model):
    """
    Fields-
    1. cycle_date- Date (Start of month for the cycle
    2. Foreign Keys:
    Relationships-
    1. One to Many with Box                         --In 'Box' Model
    2. Many to Many with Item                       --In 'Item' Model
    """
    cycle_date = models.DateField(primary_key=True)

    def __str__(self):
        return self.cycle_date


class Box(models.Model):
    """
    Fields-
    1. id = models.AutoField(primary_key=True) is created by default
    2. 4 Foreign Keys to the Tables
    models.ForeignKey(<Model>, on_delete=models.ON_CASCADE)
    Relationships-
    1. Many to Many with User                       --In 'User Profile' Model
    2. Many to One with Selling Cycle               --In This Model
    3. Many to Many with Items                      --In 'Item' Model
    4. Many to One with Interest Groups             --In This Model
    """
    box_id = models.IntegerField(primary_key=True)
    sold_during = models.ForeignKey(SellingCycle, on_delete=models.CASCADE)
    type = models.ForeignKey(InterestGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.box_id


class Item(models.Model):
    """
    Fields-
    1. id = models.AutoField(primary_key=True) is created by default
    2. item_name- Name of item (String)
    3. item_Description- Description of the item (String)
    4. item_quantity- Number of items in stock (Integer)
    5. price_per_item- Price to sell an item (Decimal)
    6. Foreign Keys:
    Relationships-
    Many to Many with Interest Group                --In 'Interest_Group' Model
    Many to Many with Box                           --In This Model
    Ternary Relationship with Supplier and Orders   --In This Model
    Many to Many with Selling Cycle                 --In This Model
    """
    item_name = models.CharField(max_length=40)
    item_description = models.CharField(max_length=500)
    item_quantity = models.IntegerField(default=0)
    price_per_item = models.DecimalField(max_digits=6, decimal_places=2)
    contained_in = models.ManyToManyField(Box)
    sold_by = models.ManyToManyField('inventory.Supplier', through='inventory.SellingOrder')
    sold_in = models.ManyToManyField(SellingCycle)

    def __str__(self):
        return '{} {}'.format(self.id, self.item_name)
