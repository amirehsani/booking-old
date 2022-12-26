from django.core.management import BaseCommand
from .models import CurrencyExchangeRate


def get_latest_exchange_rates():
    return [
        {'currency_from': 'USD', 'currency_to': 'IRR', 'rate': '400_00'}
    ]


# Update exchange rate
class Command(BaseCommand):
    def handle(self, *args, **options):
        latest_exchange_rate = get_latest_exchange_rates()

        updated_instances = []

        for new_exchange_rate in latest_exchange_rate:
            try:
                exchange_rate = CurrencyExchangeRate.objects.get(
                    currency_from=new_exchange_rate['currency_from'],
                    currency_to=new_exchange_rate['currency_to'],
                )
                exchange_rate.rate = new_exchange_rate['rate']
                updated_instances.append(exchange_rate)

            except CurrencyExchangeRate.DoesNotExist:
                CurrencyExchangeRate.objects.create(
                    currency_from=new_exchange_rate['currency_from'],
                    currency_to=new_exchange_rate['currency_to'],
                    rate=new_exchange_rate['rate'],
                )

