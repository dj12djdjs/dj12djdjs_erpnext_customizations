from __future__ import unicode_literals

import frappe
from erpnext.stock.utils import get_incoming_rate

def update(doc, method=None):
	pl_name = "Landed Cost"
	lc_pl_filters = {
		"price_list": pl_name
	}

	for item in doc.items:
		lc_pl_filters.update({"item_code": item.item_code})
		item_price = frappe.db.get_list('Item Price', filters=lc_pl_filters, fields=['name'], as_list=True)
		if len(item_price) > 0:
			if len(item_price[0]) > 0:
				item_price = frappe.get_cached_doc('Item Price', item_price[0][0])
			else:
				item_price = None
		else:
				item_price = None
		args = {
			"item_code": item.item_code
		}
		lc = get_incoming_rate(args)

		if item_price:
			item_price.price_list_rate = lc
		else:
			item = frappe.get_cached_doc("Item", item.item_code)
			item_price = frappe.get_doc({
				"doctype": "Item Price",
				"item_code": item.item_code,
				"item_name": item.item_name,
				"brand": item.brand,
				"item_description": item.description,
				"price_list": pl_name,
				"selling": True,
				"currency": frappe.get_cached_doc("Price List", pl_name).currency,
				"price_list_rate": lc
			})
		item_price.save()
