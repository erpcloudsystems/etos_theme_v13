import frappe

__version__ = '0.0.1'

def get_img():
    # frappe.msgprint(str("get_img"))
    default_company = frappe.db.get_single_value("Global Defaults", "default_company")
    if default_company:
        logo = frappe.db.get_value("Company", default_company, "company_logo")
    else:
        logo = "/assets/etos_theme_v13/images/etos_lite.png"
    return logo