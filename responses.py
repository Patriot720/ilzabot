# -*- coding: utf8 -*-
import re
strkek = 'Вкусный винегрет;Килограмм котлет;Пламенный привет;Злобный людоед;Старый Магомед;На руке кастет;Быстрый интернет;Выступил квартет;Он ушел в рассвет;Черный пистолет;Парочка конфет;В Сирии ракет;Погасили свет;Из яйца омлет;Сильный Пересвет;Завонял клозет;Одноногий табурет;Лебедя балет;Аккомпанемент;Пачка сигарет;Золотой браслет;Старенький скелет;Рокерский дуэт;Подай мне тот предмет;Наварил ты мет;Из трех блюд обед;Техничный пируэт;Из сосны паркет;Кабаниный след;Пушкин был поэт;Написал поэму Фет;На концерт билет;Краденный мопед;Профи ортопед;Тысяча побед;В сухпайке галет;Ну привед, медвед;Горный велосипед;Злобный мясоед;Лезь ты на Мамбет;Быстрый вафлоед;Слушай не даб степ;Ягодный рулет;Восемь здесь планет;Сломанный мольберт;Мудрый импотент;Потанцуй-ка минуэт;Сделай мне минет;Несусветный бред;Старый добрый дед;Значимый секрет;Порванный портрет;Про хача куплет;Сталин дал совет;Мокрый кабриолет;Клетчатый плед;Школьника рунет;Редкий честный мент;Он знакомый кент;На андроиде планшет;Карликовый Шкед;Психов лазарет;Издавай декрет;Мой приоритет;Ленина завет;Множество газет;Много-много лет;Дофига кассет;Сломан трафарет;В Дагестане много бед;Запустил торпед;Мой кардибалет;Греческий атлет;Русский драндулет;Голубой карсет;Модный туалет;Американский госдеп;Притянул комет;Блестящий амулет;Стоянка для карет;Ты собаковед;Странный монумент;Как живой макет;Убежал кадет;Дамы марафет;Голубой берет;Бабкиных бесед;Из жука паштет;Праздничный банкет;В ванной шпингалет;Дал тебе обет;На торрент запрет;Трудный факультет;Заманчивый фермент;Пиковый валет;Стреляет старый фальконет;Ярый ты эстет;Кукуруз брикет;Порванный жакет;Поиграем мы в крокет;Добрый дядя Фред;Мой менталитет;Суверенитет;Судака хребет;Карстовый просвет;В фото есть засвет;Стрельнул арбалет;Шекспировский сонет;Главный ты скинхед;Из пластин бронежилет;Древний минарет;Музыкальный инструмент;Сигаретный вред;БМВ пакет;Розовый букет;Прокричали вслед;Голодный муравьед;Цветущий пустоцвет;Сборничек примет;С молотком сосед;Много старых кед;Городской бюджет;С Хогвардса конверт;Ну и пидора ответ'
responses_list = strkek.split(';')
centerino = """кто в серединке у того яйца на резинке
а кто по краям тому денежки в карман

кто посерединке тот женится на динке (димке, свинке) 
кто по краям тому по золотым коням

кто посерединке тот кушает ботинки.
а кто по краям тот кушает банан"""
centerino_list = centerino.split()
pizda = """пошли!
— куда? 
— тащить лошадь из пруда я руками за узду а ты губами за пизду"""
pizda_list = re.split('\W+', pizda,3)
kakay = """лысый сходи пописай
лохматый сходи покакай"""
kakay_list = kakay.split('\n')
for i,val in enumerate(kakay_list):
	kakay_list[i]  = kakay_list[i].split()
ruka = """дай мне!
— у тебя рука в говне!"""
ruka_list = re.split('\W+', ruka,2)
money = """дай денег
— поссы на веник"""
money_list = money.split('\n')
hui = "кусай за хуй злее будешь пиздеть не будешь будешь пиздеть будешь висеть будешь висеть пиздеть будешь схвачен отхуячен"
zhui = """а
хуй на
жуй два
соси четыре у тебя ебало шире
соси миллион будешь чемпион
соси два миллиона будешь круче чемпиона
соси корзину хватит на всю зиму
хуёв тебе сарай сиди перебирай"""
zhui_list = zhui.split('\n')
