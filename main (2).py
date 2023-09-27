def linearSearchProduct(productList, targetProduct):
    indices = []
    
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    
    return indices

# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result1 = linearSearchProduct(products, target)
print(result1) 
result2 = linearSearchProduct(products,target2)
print(result2)