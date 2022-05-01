from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(_("slug"), unique=True, null=False)
    content = models.TextField(_("content"))
    # recipeCategory = models.ManyToManyField('RecipeCategory')
    # recipeCuisine = 	The cuisine of the recipe (for example, French or Ethiopian)
    ingredients = models.ManyToManyField("Ingredient", 
                                         through='IngredientsList', 
                                         verbose_name=_("ingredients"))
    kitchenware = models.ManyToManyField("Kitchenware", verbose_name=_("Kitchenware"))
    instructions = models.TextField(_("instructions"), help_text="Steps separator is semi-colon")
    class Meta:
        verbose_name = _("recipe")
        verbose_name_plural = _("recipes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"slug": self.slug})

class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(_("slug"), unique=True, null=False)
    content = models.TextField(_("content"))
    # Hierarchy and tags
    # Photo

    class Meta:
        verbose_name = _("ingredient")
        verbose_name_plural = _("ingredients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={"pk": self.pk})


class Unit(models.Model):

    name = models.CharField(max_length=64, unique=True)
    symbol = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = _("unit")
        verbose_name_plural = _("units")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("unit_detail", kwargs={"pk": self.pk})


class IngredientsList(models.Model):

    qty = models.FloatField(_("quantity"))
    unit = models.ForeignKey('Unit', related_name='unit', on_delete=models.PROTECT)
    ingredient = models.ForeignKey("Ingredient", verbose_name=_("ingredient"), on_delete=models.PROTECT)
    recipe = models.ForeignKey("Recipe", verbose_name=_("recipe"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ingredients list")
        verbose_name_plural = _("ingredients lists")

    def __str__(self):
        return f"{self.qty} {self.unit} of {self.ingredient}"


class Kitchenware(models.Model):

    name = models.CharField(_("name"), max_length=32)
    content = models.TextField(_("content"), null=True, blank=True)
    # icon =

    class Meta:
        verbose_name = _("kitchenware")
        verbose_name_plural = _("kitchenwares")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("kitchenware_detail", kwargs={"pk": self.pk})

class Package(models.Model):

    name = models.CharField(_("name"), max_length=64)
    meals = models.ManyToManyField("Recipe", related_name='recipe', verbose_name=_("meals"))

    class Meta:
        verbose_name = _("package")
        verbose_name_plural = _("packages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("package_detail", kwargs={"pk": self.pk})



class BlogPost(models.Model):

    title = models.CharField(max_length=128)
    publish_date = models.DateTimeField(_("publish date"), blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    short_content = models.TextField(_("short content"))
    content = models.TextField(_("content"))


    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("BlogPost_detail", kwargs={"pk": self.pk})
