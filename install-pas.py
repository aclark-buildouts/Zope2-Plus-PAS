# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('ZODBUserManager')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBGroupManager('ZODBGroupManager')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBRoleManager('ZODBRoleManager')
app.acl_users.manage_addProduct['PluggableAuthService'].addCookieAuthHelper('CookieAuthHelper')
app.acl_users.manage_addProduct['PluggableAuthService'].addDelegatingMultiPlugin('DelegatingMultiPlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addDomainAuthHelper('DomainAuthHelper')
app.acl_users.manage_addProduct['PluggableAuthService'].addDynamicGroupsPlugin('DynamicGroupsPlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addHTTPBasicAuthHelper('HTTPBasicAuthHelper')
app.acl_users.manage_addProduct['PluggableAuthService'].addInlineAuthHelper('InlineAuthHelper')
app.acl_users.manage_addProduct['PluggableAuthService'].addLocalRolePlugin('LocalRolePlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addRecursiveGroupsPlugin('RecursiveGroupsPlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addRequestTypeSniffer('RequestTypeSniffer')
app.acl_users.manage_addProduct['PluggableAuthService'].addScriptablePlugin('ScriptablePlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addSearchPrincipalsPlugin('SearchPrincipalsPlugin')
app.acl_users.manage_addProduct['PluggableAuthService'].addSessionAuthHelper('SessionAuthHelper')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBGroupManager('ZODBGroupManager')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBRoleManager('ZODBRoleManager')
app.acl_users.manage_addProduct['PluggableAuthService'].addZODBUserManager('ZODBUserManager')

transaction.commit()
