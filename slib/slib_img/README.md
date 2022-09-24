# 画像ファイルを処理するプログラミングです

## imgs = ImgFolder('~/')
> 画像が入っているディレクトリを入力

## imgs.change_format(format, new_folder)
> ディレクトリにある画像のフォーマットを変更
> 
> format: jpgなどの画像形式を指定　(例：format='jpg')
> 
> new_folder: 変換後の画像の保存先（例：new_folder='~/happy'）

## imgs.reverse_index(new_folder)
> ディレクトリにある画像のindexを逆順に並べる
>
> new_folder: 変換後の画像の保存先（例：new_folder='~/happy'）
