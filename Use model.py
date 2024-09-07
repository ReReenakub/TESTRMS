import numpy as np
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# ข้อมูล
data = [
    # (ข้อมูลตัวอย่าง)
]

# ค่าที่เป็นไปได้รวมถึง 'เสมอ'
colors = ['แดง', 'น้ำเงิน', 'เสมอ']
label_encoder = LabelEncoder()
label_encoder.fit(colors)

# โหลดโมเดล
model = load_model('lstm_model.keras')

# การทำนาย
next_colors = ['แดง', 'น้ำเงิน', 'แดง']
next_colors_encoded = np.array([label_encoder.transform([color])[0] for color in next_colors]).reshape(1, 3, 1)

prediction = model.predict(next_colors_encoded)

# แสดงผลลัพธ์
predicted_color_index = np.argmax(prediction)
predicted_color = label_encoder.inverse_transform([predicted_color_index])
print(f"ผลลัพธ์ที่มีโอกาสออกมากที่สุดคือ: {predicted_color[0]}")
