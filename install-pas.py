# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction


def install_plugins(uf):
    factory = uf.manage_addProduct['PluggableAuthService']

    factory.addZODBUserManager('ZODBUserManager')
    factory.addZODBGroupManager('ZODBGroupManager')
    factory.addZODBRoleManager('ZODBRoleManager')
    factory.addCookieAuthHelper('CookieAuthHelper')
    #factory.addDelegatingMultiPlugin('DelegatingMultiPlugin')
    #factory.addDomainAuthHelper('DomainAuthHelper')
    factory.addDynamicGroupsPlugin('DynamicGroupsPlugin')
    factory.addHTTPBasicAuthHelper('HTTPBasicAuthHelper')
    factory.addInlineAuthHelper('InlineAuthHelper')
    factory.addLocalRolePlugin('LocalRolePlugin')
    factory.addRecursiveGroupsPlugin('RecursiveGroupsPlugin')
    #factory.addRequestTypeSniffer('RequestTypeSniffer')
    factory.addScriptablePlugin('ScriptablePlugin')
    factory.addSearchPrincipalsPlugin('SearchPrincipalsPlugin')
    #factory.addSessionAuthHelper('SessionAuthHelper')

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()

install_plugins(app.acl_users)

app.acl_users.ZODBUserManager.doAddUser('admin', 'admin')

transaction.commit()
