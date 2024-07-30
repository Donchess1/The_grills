from django.apps import AppConfig


class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self):
        import shop.signals

class GrillzConfig(AppConfig):
    name = 'grillz'
