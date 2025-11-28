
def embedding():
    print("call gpt")
    print("save embedding")

def embed(text):
    return f'embedded {text}'

def embed_api(text):
    vec = embed(text)
    return {'vector': vec, 'dim': len(vec)}