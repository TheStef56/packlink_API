import requests
from packlink_API.base import PacklinkBase

class PacklinkShipment(PacklinkBase):
    def __init__(self, user: str, password: str):
        self.user     = user
        self.password = password
        self.token    = None
        self.payload  = {
            "carrier"                : "",
            "service"                : "",
            "service_id"             : 0,
            "collection_date"        : "",
            "collection_time"        : "",
            "adult_signature"        : False,
            "additional_handling"    : False,
            "insurance"              : {"amount":0, "insurance_selected": False},
            "print_in_store_selected": False,
            "proof_of_delivery"      : False,
            "priority"               : False,
            "content"                : "",
            "content_second_hand"    : False,
            "contentvalue"           : 0,
            "currency"               : "",
            "from"                   : {},
            "packages"               : [],
            "to"                     : {},
            "has_customs"            : False
        }

    def set_shipping_details(
                    self,
                    city    : str,
                    country : str, # IT
                    state   : str, # Italia
                    zip_code: str,
                    email   : str,
                    name    : str,
                    phone   : str,
                    street1 : str,
                    surname : str,
                    from_to : str = "from"
                   ): 
        self.payload[from_to] = {
                "city"    : city,
                "country" : country,
                "state"   : state,
                "zip_code": zip_code,
                "email"   : email,
                "name"    : name,
                "phone"   : phone,
                "street1" : street1,
                "surname" : surname
            }

    def append_package(self,
                       height: int,
                       length: int,
                       width : int,
                       weight: float,
                       name  : str = "custom-name",
                       id    : str = "custom-parcel-id"
                       ):
        self.payload["packages"].append(
            {
                "height": height,
                "id"    : id,
                "length": length,
                "name"  : name,
                "weight": weight,
                "width" : width
            }
        )
        
    def carrier_details(self,
                        carrier        : str, # Poste Italiane
                        service        : str, # Crono Standard
                        service_id     : int,
                        collection_date: str, # 2025/08/04
                        collection_time: str, # 09:00-18:30
                        content_value  : int,
                        content        : str, # "Abbigliamento"
                        currency       : str = "EUR",
                        ):
        self.payload.update({
            "carrier"        : carrier,
            "service"        : service,
            "service_id"     : service_id,
            "collection_date": collection_date,
            "collection_time": collection_time,
            "contentvalue"   : content_value,
            "content"        : content,
            "currency"       : currency
        })

    def commit_shipment(self):
        url = "https://api.packlink.com/v1/shipments"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=self.payload)
        if response.status_code == 201:
            return True
        return False