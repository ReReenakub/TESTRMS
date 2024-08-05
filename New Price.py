from itertools import product

price_value_pairs = [
    (50, 138, 3),
    (100, 276, 3),
    (300, 864, 3),
    (500, 1560, 3),
    (1000, 3240, 5)
]

def calculate_combinations(pairs):
    results = {}
    details = []

    counts_ranges = [range(max_count + 1) for _, _, max_count in pairs]

    for counts in product(*counts_ranges):
        if 0 < sum(counts):
            total_price = sum(p * c for (p, _, _), c in zip(pairs, counts))
            total_value = sum(v * c for (_, v, _), c in zip(pairs, counts))
            if total_price not in results or total_value > results[total_price][1]:
                results[total_price] = (counts, total_value)

    for price, (counts, value) in results.items():
        details.append((price, value, counts))

    return details


details = calculate_combinations(price_value_pairs)
print(f"มีทั้งหมด: {len(details)} รูปแบบ")
print("""นี่คือราคาทั้งหมด
🔽 🔽 🔽 🔽""")

sorted_details = sorted(details, key=lambda x: (x[0], x[1]))

for price, value, counts in sorted_details:
    count_detail = ' + '.join(
        [f"{pairs[0]}" for pairs, count in zip(price_value_pairs, counts) if count > 0 for _ in range(count)])
    print(f"ราคา {price} บาท ได้ {value} CP แพ็ค: {count_detail}")
