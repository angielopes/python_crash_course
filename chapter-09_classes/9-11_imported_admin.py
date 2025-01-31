"""Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module.
Create a separate file, make an Admin instance, and call
show_privileges() to show that everything is working correctly."""

import module_admin

admin_user = module_admin.Admin("Angela", "Lopes", "angela_lopes")
admin_user.describe_user()

admin_privileges = admin_user.privileges
admin_privileges.show_privileges()
