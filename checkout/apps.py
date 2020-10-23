from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals

# Custom ready method, this must be referenced in the __init__ file of this module
# if not referenced, the signals file that ready() references would not work
