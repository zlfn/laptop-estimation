import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# CSV 파일 로드
df = pd.read_csv('laptops_data.csv')

# NaN 값을 가진 행 삭제
df.dropna(inplace=True)


# 필요한 특성 선택 (CPU, GPU, RAM 등)
X = df[['Status', 'CPU', 'RAM', 'Storage', 'GPU', 'Screen', 'Touch']]  # 필요한 열 선택

# 종속 변수 (가격) 선택
y = df['Final Price']

# 데이터 분할 (훈련 세트와 테스트 세트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#print(df)
# 선형 회귀 모델 초기화 및 훈련
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test)

# 성능 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# 새로운 노트북 성능 데이터 입력
new_data = np.array([[1, 40000, 16, 512, 12000, 15.6, 0]])  # 필요한 특성 입력

# 예상 가격 예측
predicted_price = model.predict(new_data)
print(f"예상 가격: ${predicted_price[0]:.2f}")

