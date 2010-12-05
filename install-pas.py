# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()
transaction.commit()

app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('users')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBGroupManager('groups')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBRoleManager('roles')


#app.acl_users.manage_addProduct['PluggableAuthService'].addCookieAuthHelperForm('cookies')
#app.acl_users.manage_addProduct['PluggableAuthService'].addDelegatingMultiPluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addDomainAuthHelperForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addDynamicGroupsPluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addHTTPBasicAuthHelperForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addInlineAuthHelperForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addLocalRolePluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addRecursiveGroupsPluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addRequestTypeSnifferForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addScriptablePluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addSearchPrincipalsPluginForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addSessionAuthHelperForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addZODBGroupManagerForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addZODBRoleManagerForm('
#app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManagerForm('


transaction.commit()
