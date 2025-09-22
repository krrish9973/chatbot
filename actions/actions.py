import random
import time
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConfirmBooking(Action):
    def name(self) -> Text:
        return "action_confirm_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name") or "Guest"
        number_of_guests = tracker.get_slot("number_of_guests") or "unknown number of"
        start_date = tracker.get_slot("start_date") or "unknown date"
        end_date = tracker.get_slot("end_date") or "unknown date"
        payment_method = tracker.get_slot("payment_method") or "unknown method"
        meal = tracker.get_slot("meal_preference") or "No Selection"
        print(meal)

        message = f"Great! I've reserved a room under the name {name} for {number_of_guests} guest(s), from {start_date} to {end_date}.And You have selected the Meal: {meal}\n The selected payment method is {payment_method}. Could you please confirm if everything is correct?"

        dispatcher.utter_message(text=message)
        return []

class ActionBookingSummary(Action):
    def name(self) -> Text:
        return "action_booking_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name") or "Guest"
        number_of_guests = tracker.get_slot("number_of_guests") or "unknown number of"
        start_date = tracker.get_slot("start_date") or "unknown date"
        end_date = tracker.get_slot("end_date") or "unknown date"
        payment_method = tracker.get_slot("payment_method") or "unknown method"
        booking_id = str(int(time.time())) + str(random.randint(10, 99))
        meal = tracker.get_slot("meal_preference") or "No Selection"
        print(meal)
        message = f"Thank you, {name}! . Booking Id : {booking_id}, Your reservation for {number_of_guests} guest(s),  from {start_date} to {end_date}, with Meal Selected as {meal}\n and payment via {payment_method} has been successfully confirmed with us. We are delighted to host you at MoonLight Hotel and look forward to making your stay truly exceptional."

        dispatcher.utter_message(text=message)
        return []