def calculate_discount(price: float, discount: float) -> float:
    if discount < 0.0 or discount > 1.0:
        raise ValueError('Discount must be between 0 and 1')
    return price * (1 - discount)