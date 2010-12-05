# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()
transaction.commit()

app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('ZODBUserManager')
transaction.commit()
