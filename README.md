# PACKLINK_API

## What is it? 

packlink_API is python implementation of the interactions with packlink APIs, to:

- Retrieve the available shipping options for one/multiple package(s) (given width, heigth, length and weigth) with the available carriers.

- Create a shipment automatically ready to be paid.

## Installation

move the module packlink_API into the directory of your main program, then import what you need:

```python
    from packlink_API.preview import PacklinkProPreview
```


## Usage


Preview :
```python
# usage:
p = PacklinkProPreview("user", "password", "IT", "IT", 12345, 12345)
p.login()
p.add_package(10, 10, 2, 0.15)
p.makereq()
p.select_best()
p.logout()

print(p.carrier)
print(p.price)
print(p.shipping_time)
# ...
```
or, without logging in:
```python
p = PacklinkFreePreview("IT", "IT", 12345, 12345, 10, 10, 2, 0.15)
p.makereq()
p.select_best()

print(p.carrier)
print(p.price)
print(p.shipping_time)
# ...
```
Shipment:
```python
# usage
s = PacklinkShipment("user", "password")
s.login()
s.set_shipping_details(city,
                      country,   # "IT"
                      state,     # "Italy"
                      zip_cod,
                      email,
                      name,
                      phone,
                      street1,
                      surname,
                      "from")

s.set_shipping_details(city,
                      country,   # "IT"
                      state,     # "Italy"
                      zip_cod,
                      email,
                      name,
                      phone,
                      street1,
                      surname,
                      "to")
s.carrier_details(carrier,         # Poste Italiane
                  service,         # Crono Standard
                  service_id,
                  collection_date, # 2025/08/04
                  collection_time, # 09:00-18:30
                  content_value,
                  content,         # "Abbigliamento"
                  currency)

s.append_package(height,
                length,
                width ,
                weight,
                name,
                pid)

s.commit_shipment()
s.logout()
# ...
```