import urequests as requests
import network
from utime import sleep

sta_if = network.WLAN(network.STA_IF)

def do_connect(SSID, PASSWORD):
    '''
    Function to connect to the internet via WiFi
    '''

    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        print('Connecting to the network', SSID + "...")
        while not sta_if.isconnected():
            pass
    print('Network configuration(IP/Mask/GATEWAY/DNS:', sta_if.ifconfig(), '\n')


def get_blynk_constructor(device_token, pin_name, value_to_post, debug=True):
    '''
    Constructs the URL for a Blynk GET request to post a pin value.
    '''

    get_blynk_url = "http://ny3.blynk.cloud/external/api/update?token=" + device_token + "&" + str(pin_name) + "=" + str(value_to_post)
    if debug:
        print(get_blynk_url)
    return get_blynk_url


def event_blynk_constructor(token, event_code):
    '''
    Constructs the URL for sending an event in Blynk.
    '''

    event_description = 'None'
    event_blynk_url = "https://blynk.cloud/external/api/logEvent?token=" + token + "&code=" + event_code + "&description=" + event_description
    print(event_blynk_url)
    return event_blynk_url


def get_request(device_token, pin_name, value_to_post, debug=True):
    '''
    Sends a GET request to an API service.
    '''

    get_blynk_url = get_blynk_constructor(device_token=device_token,
                                          pin_name=pin_name,
                                          value_to_post=value_to_post,
                                          debug=debug)
    response = requests.get(get_blynk_url)
    if debug:
        print(debug)
        print(response.status_code, response.text)
    if response.status_code != 200:
        print("Bad status code received")
    return response.status_code, response.text


def get_request_event(device_token, event_code, debug=True):
    '''
    Sends a GET request to an API service for an event.
    '''

    get_blynk_url = event_blynk_constructor(token=device_token,
                                            event_code=event_code)

    response = requests.get(get_blynk_url)
