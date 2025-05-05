from django.shortcuts import render
def index_page(request):
    context = {
        "page_name": "Информация о пользователе",
        "show_info": True,
        "user_image_url": "https://my.mshp.ru/media/ck_uploads/alekseev_ns/2024/02/03/ubgqxr.jpg",
        "user_name": "Иван",
        "user_surname": "Иванов",
        "user_patronymic": "Иванович",
        "online": False,
        "last_seen": "сегодня в 21:34",
        "location": "Россия",
        "show_comments": True,
        "comments": [
            "Всем привет, я только что зарегистрировался!",
            "Ого, как много тут людей ╰(*°▽°*)╯",
            "Я разобрался, как тут всё устроено!",
            "Я, к слову, учу Python Django!",
        ],
        "interests_show": True,
        "interests_films_show": True,
        "interests_films": [
            "Это выдуманное название фильма",
            "Так сделано, чтобы не нарушить авторские права",
            "Чебурашка",
        ],
        "interests_music_show": True,
        "interests_music": [
            "Ну очень классная музыка",
            "Евровидение 2012",
            "Спокойной ночи малыши",
            "Supermegahit",
        ],
    }
    return render(request, "index.html", context) 
