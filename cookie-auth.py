# Run ``bin/zope2 run basic-auth.py`` to replace the top level Zope 2
# acl_users with a PAS acl_users that does basic auth

import transaction

from Products.PluggableAuthService.interfaces.plugins import \
    IAuthenticationPlugin
from Products.PluggableAuthService.interfaces.plugins import IChallengePlugin
from Products.PluggableAuthService.interfaces.plugins import IExtractionPlugin
from Products.PluggableAuthService.interfaces.plugins import \
    IRoleAssignerPlugin
from Products.PluggableAuthService.interfaces.plugins import \
    IRoleEnumerationPlugin
from Products.PluggableAuthService.interfaces.plugins import IRolesPlugin
from Products.PluggableAuthService.interfaces.plugins import IUserAdderPlugin
from Products.PluggableAuthService.interfaces.plugins import \
    IUserEnumerationPlugin


def install_pas(app):
    app.manage_delObjects('acl_users')
    app.manage_addProduct['PluggableAuthService'].addPluggableAuthService()


def install_plugins(uf):
    pas_factory = uf.manage_addProduct['PluggableAuthService']

    # We need the user manager to add a user
    pas_factory.addZODBUserManager('ZODBUserManager')

    # We need the role manager to add a role
    pas_factory.addZODBRoleManager('ZODBRoleManager')

    # We need the cookie auth helper to do basic auth
    pas_factory.addCookieAuthHelper('CookieAuthHelper')
    uf.CookieAuthHelper.cookie_name = 'CookieAuthHelper'


def activate_plugins(plugins):
    # users
    plugins.activatePlugin(IAuthenticationPlugin, 'ZODBUserManager')
    plugins.activatePlugin(IUserAdderPlugin, 'ZODBUserManager')
    plugins.activatePlugin(IUserEnumerationPlugin, 'ZODBUserManager')

    # roles
    plugins.activatePlugin(IRoleAssignerPlugin, 'ZODBRoleManager')
    plugins.activatePlugin(IRolesPlugin, 'ZODBRoleManager')
    plugins.activatePlugin(IRoleEnumerationPlugin, 'ZODBRoleManager')

    # cookie auth
    plugins.activatePlugin(IChallengePlugin, 'CookieAuthHelper')
    plugins.activatePlugin(IExtractionPlugin, 'CookieAuthHelper')


def add_logo(app):
    fn = 'Vlogo250.gif'
    logo = open(fn, 'rb').read()
    app.manage_addProduct['Image'].manage_addImage(fn, logo)


def update_index(index):
    update = """
<a tal:attributes="href here/absolute_url"><img
    tal:attributes="src python: here.absolute_url() + '/Vlogo250.gif'"></a>
<h1>Welcome to Zope 2!</h1>
<ul>
<li>
    <a href="http://docs.zope.org/#zope-2">Documentation</a>
</li>
<li>
    <a tal:attributes="href python: here.absolute_url() +
        '/manage_main'">Administration</a>
</li>
</ul>
    """
    index.write(update)


if __name__ == '__main__':
    app = locals()['app']  # make pyflakes happy
    install_pas(app)
    install_plugins(app.acl_users)
    activate_plugins(app.acl_users.plugins)
    add_logo(app)
    update_index(app.index_html)
    transaction.commit()
