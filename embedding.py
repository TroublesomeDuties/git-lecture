
def embedding():
    print("call gpt")
    print("save embedding")

def embed(text):
    return f'embedding external by {text}'

def embed_api(text):
    vec = embed(text)
    return {'vector': vec, 'dim': len(vec)}
