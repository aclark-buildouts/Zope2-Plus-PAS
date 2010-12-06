# Run via bin/zope2 run install.py to replace top level acl_users with a PAS

import transaction

from Products.PluggableAuthService.interfaces.plugins import IAuthenticationPlugin
from Products.PluggableAuthService.interfaces.plugins import IChallengePlugin
from Products.PluggableAuthService.interfaces.plugins import IExtractionPlugin
from Products.PluggableAuthService.interfaces.plugins import IRoleAssignerPlugin
from Products.PluggableAuthService.interfaces.plugins import IRoleEnumerationPlugin
from Products.PluggableAuthService.interfaces.plugins import IRolesPlugin
from Products.PluggableAuthService.interfaces.plugins import IUserAdderPlugin
from Products.PluggableAuthService.interfaces.plugins import IUserEnumerationPlugin

def unignore_exceptions():
    app.error_log.setProperties(0, '')

def install_plugins(uf):
    pas_factory = uf.manage_addProduct['PluggableAuthService']

    # We need the user manager plugin to add a user
    pas_factory.addZODBUserManager('ZODBUserManager')

    # We need the role manager plugin to add a user
    pas_factory.addZODBRoleManager('ZODBRoleManager')

    # We need the basic auth helper to do basic auth
    pas_factory.addHTTPBasicAuthHelper('HTTPBasicAuthHelper')

    # We need the cookie auth helper to do cookie auth
    #pas_factory.addCookieAuthHelper('CookieAuthHelper')

    # The rest of these are optional
    #pas_factory.addZODBGroupManager('ZODBGroupManager')
    #pas_factory.addDynamicGroupsPlugin('DynamicGroupsPlugin')
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

# users
app.acl_users.plugins.activatePlugin(IAuthenticationPlugin, 'ZODBUserManager')
app.acl_users.plugins.activatePlugin(IUserAdderPlugin, 'ZODBUserManager')
app.acl_users.plugins.activatePlugin(IUserEnumerationPlugin, 'ZODBUserManager')

# roles
app.acl_users.plugins.activatePlugin(IRoleAssignerPlugin, 'ZODBRoleManager')
app.acl_users.plugins.activatePlugin(IRolesPlugin, 'ZODBRoleManager')
app.acl_users.plugins.activatePlugin(IRoleEnumerationPlugin, 'ZODBRoleManager')

# http auth
app.acl_users.plugins.activatePlugin(IChallengePlugin, 'HTTPBasicAuthHelper')
app.acl_users.plugins.activatePlugin(IExtractionPlugin, 'HTTPBasicAuthHelper')

#app.acl_users.plugins.activatePlugin(IChallengePlugin, 'CookieAuthHelper')
#IRolesPluginapp.acl_users.plugins.activatePlugin(IExtractionPlugin, 'CookieAuthHelper')

unignore_exceptions()
transaction.commit()

