from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('บอทเกม')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.midasbuy.com/midasbuy/th/buy/pubgm")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="paymentChannel_342"]').click()

UID = StringVar()
Label(padx=10, font=30).grid(row=0, sticky=W)
Entry(font=30, width=30, textvariable=UID).grid(row=0, column=1)

choice = StringVar(value='เลือกเกม')
Label(text='ใส่ UID เกม', padx=10, font=30).grid(row=0, column=0)
combo = ttk.Combobox(width=30, font=30, textvariable=choice)
combo['values'] = ('VALORANT',)
combo.grid(row=1, column=1)

Price = StringVar()
Label(text='ราคา', padx=10, font=30).grid(row=3, sticky=W)
et2 = Entry(font=30, width=30, textvariable=Price)
et2.grid(row=3, column=1)


def deletetext():
    et2.delete(0, END)


def calculate():
    amont = UID.get()
    currency = choice.get()
    currency2 = Price.get()

    if currency == 'VALORANT':
        element = driver.find_element(By.ID, "userId")
        element.send_keys(amont)
        time.sleep(1.5)
        driver.find_element(By.XPATH, '//*[@id="mdn-submit"]').click()
        time.sleep(1.5)
        driver.find_element(By.CLASS_NAME, 'order-summary__content')
        time.sleep(1)
        if driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/main/div[2]/div[1]/div/div/div[1]/div/div'):
            driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/main/div[2]/div[1]/div/div/div[1]/div/div').click()
        else:
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/button').click()
        element.clear()

Button(text='เรียบร้อย', font=30, width=15, command=calculate).grid(row=4, column=1, sticky=W)
Button(text='ลบข้อมูล', font=30, width=15, command=deletetext).grid(row=4, column=1, sticky=E)

root.mainloop()
