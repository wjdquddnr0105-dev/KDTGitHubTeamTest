import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# 모델 불러오기 (서버 시작 시 1회만 로드)
model = tf.keras.models.load_model('cats_and_dogs_classifier.h5')
class_names = ['cats', 'dogs']


@app.route('/predict', methods=['POST'])
def predict():
    # FormData에서 이미지 파일 받기
    if 'image' not in request.files:
        return jsonify({'error': '이미지 파일이 없습니다. "image" 키로 파일을 전송해주세요.'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': '파일이 선택되지 않았습니다.'}), 400

    try:
        # 이미지 읽기 및 전처리
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')  # RGB로 변환 (PNG 등 대응)
        image = image.resize((150, 150))  # 모델 입력 크기에 맞게 리사이즈
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)  # 배치 차원 추가

        # 예측
        result = model.predict(image_array)
        predicted_index = int(result[0][0])
        predicted_class = class_names[predicted_index]
        confidence = float(result[0][0])

        return jsonify({
            'prediction': predicted_class,
            'confidence': confidence,
            'result': f'이 사진은 {predicted_class}입니다.'
        })

    except Exception as e:
        return jsonify({'error': f'예측 중 오류 발생: {str(e)}'}), 500


@app.route('/test/add', methods=['GET'])
def testfunc1():
    print('테스트: 기능 추가')


if __name__ == '__main__':
    print("서버가 시작됩니다... http://localhost:5000")
    print("POST /predict 엔드포인트로 이미지를 전송하세요.")
    app.run(debug=True, port=5000)
