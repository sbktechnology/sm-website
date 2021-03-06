app_name = "systematrix_website"
app_title = "Systematrix Solutions Pvt. Ltd."
app_publisher = "Systematrix"
app_description = "Appp for managing  website"
app_icon = "icon-website"
app_color = "#483D8B"
app_email = "info@systematrix.co.in"
app_url = "https://frappe.io/apps/systematrix_website"
app_version = "0.0.1"

web_include_css = ["assets/systematrix_website/css/frappe-io-web.css", "assets/frappe/css/hljs.css"]
web_include_js = "/assets/frappe/js/lib/highlight.pack.js"

fixtures = [
	"Website Settings",
	"Website Script",
	"Contact Us Settings",
	"Web Form"
]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/systematrix_website/css/systematrix_website.css"
# app_include_js = "/assets/systematrix_website/js/systematrix_website.js"

# include js, css files in header of web template
# web_include_css = "/assets/systematrix_website/css/systematrix_website.css"
# web_include_js = "/assets/systematrix_website/js/systematrix_website.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "systematrix_website.install.before_install"
# after_install = "systematrix_website.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "systematrix_website.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"systematrix_website.tasks.all"
# 	],
# 	"daily": [
# 		"systematrix_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"systematrix_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"systematrix_website.tasks.weekly"
# 	]
# 	"monthly": [
# 		"systematrix_website.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "systematrix_website.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "systematrix_website.event.get_events"
# }

