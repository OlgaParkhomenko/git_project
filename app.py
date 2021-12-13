from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

menu_links = {'index': 'Главная - Сальвадор Дали',
              'about': 'Про Сальвадора',
              'contact': 'Написать отзыв'
              }


@app.route("/")
def default_page():
    return index_page()


@app.route("/index")
def index_page():
    title = 'Образ Сальвадора Дали в кинематографе'
    table_header = ['Год', 'Страна', 'Название', 'Режиссер', 'Сальвадор Дали']
    table_data = [['1978', 'Швеция', 'Приключения Пикассо', 'Таге Даниэльссон', ''],
                  ['1991', 'Испания, Болгария', 'Дали', 'Антонио Рибас', 'Лоренцо Куинн'],
                  ['2001', 'Германия, Испания, Мексика', 'Бунюэль и стол царя Соломона', 'Карлос Саура',
                   'Эрнесто Альтерио'],
                  ['2008', 'Великобритания, Испания', 'Отголоски прошлого', 'Пол Моррисон', 'Роберт Паттинсон'],
                  ['2011', 'США, Испания', 'Полночь в Париже', 'Вуди Аллен', 'Эдриен Броуди']
                  ]
    output = render_template('index.html', title=title, menu_links=menu_links, table_header=table_header, table_data=table_data)
    return output


@app.route("/about")
def about_page():
    title = 'Биография Сальвадора Дали'
    image = 'static/salvador-dali.png'
    h3_dict = {'': 'texts/general_info.txt',
               'Детство': 'texts/childhood.txt',
               'Юность': 'texts/young_adulthood.txt',
               'Молодые годы': 'texts/youth.txt'}

    def upload_content(data_dict):
        for i, k in data_dict.items():
            with open(k, 'r', encoding='utf-8') as f:
                text_insert = {i: f.readlines()}
                h3_dict.update(text_insert)
        return data_dict

    output = render_template('about.html', title=title, menu_links=menu_links, image=image,  data_dict=upload_content(h3_dict))
    return output


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    title = 'Написать отзыв'

    def data_collecting():
        if request.method == "POST":
            first_name = request.form.get("fname") or ''
            last_name = request.form.get("lname") or ''
            email = request.form.get("email") or ''
            options = request.form.get("options") or ''
            message = request.form.get("message") or ''
            answer = request.form.get("answer") or ''
            response = [first_name, last_name, email, options, message, answer]
            with open('texts/responses.txt', 'a', encoding='utf-8') as f:
                for i in response:
                    f.writelines(i)
                    f.write('\n')
                f.write('\n')
        return render_template('form.html')

    output = render_template('contact.html', title=title, menu_links=menu_links, data_collecting=data_collecting())
    return output


@app.errorhandler(404)
def page_not_found(e):
    image = 'static/404.png'
    message = '404 : Что-то пошло не так'
    return render_template('error.html', menu_links=menu_links, image=image, message=message)


@app.errorhandler(500)
def internal_server_error(e):
    image = 'static/500.png'
    message = '500 : Случилась ошибка'
    return render_template('error.html', menu_links=menu_links, image=image, message=message)


if __name__ == "__main__":
    app.run()
