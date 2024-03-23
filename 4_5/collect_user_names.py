import pyad

pyad.set_defaults(ldap_server="o3.ru")  # Укажите ваш сервер LDAP

ou = pyad.adcontainer.ADContainer.from_dn("ws-kzn-it003")  # Укажите путь к вашей организационной  единице (OU)

for user in ou.get_children():
    print(user.get_attribute("sAMAccountName"))