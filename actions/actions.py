# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionProvideImmigrationInfo(Action):
    def name(self) -> Text:
        return "action_provide_immigration_info"

    async def run(self, dispatcher, tracker, domain):
        intent = tracker.get_intent_of_latest_message()
        if intent == "general_immigration_query":
            dispatcher.utter_message(text="To immigrate to Canada, you usually need to go through a multi-step process. For more information, visit [Canada Immigration](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada.html).")
        elif intent == "student_immigration_query":
            dispatcher.utter_message(text="For students looking to immigrate to Canada, there are special programs and permits available. For more information, visit [Canada Student Visa](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html).")

        return []
    
class ActionExpressEntry(Action):
    def name(self):
        return "action_express_entry"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Express Entry is a system for skilled workers to immigrate to Canada. It provides a faster way for eligible candidates to settle in the country.")
        return []

class ActionStudentPath(Action):
    def name(self):
        return "action_student_path"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="To study in Canada, you'll generally need a study permit or a student visa. Requirements may include proof of funds, a letter of acceptance from a Canadian institution, and other documentation.")
        return []
