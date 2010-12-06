# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

from Products.PluggableAuthService.interfaces.plugins import IAuthenticationPlugin
from Products.PluggableAuthService.interfaces.plugins import IRoleAssignerPlugin
from Products.PluggableAuthService.interfaces.plugins import IUserAdderPlugin

def unignore_exceptions():
    app.error_log.setProperties(0, None)

def install_plugins(uf):
    pas_factory = uf.manage_addProduct['PluggableAuthService']

    # We need the user manager plugin to add a user
    pas_factory.addZODBUserManager('ZODBUserManager')

    # We need the role manager plugin to add a user
    pas_factory.addZODBRoleManager('ZODBRoleManager')

    # The rest of these are optional
    #pas_factory.addZODBGroupManager('ZODBGroupManager')
    #pas_factory.addCookieAuthHelper('CookieAuthHelper')
    #pas_factory.addDynamicGroupsPlugin('DynamicGroupsPlugin')
    #pas_factory.addHTTPBasicAuthHelper('HTTPBasicAuthHelper')
    #pas_factory.addInlineAuthHelper('InlineAuthHelper')
    #pas_factory.addLocalRolePlugin('LocalRolePlugin')
    #pas_factory.addRecursiveGroupsPlugin('RecursiveGroupsPlugin')
    #pas_factory.addSearchPrincipalsPlugin('SearchPrincipalsPlugin')
    #pas_factory.addScriptablePlugin('ScriptablePlugin')

    #factory = XXX # These aren't part of PAS, so they'll need a different factory
    #addDelegatingMultiPlugin('DelegatingMultiPlugin')
    #addDomainAuthHelper('DomainAuthHelper')
    #addRequestTypeSniffer('RequestTypeSniffer')
    #addSessionAuthHelper('SessionAuthHelper')

app.manage_delObjects('acl_users')
app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()
install_plugins(app.acl_users)
app.acl_users.plugins.activatePlugin(IAuthenticationPlugin, 'ZODBUserManager')
app.acl_users.plugins.activatePlugin(IRoleAssignerPlugin, 'ZODBRoleManager')
app.acl_users.plugins.activatePlugin(IUserAdderPlugin, 'ZODBUserManager')
unignore_exceptions()
transaction.commit()
