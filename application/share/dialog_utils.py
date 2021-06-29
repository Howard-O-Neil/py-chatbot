import json

class DialogUtils:
    # fulfillmentState (Fulfilled | Failed | ReadyForFulfillment)
    def close(self, fulfillmentState):
        res = {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": fulfillmentState,
            }   
        }
        return res
    
    def confirm_intent(self):
        # lack of 

        # "intentName": "intent-name"
        # "slots": {
        #     "slot-name": "value",
        #     "slot-name": "value",
        #     "slot-name": "value"  
        # },

        res = {
            "dialogAction": {
                "type": "ConfirmIntent",
            }
        }
        return res

    def delegate(self):
        res = {
            "dialogAction": {
                "type": "Delegate",
            }
        }
        return res

    def elicitIntent(self):
        res = {
            "dialogAction": {
                "type": "ElicitIntent",
            }
        }
        return res

    def elicitSlot(self, elicit_slot):
        # lack of 

        # "intentName": "intent-name"
        # "slots": {
        #     "slot-name": "value",
        #     "slot-name": "value",
        #     "slot-name": "value"  
        # },

        res = {
            "dialogAction": {
                "type": "ElicitSlot",
                "slotToElicit" : elicit_slot,
            }
        }
        return res

dialogUtils = DialogUtils()