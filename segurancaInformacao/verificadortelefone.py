import phonenumbers

from phonenumbers import geocoder

numeroTelefone = input("Digite o telefone no formato: +XXXXYYYYYYYYY: ")

numero_Telefone = phonenumbers.parse(numeroTelefone, None)

loc = geocoder.description_for_number(numero_Telefone, "pt")

print(f"Localização : {loc}")