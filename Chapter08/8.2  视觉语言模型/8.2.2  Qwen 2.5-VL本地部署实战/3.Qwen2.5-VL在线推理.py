from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1/',
    # 设置自己的ModelScope Token
    api_key='3e0fccc2-xxx',
)

response = client.chat.completions.create(
    # ModelScope Model-Id
    model='Qwen/Qwen2.5-VL-7B-Instruct',
    messages=[{
        'role':
            'user',
        'content': [{
            'type': 'text',
            'text': '请认真仔细的描述这幅图',
        }, {
            'type': 'image_url',
            'image_url': {
                'url':
                    'https://modelscope.oss-cn-beijing.aliyuncs.com/demo/images/audrey_hepburn.jpg',
            },
        }],
    }],
    stream=False
)

print(response.choices[0].message.content)
