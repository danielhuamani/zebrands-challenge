def product_add_visit(product):
    product.visits = product.visits + 1
    product.save()