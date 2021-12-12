from flask import Flask
from flask import render_template


app = Flask(__name__)


# @app.route("/", defaults={'my_path': ''})
# @app.route("/<path:my_path>")
# def menu(my_path):
#     menu_links = {"index": 'Главная - Сальвадор Дали',
#                   "about": 'Про Сальвадора',
#                   "contact": 'Написать отзыв'
#                   }
#     output = render_template('menu.html', menu_links=menu_links)
#     return output

menu_links = {"index": 'Главная - Сальвадор Дали',
              "about": 'Про Сальвадора',
              "contact": 'Написать отзыв'
                  }


@app.route("/index")
def index_page():
    title = 'Образ Сальвадора Дали в кинематографе'
    table_header = ['Год', 'Страна', 'Название', 'Режиссер', 'Сальвадор Дали']
    table_data = [['1978', 'Швеция', 'Приключения Пикассо', 'Таге Даниэльссон', ''],
                  ['1991', 'Испания, Болгария', 'Дали', 'Антонио Рибас', 'Лоренцо Куинн'],
                  ['2001', 'Германия, Испания, Мексика', 'Бунюэль и стол царя Соломона', 'Карлос Саура', 'Эрнесто Альтерио'],
                  ['2008', 'Великобритания, Испания', 'Отголоски прошлого', 'Пол Моррисон', 'Роберт Паттинсон'],
                  ['2011', 'США, Испания', 'Полночь в Париже', 'Вуди Аллен', 'Эдриен Броуди']
                  ]
    global menu_links
    output = render_template('index.html', title=title, table_header=table_header, table_data=table_data, menu_links=menu_links)
    return output


@app.route("/about")
def about_page():
    title = 'Биография Сальвадора Дали'
    image = './images/salvador-dali.png'
    h3_dict = {'': './texts/general_info.txt',
               'Детство': './texts/childhood.txt',
               'Юность': './texts/young_adulthood.txt',
               'Молодые годы': './texts/youth.txt'}

    def upload_content(data_dict):
        for i, k in data_dict.items():
            with open(k, 'r', encoding='utf-8') as f:
                text_insert = {i: f.readlines()}
                h3_dict.update(text_insert)
        return data_dict

    output = render_template('about.html', title=title, image=image,  data_dict=upload_content(h3_dict))
    return output


@app.route("/contact")
def contact_page():
    title = 'Написать отзыв'
    output = render_template('contact.html', title=title)
    return output


if __name__ == "__main__":
    app.run()
