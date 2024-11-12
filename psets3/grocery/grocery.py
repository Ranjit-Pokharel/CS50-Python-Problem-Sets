def main():
	# empty list (dict key:value) to store 
	items = dict()

	while True:
		try:
			# get items from user
			item = get_items()

			# sort the items and convert back to dict
			items = dict(sorted(manage_list(item, items).items()))

		except EOFError:
			# if ctrl + d press then list items with their value
			display_list(items)
			break

def get_items():
	return input().upper()

def manage_list(item, items):
	if item in items.keys():
		items[item] += 1
		return items
	items[item] = 1
	return items

def display_list(items):
	for item in items:
		print(f"{items[item]} {item}")

if __name__ == "__main__":
	main()