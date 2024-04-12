from django.contrib import admin
from .models import Neighborhood, PropertyType, SaleStatus, Listing, Agent

admin.site.register(Neighborhood)
admin.site.register(PropertyType)
admin.site.register(SaleStatus)
admin.site.register(Listing)
admin.site.register(Agent)

