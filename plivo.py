import requests


# Fill in your details here to be posted to the login form.
payload = {
    'id_username': 'plivoiview@gmail.com',
    'id_password': 'plivoguest123'
}


# Use 'with' to ensure the session context is closed after use.

p = requests.post("https://manage.plivo.com/accounts/login/", data=payload)
# print the html returned or something more intelligent to see if it's a successful login page.
# print (p.text)
print (p.status_code)
# An authorised request.
r = requests.get('https://manage.plivo.com/dashboard/')
print (r.text)
        # etc...

r = requests.get('https://manage.plivo.com/accounts/login/')
# print (r.text)
print (r.status_code)
