## **Парсеры с использованием библиотеки BeautifulSoup**

### <ins>Парсинг разбиения на страницы:</ins>

***pagination_4-6-3.py***

    На сайте http://parsinger.ru/html/index3_page_1.html необходимо извлечь названия товара с каждой страницы (всего 4 страницы).
    Данные с каждой страницы сохранить в списке.
    По итогу работы должны получится 4 списка которые хранятся в списке (список списков).
    Метод strip()использовать не нужно.


***pagination_4-6-4.py***

    На сайте http://parsinger.ru/html/index3_page_4.html пройти по всем страницам в категории мыши (всего  4 страницы). 
    На каждой странице с каждой карточки с товаром (всего 32 товаров) извлечь   `<p class="article"> Артикул: 80244813 </p>`.
    Суммировать все собранные значения.

***pagination_4-6-5.py***

    На сайте http://parsinger.ru/html/index1_page_1.html  пройти по всем категориям, страницам и карточкам с товарами (всего 160шт).
    Собираем с каждой карточки стоимость товара умножая на количество товара в наличии.
    Суммируем получившийся результат и получаем общую стоимость всех товаров.

### <ins>Парсинг таблиц:</ins>

***parsing_tables_4-8-2.py***

    На  сайте https://parsinger.ru/table/1/index.html расположена таблица.
    Необходимо собрать все уникальные числа из таблицы (кроме цифр в заголовке) и суммировать их.

***parsing_tables_4-8-3.py***

    На  сайте https://parsinger.ru/table/2/index.html расположена таблица.
    Необходимо собрать числа с 1го столбца и суммировать их.

***parsing_tables_4-8-4.py***

    На  сайте https://parsinger.ru/table/3/index.html расположена таблица.
    Необходимо собрать числа которые выделены жирным шрифтом и суммировать их.

***parsing_tables_4-8-5.py***

    На  сайте https://parsinger.ru/table/4/index.html расположена таблица.
    Необходимо собрать числа в зелёных ячейках и суммировать их.

***parsing_tables_4-8-6.py***

    На  сайте https://parsinger.ru/table/5/index.html расположена таблица.
    Необходимо умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать.

***parsing_tables_4-8-7.py***

    На  сайте https://parsinger.ru/table/5/index.html расположена таблица.
    Необходимо сформировать словарь, где ключ будет автоматически формироваться из заголовка столбцов, а значения - сумма всех чисел в столбце.
    Округлить каждое число до 3х символов после запятой.

### <ins>Парсинг с сохранением в csv:</ins>

***parsing2csv_4-9-4.py***

    Необходимо собрать данные в категории HDD (https://parsinger.ru/html/index1_page_1.html) со всех 4х страниц и сохранить всё в csv-файл. 

***parsing2csv_4-9-5.py***

    Необходимо собрать данные со всех страниц и категорий на сайте http://parsinger.ru/html/index1_page_1.html и и сохранить всё в csv-файл. Заголовки  указывать не нужно.

***parsing2csv_4-9-6.py***

    Необходимо собрать данные в категории watch (http://parsinger.ru/html/index1_page_1.html) c каждой карточки (всего их 32) и сохранить всё в csv-файл.

***parsing2csv_4-9-7.py***

    Необходимо собрать данные в каждой категории c каждой карточки (всего их 160) с сайта http://parsinger.ru/html/index1_page_1.html  и сохранить всё в csv-файл.

### <ins>Парсинг с сохранением в json:</ins>

***parsing2json_4-10-4.py***

    Необходимо собрать все данные с карточек  1 любой категории на сайте http://parsinger.ru/html/index1_page_1.html и сохранить всё в json-файл.

***parsing2json_4-10-5.py***

    Необходимо собрать все данные с карточек со всех 5 категорий на сайте http://parsinger.ru/html/index1_page_1.html и сохранить всё в json-файл. 

***parsing2json_4-10-6.py***

    Необходимо собрать все данные с карточек товаров + ссылка на карточку из 1 любой категории на сайте http://parsinger.ru/html/index3_page_1.html и сохранить всё в json-файл.

***parsing2json_4-10-7.py***

    Необходимо собрать все данные с карточек товаров + ссылка на карточку со всех 5 категорий на сайте http://parsinger.ru/html/index1_page_1.html и сохранить всё в json-файл.

### <ins>Парсинг json:</ins>

***parsing_json_4-11.py***

    http://parsinger.ru/downloads/get_json/res.json
    
    1. Используйте полученный по ссылке JSON, чтобы посчитать количество товара в каждой категории.
    В результате необходимо получить словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}, где N - это общее количество товаров
    Количество вы найдёте в каждой карточке товара.
    
    2. Используйте полученный по ссылке JSON, чтобы посчитать стоимость товаров в каждой отдельной категории.
    В результате необходимо получить {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}, где N - это общая стоимость товаров.
