# from PIL import Image

# def main():

#     # 変数の定義
#     input_path = 'input.jpeg'

#     # 画像の読み込み
#     try:
#         with Image.open(input_path) as image:
#             image.show()
#             # 画像情報の表示
#             print(f'image:\n{image}')
#             print(f'type:\n{type(image)}')
#             print(f'filename:\n{image.filename}')
#             print(f'mode: {image.mode}')
#             print(f'size: {image.size}')
            
#             if image.width > 2000:
#                 # resize code.
#                 img_resize = image.resize((256, 256))
#                 img_resize.save('./resized.jpg')
                
#             print(f'width: {image.width}')
#             print(f'height: {image.height}')
#             print(f'format: {image.format}')
#             print(f'min, max: {image.getextrema()}')
#             print(f'information:\n{image.info}')

#     except FileNotFoundError:
#         print(f'Failed to load image from {input_path}')
#     except IOError:
#         print(f'Failed to open image {input_path}')

# if __name__ == '__main__':
#     main()

from PIL import Image, ImageDraw
def main():
    # 変数の定義
    input_path = "./input.jpeg"
    output_path = "./monkeyWithCircle.png"

    # 画像の読み込み
    image = Image.open(input_path)

    # 画像が読み込めなかった場合の例外処理
    if image is None:
        print(f'Failed to load image from {input_path}')
        return
    # ImageDrawオブジェクトの生成
    draw = ImageDraw.Draw(image)

    # 画像上に円の描画
    draw.ellipse((10, 10, 90, 90), outline=(0, 255, 0), width=2)
    draw.ellipse((70, 70, 230, 230), outline=(255, 255, 0), width=6)
    draw.ellipse((150, 150, 250, 250), fill=(0, 255, 255))

    # 画像の保存
    image.save(output_path)
    print(f"Saved image to {output_path}")


if __name__ == '__main__':
    main()
    