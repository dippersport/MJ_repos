from pytube import YouTube

def download_video(video_url, output_path):
    try:
        # Создаем объект YouTube с указанным URL видео
        yt = YouTube(video_url)
        
        # Выбираем наилучшее доступное видео качества
        video_stream = yt.streams.get_highest_resolution()
        
        # Скачиваем видео в указанный путь
        video_stream.download(output_path)
        print("Видео успешно скачано в", output_path)
    except Exception as e:
        print("Произошла ошибка при скачивании видео:", str(e))

# Задайте URL-адрес видео здесь
video_url = "https://www.youtube.com/watch?v=8Mv5t-3MWQA"  # Замените на реальный URL видео

# Задайте путь для сохранения видео
output_path = "path/to/save/video.mp4"  # Путь, куда сохранить видео

# Вызываем функцию для скачивания видео
download_video(video_url, output_path)


