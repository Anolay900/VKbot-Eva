import vk_api
from vk_api.longpoll import VkEventType
from MyLongPoll import MyVkLongPoll
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Режим работы / Адрес', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Сотрудничество', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('ЛитРес', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Лекции', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Квесты', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_openlink_button('Афиша',
                             link='https://vk.com/pages?oid=-86441433&p=%D0%90%D0%9A%D0%A2%D0%A3%D0%90%D0%9B%D0%AC%D0%9D%D0%90%D0%AF%20%D0%90%D0%A4%D0%98%D0%A8%D0%90')
keyboard.add_openlink_button('Продлить книги', link='https://vk.com/app5708398_-86441433')
keyboard.add_line()
keyboard.add_openlink_button('Связаться с библиотекарем', link='https://vk.com/app5708398_-86441433')
keyboard.add_button('Выход', color=VkKeyboardColor.NEGATIVE)

lecture = VkKeyboard(one_time=False)
lecture.add_openlink_button('Путь осознанного счастья',
                            link='https://www.youtube.com/playlist?list=PLdeNBHfiUO8L9e7fZoMdFQEj844Hiudi0')
lecture.add_openlink_button('Писатель в городе',
                            link='https://www.youtube.com/playlist?list=PLdeNBHfiUO8K_2p6kHPvS3z5ocnDMi65E')
lecture.add_line()
lecture.add_openlink_button('Взламывая домашние библиотеки',
                            link='https://www.youtube.com/playlist?list=PLdeNBHfiUO8KUlBGoJM1LvOlICNvZxnJL')
lecture.add_openlink_button('Культурный минимум',
                            link='https://www.youtube.com/playlist?list=PLdeNBHfiUO8JaHmetGxGMI-1VHBgowHWM')
lecture.add_line()
lecture.add_openlink_button('Секретные материалы',
                            link='https://www.youtube.com/playlist?list=PLdeNBHfiUO8Lxnnr07O_DxPzGmp4iYiqD')
lecture.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

quest = VkKeyboard(one_time=True)
quest.add_button('Сказки для взрослых', color=VkKeyboardColor.PRIMARY)
quest.add_button('Дракула', color=VkKeyboardColor.PRIMARY)
quest.add_line()
quest.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

# Квест по Дракуле
# ________________________________________________________________

dracula1 = VkKeyboard(one_time=True)
dracula1.add_button('КИ12', color=VkKeyboardColor.PRIMARY)
dracula1.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

dracula_exp = VkKeyboard(one_time=True)
dracula_exp.add_button('Карта истории', color=VkKeyboardColor.PRIMARY)
dracula_exp.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

dracula = VkKeyboard(one_time=False)
dracula.add_button('КИ1', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ2', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('КИ3', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ4', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('КИ5', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ6', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('КИ7', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ8', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('КИ9', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ10', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('КИ11', color=VkKeyboardColor.PRIMARY)
dracula.add_button('КИ13', color=VkKeyboardColor.PRIMARY)
dracula.add_line()
dracula.add_button('Открыть карту решения', color=VkKeyboardColor.PRIMARY)

dracula_points = VkKeyboard(one_time=False)
dracula_points.add_button('Истина', color=VkKeyboardColor.PRIMARY)
dracula_points.add_button('Пройти повторно', color=VkKeyboardColor.PRIMARY)
dracula_points.add_line()
dracula_points.add_button('Квесты', color=VkKeyboardColor.NEGATIVE)
dracula_points.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

dracula_1a = VkKeyboard(one_time=False)
dracula_1a.add_button('1А', color=VkKeyboardColor.PRIMARY)
dracula_1a.add_button('1Б', color=VkKeyboardColor.PRIMARY)
dracula_1a.add_button('1В', color=VkKeyboardColor.PRIMARY)

dracula_2a = VkKeyboard(one_time=False)
dracula_2a.add_button('2А', color=VkKeyboardColor.PRIMARY)
dracula_2a.add_button('2Б', color=VkKeyboardColor.PRIMARY)
dracula_2a.add_button('2В', color=VkKeyboardColor.PRIMARY)

dracula_3a = VkKeyboard(one_time=False)
dracula_3a.add_button('3А', color=VkKeyboardColor.PRIMARY)
dracula_3a.add_button('3Б', color=VkKeyboardColor.PRIMARY)
dracula_3a.add_button('3В', color=VkKeyboardColor.PRIMARY)

dracula_4a = VkKeyboard(one_time=False)
dracula_4a.add_button('4А', color=VkKeyboardColor.PRIMARY)
dracula_4a.add_button('4Б', color=VkKeyboardColor.PRIMARY)
dracula_4a.add_button('4В', color=VkKeyboardColor.PRIMARY)

dracula_5a = VkKeyboard(one_time=False)
dracula_5a.add_button('5А', color=VkKeyboardColor.PRIMARY)
dracula_5a.add_button('5Б', color=VkKeyboardColor.PRIMARY)
dracula_5a.add_button('5В', color=VkKeyboardColor.PRIMARY)

dracula_6a = VkKeyboard(one_time=False)
dracula_6a.add_button('6А', color=VkKeyboardColor.PRIMARY)
dracula_6a.add_button('6Б', color=VkKeyboardColor.PRIMARY)
dracula_6a.add_button('6В', color=VkKeyboardColor.PRIMARY)

dracula_7a = VkKeyboard(one_time=False)
dracula_7a.add_button('7А', color=VkKeyboardColor.PRIMARY)
dracula_7a.add_button('7Б', color=VkKeyboardColor.PRIMARY)
dracula_7a.add_button('7В', color=VkKeyboardColor.PRIMARY)

dracula_8a = VkKeyboard(one_time=False)
dracula_8a.add_button('8А', color=VkKeyboardColor.PRIMARY)
dracula_8a.add_button('8Б', color=VkKeyboardColor.PRIMARY)
dracula_8a.add_button('8В', color=VkKeyboardColor.PRIMARY)

dracula_9a = VkKeyboard(one_time=False)
dracula_9a.add_button('9А', color=VkKeyboardColor.PRIMARY)
dracula_9a.add_button('9Б', color=VkKeyboardColor.PRIMARY)
dracula_9a.add_button('9В', color=VkKeyboardColor.PRIMARY)

dracula_10a = VkKeyboard(one_time=False)
dracula_10a.add_button('10А', color=VkKeyboardColor.PRIMARY)
dracula_10a.add_button('10Б', color=VkKeyboardColor.PRIMARY)
dracula_10a.add_button('10В', color=VkKeyboardColor.PRIMARY)

dracula_11a = VkKeyboard(one_time=False)
dracula_11a.add_button('11А', color=VkKeyboardColor.PRIMARY)
dracula_11a.add_button('11Б', color=VkKeyboardColor.PRIMARY)
dracula_11a.add_button('11В', color=VkKeyboardColor.PRIMARY)

dracula_13a = VkKeyboard(one_time=False)
dracula_13a.add_button('13А', color=VkKeyboardColor.PRIMARY)

# Квест по страдающему средневековью
# ____________________________________________________________________________

fairytails = VkKeyboard(one_time=False)
fairytails.add_button('Вести', color=VkKeyboardColor.PRIMARY)
fairytails.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

fairytails_main = VkKeyboard(one_time=False)
fairytails_main.add_button('Ведьмино кладбище', color=VkKeyboardColor.PRIMARY)
fairytails_main.add_button('Королевский дворец', color=VkKeyboardColor.PRIMARY)
fairytails_main.add_line()
fairytails_main.add_button('Тихая деревня', color=VkKeyboardColor.PRIMARY)
fairytails_main.add_button('Восточная башня', color=VkKeyboardColor.PRIMARY)
fairytails_main.add_line()
fairytails_main.add_button('Мрачный замок', color=VkKeyboardColor.PRIMARY)
fairytails_main.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
fairytails_main.add_line()
fairytails_main.add_button('Завершить свои расследования', color=VkKeyboardColor.NEGATIVE)

necropolis = VkKeyboard(one_time=False)
necropolis.add_button('Отчет писаря. Дело Ведьминого кладбища', color=VkKeyboardColor.PRIMARY)
necropolis.add_button('Задать вопрос Королеве', color=VkKeyboardColor.PRIMARY)
necropolis.add_line()
necropolis.add_button('Осмотреть кладбище', color=VkKeyboardColor.PRIMARY)
necropolis.add_button('Осмотреть темницу', color=VkKeyboardColor.PRIMARY)
necropolis.add_line()
necropolis.add_button('Поговорить с Королем', color=VkKeyboardColor.PRIMARY)
necropolis.add_button('Поговорить с Архиепископом', color=VkKeyboardColor.PRIMARY)
necropolis.add_line()
necropolis.add_button('Вопросы Ведьминого кладбища', color=VkKeyboardColor.NEGATIVE)
necropolis.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

cemetery2 = VkKeyboard(one_time=False)
cemetery2.add_button('Внешние признаки Королевы', color=VkKeyboardColor.PRIMARY)
cemetery2.add_line()
cemetery2.add_button('Колдовская работа', color=VkKeyboardColor.PRIMARY)
cemetery2.add_line()
cemetery2.add_button('Происхождение Королевы', color=VkKeyboardColor.PRIMARY)

cemetery3 = VkKeyboard(one_time=False)
cemetery3.add_button('К месту происшествия', color=VkKeyboardColor.PRIMARY)

cemetery4 = VkKeyboard(one_time=False)
cemetery4.add_button('Вы занимаетесь магическими искусствами?', color=VkKeyboardColor.PRIMARY)
cemetery4.add_line()
cemetery4.add_button('Вы признаете свою вину?', color=VkKeyboardColor.PRIMARY)
cemetery4.add_line()
cemetery4.add_button('Вы были на кладбище ночью?', color=VkKeyboardColor.PRIMARY)

cemetery5 = VkKeyboard(one_time=False)
cemetery5.add_button('Могилы', color=VkKeyboardColor.PRIMARY)
cemetery5.add_line()
cemetery5.add_button('Останки', color=VkKeyboardColor.PRIMARY)
cemetery5.add_line()
cemetery5.add_button('Пыльца фей. Страстоцвет', color=VkKeyboardColor.PRIMARY)
cemetery5.add_line()
cemetery5.add_button('Растительность', color=VkKeyboardColor.PRIMARY)
cemetery5.add_line()
cemetery5.add_button('К месту происшествия', color=VkKeyboardColor.NEGATIVE)

cemetery6 = VkKeyboard(one_time=False)
cemetery6.add_button('Травы', color=VkKeyboardColor.PRIMARY)
cemetery6.add_line()
cemetery6.add_button('Лежанка', color=VkKeyboardColor.PRIMARY)
cemetery6.add_line()
cemetery6.add_button('Пыльца фей. Белокрыльник', color=VkKeyboardColor.PRIMARY)
cemetery6.add_line()
cemetery6.add_button('Окно', color=VkKeyboardColor.PRIMARY)
cemetery6.add_line()
cemetery6.add_button('К месту происшествия', color=VkKeyboardColor.NEGATIVE)

cemetery7 = VkKeyboard(one_time=False)
cemetery7.add_button('К уликам кладбища', color=VkKeyboardColor.PRIMARY)

cemetery8 = VkKeyboard(one_time=False)
cemetery8.add_button('К уликам темницы', color=VkKeyboardColor.PRIMARY)

cemetery9 = VkKeyboard(one_time=False)
cemetery9.add_button('Подкупить Короля', color=VkKeyboardColor.PRIMARY)
cemetery9.add_line()
cemetery9.add_button('Убедить Короля', color=VkKeyboardColor.PRIMARY)
cemetery9.add_line()
cemetery9.add_button('Запугать Короля', color=VkKeyboardColor.PRIMARY)

cemetery10 = VkKeyboard(one_time=False)
cemetery10.add_button('Подкупить Архиепископа', color=VkKeyboardColor.PRIMARY)
cemetery10.add_line()
cemetery10.add_button('Убедить Архиепископа', color=VkKeyboardColor.PRIMARY)
cemetery10.add_line()
cemetery10.add_button('Запугать Архиепископа', color=VkKeyboardColor.PRIMARY)

cemetery11 = VkKeyboard(one_time=False)
cemetery11.add_button('Да, виновна', color=VkKeyboardColor.PRIMARY)
cemetery11.add_button('Нет, невиновна', color=VkKeyboardColor.PRIMARY)

cemetery12 = VkKeyboard(one_time=False)
cemetery12.add_button('Король', color=VkKeyboardColor.PRIMARY)
cemetery12.add_button('Фаворит', color=VkKeyboardColor.PRIMARY)
cemetery12.add_line()
cemetery12.add_button('Брат', color=VkKeyboardColor.PRIMARY)
cemetery12.add_button('Архиепископ', color=VkKeyboardColor.PRIMARY)

cemetery13 = VkKeyboard(one_time=False)
cemetery13.add_button('Золушка', color=VkKeyboardColor.PRIMARY)
cemetery13.add_button('Русалочка', color=VkKeyboardColor.PRIMARY)
cemetery13.add_line()
cemetery13.add_button('Умная Эльза', color=VkKeyboardColor.PRIMARY)
cemetery13.add_button('Дикие лебеди', color=VkKeyboardColor.PRIMARY)
cemetery13.add_line()
cemetery13.add_button('Румпельштильцхен', color=VkKeyboardColor.PRIMARY)
cemetery13.add_button('Белоснежка и семь гномов', color=VkKeyboardColor.PRIMARY)

sleepy = VkKeyboard(one_time=False)
sleepy.add_button('Отчет писаря. Дело Королевского дворца', color=VkKeyboardColor.PRIMARY)
sleepy.add_button('Поговорить с хозяйкой', color=VkKeyboardColor.PRIMARY)
sleepy.add_line()
sleepy.add_button('Осмотреть главный зал', color=VkKeyboardColor.PRIMARY)
sleepy.add_button('Осмотреть спальню', color=VkKeyboardColor.PRIMARY)
sleepy.add_line()
sleepy.add_button('Ответные письма', color=VkKeyboardColor.PRIMARY)
sleepy.add_button('Поговорить с гонцом', color=VkKeyboardColor.PRIMARY)
sleepy.add_line()
sleepy.add_button('Вопросы Королевского дворца', color=VkKeyboardColor.NEGATIVE)
sleepy.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

sleepy2 = VkKeyboard(one_time=False)
sleepy2.add_button('Внешние признаки хозяйки', color=VkKeyboardColor.PRIMARY)
sleepy2.add_line()
sleepy2.add_button('Происхождение хозяйки', color=VkKeyboardColor.PRIMARY)
sleepy2.add_line()
sleepy2.add_button('О детях', color=VkKeyboardColor.PRIMARY)

sleepy3 = VkKeyboard(one_time=False)
sleepy3.add_button('В поместье', color=VkKeyboardColor.PRIMARY)

sleepy4 = VkKeyboard(one_time=False)
sleepy4.add_button('Подкупить хозяйку', color=VkKeyboardColor.PRIMARY)
sleepy4.add_line()
sleepy4.add_button('Убедить хозяйку', color=VkKeyboardColor.PRIMARY)
sleepy4.add_line()
sleepy4.add_button('Запугать хозяйку', color=VkKeyboardColor.PRIMARY)

sleepy5 = VkKeyboard(one_time=False)
sleepy5.add_button('Трон', color=VkKeyboardColor.PRIMARY)
sleepy5.add_line()
sleepy5.add_button('Осмотреть поместье', color=VkKeyboardColor.PRIMARY)
sleepy5.add_line()
sleepy5.add_button('Пыльца фей. Роза', color=VkKeyboardColor.PRIMARY)
sleepy5.add_line()
sleepy5.add_button('Оценка поместья', color=VkKeyboardColor.PRIMARY)
sleepy5.add_line()
sleepy5.add_button('В поместье', color=VkKeyboardColor.NEGATIVE)

sleepy6 = VkKeyboard(one_time=False)
sleepy6.add_button('К уликам тронного зала', color=VkKeyboardColor.PRIMARY)

sleepy7 = VkKeyboard(one_time=False)
sleepy7.add_button('Кровать', color=VkKeyboardColor.PRIMARY)
sleepy7.add_line()
sleepy7.add_button('Пол', color=VkKeyboardColor.PRIMARY)
sleepy7.add_line()
sleepy7.add_button('Пыльца фей. Белладонна', color=VkKeyboardColor.PRIMARY)
sleepy7.add_line()
sleepy7.add_button('Простыни', color=VkKeyboardColor.PRIMARY)
sleepy7.add_line()
sleepy7.add_button('В поместье', color=VkKeyboardColor.NEGATIVE)

sleepy8 = VkKeyboard(one_time=False)
sleepy8.add_button('К уликам спальни', color=VkKeyboardColor.PRIMARY)

sleepy9 = VkKeyboard(one_time=False)
sleepy9.add_button('Письмо от Графини', color=VkKeyboardColor.PRIMARY)
sleepy9.add_line()
sleepy9.add_button('Письмо от Короля Первого Царства', color=VkKeyboardColor.PRIMARY)
sleepy9.add_line()
sleepy9.add_button('Письмо от Королевы Первого Царства', color=VkKeyboardColor.PRIMARY)
sleepy9.add_line()
sleepy9.add_button('Письмо от правителей Старого королевства', color=VkKeyboardColor.PRIMARY)
sleepy9.add_line()
sleepy9.add_button('В поместье', color=VkKeyboardColor.NEGATIVE)

sleepy10 = VkKeyboard(one_time=False)
sleepy10.add_button('Вернуться к письмам', color=VkKeyboardColor.PRIMARY)

sleepy11 = VkKeyboard(one_time=False)
sleepy11.add_button('Подкупить гонца', color=VkKeyboardColor.PRIMARY)
sleepy11.add_line()
sleepy11.add_button('Убедить гонца', color=VkKeyboardColor.PRIMARY)
sleepy11.add_line()
sleepy11.add_button('Запугать гонца', color=VkKeyboardColor.PRIMARY)

sleepy12 = VkKeyboard(one_time=False)
sleepy12.add_button('Гонец', color=VkKeyboardColor.PRIMARY)
sleepy12.add_line()
sleepy12.add_button('Король Первого Царства', color=VkKeyboardColor.PRIMARY)
sleepy12.add_line()
sleepy12.add_button('Король Старого Королевства', color=VkKeyboardColor.PRIMARY)
sleepy12.add_line()
sleepy12.add_button('Бывший король Старого Королевства', color=VkKeyboardColor.PRIMARY)

sleepy13 = VkKeyboard(one_time=False)
sleepy13.add_button('гонец', color=VkKeyboardColor.PRIMARY)
sleepy13.add_button('король Первого Царства', color=VkKeyboardColor.PRIMARY)
sleepy13.add_line()
sleepy13.add_button('королева Первого Царства', color=VkKeyboardColor.PRIMARY)
sleepy13.add_button('король Старого Королевства', color=VkKeyboardColor.PRIMARY)
sleepy13.add_line()
sleepy13.add_button('королева Старого Королевства', color=VkKeyboardColor.PRIMARY)
sleepy13.add_button('графиня', color=VkKeyboardColor.PRIMARY)
sleepy13.add_line()
sleepy13.add_button('хозяйка', color=VkKeyboardColor.PRIMARY)
sleepy13.add_button('бывший король Старого Королевства', color=VkKeyboardColor.PRIMARY)

sleepy14 = VkKeyboard(one_time=False)
sleepy14.add_button('Снежная королева', color=VkKeyboardColor.PRIMARY)
sleepy14.add_button('Спящая красавица', color=VkKeyboardColor.PRIMARY)
sleepy14.add_line()
sleepy14.add_button('Братец и сестрица', color=VkKeyboardColor.PRIMARY)
sleepy14.add_button('Белоснежка и Алоцветик', color=VkKeyboardColor.PRIMARY)
sleepy14.add_line()
sleepy14.add_button('Красавица и чудовище', color=VkKeyboardColor.PRIMARY)
sleepy14.add_button('Госпожа Метелица', color=VkKeyboardColor.PRIMARY)

red = VkKeyboard(one_time=False)
red.add_button('Отчет писаря. Дело Тихой деревни', color=VkKeyboardColor.PRIMARY)
red.add_button('Поговорить с дровосеком', color=VkKeyboardColor.PRIMARY)
red.add_line()
red.add_button('Осмотреть дом отшельницы', color=VkKeyboardColor.PRIMARY)
red.add_button('Осмотреть стол', color=VkKeyboardColor.PRIMARY)
red.add_line()
red.add_button('Поговорить с лесничим', color=VkKeyboardColor.PRIMARY)
red.add_button('Поговорить с сыном дровосека', color=VkKeyboardColor.PRIMARY)
red.add_line()
red.add_button('Вопросы Тихой деревни', color=VkKeyboardColor.NEGATIVE)
red.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

red2 = VkKeyboard(one_time=False)
red2.add_button('Расположение дома', color=VkKeyboardColor.PRIMARY)
red2.add_line()
red2.add_button('Внешние признаки пропавшей', color=VkKeyboardColor.PRIMARY)
red2.add_line()
red2.add_button('Случаи пропажи людей', color=VkKeyboardColor.PRIMARY)

red3 = VkKeyboard(one_time=False)
red3.add_button('В деревню', color=VkKeyboardColor.PRIMARY)

red4 = VkKeyboard(one_time=False)
red4.add_button('Подкупить дровосека', color=VkKeyboardColor.PRIMARY)
red4.add_line()
red4.add_button('Убедить дровосека', color=VkKeyboardColor.PRIMARY)
red4.add_line()
red4.add_button('Запугать дровосека', color=VkKeyboardColor.PRIMARY)

red5 = VkKeyboard(one_time=False)
red5.add_button('Камин', color=VkKeyboardColor.PRIMARY)
red5.add_line()
red5.add_button('Кровать отшельницы', color=VkKeyboardColor.PRIMARY)
red5.add_line()
red5.add_button('Пол дома', color=VkKeyboardColor.PRIMARY)
red5.add_line()
red5.add_button('Стол', color=VkKeyboardColor.PRIMARY)
red5.add_line()
red5.add_button('Пыльца фей. Аконит', color=VkKeyboardColor.PRIMARY)
red5.add_line()
red5.add_button('В деревню', color=VkKeyboardColor.NEGATIVE)

red6 = VkKeyboard(one_time=False)
red6.add_button('К уликам дома', color=VkKeyboardColor.PRIMARY)

red7 = VkKeyboard(one_time=False)
red7.add_button('Пирожки', color=VkKeyboardColor.PRIMARY)
red7.add_line()
red7.add_button('Графин', color=VkKeyboardColor.PRIMARY)
red7.add_line()
red7.add_button('Пыльца фей. Дурман', color=VkKeyboardColor.PRIMARY)
red7.add_line()
red7.add_button('Скатерть', color=VkKeyboardColor.PRIMARY)
red7.add_line()
red7.add_button('В деревню', color=VkKeyboardColor.NEGATIVE)

red8 = VkKeyboard(one_time=False)
red8.add_button('К уликам на столе', color=VkKeyboardColor.PRIMARY)

red9 = VkKeyboard(one_time=False)
red9.add_button('Подкупить лесничего', color=VkKeyboardColor.PRIMARY)
red9.add_line()
red9.add_button('Убедить лесничего', color=VkKeyboardColor.PRIMARY)
red9.add_line()
red9.add_button('Запугать лесничего', color=VkKeyboardColor.PRIMARY)

red10 = VkKeyboard(one_time=False)
red10.add_button('Подкупить сына дровосека', color=VkKeyboardColor.PRIMARY)
red10.add_line()
red10.add_button('Убедить сына дровосека', color=VkKeyboardColor.PRIMARY)
red10.add_line()
red10.add_button('Запугать сына дровосека', color=VkKeyboardColor.PRIMARY)

red11 = VkKeyboard(one_time=False)
red11.add_button('Сбежала', color=VkKeyboardColor.PRIMARY)
red11.add_line()
red11.add_button('Была похищена', color=VkKeyboardColor.PRIMARY)
red11.add_line()
red11.add_button('Была убита', color=VkKeyboardColor.PRIMARY)
red11.add_line()
red11.add_button('Отправилась в погоню', color=VkKeyboardColor.PRIMARY)

red12 = VkKeyboard(one_time=False)
red12.add_button('Лесничий', color=VkKeyboardColor.PRIMARY)
red12.add_line()
red12.add_button('Дровосек', color=VkKeyboardColor.PRIMARY)
red12.add_line()
red12.add_button('Сын дровосека', color=VkKeyboardColor.PRIMARY)
red12.add_line()
red12.add_button('Отшельница', color=VkKeyboardColor.PRIMARY)

red13 = VkKeyboard(one_time=False)
red13.add_button('Принцесса на горошине', color=VkKeyboardColor.PRIMARY)
red13.add_button('Три медведя', color=VkKeyboardColor.PRIMARY)
red13.add_line()
red13.add_button('Дюймовочка', color=VkKeyboardColor.PRIMARY)
red13.add_button('Домик в лесу', color=VkKeyboardColor.PRIMARY)
red13.add_line()
red13.add_button('Гензель и Гретель', color=VkKeyboardColor.PRIMARY)
red13.add_button('Красная Шапочка', color=VkKeyboardColor.PRIMARY)

raps = VkKeyboard(one_time=False)
raps.add_button('Отчет писаря. Дело Восточной башни', color=VkKeyboardColor.PRIMARY)
raps.add_button('Поговорить с пострадавшим', color=VkKeyboardColor.PRIMARY)
raps.add_line()
raps.add_button('Осмотреть лесную поляну', color=VkKeyboardColor.PRIMARY)
raps.add_button('Осмотреть башню', color=VkKeyboardColor.PRIMARY)
raps.add_line()
raps.add_button('Осмотреть окрестности', color=VkKeyboardColor.PRIMARY)
raps.add_button('Поговорить со старушкой', color=VkKeyboardColor.PRIMARY)
raps.add_line()
raps.add_button('Вопросы Восточной башни', color=VkKeyboardColor.NEGATIVE)
raps.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

raps2 = VkKeyboard(one_time=False)
raps2.add_button('Внешние признаки пострадавшего', color=VkKeyboardColor.PRIMARY)
raps2.add_line()
raps2.add_button('Происхождение пострадавшего', color=VkKeyboardColor.PRIMARY)
raps2.add_line()
raps2.add_button('Куда направлялся пострадавший', color=VkKeyboardColor.PRIMARY)

raps3 = VkKeyboard(one_time=False)
raps3.add_button('К башне', color=VkKeyboardColor.PRIMARY)

raps4 = VkKeyboard(one_time=False)
raps4.add_button('Подкупить пострадавшего', color=VkKeyboardColor.PRIMARY)
raps4.add_line()
raps4.add_button('Убедить пострадавшего', color=VkKeyboardColor.PRIMARY)
raps4.add_line()
raps4.add_button('Запугать пострадавшего', color=VkKeyboardColor.PRIMARY)

raps5 = VkKeyboard(one_time=False)
raps5.add_button('Башня', color=VkKeyboardColor.PRIMARY)
raps5.add_line()
raps5.add_button('Веревка', color=VkKeyboardColor.PRIMARY)
raps5.add_line()
raps5.add_button('Кусты ежевики', color=VkKeyboardColor.PRIMARY)
raps5.add_line()
raps5.add_button('Пыльца фей. Акация', color=VkKeyboardColor.PRIMARY)
raps5.add_line()
raps5.add_button('К башне', color=VkKeyboardColor.NEGATIVE)

raps6 = VkKeyboard(one_time=False)
raps6.add_button('К уликам на лесной поляне', color=VkKeyboardColor.PRIMARY)

raps7 = VkKeyboard(one_time=False)
raps7.add_button('Странная веревка', color=VkKeyboardColor.PRIMARY)
raps7.add_line()
raps7.add_button('Ножницы', color=VkKeyboardColor.PRIMARY)
raps7.add_line()
raps7.add_button('Пыльца фей. Колокольчик', color=VkKeyboardColor.PRIMARY)
raps7.add_line()
raps7.add_button('Шелковые нити', color=VkKeyboardColor.PRIMARY)
raps7.add_line()
raps7.add_button('К башне', color=VkKeyboardColor.NEGATIVE)

raps8 = VkKeyboard(one_time=False)
raps8.add_button('К уликам в башне', color=VkKeyboardColor.PRIMARY)

raps9 = VkKeyboard(one_time=False)
raps9.add_button('Цветущий сад', color=VkKeyboardColor.PRIMARY)
raps9.add_line()
raps9.add_button('Вглубь леса', color=VkKeyboardColor.PRIMARY)
raps9.add_line()
raps9.add_button('Домик на краю леса', color=VkKeyboardColor.PRIMARY)

raps10 = VkKeyboard(one_time=False)
raps10.add_button('Подкупить старушку', color=VkKeyboardColor.PRIMARY)
raps10.add_line()
raps10.add_button('Убедить старушку', color=VkKeyboardColor.PRIMARY)
raps10.add_line()
raps10.add_button('Запугать старушку', color=VkKeyboardColor.PRIMARY)

raps11 = VkKeyboard(one_time=False)
raps11.add_button('Старушка', color=VkKeyboardColor.PRIMARY)
raps11.add_line()
raps11.add_button('Человек, которого он ищет', color=VkKeyboardColor.PRIMARY)
raps11.add_line()
raps11.add_button('Хозяева дома', color=VkKeyboardColor.PRIMARY)
raps11.add_line()
raps11.add_button('Несчастный случай', color=VkKeyboardColor.PRIMARY)

raps12 = VkKeyboard(one_time=False)
raps12.add_button('Старушку', color=VkKeyboardColor.PRIMARY)
raps12.add_line()
raps12.add_button('Девушку', color=VkKeyboardColor.PRIMARY)
raps12.add_line()
raps12.add_button('Хозяев дома', color=VkKeyboardColor.PRIMARY)

raps13 = VkKeyboard(one_time=False)
raps13.add_button('Рапунцель', color=VkKeyboardColor.PRIMARY)
raps13.add_button('Дева Малейн', color=VkKeyboardColor.PRIMARY)
raps13.add_line()
raps13.add_button('Свинопас', color=VkKeyboardColor.PRIMARY)
raps13.add_button('Королевские дети', color=VkKeyboardColor.PRIMARY)
raps13.add_line()
raps13.add_button('Три апельсина', color=VkKeyboardColor.PRIMARY)
raps13.add_button('Принц и нищий', color=VkKeyboardColor.PRIMARY)

blue = VkKeyboard(one_time=False)
blue.add_button('Отчет писаря. Дело Мрачного замка', color=VkKeyboardColor.PRIMARY)
blue.add_button('Поговорить с баронессой', color=VkKeyboardColor.PRIMARY)
blue.add_line()
blue.add_button('Осмотреть тело Барона', color=VkKeyboardColor.PRIMARY)
blue.add_button('Осмотреть гостиную', color=VkKeyboardColor.PRIMARY)
blue.add_line()
blue.add_button('Поговорить с братьями', color=VkKeyboardColor.PRIMARY)
blue.add_button('Поговорить с сестрой', color=VkKeyboardColor.PRIMARY)
blue.add_line()
blue.add_button('Вопросы Мрачного замка', color=VkKeyboardColor.NEGATIVE)
blue.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

husband2 = VkKeyboard(one_time=False)
husband2.add_button('Внешние признаки барона', color=VkKeyboardColor.PRIMARY)
husband2.add_line()
husband2.add_button('Родословная барона', color=VkKeyboardColor.PRIMARY)
husband2.add_line()
husband2.add_button('Отношения в семье', color=VkKeyboardColor.PRIMARY)

husband3 = VkKeyboard(one_time=False)
husband3.add_button('К замку', color=VkKeyboardColor.PRIMARY)

husband4 = VkKeyboard(one_time=False)
husband4.add_button('Подкупить баронессу', color=VkKeyboardColor.PRIMARY)
husband4.add_line()
husband4.add_button('Убедить баронессу', color=VkKeyboardColor.PRIMARY)
husband4.add_line()
husband4.add_button('Запугать баронессу', color=VkKeyboardColor.PRIMARY)

husband5 = VkKeyboard(one_time=False)
husband5.add_button('Осмотреть внутренние карманы', color=VkKeyboardColor.PRIMARY)
husband5.add_line()
husband5.add_button('Дать команду собаке взять след', color=VkKeyboardColor.PRIMARY)
husband5.add_line()
husband5.add_button('Пыльца фей. Горечавка', color=VkKeyboardColor.PRIMARY)
husband5.add_line()
husband5.add_button('Осмотреть нож', color=VkKeyboardColor.PRIMARY)
husband5.add_line()
husband5.add_button('К замку', color=VkKeyboardColor.NEGATIVE)

husband6 = VkKeyboard(one_time=False)
husband6.add_button('К скрытым уликам', color=VkKeyboardColor.PRIMARY)

husband7 = VkKeyboard(one_time=False)
husband7.add_button('Ключница', color=VkKeyboardColor.PRIMARY)
husband7.add_line()
husband7.add_button('Портрет на стене', color=VkKeyboardColor.PRIMARY)
husband7.add_line()
husband7.add_button('Пыльца фей. Мак', color=VkKeyboardColor.PRIMARY)
husband7.add_line()
husband7.add_button('Амбарная книга', color=VkKeyboardColor.PRIMARY)
husband7.add_line()
husband7.add_button('Ключ', color=VkKeyboardColor.PRIMARY)
husband7.add_line()
husband7.add_button('К замку', color=VkKeyboardColor.NEGATIVE)

husband8 = VkKeyboard(one_time=False)
husband8.add_button('К уликам гостиной', color=VkKeyboardColor.PRIMARY)

husband9 = VkKeyboard(one_time=False)
husband9.add_button('Подкупить братьев', color=VkKeyboardColor.PRIMARY)
husband9.add_line()
husband9.add_button('Убедить братьев', color=VkKeyboardColor.PRIMARY)
husband9.add_line()
husband9.add_button('Запугать братьев', color=VkKeyboardColor.PRIMARY)

husband10 = VkKeyboard(one_time=False)
husband10.add_button('Подкупить сестру', color=VkKeyboardColor.PRIMARY)
husband10.add_line()
husband10.add_button('Убедить сестру', color=VkKeyboardColor.PRIMARY)
husband10.add_line()
husband10.add_button('Запугать сестру', color=VkKeyboardColor.PRIMARY)

mur2 = VkKeyboard(one_time=False)
mur2.add_button('От 0 до 5 баллов', color=VkKeyboardColor.PRIMARY)
mur2.add_line()
mur2.add_button('От 6 до 10 баллов', color=VkKeyboardColor.PRIMARY)
mur2.add_line()
mur2.add_button('От 11 до 15 баллов', color=VkKeyboardColor.PRIMARY)
mur2.add_line()
mur2.add_button('К карте', color=VkKeyboardColor.NEGATIVE)

husband11 = VkKeyboard(one_time=False)
husband11.add_button('Баронесса', color=VkKeyboardColor.PRIMARY)
husband11.add_line()
husband11.add_button('Барон', color=VkKeyboardColor.PRIMARY)
husband11.add_line()
husband11.add_button('Братья', color=VkKeyboardColor.PRIMARY)
husband11.add_line()
husband11.add_button('Сестра', color=VkKeyboardColor.PRIMARY)

husband12 = VkKeyboard(one_time=False)
husband12.add_button('баронесса', color=VkKeyboardColor.PRIMARY)
husband12.add_line()
husband12.add_button('барон', color=VkKeyboardColor.PRIMARY)
husband12.add_line()
husband12.add_button('братья', color=VkKeyboardColor.PRIMARY)
husband12.add_line()
husband12.add_button('сестра', color=VkKeyboardColor.PRIMARY)

husband13 = VkKeyboard(one_time=False)
husband13.add_button('Король Дроздобород', color=VkKeyboardColor.PRIMARY)
husband13.add_button('Огниво', color=VkKeyboardColor.PRIMARY)
husband13.add_line()
husband13.add_button('Гамельнский крысолов', color=VkKeyboardColor.PRIMARY)
husband13.add_button('Джек и бобовый стебель', color=VkKeyboardColor.PRIMARY)
husband13.add_line()
husband13.add_button('Синяя Борода', color=VkKeyboardColor.PRIMARY)
husband13.add_button('Новое платье короля', color=VkKeyboardColor.PRIMARY)

fairy_end = VkKeyboard(one_time=False)
fairy_end.add_button('Повторить игру', color=VkKeyboardColor.PRIMARY)
fairy_end.add_line()
fairy_end.add_button('Перечень сказок', color=VkKeyboardColor.PRIMARY)
fairy_end.add_line()
fairy_end.add_button('Квесты', color=VkKeyboardColor.NEGATIVE)
fairy_end.add_line()
fairy_end.add_button('В меню', color=VkKeyboardColor.NEGATIVE)

answers = VkKeyboard(one_time=False)
answers.add_button('Продолжить расследование', color=VkKeyboardColor.NEGATIVE)


def write_message(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': keyboard.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_lecture(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': lecture.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_quest(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': quest.get_keyboard(), 'attachment': ','.join(attachments)})


# Квест по Дракуле
# ______________________________________________________________________

def write_message_dracula_exp(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_exp.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula1(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula1.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_points(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_points.get_keyboard(),
                                           'attachment': ','.join(attachments)})


def write_message_dracula_1a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_1a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_2a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_2a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_3a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_3a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_4a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_4a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_5a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_5a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_6a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_6a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_7a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_7a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_8a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_8a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_9a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_9a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_10a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_10a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_11a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_11a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_dracula_13a(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': dracula_13a.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_end(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'attachment': ','.join(attachments)})


# Квест по страдающему средневековью
# _____________________________________________________________________________________

def write_message_tale_begins(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': fairytails.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_map(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': fairytails_main.get_keyboard(),
                                           'attachment': ','.join(attachments)})


def write_message_witch_hour(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': necropolis.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_report(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_back(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery3.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_questions(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery4.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_grave(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery5.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_prison(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery6.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_evidence(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery7.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_evidence2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery8.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_king(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery9.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_priest(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery10.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_guilt(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery11.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_who(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery12.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_witch_story(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': cemetery13.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty3(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy3.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty4(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy4.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty5(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy5.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty_evidence(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy6.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty_evidence2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy7.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty6(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy8.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty7(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy9.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty8(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy10.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty9(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy11.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty10(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy12.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty11(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy13.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beauty12(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': sleepy14.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat3(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red3.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat4(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red4.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat5(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red5.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat6(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red6.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat7(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red7.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat8(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red8.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat9(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red9.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat10(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red10.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat11(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red11.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat12(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red12.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_hat13(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': red13.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower3(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps3.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower4(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps4.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower5(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps5.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower6(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps6.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower7(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps7.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower8(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps8.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower9(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps9.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower10(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps10.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower11(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps11.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower12(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps12.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_tower13(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': raps13.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': blue.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard2(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard3(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband3.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard4(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband4.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard5(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband5.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard6(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband6.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard7(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband7.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard8(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband8.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard9(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband9.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard10(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband10.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard11(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband11.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard12(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband12.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard13(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': husband13.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_beard14(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': mur2.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_pointstale(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': fairy_end.get_keyboard(), 'attachment': ','.join(attachments)})


def write_message_pointser(sender, message):
    authorization.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                           'keyboard': answers.get_keyboard(), 'attachment': ','.join(attachments)})


token = ''
# токен группы, к которой привязан бот я убрала

authorization = vk_api.VkApi(token=token)
longpoll = MyVkLongPoll(authorization)
upload = VkUpload(authorization)


# Квест по страдающему средневековью
# _____________________________________________________________________
photo_links = {
    # Основные
    'img': './pic/MyEmoji_20200608_181419_595.jpg',
    'img1': './pic/MyEmoji20200608181418452.jpg',
    'img2': './pic/MyEmoji202006890225500.jpg',
    'img3': './pic/MyEmoji_7.jpg',
    'img4': './pic/MyEmoji20200456799765.jpg',
    'img5': './pic/MyEmoji_20200608_181418_427-4.jpg',
    'img6': './pic/MyEmoji202006743022245.jpg',
    'img7': './pic/MyEmoji_20200608_181418_427.jpg',

    # Дракула
    'drac': './pic/vamp.jpg',
    'drac1': './pic/vamp1.jpg',
    'drac_a': './pic/vamp_ku1.jpg',
    'drac_a2': './pic/vamp_ku2.jpg',
    'drac_a3': './pic/vamp_ku3.jpg',
    'drac_a4': './pic/vamp_ku4.jpg',
    'drac_a5': './pic/vamp_ku5.jpg',
    'drac_a6': './pic/vamp_ku6.jpg',
    'drac_a7': './pic/vamp_ku7.jpg',
    'drac_a8': './pic/vamp_ku8.jpg',
    'drac_a9': './pic/vamp_ku9.jpg',
    'drac_a10': './pic/vamp_ku10.jpg',
    'drac_a11': './pic/vamp_ku11.jpg',
    'drac_a13': './pic/vamp_ku13.jpg',
    'drac_answers': './pic/vamp_answers.jpg',
    
    # Квест по страдающему средневековью
    'fairy': './pic/rules.png',
    'main_map': './pic/map.png',
    'cemetery1': './pic/cemetery1.png',
    'report_swan': './pic/report.png',
    'queens_look': './pic/queens_look.png',
    'work': './pic/witch_work.png',
    'origin': './pic/origin.png',
    'question_queen': './pic/question_queen.png',
    'question_1': './pic/question1.png',
    'question_2': './pic/question2.png',
    'question_3': './pic/question3.png',
    'cemetery': './pic/cemetery.png',
    'graves': './pic/graves.png',
    'bones': './pic/bones.png',
    'grass': './pic/grass.png',
    'fairy_magic': './pic/fairy_magic.png',
    'prison': './pic/prison.png',
    'nettle': './pic/nettle.png',
    'small_bed': './pic/small_bed.png',
    'window': './pic/window.png',
    'fairy_magic2': './pic/fairy_magic2.png',
    'talk_king': './pic/talk_king.png',
    'gold_king': './pic/gold_king.png',
    'kind_king': './pic/kind_king.png',
    'fear_king': './pic/fear_king.png',
    'talk_priest':  './pic/talk_priest.png',
    'gold_priest': './pic/gold_priest.png',
    'kind_priest': './pic/kind_priest.png',
    'fear_priest': './pic/fear_priest.png',
    'guilt': './pic/guilty_queen.png',
    'who': './pic/who.png',
    'swan_story': './pic/swan_story.png',
    'king_castle': './pic/king_castle.png',
    'lady_look': './pic/lady_look.png',
    'lady_original': './pic/lady_original.png',
    'child': './pic/child.png',
    'castle_deal': './pic/castle_deal.png',
    'talk_lady': './pic/talk_lady.png',
    'gold_lady': './pic/gold_lady.png',
    'kind_lady': './pic/kind_lady.png',
    'fear_lady': './pic/fear_lady.png',
    'throne_room': './pic/throne_room.png',
    'throne': './pic/throne.png',
    'house_look': './pic/house_look.png',
    'house_gold': './pic/house_gold.png',
    'fairy_magic3': './pic/fairy_magic3.png',
    'fairy_magic4': './pic/fairy_magic4.png',
    'sleepy_bed': './pic/sleepy_bed.png',
    'sleep_room': './pic/sleep_room.png',
    'sleepy_floar': './pic/sleepy_floar.png',
    'sleepy_sheets': './pic/sleepy_sheets.png',
    'letters': './pic/letters.png',
    'countess': './pic/countess.png',
    'sleepy_king': './pic/sleepy_king.png',
    'sleepy_queen': './pic/sleepy_queen.png',
    'old_kindom_rulers': './pic/old_kindom_rulers.png',
    'talk_runner': './pic/talk_runner.png',
    'gold_runner': './pic/gold_runner.png',
    'kind_runner': './pic/kind_runner.png',
    'fear_runner': './pic/fear_runner.png',
    'father_child': './pic/father_child.png',
    'honor': './pic/honor.png',
    'sleepy_what': './pic/sleepy_what.png',
    'red_hat': './pic/red_hat.png',
    'report_vil': './pic/report_vil.png',
    'house_red': './pic/house_red.png',
    'woman_red': './pic/woman_red.png',
    'missing': './pic/missing.png',
    'talk_wood': './pic/talk_wood.png',
    'gold_wood': './pic/gold_wood.png',
    'kind_wood': './pic/kind_wood.png',
    'fear_wood': './pic/fear_wood.png',
    'redhouse_look': './pic/redhouse_look.png',
    'fire': './pic/fire.png',
    'red_bed': './pic/red_bed.png',
    'red_floar': './pic/red_floar.png',
    'red_table': './pic/red_table.png',
    'fairy_magic5': './pic/fairy_magic5.png',
    'table_look': './pic/table_look.png',
    'pie': './pic/pie.png',
    'blood': './pic/blood.png',
    'tablecloth': './pic/tablecloth.png',
    'fairy_magic6': './pic/fairy_magic6.png',
    'forester_talk': './pic/forester_talk.png',
    'gold_forester': './pic/gold_forester.png',
    'kind_forester': './pic/kind_forester.png',
    'fear_forester': './pic/fear_forester.png',
    'son_talk': './pic/son_talk.png',
    'gold_son': './pic/gold_son.png',
    'kind_son': './pic/kind_son.png',
    'fear_son': './pic/fear_son.png',
    'red_woman_where': './pic/red_woman_where.png',
    'red_missing_people': './pic/red_missing_people.png',
    'red_what': './pic/red_what.png',
    'eastern_tower': './pic/eastern_tower.png',
    'prince_look': './pic/prince_look.png',
    'tower_report': './pic/tower_report.png',
    'prince_origin': './pic/prince_origin.png',
    'where_are_you_going': './pic/where_are_you_going.png',
    'talk_prince': './pic/talk_prince.png',
    'gold_prince': './pic/gold_prince.png',
    'kind_prince': './pic/kind_prince.png',
    'fear_prince': './pic/fear_prince.png',
    'look_glade': './pic/look_glade.png',
    'glade_rope': './pic/glade_rope.png',
    'glade_berries': './pic/glade_berries.png',
    'glade_tower': './pic/glade_tower.png',
    'fairy_magic7': './pic/fairy_magic7.png',
    'fairy_magic8': './pic/fairy_magic8.png',
    'look_tower': './pic/look_tower.png',
    'tower_rope': './pic/tower_rope.png',
    'tower_sc': './pic/tower_sc.png',
    'tower_silk': './pic/tower_silk.png',
    'look_near': './pic/look_near.png',
    'near_garden': './pic/near_garden.png',
    'near_forest': './pic/near_forest.png',
    'near_house': './pic/near_house.png',
    'talk_granny': './pic/talk_granny.png',
    'gold_granny': './pic/gold_granny.png',
    'kind_granny': './pic/kind_granny.png',
    'fear_granny': './pic/fear_granny.png',
    'blind': './pic/blind.png',
    'looking_for': './pic/looking_for.png',
    'raps_what': './pic/raps_what.png',
    'husband': './pic/dark.png',
    'dark_report': './pic/dark_report.png',
    'dark_origin': './pic/dark_origin.png',
    'dark_family': './pic/dark_family.png',
    'dark_look': './pic/dark_look.png',
    'talk_duke': './pic/talk_duke.png',
    'gold_duke': './pic/gold_duke.png',
    'kind_duke': './pic/kind_duke.png',
    'fear_duke': './pic/fear_duke.png',
    'body_look': './pic/body_look.png',
    'pocket': './pic/pocket.png',
    'doggy': './pic/doggy.png',
    'knife': './pic/knife.png',
    'fairy_magic9': './pic/fairy_magic9.png',
    'fairy_magic10': './pic/fairy_magic10.png',
    'guest_look': './pic/guest_look.png',
    'guest_key': './pic/guest_key.png',
    'portrait': './pic/portrait.png',
    'book': './pic/book.png',
    'talk_brothers': './pic/talk_brothers.png',
    'gold_brothers': './pic/gold_brothers.png',
    'fear_brothers': './pic/fear_brothers.png',
    'kind_brothers': './pic/kind_brothers.png',
    'talk_sister': './pic/talk_sister.png',
    'gold_sister': './pic/gold_sister.png',
    'fear_sister': './pic/fear_sister.png',
    'kind_sister': './pic/kind_sister.png',
    'magic_key': './pic/magic_key.png',
    'mur': './pic/mur.png',
    'nomur': './pic/nomur.png',
    'murwhat': './pic/murwhat.png',
    'low': './pic/low.png',
    'hight': './pic/hight.png',
    'middle': './pic/middle.png',
    'red_red': './pic/red_red.jpg',
    'sleep_beauty': './pic/sleep_beauty.jpg',
    'wild_swan': './pic/wild_swan.jpg',
    'rapuns': './pic/rapuns.jpg',
    'blue_beard': './pic/blue_beard.jpg'
}

photos = {}
for key in photo_links:
    upload_image = upload.photo_messages(photos=photo_links[key])[0]
    photos[key] = upload_image

# photos['fairy']


blue_beard1 = './pic/blue_beard.jpg'
upload_image = upload.photo_messages(photos=blue_beard1)[0]
blue_beard = upload_image

counter_fairy = 0

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received = event.text
        sender = event.user_id
        if 'Привет' in received or 'Здравствуйте' in received or 'Добрый день' in received or 'привет' in received or 'здравствуйте' in received or 'добрый день' in received or 'Добрый вечер' in received or 'добрый вечер' in received or 'Доброе утро' in received or 'доброе утро' in received or 'здрасте' in received or 'Здрасте' in received:
            attachments = ['photo{}_{}'.format(photos['img']['owner_id'], photos['img']['id'])]
            write_message(sender,
                          'Доброго времени суток!\nЯ официальный бот-помощник библиотеки №146.\nМеня зовут Эва. Вот, что я умею :)')
        if 'Эва' in received or 'эва' in received:
            attachments = ['photo{}_{}'.format(photos['img1']['owner_id'], photos['img1']['id'])]
            write_message(sender, 'Я здесь! Чем могу помочь?')
        if received == 'Режим работы / Адрес':
            attachments = ['photo{}_{}'.format(photos['img2']['owner_id'], photos['img2']['id'])]
            write_message(sender,
                          'Временно не обслуживаем до 15 января. Связаться с нами, продлить книги можно в будние дни (9:30-18:00) по телефону, email и VK 💙\n\nАдрес: ул.Генерала Белова, д.29, к.3, м.Домодедовская')
        if received == 'Сотрудничество':
            attachments = ['photo{}_{}'.format(photos['img3']['owner_id'], photos['img3']['id'])]
            write_message(sender,
                          'Приглашаем к сотрудничеству:\n\n✔Людей, желающих организовать кружки или проводить мастер – классы;'
                          '\n✔Лидеров, желающих организовать объединения единомышленников;'
                          '\n✔Творческих людей, желающих организовывать свои концерты, выставки и встречи;'
                          '\n✔Лекторов;'
                          '\n✔Преподавателей;'
                          '\n✔Волонтеров.'
                          '\nЕсли у Вас есть знания, талант или идея, но нет возможности их реализации – наша библиотека предоставит Вам свою площадку.'
                          '\nУ нас созданы комфортные условия для общения и творческого развития.'
                          '\n\n☎: 8(495) 393-00-32')
        if received == 'ЛитРес':
            attachments = ['photo{}_{}'.format(photos['img4']['owner_id'], photos['img4']['id'])]
            write_message(sender, 'Для того, чтобы получить БЕСПЛАТНЫЙ доступ к электронный библиотеке ЛитРес,'
                                  'вам нужно совершить всего лишь три простых действия:'
                                  '\n\n1) Прийти в библиотеку №146'
                                  '\n2) Стать нашим читателем'
                                  '\n3) Получить логин и пароль от ЛитРеса'
                                  '\n\nЕсли у вас уже есть Единый читательский билет, '
                                  'вы можете написать нам на почту или в личные сообщения группы и получить бесплатный доступ к ЛитРес.')
        if received == 'Лекции':
            attachments = ['photo{}_{}'.format(photos['img5']['owner_id'], photos['img5']['id'])]
            write_message_lecture(sender, 'Пожалуйста, выберите плейлист.')
        if received == 'В меню':
            attachments = ['photo{}_{}'.format(photos['img6']['owner_id'], photos['img6']['id'])]
            write_message(sender, 'И вот мы снова здесь :)')
        if received == 'Квесты' or received == 'Назад':
            attachments = ['photo{}_{}'.format(photos['img5']['owner_id'], photos['img5']['id'])]
            write_message_quest(sender, 'Во что хотите сыграть?')
        if received == 'Выход':
            attachments = ['photo{}_{}'.format(photos['img7']['owner_id'], photos['img7']['id'])]
            write_message_end(sender, 'Если Вам снова понадобится моя помощь, позовите меня по имени - Эва.')

            # Квест по Дракуле

        if received == 'Дракула' or received == 'Пройти повторно':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula1(sender,
                                   'Вы способны остановить ход времени и перемещаться в различные моменты жизни покойного,'
                                   ' чтобы спасти его от гибели. Вы можете повлиять лишь на краткие мгновения,'
                                   ' но вашего аккуратного вмешательства должно хватить.'
                                   'Теперь события прошлого будут разворачиваться по-новому.'
                                   '\nНачнем?'
                                   '\n\nВсего в колоде 13 Карт Истории. Они разложены в хронологическом порядке, '
                                   'однако вы можете открывать их в любой последовательности.'
                                   '\n\nИтак, сначала вам предстоит узнать обстоятельства смерти, которую нужно предотвратить.'
                                   'Для этого выберите Карту Истории №12'
                                   '\n\nP.S. Если вам нужно увеличить картинку, нажмите на фото, затем на вкладку «еще» и выберите пункт «Открыть оригинал».')

        if received == 'КИ12':
            attachments = ['photo{}_{}'.format(photos['drac1']['owner_id'], photos['drac1']['id'])]
            write_message_dracula_exp(sender, 'Прочтите содержимое Карты Истории.'
                                              '\n\nТеперь пришел черед рассказать о ходе игры.'
                                              ' Каждый ход определяйте, в какую точку времени отправиться и как изменить события прошлого.'
                                              '\n\nУ вас появились какие-то гипотезы? Прекрасно! '
                                              'Давайте выберем следующую Карту истории. Для этого нажмите на кнопку «Карта истории».')

        if received == 'Карта истории':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula(sender, 'Перед вами вновь Карты Истории.'
                                          'Теперь вы самостоятельно можете выбрать, в какой отрезок отправиться.'
                                          'Для того, чтобы открыть карту, нажмите на кнопку с идентичным карте номером.'
                                          '\n\nВнимание! Если вы хотите увеличить сложность игры, то откройте любые 10 карт из 13.'
                                          '\n\nКонец игры наступит, когда вы откроете все карты и примите последнее решение. '
                                          'Когда это произойдет, откройте подсчет баллов, чтобы узнать, удалось ли вам изменить прошлое.')

        if received == '1В' or received == '8Б':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula(sender, 'Каков будет ваш следующий выбор?')

        if received == '2В' or received == '3В' or received == '4В' or received == '5А' or received == '6А' or received == '7А' or received == '9А' or received == '10Б' or received == '11В':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula(sender, 'Каков будет ваш следующий выбор?')

        if received == '1А' or received == '2А' or received == '3А' or received == '4Б' or received == '5Б' or received == '5В' or received == '6Б' or received == '7Б' or received == '8В' or received == '9Б' or received == '10В' or received == '11Б':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula(sender, 'Каков будет ваш следующий выбор?')

        if received == '13А' or received == '1Б' or received == '2Б' or received == '3Б' or received == '4А' or received == '6В' or received == '7В' or received == '8А' or received == '9В' or received == '10А' or received == '11А':
            attachments = ['photo{}_{}'.format(photos['drac']['owner_id'], photos['drac']['id'])]
            write_message_dracula(sender, 'Каков будет ваш следующий выбор?')

        if received == 'КИ1':
            attachments = ['photo{}_{}'.format(photos['drac_a']['owner_id'], photos['drac_a']['id'])]
            write_message_dracula_1a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 1А, 1Б или 1В.')

        if received == 'КИ2':
            attachments = ['photo{}_{}'.format(photos['drac_a2']['owner_id'], photos['drac_a2']['id'])]
            write_message_dracula_2a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 2А, 2Б или 2В.')

        if received == 'КИ3':
            attachments = ['photo{}_{}'.format(photos['drac_a3']['owner_id'], photos['drac_a3']['id'])]
            write_message_dracula_3a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 3А, 3Б или 3В.')

        if received == 'КИ4':
            attachments = []
            attachments.append('photo{}_{}'.format(photos['drac_a4']['owner_id'], photos['drac_a4']['id']))
            write_message_dracula_4a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 4А, 4Б или 4В.')

        if received == 'КИ5':
            attachments = ['photo{}_{}'.format(photos['drac_a5']['owner_id'], photos['drac_a5']['id'])]
            write_message_dracula_5a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 5А, 5Б или 5В.')

        if received == 'КИ6':
            attachments = ['photo{}_{}'.format(photos['drac_a6']['owner_id'], photos['drac_a6']['id'])]
            write_message_dracula_6a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 6А, 6Б или 6В.')

        if received == 'КИ7':
            attachments = ['photo{}_{}'.format(photos['drac_a7']['owner_id'], photos['drac_a7']['id'])]
            write_message_dracula_7a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 7А, 7Б или 7В.')

        if received == 'КИ8':
            attachments = ['photo{}_{}'.format(photos['drac_a8']['owner_id'], photos['drac_a8']['id'])]
            write_message_dracula_8a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 8А, 8Б или 8В.')

        if received == 'КИ9':
            attachments = ['photo{}_{}'.format(photos['drac_a9']['owner_id'], photos['drac_a9']['id'])]
            write_message_dracula_9a(sender,
                                     'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 9А, 9Б или 9В.')

        if received == 'КИ10':
            attachments = ['photo{}_{}'.format(photos['drac_a10']['owner_id'], photos['drac_a10']['id'])]
            write_message_dracula_10a(sender,
                                      'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 10А, 10Б или 10В.')

        if received == 'КИ11':
            attachments = ['photo{}_{}'.format(photos['drac_a11']['owner_id'], photos['drac_a11']['id'])]
            write_message_dracula_11a(sender,
                                      'Выберите один из трех вариантов изменения прошлого и отправьте ваше решение в форме ответа: 11А, 11Б или 11В.')

        if received == 'КИ13':
            attachments = ['photo{}_{}'.format(photos['drac_a13']['owner_id'], photos['drac_a13']['id'])]
            write_message_dracula_13a(sender, 'Прочтите карту и напишите в форме ответа «13А».')

        if received == 'Открыть карту решения':
            attachments = ['photo{}_{}'.format(photos['drac_answers']['owner_id'], photos['drac_answers']['id'])]
            write_message_dracula_points(sender,
                                         'Вы открыли все Карты Истории и приняли решения, которые могли изменить прошлое. '
                                         'Изменения, принятые вами в прошлом, вступают в силу одновременно после вашего последнего прыжка во времени. '
                                         '\n\nМеньше 0 очков: О, нет! Невероятно. Вы все испортили и сделали смерть еще более неотвратимой.'
                                         '\n\n0-3 очков: Вы шли верным путем, но не смогли обмануть судьбу.'
                                         '\n\n4-6 очков: Вы были близки к успеху, но судьба неумолима.'
                                         '\n\n7-8 очков: Поздравляем! Вам и правда удалось изменить прошлое.'
                                         '\n\n9 очков или больше: Вы распутали историю и с легкостью предотвратили смерть.'
                                         '\n\nХотите узнать, что случилось на самом деле? Нажмите кнопку «Истина».')

        if received == 'Истина':
            write_message_dracula_points(sender,
                                         'Мы надеемся, что вам понравилось это литературное путешествие в прошлое, и вскоре вы отправитесь в новое, чтобы изменить еще одну судьбу.'
                                         '\n\nМы надеемся, что вам понравилось это литературное путешествие в прошлое, и вскоре вы отправитесь в новое, чтобы изменить еще одну судьбу.'
                                         '\n\nКнига Брэма Стокера «Дракула» и тысячи других книг бесплатно в ЛитРес при записи в библиотеку.'
                                         '\n\nСсылка на роман: https://www.litres.ru/brem-stoker/drakula-128393/')

        # Квест по страдающему средневековью
        # ____________________________________________

        if received == 'Сказки для взрослых' or received == 'Вжух' or received == 'вжух' or received == 'Вжух!' or received == 'вжух!' or received == 'Повторить игру':
            counter_fairy += 1
            attachments = ['photo{}_{}'.format(photos['fairy']['owner_id'], photos['fairy']['id'])]
            write_message_tale_begins(sender,
                                      'Вы – представитель святой инквизиции, страж народа, который расследует самые неординарные и жестокие преступления.'
                                      '\n\nВремена неспокойные, народ сомневается в нынешней власти, которая, по их мнению, не в состоянии защитить простых жителей.'
                                      'Вам необходимо раскрыть пять дел и наказать виновных.'
                                      '\n\nПо прибытии на локацию вас введут в курс дела, а после предложат варианты последующих действий.'
                                      'Всего можно выделить три типа ведения расследования:'
                                      '\n\nОсмотр места происшествия – поиск улик;'
                                      '\nОпрос свидетелей;'
                                      '\nЗапрос записей писаря, чтобы узнать дополнительную информацию.'
                                      '\n\nНарод в любой момент может поднять бунт, поэтому время у вас ограничено.'
                                      'Но не тревожьтесь, у вас в арсенале есть пыльца фей – проявитель магических следов, если в деле замешано колдовство – пыльца покажет это.'
                                      '\n\nИ будьте осторожны при разговоре со свидетелями. Не всех можно подкупить, не всех можно убедить и не всех можно запугать.'
                                      'При неправильном взаимодействии свидетель откажется беседовать с вами.'
                                      '\n\nВ конце каждого дела вам предстоит ответить на несколько вопросов. В том числе, кто жертва, а кто преступник.'
                                      '\n\nУдачи.')
        if received == 'Вести':
            attachments = ['photo{}_{}'.format(photos['main_map']['owner_id'], photos['main_map']['id'])]
            write_message_map(sender, 'Милорд,'
                                      '\n\nВ эти времена благодать Божья покинула эти земли, народ взволнован, наше влияние падает. Мы верим, что в ваших силах оказать нам милость.'
                                      '\n\nНа Ведьмином кладбище было схвачено исчадие Ада, притворявшееся королевой.'
                                      'Ведьма околдовала знатного господина, который попросил нас доказать ее невиновность.'
                                      'Мы не можем лишать этого агнца божьего надежды на спасения души падшей женщины.'
                                      'Просим Вас прибыть туда в ближайшее время.'
                                      '\n\nВ Мрачном замке Бог забрал душу барона. Ироды лишили жизни благодетельного человека. Вдова безутешна. Ради всего святого, найдите виновных.'
                                      '\n\nВ окрестностях Восточной башни грешники лишили зрения Божье дитя.'
                                      'Ослепши, бродил он по лесу, не ведая дороги. Станьте же Дланью Господней для этой несчастной души.'
                                      '\n\nОколо Тихой деревни пропадают люди, коих мы поклялись защищать. В доме на отшибе свершилась какая-то дьявольщина, пролилась кровь.'
                                      'Пропала старая отшельница. Разберитесь, в чем дело.'
                                      '\n\nВ Королевском замке, в глухом лесу, свершилось чудо. Знатная дама нашла двух младенцев в своей обители.'
                                      'Дева хочет отыскать родителей. Расположение замка стратегически важно для нас. Не подведите.'
                                      '\n\nДа благословит Вас Всевышний.'
                                      '\n\nБрат Микаэль.')

        if received == 'К карте' or received == 'Продолжить расследование':
            attachments = ['photo{}_{}'.format(photos['main_map']['owner_id'], photos['main_map']['id'])]
            write_message_map(sender, ' ')

        if received == 'Ведьмино кладбище' or received == 'К месту происшествия':
            attachments = ['photo{}_{}'.format(photos['cemetery1']['owner_id'], photos['cemetery1']['id'])]
            write_message_witch_hour(sender, ' ')

        if received == 'Отчет писаря. Дело Ведьминого кладбища':
            attachments = ['photo{}_{}'.format(photos['report_swan']['owner_id'], photos['report_swan']['id'])]
            write_message_witch_report(sender, ' ')

        if received == 'Внешние признаки Королевы':
            attachments = ['photo{}_{}'.format(photos['queens_look']['owner_id'], photos['queens_look']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Колдовская работа':
            attachments = ['photo{}_{}'.format(photos['work']['owner_id'], photos['work']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Происхождение Королевы':
            attachments = ['photo{}_{}'.format(photos['origin']['owner_id'], photos['origin']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Задать вопрос Королеве':
            attachments = ['photo{}_{}'.format(photos['question_queen']['owner_id'], photos['question_queen']['id'])]
            write_message_witch_questions(sender, ' ')

        if received == 'Вы занимаетесь магическими искусствами?':
            attachments = ['photo{}_{}'.format(photos['question_1']['owner_id'], photos['question_1']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Вы признаете свою вину?':
            attachments = ['photo{}_{}'.format(photos['question_2']['owner_id'], photos['question_2']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Вы были на кладбище ночью?':
            attachments = ['photo{}_{}'.format(photos['question_3']['owner_id'], photos['question_3']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Осмотреть кладбище':
            attachments = ['photo{}_{}'.format(photos['cemetery']['owner_id'], photos['cemetery']['id'])]
            write_message_witch_grave(sender, ' ')

        if received == 'К уликам кладбища':
            attachments = ['photo{}_{}'.format(photos['cemetery1']['owner_id'], photos['cemetery1']['id'])]
            write_message_witch_grave(sender, ' ')

        if received == 'Могилы':
            attachments = ['photo{}_{}'.format(photos['graves']['owner_id'], photos['graves']['id'])]
            write_message_witch_evidence(sender, ' ')

        if received == 'Останки':
            attachments = ['photo{}_{}'.format(photos['bones']['owner_id'], photos['bones']['id'])]
            write_message_witch_evidence(sender, ' ')

        if received == 'Пыльца фей. Страстоцвет':
            attachments = ['photo{}_{}'.format(photos['fairy_magic']['owner_id'], photos['fairy_magic']['id'])]
            write_message_witch_evidence(sender, ' ')

        if received == 'Растительность':
            attachments = ['photo{}_{}'.format(photos['grass']['owner_id'], photos['grass']['id'])]
            write_message_witch_evidence(sender, ' ')

        if received == 'Осмотреть темницу':
            attachments = ['photo{}_{}'.format(photos['prison']['owner_id'], photos['prison']['id'])]
            write_message_witch_prison(sender, ' ')

        if received == 'К уликам темницы':
            attachments = ['photo{}_{}'.format(photos['prison']['owner_id'], photos['prison']['id'])]
            write_message_witch_prison(sender, ' ')

        if received == 'Травы':
            attachments = ['photo{}_{}'.format(photos['nettle']['owner_id'], photos['nettle']['id'])]
            write_message_witch_evidence2(sender, ' ')

        if received == 'Лежанка':
            attachments = ['photo{}_{}'.format(photos['small_bed']['owner_id'], photos['small_bed']['id'])]
            write_message_witch_evidence2(sender, ' ')

        if received == 'Пыльца фей. Белокрыльник':
            attachments = ['photo{}_{}'.format(photos['fairy_magic2']['owner_id'], photos['fairy_magic2']['id'])]
            write_message_witch_evidence2(sender, ' ')

        if received == 'Окно':
            attachments = ['photo{}_{}'.format(photos['window']['owner_id'], photos['window']['id'])]
            write_message_witch_evidence2(sender, ' ')

        if received == 'Поговорить с Королем':
            attachments = ['photo{}_{}'.format(photos['talk_king']['owner_id'], photos['talk_king']['id'])]
            write_message_witch_king(sender, ' ')

        if received == 'Подкупить Короля':
            attachments = ['photo{}_{}'.format(photos['gold_king']['owner_id'], photos['gold_king']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Убедить Короля':
            attachments = ['photo{}_{}'.format(photos['kind_king']['owner_id'], photos['kind_king']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Запугать Короля':
            attachments = ['photo{}_{}'.format(photos['fear_king']['owner_id'], photos['fear_king']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Поговорить с Архиепископом':
            attachments = ['photo{}_{}'.format(photos['talk_priest']['owner_id'], photos['talk_priest']['id'])]
            write_message_witch_priest(sender, ' ')

        if received == 'Подкупить Архиепископа':
            attachments = ['photo{}_{}'.format(photos['gold_priest']['owner_id'], photos['gold_priest']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Убедить Архиепископа':
            attachments = ['photo{}_{}'.format(photos['kind_priest']['owner_id'], photos['kind_priest']['id'])]
            write_message_witch_back(sender, ' ')

        if received == 'Запугать Архиепископа':
            attachments = []
            attachments.append('photo{}_{}'.format(photos['fear_priest']['owner_id'], photos['fear_priest']['id']))
            write_message_witch_back(sender, ' ')

        if received == 'Вопросы Ведьминого кладбища':
            attachments = ['photo{}_{}'.format(photos['guilt']['owner_id'], photos['guilt']['id'])]
            write_message_witch_guilt(sender, ' ')

        if received == 'Да, виновна':
            attachments = ['photo{}_{}'.format(photos['who']['owner_id'], photos['who']['id'])]
            write_message_witch_who(sender, ' ')

        if received == 'Нет, невиновна':
            attachments = ['photo{}_{}'.format(photos['who']['owner_id'], photos['who']['id'])]
            write_message_witch_who(sender, ' ')

        if received == 'Король' or received == 'Фаворит' or received == 'Архиепископ':
            attachments = ['photo{}_{}'.format(photos['swan_story']['owner_id'], photos['swan_story']['id'])]
            write_message_witch_story(sender, ' ')

        if received == 'Брат':
            attachments = ['photo{}_{}'.format(photos['swan_story']['owner_id'], photos['swan_story']['id'])]
            write_message_witch_story(sender, ' ')

        if received == 'Дикие лебеди':
            attachments = ['photo{}_{}'.format(photos['wild_swan']['owner_id'], photos['wild_swan']['id'])]
            write_message_pointser(sender, 'Что же произошло на самом деле? \n\nКоролева Элиза была вовсе не ведьмой. '
                                           'Девушка шила из крапивы рубашки своим братьям, которых превратила в лебедей их мачеха. '
                                           'Только ночью принимали они свой истинный облик. Один из братьев попросил инквизицию расследовать это дело.'
                                           '\n\nПравильные ответы:'
                                           '\n1. Невиновна'
                                           '\n2. Брат'
                                           '\n3. "Дикие лебеди"'
                                           '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Золушка' or received == 'Русалочка' or received == 'Умная Эльза' or received == 'Белоснежка и семь гномов' or received == 'Румпельштильцхен':
            attachments = ['photo{}_{}'.format(photos['wild_swan']['owner_id'], photos['wild_swan']['id'])]
            write_message_pointser(sender, 'Что же произошло на самом деле? \n\nКоролева Элиза была вовсе не ведьмой. '
                                           'Девушка шила из крапивы рубашки своим братьям, которых превратила в лебедей их мачеха. '
                                           'Только ночью принимали они свой истинный облик. Один из братьев попросил инквизицию расследовать это дело.'
                                           '\n\nПравильные ответы:'
                                           '\n1. Невиновна'
                                           '\n2. Брат'
                                           '\n3. "Дикие лебеди"'
                                           '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Королевский дворец' or received == 'В поместье':
            attachments = ['photo{}_{}'.format(photos['king_castle']['owner_id'], photos['king_castle']['id'])]
            write_message_beauty(sender, ' ')

        if received == 'Отчет писаря. Дело Королевского дворца':
            attachments = ['photo{}_{}'.format(photos['castle_deal']['owner_id'], photos['castle_deal']['id'])]
            write_message_beauty2(sender, ' ')

        if received == 'Внешние признаки хозяйки':
            attachments = ['photo{}_{}'.format(photos['lady_look']['owner_id'], photos['lady_look']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Происхождение хозяйки':
            attachments = ['photo{}_{}'.format(photos['lady_original']['owner_id'], photos['lady_original']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'О детях':
            attachments = ['photo{}_{}'.format(photos['child']['owner_id'], photos['child']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Поговорить с хозяйкой':
            attachments = ['photo{}_{}'.format(photos['talk_lady']['owner_id'], photos['talk_lady']['id'])]
            write_message_beauty4(sender, ' ')

        if received == 'Подкупить хозяйку':
            attachments = ['photo{}_{}'.format(photos['gold_lady']['owner_id'], photos['gold_lady']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Убедить хозяйку':
            attachments = ['photo{}_{}'.format(photos['kind_lady']['owner_id'], photos['kind_lady']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Запугать хозяйку':
            attachments = ['photo{}_{}'.format(photos['fear_lady']['owner_id'], photos['fear_lady']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Осмотреть главный зал':
            attachments = ['photo{}_{}'.format(photos['throne_room']['owner_id'], photos['throne_room']['id'])]
            write_message_beauty5(sender, ' ')

        if received == 'К уликам тронного зала':
            attachments = ['photo{}_{}'.format(photos['throne_room']['owner_id'], photos['throne_room']['id'])]
            write_message_beauty5(sender, ' ')

        if received == 'Трон':
            attachments = ['photo{}_{}'.format(photos['throne']['owner_id'], photos['throne']['id'])]
            write_message_beauty_evidence(sender, ' ')

        if received == 'Осмотреть поместье':
            attachments = ['photo{}_{}'.format(photos['house_look']['owner_id'], photos['house_look']['id'])]
            write_message_beauty_evidence(sender, ' ')

        if received == 'Пыльца фей. Роза':
            attachments = ['photo{}_{}'.format(photos['fairy_magic3']['owner_id'], photos['fairy_magic3']['id'])]
            write_message_beauty_evidence(sender, ' ')

        if received == 'Оценка поместья':
            attachments = ['photo{}_{}'.format(photos['house_gold']['owner_id'], photos['house_gold']['id'])]
            write_message_beauty_evidence(sender, ' ')

        if received == 'Кровать':
            attachments = ['photo{}_{}'.format(photos['sleepy_bed']['owner_id'], photos['sleepy_bed']['id'])]
            write_message_beauty_evidence2(sender, ' ')

        if received == 'Пол':
            attachments = ['photo{}_{}'.format(photos['sleepy_floar']['owner_id'], photos['sleepy_floar']['id'])]
            write_message_beauty_evidence2(sender, ' ')

        if received == 'Пыльца фей. Белладонна':
            attachments = ['photo{}_{}'.format(photos['fairy_magic4']['owner_id'], photos['fairy_magic4']['id'])]
            write_message_beauty_evidence2(sender, ' ')

        if received == 'Простыни':
            attachments = ['photo{}_{}'.format(photos['sleepy_sheets']['owner_id'], photos['sleepy_sheets']['id'])]
            write_message_beauty_evidence2(sender, ' ')

        if received == 'Осмотреть спальню':
            attachments = ['photo{}_{}'.format(photos['sleep_room']['owner_id'], photos['sleep_room']['id'])]
            write_message_beauty_evidence2(sender, ' ')

        if received == 'К уликам спальни':
            attachments = ['photo{}_{}'.format(photos['sleep_room']['owner_id'], photos['sleep_room']['id'])]
            write_message_beauty6(sender, ' ')

        if received == 'Ответные письма' or received == 'Вернуться к письмам':
            attachments = ['photo{}_{}'.format(photos['letters']['owner_id'], photos['letters']['id'])]
            write_message_beauty7(sender, ' ')

        if received == 'Письмо от Графини':
            attachments = ['photo{}_{}'.format(photos['countess']['owner_id'], photos['countess']['id'])]
            write_message_beauty8(sender, ' ')

        if received == 'Письмо от Короля Первого Царства':
            attachments = ['photo{}_{}'.format(photos['sleepy_king']['owner_id'], photos['sleepy_king']['id'])]
            write_message_beauty8(sender, ' ')

        if received == 'Письмо от Королевы Первого Царства':
            attachments = ['photo{}_{}'.format(photos['sleepy_queen']['owner_id'], photos['sleepy_queen']['id'])]
            write_message_beauty8(sender, ' ')

        if received == 'Письмо от правителей Старого королевства':
            attachments = ['photo{}_{}'.format(photos['old_kindom_rulers']['owner_id'], photos['old_kindom_rulers']['id'])]
            write_message_beauty8(sender, ' ')

        if received == 'Поговорить с гонцом':
            attachments = ['photo{}_{}'.format(photos['talk_runner']['owner_id'], photos['talk_runner']['id'])]
            write_message_beauty9(sender, ' ')

        if received == 'Подкупить гонца':
            attachments = ['photo{}_{}'.format(photos['gold_runner']['owner_id'], photos['gold_runner']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Убедить гонца':
            attachments = ['photo{}_{}'.format(photos['kind_runner']['owner_id'], photos['kind_runner']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Запугать гонца':
            attachments = ['photo{}_{}'.format(photos['fear_runner']['owner_id'], photos['fear_runner']['id'])]
            write_message_beauty3(sender, ' ')

        if received == 'Вопросы Королевского дворца':
            attachments = ['photo{}_{}'.format(photos['father_child']['owner_id'], photos['father_child']['id'])]
            write_message_beauty10(sender, ' ')

        if received == 'Гонец' or received == 'Король Старого Королевства' or received == 'Бывший король Старого Королевства':
            attachments = ['photo{}_{}'.format(photos['honor']['owner_id'], photos['honor']['id'])]
            write_message_beauty11(sender, ' ')

        if received == 'Король Первого Царства':
            attachments = ['photo{}_{}'.format(photos['honor']['owner_id'], photos['honor']['id'])]
            write_message_beauty11(sender, ' ')

        if received == 'гонец' or received == 'король Старого Королевства' or received == 'бывший король Старого Королевства' or received == 'хозяйка' or received == 'королева Старого Королевства' or received == 'королева Первого Царства' or received == 'графиня':
            attachments = ['photo{}_{}'.format(photos['sleepy_what']['owner_id'], photos['sleepy_what']['id'])]
            write_message_beauty12(sender, ' ')

        if received == 'король Первого Царства':
            attachments = ['photo{}_{}'.format(photos['sleepy_what']['owner_id'], photos['sleepy_what']['id'])]
            write_message_beauty12(sender, ' ')

        if received == 'Спящая красавица':
            attachments = ['photo{}_{}'.format(photos['sleep_beauty']['owner_id'], photos['sleep_beauty']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nТалию, пострадавшую от проклятия веретена, нашел в лесу Король Первого Царства. '
                                   'Воспользовавшись беззащитным положением девушки, Его Высочество отправился восвояси. '
                                   '\n\nЧерез 9 месяцев Талия родила близнецов, а еще через какое-то время один из детей вытащил отравленную иглу из пальца матери.\nТак принцесса пробудилась от сна.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Король Первого Царства'
                                   '\n2. Король Первого Царства'
                                   '\n3. "Спящая красавица"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Снежная королева' or received == 'Братец и сестрица' or received == 'Белоснежка и Алоцветик' or received == 'Красавица и чудовище' or received == 'Госпожа Метелица':
            attachments = ['photo{}_{}'.format(photos['sleep_beauty']['owner_id'], photos['sleep_beauty']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nТалию, пострадавшую от проклятия веретена, нашел в лесу Король Первого Царства. '
                                   'Воспользовавшись беззащитным положением девушки, Его Высочество отправился восвояси. '
                                   '\n\nЧерез 9 месяцев Талия родила близнецов, а еще через какое-то время один из детей вытащил отравленную иглу из пальца матери.\nТак принцесса пробудилась от сна.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Король Первого Царства'
                                   '\n2. Король Первого Царства'
                                   '\n3. "Спящая красавица"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Тихая деревня' or received == 'В деревню':
            attachments = ['photo{}_{}'.format(photos['red_hat']['owner_id'], photos['red_hat']['id'])]
            write_message_hat(sender, ' ')

        if received == 'Отчет писаря. Дело Тихой деревни':
            attachments = ['photo{}_{}'.format(photos['report_vil']['owner_id'], photos['report_vil']['id'])]
            write_message_hat2(sender, ' ')

        if received == 'Расположение дома':
            attachments = ['photo{}_{}'.format(photos['house_red']['owner_id'], photos['house_red']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Внешние признаки пропавшей':
            attachments = ['photo{}_{}'.format(photos['woman_red']['owner_id'], photos['woman_red']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Случаи пропажи людей':
            attachments = ['photo{}_{}'.format(photos['missing']['owner_id'], photos['missing']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Поговорить с дровосеком':
            attachments = ['photo{}_{}'.format(photos['talk_wood']['owner_id'], photos['talk_wood']['id'])]
            write_message_hat4(sender, ' ')

        if received == 'Подкупить дровосека':
            attachments = ['photo{}_{}'.format(photos['gold_wood']['owner_id'], photos['gold_wood']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Убедить дровосека':
            attachments = ['photo{}_{}'.format(photos['kind_wood']['owner_id'], photos['kind_wood']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Запугать дровосека':
            attachments = ['photo{}_{}'.format(photos['fear_wood']['owner_id'], photos['fear_wood']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Осмотреть дом отшельницы':
            attachments = ['photo{}_{}'.format(photos['redhouse_look']['owner_id'], photos['redhouse_look']['id'])]
            write_message_hat5(sender, ' ')

        if received == 'К уликам дома':
            attachments = ['photo{}_{}'.format(photos['redhouse_look']['owner_id'], photos['redhouse_look']['id'])]
            write_message_hat5(sender, ' ')

        if received == 'Камин':
            attachments = ['photo{}_{}'.format(photos['fire']['owner_id'], photos['fire']['id'])]
            write_message_hat6(sender, ' ')

        if received == 'Кровать отшельницы':
            attachments = ['photo{}_{}'.format(photos['red_bed']['owner_id'], photos['red_bed']['id'])]
            write_message_hat6(sender, ' ')

        if received == 'Пол дома':
            attachments = ['photo{}_{}'.format(photos['red_floar']['owner_id'], photos['red_floar']['id'])]
            write_message_hat6(sender, ' ')

        if received == 'Стол':
            attachments = ['photo{}_{}'.format(photos['red_table']['owner_id'], photos['red_table']['id'])]
            write_message_hat6(sender, ' ')

        if received == 'Пыльца фей. Аконит':
            attachments = ['photo{}_{}'.format(photos['fairy_magic5']['owner_id'], photos['fairy_magic5']['id'])]
            write_message_hat6(sender, ' ')

        if received == 'Осмотреть стол':
            attachments = ['photo{}_{}'.format(photos['table_look']['owner_id'], photos['table_look']['id'])]
            write_message_hat7(sender, ' ')

        if received == 'К уликам на столе':
            attachments = ['photo{}_{}'.format(photos['table_look']['owner_id'], photos['table_look']['id'])]
            write_message_hat7(sender, ' ')

        if received == 'Пирожки':
            attachments = ['photo{}_{}'.format(photos['pie']['owner_id'], photos['pie']['id'])]
            write_message_hat8(sender, ' ')

        if received == 'Графин':
            attachments = ['photo{}_{}'.format(photos['blood']['owner_id'], photos['blood']['id'])]
            write_message_hat8(sender, ' ')

        if received == 'Пыльца фей. Дурман':
            attachments = ['photo{}_{}'.format(photos['fairy_magic6']['owner_id'], photos['fairy_magic6']['id'])]
            write_message_hat8(sender, ' ')

        if received == 'Скатерть':
            attachments = ['photo{}_{}'.format(photos['tablecloth']['owner_id'], photos['tablecloth']['id'])]
            write_message_hat8(sender, ' ')

        if received == 'Поговорить с лесничим':
            attachments = ['photo{}_{}'.format(photos['forester_talk']['owner_id'], photos['forester_talk']['id'])]
            write_message_hat9(sender, ' ')

        if received == 'Подкупить лесничего':
            attachments = ['photo{}_{}'.format(photos['gold_forester']['owner_id'], photos['gold_forester']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Убедить лесничего':
            attachments = ['photo{}_{}'.format(photos['kind_forester']['owner_id'], photos['kind_forester']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Запугать лесничего':
            attachments = ['photo{}_{}'.format(photos['fear_forester']['owner_id'], photos['fear_forester']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Поговорить с сыном дровосека':
            attachments = ['photo{}_{}'.format(photos['son_talk']['owner_id'], photos['son_talk']['id'])]
            write_message_hat10(sender, ' ')

        if received == 'Подкупить сына дровосека':
            attachments = ['photo{}_{}'.format(photos['gold_son']['owner_id'], photos['gold_son']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Убедить сына дровосека':
            attachments = ['photo{}_{}'.format(photos['kind_son']['owner_id'], photos['kind_son']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Запугать сына дровосека':
            attachments = ['photo{}_{}'.format(photos['fear_son']['owner_id'], photos['fear_son']['id'])]
            write_message_hat3(sender, ' ')

        if received == 'Вопросы Тихой деревни':
            attachments = ['photo{}_{}'.format(photos['red_woman_where']['owner_id'], photos['red_woman_where']['id'])]
            write_message_hat11(sender, ' ')

        if received == 'Сбежала' or received == 'Была похищена' or received == 'Отправилась в погоню':
            attachments = ['photo{}_{}'.format(photos['red_missing_people']['owner_id'], photos['red_missing_people']['id'])]
            write_message_hat12(sender, ' ')

        if received == 'Была убита':
            attachments = ['photo{}_{}'.format(photos['red_missing_people']['owner_id'], photos['red_missing_people']['id'])]
            write_message_hat12(sender, ' ')

        if received == 'Дровосек' or received == 'Сын дровосека' or received == 'Отшельница':
            attachments = ['photo{}_{}'.format(photos['red_what']['owner_id'], photos['red_what']['id'])]
            write_message_hat13(sender, ' ')

        if received == 'Лесничий':
            attachments = ['photo{}_{}'.format(photos['red_what']['owner_id'], photos['red_what']['id'])]
            write_message_hat13(sender, ' ')

        if received == 'Красная Шапочка':
            attachments = ['photo{}_{}'.format(photos['red_red']['owner_id'], photos['red_red']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nЛес уже давно стал охотничьими угодьями оборотня. Люди и раньше пропадали, но впервые волк забрался в чужое жилище.'
                                   '\n\nИзбавившись от старой отшельницы, оборотень приготовил из нее явства и подал Красной Шапочке в качестве угощения. '
                                   '\nВскоре девочка сама стала закуской.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Была убита'
                                   '\n2. Лесничий'
                                   '\n3. "Красная Шапочка"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Принцесса на горошине' or received == 'Три медведя' or received == 'Дюймовочка' or received == 'Домик в лесу' or received == 'Гензель и Гретель':
            attachments = ['photo{}_{}'.format(photos['red_red']['owner_id'], photos['red_red']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nЛес уже давно стал охотничьими угодьями оборотня. Люди и раньше пропадали, но впервые волк забрался в чужое жилище.'
                                   '\n\nИзбавившись от старой отшельницы, оборотень приготовил из нее явства и подал Красной Шапочке в качестве угощения. '
                                   '\nВскоре девочка сама стала закуской.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Была убита'
                                   '\n2. Лесничий'
                                   '\n3. "Красная Шапочка"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Восточная башня' or received == 'К башне':
            attachments = ['photo{}_{}'.format(photos['eastern_tower']['owner_id'], photos['eastern_tower']['id'])]
            write_message_tower(sender, ' ')

        if received == 'Отчет писаря. Дело Восточной башни':
            attachments = ['photo{}_{}'.format(photos['tower_report']['owner_id'], photos['tower_report']['id'])]
            write_message_tower2(sender, ' ')

        if received == 'Внешние признаки пострадавшего':
            attachments = ['photo{}_{}'.format(photos['prince_look']['owner_id'], photos['prince_look']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Происхождение пострадавшего':
            attachments = ['photo{}_{}'.format(photos['prince_origin']['owner_id'], photos['prince_origin']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Куда направлялся пострадавший':
            attachments = ['photo{}_{}'.format(photos['where_are_you_going']['owner_id'], photos['where_are_you_going']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Поговорить с пострадавшим':
            attachments = ['photo{}_{}'.format(photos['talk_prince']['owner_id'], photos['talk_prince']['id'])]
            write_message_tower4(sender, ' ')

        if received == 'Подкупить пострадавшего':
            attachments = ['photo{}_{}'.format(photos['gold_prince']['owner_id'], photos['gold_prince']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Убедить пострадавшего':
            attachments = ['photo{}_{}'.format(photos['kind_prince']['owner_id'], photos['kind_prince']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Запугать пострадавшего':
            attachments = ['photo{}_{}'.format(photos['fear_prince']['owner_id'], photos['fear_prince']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Осмотреть лесную поляну':
            attachments = ['photo{}_{}'.format(photos['look_glade']['owner_id'], photos['look_glade']['id'])]
            write_message_tower5(sender, ' ')

        if received == 'К уликам на лесной поляне':
            attachments = ['photo{}_{}'.format(photos['look_glade']['owner_id'], photos['look_glade']['id'])]
            write_message_tower5(sender, ' ')

        if received == 'Башня':
            attachments = ['photo{}_{}'.format(photos['glade_tower']['owner_id'], photos['glade_tower']['id'])]
            write_message_tower6(sender, ' ')

        if received == 'Веревка':
            attachments = ['photo{}_{}'.format(photos['glade_rope']['owner_id'], photos['glade_rope']['id'])]
            write_message_tower6(sender, ' ')

        if received == 'Кусты ежевики':
            attachments = ['photo{}_{}'.format(photos['glade_berries']['owner_id'], photos['glade_berries']['id'])]
            write_message_tower6(sender, ' ')

        if received == 'Пыльца фей. Акация':
            attachments = ['photo{}_{}'.format(photos['fairy_magic7']['owner_id'], photos['fairy_magic7']['id'])]
            write_message_tower6(sender, ' ')

        if received == 'Осмотреть башню':
            attachments = ['photo{}_{}'.format(photos['look_tower']['owner_id'], photos['look_tower']['id'])]
            write_message_tower7(sender, ' ')

        if received == 'К уликам в башне':
            attachments = ['photo{}_{}'.format(photos['look_tower']['owner_id'], photos['look_tower']['id'])]
            write_message_tower7(sender, ' ')

        if received == 'Странная веревка':
            attachments = ['photo{}_{}'.format(photos['tower_rope']['owner_id'], photos['tower_rope']['id'])]
            write_message_tower8(sender, ' ')

        if received == 'Ножницы':
            attachments = ['photo{}_{}'.format(photos['tower_sc']['owner_id'], photos['tower_sc']['id'])]
            write_message_tower8(sender, ' ')

        if received == 'Шелковые нити':
            attachments = ['photo{}_{}'.format(photos['tower_silk']['owner_id'], photos['tower_silk']['id'])]
            write_message_tower8(sender, ' ')

        if received == 'Пыльца фей. Колокольчик':
            attachments = ['photo{}_{}'.format(photos['fairy_magic8']['owner_id'], photos['fairy_magic8']['id'])]
            write_message_tower8(sender, ' ')

        if received == 'Осмотреть окрестности':
            attachments = ['photo{}_{}'.format(photos['look_near']['owner_id'], photos['look_near']['id'])]
            write_message_tower9(sender, ' ')

        if received == 'Цветущий сад':
            attachments = ['photo{}_{}'.format(photos['near_garden']['owner_id'], photos['near_garden']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Вглубь леса':
            attachments = ['photo{}_{}'.format(photos['near_forest']['owner_id'], photos['near_forest']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Домик на краю леса':
            attachments = ['photo{}_{}'.format(photos['near_house']['owner_id'], photos['near_house']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Поговорить со старушкой':
            attachments = ['photo{}_{}'.format(photos['talk_granny']['owner_id'], photos['talk_granny']['id'])]
            write_message_tower10(sender, ' ')

        if received == 'Подкупить старушку':
            attachments = ['photo{}_{}'.format(photos['gold_granny']['owner_id'], photos['gold_granny']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Убедить старушку':
            attachments = ['photo{}_{}'.format(photos['kind_granny']['owner_id'], photos['kind_granny']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Запугать старушку':
            attachments = ['photo{}_{}'.format(photos['fear_granny']['owner_id'], photos['fear_granny']['id'])]
            write_message_tower3(sender, ' ')

        if received == 'Вопросы Восточной башни':
            attachments = ['photo{}_{}'.format(photos['blind']['owner_id'], photos['blind']['id'])]
            write_message_tower11(sender, ' ')

        if received == 'Человек, которого он ищет' or received == 'Хозяева дома' or received == 'Несчастный случай':
            attachments = ['photo{}_{}'.format(photos['looking_for']['owner_id'], photos['looking_for']['id'])]
            write_message_tower12(sender, ' ')

        if received == 'Старушка':
            attachments = ['photo{}_{}'.format(photos['looking_for']['owner_id'], photos['looking_for']['id'])]
            write_message_tower12(sender, ' ')

        if received == 'Старушку' or received == 'Хозяев дома':
            attachments = ['photo{}_{}'.format(photos['raps_what']['owner_id'], photos['raps_what']['id'])]
            write_message_tower13(sender, ' ')

        if received == 'Девушку':
            attachments = ['photo{}_{}'.format(photos['raps_what']['owner_id'], photos['raps_what']['id'])]
            write_message_tower13(sender, ' ')

        if received == 'Рапунцель':
            attachments = ['photo{}_{}'.format(photos['rapuns']['owner_id'], photos['rapuns']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nРапунцель отдали старой ведьме в качестве платы за колдовскую траву. Девушка росла в неприступной башне, единсвтенный вход которой - коса Рапунцель.'
                                   '\n\nОднажды принц соседнего королевства наткнулся на странную постройку в лесу и познакомился с девушкой. Замышляя совместный побег, молодые люди стали встречаться чаще. '
                                   '\n\nК сожалению, это заметила ведьма, вырастившая Рапунцель. Она отрезала девушке волосы, переместила ее на пустырь, а принца сбросила с башни. Бедняга выколол глаза о куст еживики.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Старушка'
                                   '\n2. Девушку'
                                   '\n3. "Рапунцель"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Дева Малейн' or received == 'Свинопас' or received == 'Королевские дети' or received == 'Три апельсина' or received == 'Принц и нищий':
            attachments = ['photo{}_{}'.format(photos['rapuns']['owner_id'], photos['rapuns']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nРапунцель отдали старой ведьме в качестве платы за колдовскую траву. Девушка росла в неприступной башне, единсвтенный вход которой - коса Рапунцель.'
                                   '\n\nОднажды принц соседнего королевства наткнулся на странную постройку в лесу и познакомился с девушкой. Замышляя совместный побег, молодые люди стали встречаться чаще. '
                                   '\n\nК сожалению, это заметила ведьма, вырастившая Рапунцель. Она отрезала девушке волосы, переместила ее на пустырь, а принца сбросила с башни. Бедняга выколол глаза о куст еживики.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Старушка'
                                   '\n2. Девушку'
                                   '\n3. "Рапунцель"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Мрачный замок' or received == 'К замку':
            attachments = ['photo{}_{}'.format(photos['husband']['owner_id'], photos['husband']['id'])]
            write_message_beard(sender, ' ')

        if received == 'Отчет писаря. Дело Мрачного замка':
            attachments = ['photo{}_{}'.format(photos['dark_report']['owner_id'], photos['dark_report']['id'])]
            write_message_beard2(sender, ' ')

        if received == 'Родословная барона':
            attachments = ['photo{}_{}'.format(photos['dark_origin']['owner_id'], photos['dark_origin']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Отношения в семье':
            attachments = ['photo{}_{}'.format(photos['dark_family']['owner_id'], photos['dark_family']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Внешние признаки барона':
            attachments = ['photo{}_{}'.format(photos['dark_look']['owner_id'], photos['dark_look']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Поговорить с баронессой':
            attachments = ['photo{}_{}'.format(photos['talk_duke']['owner_id'], photos['talk_duke']['id'])]
            write_message_beard4(sender, ' ')

        if received == 'Подкупить баронессу':
            attachments = ['photo{}_{}'.format(photos['gold_duke']['owner_id'], photos['gold_duke']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Убедить баронессу':
            attachments = ['photo{}_{}'.format(photos['kind_duke']['owner_id'], photos['kind_duke']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Запугать баронессу':
            attachments = ['photo{}_{}'.format(photos['fear_duke']['owner_id'], photos['fear_duke']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Осмотреть тело Барона':
            attachments = ['photo{}_{}'.format(photos['body_look']['owner_id'], photos['body_look']['id'])]
            write_message_beard5(sender, ' ')

        if received == 'К скрытым уликам':
            attachments = ['photo{}_{}'.format(photos['body_look']['owner_id'], photos['body_look']['id'])]
            write_message_beard5(sender, ' ')

        if received == 'Пыльца фей. Горечавка':
            attachments = ['photo{}_{}'.format(photos['fairy_magic9']['owner_id'], photos['fairy_magic9']['id'])]
            write_message_beard6(sender, ' ')

        if received == 'Осмотреть внутренние карманы':
            attachments = ['photo{}_{}'.format(photos['pocket']['owner_id'], photos['pocket']['id'])]
            write_message_beard6(sender, ' ')

        if received == 'Дать команду собаке взять след':
            attachments = ['photo{}_{}'.format(photos['doggy']['owner_id'], photos['doggy']['id'])]
            write_message_beard6(sender, ' ')

        if received == 'Осмотреть нож':
            attachments = ['photo{}_{}'.format(photos['knife']['owner_id'], photos['knife']['id'])]
            write_message_beard6(sender, ' ')

        if received == 'Осмотреть гостиную':
            attachments = ['photo{}_{}'.format(photos['guest_look']['owner_id'], photos['guest_look']['id'])]
            write_message_beard7(sender, ' ')

        if received == 'К уликам гостиной':
            attachments = ['photo{}_{}'.format(photos['guest_look']['owner_id'], photos['guest_look']['id'])]
            write_message_beard7(sender, ' ')

        if received == 'Портрет на стене':
            attachments = ['photo{}_{}'.format(photos['portrait']['owner_id'], photos['portrait']['id'])]
            write_message_beard8(sender, ' ')

        if received == 'Ключница':
            attachments = ['photo{}_{}'.format(photos['guest_key']['owner_id'], photos['guest_key']['id'])]
            write_message_beard8(sender, ' ')

        if received == 'Амбарная книга':
            attachments = ['photo{}_{}'.format(photos['book']['owner_id'], photos['book']['id'])]
            write_message_beard8(sender, ' ')

        if received == 'Пыльца фей. Мак':
            attachments = ['photo{}_{}'.format(photos['fairy_magic10']['owner_id'], photos['fairy_magic10']['id'])]
            write_message_beard8(sender, ' ')

        if received == 'Поговорить с братьями':
            attachments = ['photo{}_{}'.format(photos['talk_brothers']['owner_id'], photos['talk_brothers']['id'])]
            write_message_beard9(sender, ' ')

        if received == 'Подкупить братьев':
            attachments = ['photo{}_{}'.format(photos['gold_brothers']['owner_id'], photos['gold_brothers']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Убедить братьев':
            attachments = ['photo{}_{}'.format(photos['kind_brothers']['owner_id'], photos['kind_brothers']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Запугать братьев':
            attachments = ['photo{}_{}'.format(photos['fear_brothers']['owner_id'], photos['fear_brothers']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Поговорить с сестрой':
            attachments = ['photo{}_{}'.format(photos['talk_sister']['owner_id'], photos['talk_sister']['id'])]
            write_message_beard10(sender, ' ')

        if received == 'Подкупить сестру':
            attachments = ['photo{}_{}'.format(photos['gold_sister']['owner_id'], photos['gold_sister']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Убедить сестру':
            attachments = ['photo{}_{}'.format(photos['kind_sister']['owner_id'], photos['kind_sister']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Запугать сестру':
            attachments = ['photo{}_{}'.format(photos['fear_sister']['owner_id'], photos['fear_sister']['id'])]
            write_message_beard3(sender, ' ')

        if received == 'Ключ':
            attachments = ['photo{}_{}'.format(photos['magic_key']['owner_id'], photos['magic_key']['id'])]
            write_message_beard8(sender, ' ')

        if received == 'Вопросы Мрачного замка':
            attachments = ['photo{}_{}'.format(photos['mur']['owner_id'], photos['mur']['id'])]
            write_message_beard11(sender, ' ')

        if received == 'Баронесса' or received == 'Братья' or received == 'Сестра':
            attachments = ['photo{}_{}'.format(photos['nomur']['owner_id'], photos['nomur']['id'])]
            write_message_beard12(sender, ' ')

        if received == 'Барон':
            attachments = ['photo{}_{}'.format(photos['nomur']['owner_id'], photos['nomur']['id'])]
            write_message_beard12(sender, ' ')

        if received == 'барон' or received == 'братья' or received == 'сестра':
            attachments = ['photo{}_{}'.format(photos['murwhat']['owner_id'], photos['murwhat']['id'])]
            write_message_beard13(sender, ' ')

        if received == 'баронесса':
            attachments = ['photo{}_{}'.format(photos['murwhat']['owner_id'], photos['murwhat']['id'])]
            write_message_beard13(sender, ' ')

        if received == 'Синяя Борода':
            attachments = ['photo{}_{}'.format(photos['blue_beard']['owner_id'], photos['blue_beard']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nБарон не отказывал своей молодой жене ни в чем: покупал дорогие наряды, разрешал устраивать приемы. Единственный запрет - не открывать маленькую потайную дверь в подвале.'
                                   '\n\nБаронессу стало одолевать любопытство, и когла она все же открыла запретную комнату, обнаруженное повергло ее в ужас. На стенах висели тела бывших жен ее мужа.'
                                   '\n\nСкрыть свой поход женщина не смогла, тогда барон решил расправиться и с ней. Баронессу спасли ее братья, вовремя зарубившие негодяя.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Барон'
                                   '\n2. баронесса'
                                   '\n3. "Синяя Борода"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Король Дроздобород' or received == 'Огниво' or received == 'Гамельнский крысолов' or received == 'Джек и бобовый стебель' or received == 'Новое платье короля':
            attachments = ['photo{}_{}'.format(photos['blue_beard']['owner_id'], photos['blue_beard']['id'])]
            write_message_pointser(sender,
                                   'Что же произошло на самом деле? \n\nБарон не отказывал своей молодой жене ни в чем: покупал дорогие наряды, разрешал устраивать приемы. Единственный запрет - не открывать маленькую потайную дверь в подвале.'
                                   '\n\nБаронессу стало одолевать любопытство, и когла она все же открыла запретную комнату, обнаруженное повергло ее в ужас. На стенах висели тела бывших жен ее мужа.'
                                   '\n\nСкрыть свой поход женщина не смогла, тогда барон решил расправиться и с ней. Баронессу спасли ее братья, вовремя зарубившие негодяя.'
                                   '\n\nПравильные ответы:'
                                   '\n1. Барон'
                                   '\n2. баронесса'
                                   '\n3. "Синяя Борода"'
                                   '\n\nЗа каждый правильный ответ вы получаете 1 балл.')

        if received == 'Завершить свои расследования':
            attachments = ['photo{}_{}'.format(photos['main_map']['owner_id'], photos['main_map']['id'])]
            write_message_beard14(sender, 'Какое количество баллов вы набрали?')

        if received == 'От 0 до 5 баллов':
            attachments = ['photo{}_{}'.format(photos['hight']['owner_id'], photos['hight']['id'])]
            write_message_pointstale(sender, ' ')

        if received == 'От 6 до 10 баллов':
            attachments = ['photo{}_{}'.format(photos['middle']['owner_id'], photos['middle']['id'])]
            write_message_pointstale(sender, ' ')

        if received == 'От 11 до 15 баллов':
            attachments = ['photo{}_{}'.format(photos['low']['owner_id'], photos['low']['id'])]
            write_message_pointstale(sender, ' ')

        if received == 'Перечень сказок':
            attachments = ['photo{}_{}'.format(photos['main_map']['owner_id'], photos['main_map']['id'])]
            write_message_pointstale(sender, 'В основу игровых событий легли:'
                                             '\n"Дикие лебеди" Ганса Христиана Андерсена'
                                             '\n"Спящая красавица" Шарля Перро'
                                             '\n"Красная Шапочка" Шарля Перро'
                                             '\n"Рапунцель" братьев Гримм'
                                             '\n\n"Синяя Борода" Шарля Перро')

        if received == 'Счетчик' or received == 'счетчик':
            write_message_end(sender, counter_fairy)
