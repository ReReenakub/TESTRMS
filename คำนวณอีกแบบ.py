import numpy as np
import pyperclip

prices = np.array([32,149,299,719,1429,2799,32,149,299,719,1429,2799,32,149,299,719,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799,1429,2799])
coupons_per_price = np.array([60,325,660,1800,3850,8100,60,325,660,1800,3850,8100,60,325,660,1800,3850,8100,3850,8100,3850,8100,3850,8100,8100,3850,8100,3850,8100,8100,3850,8100,3850,8100,8100,3850,8100,3850,8100])

sorted_prices = np.sort(prices)[::-1]

initial_budget = 9999

budget = initial_budget
spent_prices = []
total_coupons = 0
for price in sorted_prices:
    index = np.where(prices == price)[0][0]
    coupon = coupons_per_price[index]
    if budget >= price:
        budget -= price
        spent_prices.append(coupon)
        total_coupons += coupon

    else:
        continue

budgeta = initial_budget

spent_coupons0 = []
total_coupons0 = 0
for price in sorted_prices:
    index = np.where(prices == price)[0][0]
    coupon = coupons_per_price[index]
    if budgeta+50 >= price:
        budgeta -= price
        spent_coupons0.append(coupon)
        total_coupons0 += coupon

print("แพ็คที่ใช้แนะนำ:",spent_prices,'UC')
print("ใกล้เคียงที่สุดคือ:",initial_budget - budget,'บาท')
print("จำนวน UC ที่ได้:",total_coupons,'UC')
spent_prices_str = '+'.join(map(str, spent_prices))
print(spent_prices_str)

print("แพ็คที่ใช้:",spent_coupons0,'UC')
print("ใกล้เคียงที่สุดคือ:",initial_budget - budgeta,'บาท')
print("ราคา:",total_coupons0,'UC')