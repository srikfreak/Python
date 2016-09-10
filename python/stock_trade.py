import sys 

def find_max_profit(opening_prices):
	current_min_opening_price = float(opening_prices[0])
	current_max_profit = 0.0
	for op in opening_prices:
		opening_price = float(op)
		if opening_price - current_min_opening_price > current_max_profit:
			current_max_profit = opening_price - current_min_opening_price

		if opening_price < current_min_opening_price:
			current_min_opening_price = opening_price
	return current_max_profit


print find_max_profit(sys.argv[1:])

