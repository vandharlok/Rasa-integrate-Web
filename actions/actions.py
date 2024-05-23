
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk import Action
from rasa_sdk.events import SessionStarted, ActionExecuted, UserUtteranceReverted

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
        if slot_value:
            print(slot_value)
            return {"nome": slot_value}
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"nome": slot_value}

    def validate_email(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        if slot_value:
            print(slot_value)
            return {"email": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"email": slot_value}
    def validate_telefone(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        if slot_value:
            print(slot_value)
            return {"telefone": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"telefone": slot_value}
    
    def validate_instagram(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        # Salvando o slot preenchido
        if slot_value:
            print(slot_value)
            return {"instagram": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"instagram": slot_value}
    
    def validate_atua_terapeuta(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        # Lista de valores permitidos
        valid_values = ["Menos de 6 meses", "Entre 7 e 12 meses", "Entre 1 e 2 anos", "Há mais de 2 anos"]

        if slot_value in valid_values:
            return {"atua_terapeuta": slot_value}
        else:
            # Informar o usuário e pedir para escolher uma opção válida
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"atua_terapeuta": None}  # Manter o slot limpo até uma entrada válida ser fornecida

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
        

    def validate_qtd_sessoes(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"qtd_sessoes": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"qtd_sessoes": slot_value}
    def validate_faturamento_tri(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"faturamento_tri": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"faturamento_tri": slot_value}
    def validate_qtd_sess_perm(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"qtd_sess_perm": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"qtd_sess_perm": slot_value}
    def validate_mtd_proprio(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"mtd_proprio": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"mtd_proprio": slot_value}
    def validate_optd_sem(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"optd_sem": slot_value}
    
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"optd_sem": slot_value}
    def validate_vnd_sem(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"vnd_sem": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"vnd_sem": slot_value}
    def validate_invts_ads(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"invts_ads": slot_value}
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"invts_ads": slot_value}

    def validate_avg_invts(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"avg_invts": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"avg_invts": slot_value}
    def validate_cost_cust(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"cost_cust": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"cost_cust": slot_value}

    def validate_roas(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        if slot_value:
            print(slot_value)
            return {"roas": slot_value}
        
        else:
            dispatcher.utter_message(text="Por favor, escolha uma das opções fornecidas.")
            return {"roas": slot_value}

