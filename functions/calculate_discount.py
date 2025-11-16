def calculate_discount(price: float, discount: float) -> float:
    if not discount > 0 and not discount < 1:
        raise ValueError('Discount must be between 0 and 1')
    return price * (1 - discount)