import qrcode
img = qrcode.make('RAJ SINGH')

#wifi link
wifi_type='WPA'
wifi_ssid='rajnarayan_fulbr'
wifi_password='CLB2778D73'
wifi:f'WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;'
img = qrcode.make('RAJ SINGH')
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")






