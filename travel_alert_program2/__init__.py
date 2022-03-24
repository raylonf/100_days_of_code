from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
data_manager.update_destination_codes()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "GRU"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination[0],
        from_time='01/08/2022',
        to_time='10/08/2022'
    )

    if flight is None:
        continue

    if flight.price < destination[2]:
        message = f"Low price alert! Only £{flight.price} to fly from "
        f'{flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-'
        f'{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.'

        if flight.stop_overs > 0 :
            message += f'\nFlight has {flight.stop_overs} stop over, via {flight.via_city}.'
            print(message)

        notification_manager.sendEmail(email_to='raylon.f@hotmail.com', msg=message)