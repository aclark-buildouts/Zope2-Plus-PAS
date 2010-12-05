# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()
transaction.commit()

app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('users')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBGroupManager('groups')

#app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('roles')
#app.acl_users.manage_addProduct['addCookieAuthHelperForm'].
#addDelegatingMultiPluginForm
#addDomainAuthHelperForm
#addDynamicGroupsPluginForm
#addHTTPBasicAuthHelperForm
#addInlineAuthHelperForm
#addLocalRolePluginForm
#addRecursiveGroupsPluginForm
#addRequestTypeSnifferForm
#addScriptablePluginForm
#addSearchPrincipalsPluginForm
#addSessionAuthHelperForm
#addZODBGroupManagerForm
#addZODBRoleManagerForm
#addZODBUserManagerForm


transaction.commit()
