from aip import AipOcr
import json

app_id = '你的App ID'
api_key = '你的Api Key'
secret_key = '你的Secret Key'

f = open('ocr_text.jpg', 'rb')
image = f.read()

client = AipOcr(app_id, api_key, secret_key)

options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

result = client.basicAccurate(image, options)

result_format = json.dumps(result, indent=4, separators=(',', ':'), ensure_ascii=False)

print(result_format)

for item in result['words_result']:
    print(item['words'])