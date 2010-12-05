# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

app.manage_delObjects(app, 'acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('ZODBUserManager')
