import requests #necessita que a instalaçao desta bibilioteca antes da utiizaçao
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

#vetor contendo as indereços das imagens a serem baixada

t1 = time.perf_counter()
#armazena o tempo que começou a execução do codigo

#função para fazer o download
def download_image(img_url):
    img_bytes = requests.get(img_url).content #baixa a imagem e armazena na variavel
    img_name = img_url.split('/')[3] # pega a string depois da terceira / para ser o nome da imagem
    img_name = f'{img_name}.jpg' # adiciona .jpg no nome
    with open(img_name, 'wb') as img_file:  # abre o fuxo de arquivos para escrever um arquivo nomodo binario
        img_file.write(img_bytes)   
        print(f'{img_name} was downloaded...')

# cria as multthreads para fazer o download das threds em "paralelo"
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()# armazena o tempo depois da execução

print(f'Finished in {t2-t1} seconds') #printa a difeença de tempo