from flask import Flask, request, jsonify
from transformers import pipeline
from werkzeug.utils import secure_filename
import uuid
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

print('AI 모델 로딩 중...')
try:
    classifier = pipeline('image-classification', model='dima806/ai_vs_real_image_detection')
    print('AI 모델 로드 완료!')
except Exception as e:
    print(f'모델 로드 실패: {e}')
    classifier = None

def apply_80_percent_threshold(prediction, confidence):
    """80% 임계값 적용"""
    if confidence < 0.8:
        return 'UNCERTAIN', confidence * 0.5, "신뢰도가 낮아 정확한 판단이 어렵습니다"
    return prediction, confidence, "정확한 예측입니다"

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI 이미지 분류기 (80% 임계값)</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 600px; margin: 0 auto; }
            .upload-area { border: 2px dashed #ccc; padding: 20px; text-align: center; margin: 20px 0; }
            .result { margin: 20px 0; padding: 15px; border-radius: 5px; }
            .high-confidence { background-color: #d4edda; border: 1px solid #c3e6cb; }
            .low-confidence { background-color: #fff3cd; border: 1px solid #ffeaa7; }
            button { background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 AI 이미지 분류기 (80% 임계값)</h1>
            <p>이미지를 업로드하여 AI 생성 이미지인지 실제 이미지인지 판별해보세요!</p>
            <div class="upload-area">
                <p><strong>80% 이상 신뢰도만 정확한 예측으로 표시됩니다.</strong></p>
                <p>80% 미만은 "불확실"로 표시됩니다.</p>
            </div>
            
            <form id="uploadForm" enctype="multipart/form-data">
                <input type="file" id="fileInput" accept="image/*" required>
                <button type="submit">분석하기</button>
            </form>
            
            <div id="result"></div>
        </div>
        
        <script>
        document.getElementById('uploadForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            
            if (!file) {
                alert('파일을 선택해주세요.');
                return;
            }
            
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                const resultDiv = document.getElementById('result');
                
                if (result.prediction === 'UNCERTAIN') {
                    resultDiv.className = 'result low-confidence';
                } else {
                    resultDiv.className = 'result high-confidence';
                }
                
                resultDiv.innerHTML = `
                    <h3>분석 결과</h3>
                    <p><strong>예측:</strong> ${result.prediction}</p>
                    <p><strong>신뢰도:</strong> ${(result.confidence * 100).toFixed(1)}%</p>
                    <p><strong>설명:</strong> ${result.explanation}</p>
                `;
            } catch (error) {
                document.getElementById('result').innerHTML = '<p style="color: red;">오류가 발생했습니다.</p>';
            }
        });
        </script>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '파일이 선택되지 않았습니다.'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '파일이 선택되지 않았습니다.'})
    
    if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}:
        filename = secure_filename(file.filename)
        unique_filename = str(uuid.uuid4()) + '_' + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        if classifier:
            result = classifier(filepath)
            original_prediction = result[0]['label']
            original_confidence = result[0]['score']
            
            # 80% 임계값 적용
            prediction, confidence, explanation = apply_80_percent_threshold(original_prediction, original_confidence)
            
            if prediction == 'UNCERTAIN':
                explanation = f"신뢰도가 낮아 정확한 판단이 어렵습니다 (원본 신뢰도: {original_confidence:.1%}). 더 정확한 판단을 위해 다른 이미지를 시도해보세요."
            else:
                explanation = f"이 이미지는 {prediction}으로 판단됩니다 (신뢰도: {confidence:.1%})."
        else:
            prediction = 'REAL'
            confidence = 0.5
            explanation = "모델 로드 실패로 인한 기본값입니다."
        
        return jsonify({
            'filename': unique_filename,
            'prediction': prediction,
            'confidence': confidence,
            'explanation': explanation
        })
    
    return jsonify({'error': '지원되지 않는 파일 형식입니다.'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f'Starting AI Image Classifier with 80% threshold on port {port}...')
    app.run(debug=False, host='0.0.0.0', port=port)