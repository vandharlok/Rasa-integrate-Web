
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

class ActionShowButtons(Action):
    def name(self):
        return "action_show_buttons"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="/show_buttons")
        return []
    

class ValidateFormularioFabian(FormValidationAction):

    def name(self):
        return "validate_formulario_fabian"

    def validate_nome(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido

        print(slot_value)
        return {"atua_terapeuta": slot_value}

    def validate_email(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        print(slot_value)
        return {"valor_medio": slot_value}
    def validate_telefone(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        print(slot_value)
        return {"valor_medio": slot_value}
    def validate_instagram(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        print(slot_value)
        return {"valor_medio": slot_value}
    
    def validate_atua_terapeuta(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"atua_terapeuta": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"atua_terapeuta": None}

    def validate_valor_medio(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        print(slot_value)
        return {"valor_medio": slot_value}
    
class ActionSetAtuaTerapeuta(Action):
    def name(self) -> str:
        return "action_set_atua_terapeuta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Recupera o valor passado na mensagem do usuário (que é o payload do botão)
        value = tracker.latest_message.get('text')

        # Define o slot atua_terapeuta com o valor recuperado
        return [SlotSet("atua_terapeuta", value)]
    
 
