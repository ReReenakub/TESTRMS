from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QCheckBox, QTextEdit, QPushButton, QGridLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('Confirmed Sales')

layout = QGridLayout()

# Customer Information
layout.addWidget(QLabel('ชื่อลูกค้า:'), 0, 0)
customer_name = QLineEdit()
layout.addWidget(customer_name, 0, 1)

layout.addWidget(QLabel('เกม/แพค/จำนวน:'), 0, 2)
game_quantity = QLineEdit()
layout.addWidget(game_quantity, 0, 3)
layout.addWidget(QLabel('/'), 0, 4)
extra_entry = QLineEdit()
layout.addWidget(extra_entry, 0, 5)
qty = QLineEdit()
layout.addWidget(qty, 0, 6)

# Add slip option
add_slip = QCheckBox('เพิ่มช่องแบบ Slip')
layout.addWidget(add_slip, 1, 0, 1, 2)

layout.addWidget(QLabel('ยอดเงินรวม:'), 2, 0)
total_amount = QLineEdit()
layout.addWidget(total_amount, 2, 1)

# Payment Methods
layout.addWidget(QLabel('วิธีจ่าย'), 3, 0)
layout.addWidget(QLabel('ยอดโอน'), 3, 1)
layout.addWidget(QLabel('เวลา'), 3, 2)

for i in range(3):
    method = QComboBox()
    method.addItems(['Method 1', 'Method 2', 'Method 3'])
    layout.addWidget(method, 4 + i, 0)
    amount = QLineEdit()
    layout.addWidget(amount, 4 + i, 1)
    time = QLineEdit()
    layout.addWidget(time, 4 + i, 2)

# Notes
layout.addWidget(QLabel('Note:'), 7, 0)
note_text = QTextEdit()
layout.addWidget(note_text, 7, 1, 1, 5)

# Add UID option
add_uid = QCheckBox('เพิ่มช่องแบบ UID')
layout.addWidget(add_uid, 8, 0, 1, 2)

# UID Information
layout.addWidget(QLabel('Set #'), 9, 0)
layout.addWidget(QLabel('UID'), 9, 1)
layout.addWidget(QLabel('UID Name'), 9, 2)
layout.addWidget(QLabel('Package'), 9, 3)

for i in range(4):
    layout.addWidget(QLabel(f'Set #{i + 1}'), 10 + i, 0)
    uid = QLineEdit()
    layout.addWidget(uid, 10 + i, 1)
    uid_name = QLineEdit()
    layout.addWidget(uid_name, 10 + i, 2)
    package = QLineEdit()
    layout.addWidget(package, 10 + i, 3)

# Action Buttons
cancel_btn = QPushButton('ยกเลิก')
layout.addWidget(cancel_btn, 14, 0)
gift_check = QCheckBox('ของแจก')
layout.addWidget(gift_check, 14, 1)
ready_check = QCheckBox('พร้อมเติม')
layout.addWidget(ready_check, 14, 2)
confirm_btn = QPushButton('ยืนยัน')
layout.addWidget(confirm_btn, 14, 3)
close_btn = QPushButton('ปิด (ไม่บันทึก)')
layout.addWidget(close_btn, 14, 4)

window.setLayout(layout)
window.show()

app.exec_()
