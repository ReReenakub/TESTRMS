import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

# ข้อมูล
data = [
    # (ข้อมูลตัวอย่าง)
]

# ค่าที่เป็นไปได้รวมถึง 'เสมอ'
colors = ['แดง', 'น้ำเงิน', 'เสมอ']
label_encoder = LabelEncoder()
label_encoder.fit(colors)

X = []
y = []

# แปลงข้อมูลลำดับสีให้เป็นตัวเลข
for round_data in data:
    x_values = round_data[:3]
    y_value = round_data[3]

    # แปลงค่าเป็นตัวเลข
    x_encoded = [label_encoder.transform([color])[0] for color in x_values]
    y_encoded = label_encoder.transform([y_value])[0]

    X.append(x_encoded)
    y.append(y_encoded)

# แปลงข้อมูลเป็น numpy array
X = np.array(X)
y = np.array(y)

# แปลง y เป็น categorical
y = to_categorical(y, num_classes=len(colors))

# สร้างโมเดล LSTM
model = Sequential()
model.add(LSTM(50, input_shape=(3, 1)))
model.add(Dense(len(colors), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# เตรียมข้อมูลให้โมเดล LSTM
X = X.reshape((X.shape[0], X.shape[1], 1))

# ฝึกโมเดล
model.fit(X, y, epochs=500, batch_size=16, validation_split=0.2)

# บันทึกโมเดลในรูปแบบใหม่
model.save('lstm_model.keras')
