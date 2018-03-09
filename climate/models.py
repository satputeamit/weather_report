from django.db import models
from django.core.urlresolvers import reverse,reverse_lazy


class Country(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name

class MaxTemp(models.Model):

    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='max_countries')


    year=models.CharField(max_length=125,blank=True,null=True)
    jan=models.CharField(max_length=125,blank=True,null=True)
    feb=models.CharField(max_length=125,blank=True,null=True)
    mar=models.CharField(max_length=125,blank=True,null=True)
    apr=models.CharField(max_length=125,blank=True,null=True)
    may=models.CharField(max_length=125,blank=True,null=True)
    jun=models.CharField(max_length=125,blank=True,null=True)
    jul=models.CharField(max_length=125,blank=True,null=True)
    aug=models.CharField(max_length=125,blank=True,null=True)
    sep=models.CharField(max_length=125,blank=True,null=True)
    octo=models.CharField(max_length=125,blank=True,null=True)
    nov=models.CharField(max_length=125,blank=True,null=True)
    dec=models.CharField(max_length=125,blank=True,null=True)

    def __str__(self):
        return self.country.name +' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class MinTemp(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='min_countries')


    year=models.CharField(max_length=125,blank=True,null=True)
    jan=models.CharField(max_length=125,blank=True,null=True)
    feb=models.CharField(max_length=125,blank=True,null=True)
    mar=models.CharField(max_length=125,blank=True,null=True)
    apr=models.CharField(max_length=125,blank=True,null=True)
    may=models.CharField(max_length=125,blank=True,null=True)
    jun=models.CharField(max_length=125,blank=True,null=True)
    jul=models.CharField(max_length=125,blank=True,null=True)
    aug=models.CharField(max_length=125,blank=True,null=True)
    sep=models.CharField(max_length=125,blank=True,null=True)
    octo=models.CharField(max_length=125,blank=True,null=True)
    nov=models.CharField(max_length=125,blank=True,null=True)
    dec=models.CharField(max_length=125,blank=True,null=True)

    def __str__(self):
        return self.country.name +' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class MeanTemp(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='mean_countries')

    year=models.CharField(max_length=125,blank=True,null=True)
    jan=models.CharField(max_length=125,blank=True,null=True)
    feb=models.CharField(max_length=125,blank=True,null=True)
    mar=models.CharField(max_length=125,blank=True,null=True)
    apr=models.CharField(max_length=125,blank=True,null=True)
    may=models.CharField(max_length=125,blank=True,null=True)
    jun=models.CharField(max_length=125,blank=True,null=True)
    jul=models.CharField(max_length=125,blank=True,null=True)
    aug=models.CharField(max_length=125,blank=True,null=True)
    sep=models.CharField(max_length=125,blank=True,null=True)
    octo=models.CharField(max_length=125,blank=True,null=True)
    nov=models.CharField(max_length=125,blank=True,null=True)
    dec=models.CharField(max_length=125,blank=True,null=True)
    def __str__(self):
        return self.country.name +' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class Rainfall(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='rainfall_countries')

    year=models.CharField(max_length=125,blank=True,null=True)
    jan=models.CharField(max_length=125,blank=True,null=True)
    feb=models.CharField(max_length=125,blank=True,null=True)
    mar=models.CharField(max_length=125,blank=True,null=True)
    apr=models.CharField(max_length=125,blank=True,null=True)
    may=models.CharField(max_length=125,blank=True,null=True)
    jun=models.CharField(max_length=125,blank=True,null=True)
    jul=models.CharField(max_length=125,blank=True,null=True)
    aug=models.CharField(max_length=125,blank=True,null=True)
    sep=models.CharField(max_length=125,blank=True,null=True)
    octo=models.CharField(max_length=125,blank=True,null=True)
    nov=models.CharField(max_length=125,blank=True,null=True)
    dec=models.CharField(max_length=125,blank=True,null=True)
    def __str__(self):
        return self.country.name +' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class Sunshine(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='sunshine_countries')

    year=models.CharField(max_length=125,blank=True,null=True)
    jan=models.CharField(max_length=125,blank=True,null=True)
    feb=models.CharField(max_length=125,blank=True,null=True)
    mar=models.CharField(max_length=125,blank=True,null=True)
    apr=models.CharField(max_length=125,blank=True,null=True)
    may=models.CharField(max_length=125,blank=True,null=True)
    jun=models.CharField(max_length=125,blank=True,null=True)
    jul=models.CharField(max_length=125,blank=True,null=True)
    aug=models.CharField(max_length=125,blank=True,null=True)
    sep=models.CharField(max_length=125,blank=True,null=True)
    octo=models.CharField(max_length=125,blank=True,null=True)
    nov=models.CharField(max_length=125,blank=True,null=True)
    dec=models.CharField(max_length=125,blank=True,null=True)

    def __str__(self):
        return self.country.name +' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})


#Max temp, Min temp, Mean temp, Sunshine,
#and Rainfall for UK, England, Wales, and Scotland regions.
