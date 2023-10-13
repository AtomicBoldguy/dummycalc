def perform_operation(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number

def main():
    result = None
    while True:
        if result is None:
            first_number = float(input("Enter the first number: "))
        else:
            first_number = result
        operator = input("Enter the operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))
        result = perform_operation(first_number, operator, second_number)
        print("Result:", result)

if __name__ == "__main__":
    main()
#
# import requests
# from datetime import datetime, timedelta


# def get_market_rates():
#     url = "https://api/market/btcusd"
#     response = requests.get(url)
#     data = response.json()
#     current_rate = data["current_rate"]
#
#     # Calculate the timestamps for 10 minutes and 30 minutes ago
#     now = datetime.now()
#     ten_minutes_ago = now - timedelta(minutes=10)
#     thirty_minutes_ago = now - timedelta(minutes=30)
#
#     # Find the rates for the specified timestamps
#     rates = data["rates"]
#     rate_10_minutes_ago = None
#     rate_30_minutes_ago = None
#
#     for rate in rates:
#         timestamp = datetime.fromtimestamp(rate["timestamp"])
#
#         if timestamp == ten_minutes_ago:
#             rate_10_minutes_ago = rate["rate"]
#         elif timestamp == thirty_minutes_ago:
#             rate_30_minutes_ago = rate["rate"]
#
#         if rate_10_minutes_ago and rate_30_minutes_ago:
#             break
#
#     return current_rate, rate_10_minutes_ago, rate_30_minutes_ago
#
#
# def main():
#     current_rate, rate_10_minutes_ago, rate_30_minutes_ago = get_market_rates()
#
#     print("Current Rate:", current_rate)
#     print("Rate 10 Minutes Ago:", rate_10_minutes_ago)
#     print("Rate 30 Minutes Ago:", rate_30_minutes_ago)
#
#
# if __name__ == "__main__":
#     main()
