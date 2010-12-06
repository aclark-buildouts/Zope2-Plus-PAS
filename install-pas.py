# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction


def install_plugins(uf)
    uf.manage_addProduct['PluggableAuthService'].addZODBUserManager('ZODBUserManager')
    uf.manage_addProduct['PluggableAuthService'].addZODBGroupManager('ZODBGroupManager')
    uf.manage_addProduct['PluggableAuthService'].addZODBRoleManager('ZODBRoleManager')
    uf.manage_addProduct['PluggableAuthService'].addCookieAuthHelper('CookieAuthHelper')
    #uf.manage_addProduct['PluggableAuthService'].addDelegatingMultiPlugin('DelegatingMultiPlugin')
    #uf.manage_addProduct['PluggableAuthService'].addDomainAuthHelper('DomainAuthHelper')
    uf.manage_addProduct['PluggableAuthService'].addDynamicGroupsPlugin('DynamicGroupsPlugin')
    uf.manage_addProduct['PluggableAuthService'].addHTTPBasicAuthHelper('HTTPBasicAuthHelper')
    uf.manage_addProduct['PluggableAuthService'].addInlineAuthHelper('InlineAuthHelper')
    uf.manage_addProduct['PluggableAuthService'].addLocalRolePlugin('LocalRolePlugin')
    uf.manage_addProduct['PluggableAuthService'].addRecursiveGroupsPlugin('RecursiveGroupsPlugin')
    #uf.manage_addProduct['PluggableAuthService'].addRequestTypeSniffer('RequestTypeSniffer')
    uf.manage_addProduct['PluggableAuthService'].addScriptablePlugin('ScriptablePlugin')
    uf.manage_addProduct['PluggableAuthService'].addSearchPrincipalsPlugin('SearchPrincipalsPlugin')
    #uf.manage_addProduct['PluggableAuthService'].addSessionAuthHelper('SessionAuthHelper')

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()

install_plugins(app.acl_users)

app.acl_users.ZODBUserManager.doAddUser('admin','admin')

transaction.commit()
