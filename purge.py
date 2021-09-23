"""
A python script to uninstall all testing and master branch installed flatpaks
"""
import gi

gi.require_version("Flatpak", "1.0")
gi.require_version("AppStreamGlib", "1.0")

from gi.repository import Flatpak


def uninstall_app(install,app):
    if app.get_name().find("Locale") < 0:
        ref = f"app/{app.get_name()}/{app.get_arch()}/{app.get_branch()}"
        print(f"uninstalling {app.get_name()}")
        trasnaction = Flatpak.Transaction().new_for_installation(install)
        trasnaction.add_uninstall(ref)
        trasnaction.run()

installations = Flatpak.get_system_installations()
for i, install in enumerate(installations):
    user_install = install.new_user()
    for app in user_install.list_installed_refs():
        branch = app.get_branch() 
        match branch:
            case "master":
                uninstall_app(user_install,app)
            case "test":
                uninstall_app(user_install,app)
            case   _:
                pass
    for app in install.list_installed_refs():
        branch = app.get_branch()
        match branch:
            case "master":
                uninstall_app(install,app)
            case "test":
                uninstall_app(install,app)
            case   _:
                pass