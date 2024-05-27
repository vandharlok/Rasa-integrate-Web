
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from rasa_sdk import Action
from rasa_sdk.events import SessionStarted, ActionExecuted, UserUtteranceReverted
import requests

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
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "nome": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"nome": slot_value}
            else:
                return {"nome": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"nome": None} 
        
        
    def validate_email(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        session_id = tracker.sender_id      
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "email": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"email": slot_value}
            else:
                return {"email": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"email": None} 
        
        
    def validate_telefone(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        session_id = tracker.sender_id   
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "phoneNumber": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"telefone": slot_value}
            else:
                return {"telefone": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"email": None} 
    
    def validate_instagram(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        session_id = tracker.sender_id   
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "instagram": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"instagram": slot_value}
            else:
                return {"instagram": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"email": None} 
    
    def validate_atua_terapeuta(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "atua_terapeuta": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"atua_terapeuta": slot_value}
            else:
                return {"atua_terapeuta": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"atua_terapeuta": None} 
        
    def validate_valor_medio(
            self, 
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,     
            ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "valor_medio": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                return {"valor_medio": slot_value}
            else:
                return {"valor_medio": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"nome": None} 
        
    def validate_qtd_sessoes(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "qtd_sessoes": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"qtd_sessoes": slot_value}
            else:
                return {"qtd_sessoes": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"qtd_sessoes": None} 
        
    def validate_faturamento_tri(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "faturamento_tri": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"faturamento_tri": slot_value}
            else:
                return {"faturamento_tri": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"faturamento_tri": None} 
        
    def validate_qtd_sess_perm(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "qtd_sess_perm": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"qtd_sess_perm": slot_value}
            else:
                return {"qtd_sess_perm": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"qtd_sess_perm": None} 
        
    def validate_mtd_proprio(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "mtd_proprio": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"mtd_proprio": slot_value}
            else:
                return {"mtd_proprio": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"mtd_proprio": None} 
        
    def validate_optd_sem(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "optd_sem": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"optd_sem": slot_value}
            else:
                return {"optd_sem": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"optd_sem": None} 
        
    def validate_vnd_sem(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "vnd_sem": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"vnd_sem": slot_value}
            else:
                return {"vnd_sem": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"vnd_sem": None} 
        
    def validate_invts_ads(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "invts_ads": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"invts_ads": slot_value}
            else:
                return {"invts_ads": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"invts_ads": None} 
        

    def validate_avg_invts(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "avg_invts": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"avg_invts": slot_value}
            else:
                return {"avg_invts": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"avg_invts": None} 
        
    def validate_cost_cust(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "cost_cust": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"cost_cust": slot_value}
            else:
                return {"cost_cust": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"cost_cust": None} 
        

    def validate_roas(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,     
        ) -> Dict[Text,Any]:
        session_id = tracker.sender_id
        url = "http://localhost:3000/usuario/cadastro"
        data = {
            "session_id": session_id,
            "roas": slot_value,
        }
        try:
            response = requests.post(url, json=data)
            if 200 <= response.status_code < 300:
                print(slot_value)
                return {"roas": slot_value}
            else:
                return {"roas": None}
                
        except requests.exceptions.RequestException as e:
            print(e)  
            return {"roas": None} 
        

