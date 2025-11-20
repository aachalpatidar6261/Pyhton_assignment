d = {'product_id': 9944122622271, 'title': 'Aviator Sunglasses', 'price': [{'id': 50692762927423, 'product_id': 9944122622271, 'title': 'Default Title', 'price': '390.00', 'position': 1, 'inventory_policy': 'deny', 'compare_at_price': None, 'option1': 'Default Title', 'option2': None, 'option3': None, 'created_at': '2025-04-07T08:52:13-04:00', 'updated_at': '2025-04-07T08:52:13-04:00', 'taxable': True, 'barcode': None, 'fulfillment_service': 'manual', 'grams': 0, 'inventory_management': None, 'requires_shipping': True, 'sku': None, 'weight': 0.0, 'weight_unit': 'kg', 'inventory_item_id': 52754021056831, 'inventory_quantity': 0, 'old_inventory_quantity': 0, 'admin_graphql_api_id': 'gid://shopify/ProductVariant/50692762927423', 'image_id': None}], 'vendor': 'Eco-Central'}


print(d['price'][0]['price'])
print(d['title'])

import random

print(random.randint(9000000,200000000))