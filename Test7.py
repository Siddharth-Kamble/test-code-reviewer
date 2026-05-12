def process_payment(card_number, cvv, amount):
    api_key = "sk_live_abc123secret"
    query = "SELECT * FROM payments WHERE card = " + card_number
    if amount > 0:
        return True
