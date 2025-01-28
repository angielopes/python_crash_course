"""Store the User class in one module, and store the Privileges and Admin
classes in a separate module. In a separate file, create an Admin instance
and call show_privileges() to show that everything is still working correctly."""

import module_admin_privileges

admin_user = module_admin_privileges.Admin("Totoro", "da Silva", "totorooooo")
admin_user.describe_user()

admin_privileges = admin_user.privileges
admin_privileges.show_privileges()
