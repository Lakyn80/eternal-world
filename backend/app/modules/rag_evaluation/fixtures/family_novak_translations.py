from __future__ import annotations

from typing import Final

from app.modules.rag_evaluation.fixtures.family_novak_facts import FAMILY_NOVAK_FACTS

TranslationLang = Final[tuple[str, ...]]
TRANSLATION_LANGS: TranslationLang = ("ru", "en", "es", "fr")

FACT_TRANSLATIONS: dict[str, dict[str, str]] = {
    "f001": {
        "ru": "В детстве Ева жила с родителями в домике со сливовым садом у деревни Popice на юге Моравии.",
        "en": "As a child, Eva lived with her parents in a house with a plum orchard near the village of Popice in southern Moravia.",
        "es": "De pequeña, Eva vivía con sus padres en una casa con un huerto de ciruelos cerca del pueblo de Popice, en el sur de Moravia.",
        "fr": "Petite, Eva vivait avec ses parents dans une maison entourée d'un verger de pruniers près du village de Popice, en Moravie du Sud.",
    },
    "f002": {
        "ru": "Ещё до школы она по вторникам каждое утро помогала матери взвешивать абрикосы на рынке в Mikulov.",
        "en": "Even before school, she helped her mother weigh apricots at the market in Mikulov every Tuesday morning.",
        "es": "Aún antes de la escuela, ayudaba a su madre a pesar albaricoques en el mercado de Mikulov cada martes por la mañana.",
        "fr": "Avant même l'école, elle aidait sa mère à peser des abricots au marché de Mikulov chaque mardi matin.",
    },
    "f004": {
        "ru": "В пятом классе она выиграла районный конкурс чтения вслух из книги о моравских виноградниках.",
        "en": "In fifth grade she won a district reading-aloud contest with a book about Moravian vineyards.",
        "es": "En quinto curso ganó un concurso distrital de lectura en voz alta con un libro sobre viñedos moravos.",
        "fr": "En cinquième année, elle remporta un concours de lecture à voix haute avec un livre sur les vignobles moraves.",
    },
    "f006": {
        "ru": "Архивная запись указывает, что начальную школу она окончила в Mikulov с отличием в 1962 году.",
        "en": "An archival record states that she finished primary school in Mikulov with honors in 1962.",
        "es": "Un acta de archivo indica que terminó la escuela primaria en Mikulov con matrícula de honor en 1962.",
        "fr": "Un procès-verbal d'archives indique qu'elle a terminé l'école primaire à Mikulov avec mention en 1962.",
    },
    "f010": {
        "ru": "В 1968 году она поступила на педагогический факультет в Brno, чтобы изучать чешский язык и музыкальное воспитание.",
        "en": "In 1968 she enrolled at the faculty of education in Brno to study Czech and music education.",
        "es": "En 1968 ingresó en la facultad de pedagogía de Brno para estudiar checo y educación musical.",
        "fr": "En 1968, elle entra à la faculté de pédagogie de Brno pour étudier le tchèque et l'éducation musicale.",
    },
    "f011": {
        "ru": "Студенческий индекс из Brno подтверждает, что диплом она получила в июне 1972 года с темой о сельской школьной библиотеке.",
        "en": "A student index from Brno confirms that she received her diploma in June 1972 on the topic of a rural school library.",
        "es": "Un índice estudiantil de Brno confirma que obtuvo su diploma en junio de 1972 con un trabajo sobre la biblioteca escolar rural.",
        "fr": "Un index étudiant de Brno confirme qu'elle a obtenu son diplôme en juin 1972 sur le thème de la bibliothèque scolaire rurale.",
    },
    "f013": {
        "ru": "С Pavlem она познакомилась на танцах в Доме культуры на Lidická, когда он одолжил ей шаль у гардероба.",
        "en": "She met Pavel at a dance evening in the House of Culture on Lidická when he lent her a shawl at the cloakroom.",
        "es": "Conoció a Pavel en un baile en la Casa de la Cultura de Lidická, cuando él le prestó un chal en el guardarropa.",
        "fr": "Elle a rencontré Pavel lors d'un bal au palais de la culture de Lidická, quand il lui prêta un châle au vestiaire.",
    },
    "f015": {
        "ru": "Свадьба состоялась 16 сентября 1972 года в часовне святого Václav на площади Svobody в Brno.",
        "en": "The wedding took place on September 16, 1972, in the chapel of Saint Václav on Svobody Square in Brno.",
        "es": "La boda tuvo lugar el 16 de septiembre de 1972 en la capilla de San Václav en la plaza Svobody de Brno.",
        "fr": "Le mariage eut lieu le 16 septembre 1972 dans la chapelle de saint Václav sur la place Svobody à Brno.",
    },
    "f016": {
        "ru": "Свидетельство о браке в семейном архиве указывает свидетелями Jiří Novotný и учительницу Horáková.",
        "en": "The marriage certificate kept in the family archive lists Jiří Novotný and teacher Horáková as witnesses.",
        "es": "El acta de matrimonio guardada en el archivo familiar nombra como testigos a Jiří Novotný y a la profesora Horáková.",
        "fr": "L'acte de mariage conservé dans les archives familiales cite Jiří Novotný et la professeure Horáková comme témoins.",
    },
    "f018": {
        "ru": "Дочь Tereza родилась 14 марта 1974 года в роддоме на Bohuničská в Brno.",
        "en": "Her daughter Tereza was born on March 14, 1974, at the maternity hospital on Bohuničská in Brno.",
        "es": "Su hija Tereza nació el 14 de marzo de 1974 en la maternidad de la calle Bohuničská en Brno.",
        "fr": "Sa fille Tereza est née le 14 mars 1974 à la maternité de la rue Bohuničská à Brno.",
    },
    "f019": {
        "ru": "Сын Martin появился на свет 2 ноября 1977 года во время первого снега, когда Pavel застрял машиной в Kopřivnice.",
        "en": "Her son Martin was born on November 2, 1977, during the first snow, when Pavel got stuck with the car in Kopřivnice.",
        "es": "Su hijo Martin nació el 2 de noviembre de 1977 durante la primera nieve, cuando Pavel se quedó atascado con el coche en Kopřivnice.",
        "fr": "Son fils Martin est né le 2 novembre 1977 pendant les premières neiges, alors que Pavel était bloqué en voiture à Kopřivnice.",
    },
    "f022": {
        "ru": "Внучка Klára родилась в 2003 году, когда Eva уже была на пенсии и жила в Řečkovice.",
        "en": "Granddaughter Klára was born in 2003, when Eva was already retired and living in Řečkovice.",
        "es": "La nieta Klára nació en 2003, cuando Eva ya estaba jubilada y vivía en Řečkovice.",
        "fr": "La petite-fille Klára est née en 2003, alors qu'Eva était déjà retraitée et vivait à Řečkovice.",
    },
    "f024": {
        "ru": "После назначения она преподавала литературу в начальной школе в brněnské Líšeň в классе с видом на панельный район.",
        "en": "After starting work, she taught literature at an elementary school in Brno-Líšeň in a classroom overlooking the housing estate.",
        "es": "Tras su nombramiento enseñó literatura en una escuela primaria de Líšeň, en Brno, en un aula con vistas al barrio de bloques.",
        "fr": "Après sa nomination, elle enseigna la littérature dans une école primaire de Líšeň, à Brno, dans une salle donnant sur le quartier.",
    },
    "f025": {
        "ru": "Школьная хроника из Líšeň записывает, что Eva вела читательский кружок под названием Pod hvězdami.",
        "en": "The school chronicle from Líšeň records that Eva led a reading circle named Pod hvězdami.",
        "es": "La crónica escolar de Líšeň recoge que Eva dirigía un círculo de lectura llamado Pod hvězdami.",
        "fr": "La chronique scolaire de Líšeň indique qu'Eva animait un cercle de lecture nommé Pod hvězdami.",
    },
    "f028": {
        "ru": "Оценка 1989 года указывает, что Eva подготовила выпускной семинар о моравской народной поэзии.",
        "en": "A 1989 evaluation states that Eva prepared a graduation seminar on Moravian folk poetry.",
        "es": "Una evaluación de 1989 indica que Eva preparó un seminario de graduación sobre poesía popular morava.",
        "fr": "Une évaluation de 1989 indique qu'Eva a préparé un séminaire de fin d'études sur la poésie populaire morave.",
    },
    "f029": {
        "ru": "На пенсию она ушла в 2000 году после последнего школьного концерта, где играла на гитаре с учениками.",
        "en": "She retired in 2000 after the last school concert, where she played guitar with her students.",
        "es": "Se jubiló en 2000 tras el último concierto escolar, en el que tocó la guitarra con sus alumnos.",
        "fr": "Elle prit sa retraite en 2000 après le dernier concert scolaire, où elle joua de la guitare avec ses élèves.",
    },
    "f031": {
        "ru": "Гитару она купила в 1975 году и училась играть на ней песню о Моравии у соседки с Gorkého.",
        "en": "She bought a guitar in 1975 and learned to play a song about Moravia from a neighbor on Gorkého street.",
        "es": "Compró una guitarra en 1975 y aprendió a tocar una canción sobre Moravia con una vecina de la calle Gorkého.",
        "fr": "Elle s'acheta une guitare en 1975 et apprit une chanson sur la Moravie auprès d'une voisine de la rue Gorkého.",
    },
    "f034": {
        "ru": "Фотография 1995 года показывает Evu, сушащую травы на чердаке в Řečkovice.",
        "en": "A 1995 photograph shows Eva drying herbs in the attic in Řečkovice.",
        "es": "Una fotografía de 1995 muestra a Eva secando hierbas en el desván de Řečkovice.",
        "fr": "Une photographie de 1995 montre Eva faisant sécher des herbes au grenier à Řečkovice.",
    },
    "f036": {
        "ru": "В 1985 году она впервые поехала автобусом в Vienna на книжную выставку и привезла словарь австрийских идиом.",
        "en": "In 1985 she traveled by bus to Vienna for the first time for a book exhibition and brought back a dictionary of Austrian idioms.",
        "es": "En 1985 viajó por primera vez en autobús a Viena para una feria del libro y trajo un diccionario de modismos austriacos.",
        "fr": "En 1985, elle prit le bus pour la première fois pour aller à Vienne à une exposition de livres et rapporta un dictionnaire d'expressions autrichiennes.",
    },
    "f038": {
        "ru": "Дневник путешествия 1992 года описывает неделю у Balaton, где Eva каждое утро в семь часов плавала.",
        "en": "A 1992 travel diary describes a week at Lake Balaton, where Eva swam every morning at seven o'clock.",
        "es": "Un diario de viaje de 1992 describe una semana en el lago Balaton, donde Eva nadaba cada mañana a las siete.",
        "fr": "Un journal de voyage de 1992 décrit une semaine au lac Balaton, où Eva nageait chaque matin à sept heures.",
    },
    "f039": {
        "ru": "В 1999 году она прошла пеший поход по Pálava с коллегами из Líšeň до Dívčí hrady.",
        "en": "In 1999 she completed a hiking trip across Pálava with colleagues from Líšeň as far as Dívčí hrady.",
        "es": "En 1999 hizo una excursión a pie por Pálava con colegas de Líšeň hasta Dívčí hrady.",
        "fr": "En 1999, elle fit une randonnée à travers Pálava avec des collègues de Líšeň jusqu'à Dívčí hrady.",
    },
    "f041": {
        "ru": "Семейный дом в Řečkovice они купили в 1982 году и сразу посадили вишню во дворе за кухней.",
        "en": "They bought the family house in Řečkovice in 1982 and immediately planted a cherry tree in the yard behind the kitchen.",
        "es": "Compraron la casa familiar en Řečkovice en 1982 e inmediatamente plantaron un cerezo en el patio detrás de la cocina.",
        "fr": "Ils achetèrent la maison familiale à Řečkovice en 1982 et plantèrent aussitôt un cerisier dans la cour derrière la cuisine.",
    },
    "f042": {
        "ru": "Строительный план дома в Řečkovice имел штамп проектировщика Pavel Novák от 12 мая 1981 года.",
        "en": "The building plan for the house in Řečkovice bore the stamp of designer Pavel Novák dated May 12, 1981.",
        "es": "El plano de construcción de la casa en Řečkovice llevaba el sello del proyectista Pavel Novák del 12 de mayo de 1981.",
        "fr": "Le plan de construction de la maison à Řečkovice portait le tampon du concepteur Pavel Novák en date du 12 mai 1981.",
    },
    "f046": {
        "ru": "Каждое воскресенье в девять часов она звонила Tereza и спрашивала, что та готовит на обед.",
        "en": "Every Sunday at nine o'clock she called Tereza and asked what she was cooking for lunch.",
        "es": "Cada domingo a las nueve llamaba a Tereza y le preguntaba qué iba a cocinar para comer.",
        "fr": "Chaque dimanche à neuf heures, elle appelait Tereza pour lui demander ce qu'elle préparait pour le déjeuner.",
    },
    "f048": {
        "ru": "Семейный календарь 2010 года фиксирует традицию петь у ёлки колядку Nesem vám noviny.",
        "en": "The 2010 family calendar records the tradition of singing the carol Nesem vám noviny by the tree.",
        "es": "El calendario familiar de 2010 recoge la tradición de cantar junto al árbol la villancico Nesem vám noviny.",
        "fr": "Le calendrier familial de 2010 mentionne la tradition de chanter la carol Nesem vám noviny près du sapin.",
    },
    "f049": {
        "ru": "Весной она ходила с Klára собирать одуванчики на холм за Řečkovice для бабушкиного чая.",
        "en": "In spring she went with Klára to pick dandelions on the hill behind Řečkovice for grandmother's tea.",
        "es": "En primavera iba con Klára a recoger dientes de león en la colina detrás de Řečkovice para el té de la abuela.",
        "fr": "Au printemps, elle allait avec Klára cueillir des pissenlits sur la colline derrière Řečkovice pour le thé de grand-mère.",
    },
    "f051": {
        "ru": "В 2015 году врач впервые диагностировал у неё сердечный шум и рекомендовал регулярные прогулки.",
        "en": "In 2015 a doctor first diagnosed her with a heart murmur and recommended regular walks.",
        "es": "En 2015 un médico le diagnosticó por primera vez un soplo cardíaco y le recomendó paseos regulares.",
        "fr": "En 2015, un médecin lui diagnostiqua pour la première fois un souffle au cœur et recommanda des promenades régulières.",
    },
    "f053": {
        "ru": "Больничная выписка мая 2018 года указывает короткую госпитализацию из-за усталости и низкого давления.",
        "en": "A May 2018 hospital report notes a short stay on the ward due to fatigue and low blood pressure.",
        "es": "Un informe hospitalario de mayo de 2018 indica una breve hospitalización por fatiga y presión baja.",
        "fr": "Un compte rendu hospitalier de mai 2018 mentionne un court séjour pour fatigue et tension basse.",
    },
    "f056": {
        "ru": "Eva Novakova умерла 3 октября 2020 года дома в Řečkovice в окружении семьи.",
        "en": "Eva Nováková died on October 3, 2020, at home in Řečkovice surrounded by her family.",
        "es": "Eva Nováková murió el 3 de octubre de 2020 en casa, en Řečkovice, rodeada de su familia.",
        "fr": "Eva Nováková est morte le 3 octobre 2020 chez elle à Řečkovice, entourée de sa famille.",
    },
    "f057": {
        "ru": "Некролог в местной газете указывает, что похороны состоялись 9 октября 2020 года на кладбище в Řečkovice.",
        "en": "An obituary in the local newsletter states that the funeral took place on October 9, 2020, at the cemetery in Řečkovice.",
        "es": "Una esquela en el boletín local indica que el funeral tuvo lugar el 9 de octubre de 2020 en el cementerio de Řečkovice.",
        "fr": "Une nécrologie dans le journal communal indique que les funérailles eurent lieu le 9 octobre 2020 au cimetière de Řečkovice.",
    },
    "f059": {
        "ru": "Среди коллег она была известна тем, что никогда не повышала голос, но могла одним взглядом заставить замолчать весь класс.",
        "en": "Among colleagues she was known for never raising her voice, yet she could silence an entire class with a look.",
        "es": "Entre sus colegas era conocida por no alzar nunca la voz, pero podía callar a toda la clase con una mirada.",
        "fr": "Parmi ses collègues, elle était connue pour ne jamais élever la voix, tout en sachant faire taire toute une classe d'un regard.",
    },
    "f061": {
        "ru": "Рекомендательное письмо 1990 года описывает Evu как терпеливую и внимательную руководительницу читательского кружка.",
        "en": "A 1990 recommendation letter describes Eva as a patient and careful leader of the reading circle.",
        "es": "Una carta de recomendación de 1990 la describe como una paciente y cuidadosa directora del círculo de lectura.",
        "fr": "Une lettre de recommandation de 1990 la décrit comme une responsable patiente et soigneuse du cercle de lecture.",
    },
    "f062": {
        "ru": "Она чаще всего повторяла, что книга — более надёжный спутник, чем большинство людей.",
        "en": "She most often repeated that a book is a more reliable companion than most people.",
        "es": "Repetía con frecuencia que un libro es un compañero más fiable que la mayoría de las personas.",
        "fr": "Elle répétait surtout qu'un livre est un compagnon plus fiable que la plupart des gens.",
    },
    "f064": {
        "ru": "После учёбы Tereza работала медсестрой в Brno на терапевтическом отделении в Bohunice.",
        "en": "After her studies Tereza worked as a nurse in Brno on the internal medicine ward in Bohunice.",
        "es": "Tras sus estudios, Tereza trabajó como enfermera en Brno en la planta de medicina interna de Bohunice.",
        "fr": "Après ses études, Tereza travailla comme infirmière à Brno au service de médecine interne de Bohunice.",
    },
    "f066": {
        "ru": "Семейный архив хранит письмо, где Martin описывает первый совместный отпуск с детьми у Máchovo jezero.",
        "en": "The family archive keeps a letter in which Martin describes the first joint vacation with the children at Máchovo jezero.",
        "es": "El archivo familiar guarda una carta en la que Martin describe las primeras vacaciones en familia con los niños en el lago Máchovo.",
        "fr": "Les archives familiales conservent une lettre où Martin décrit les premières vacances en famille avec les enfants au lac Máchovo.",
    },
    "f067": {
        "ru": "В юности Klára играла на флейте в духовом оркестре в Kuřim, и Eva однажды пришла послушать её в сокол.",
        "en": "As a teenager Klára played flute in a brass band in Kuřim, and Eva once came to listen to her at the community hall.",
        "es": "De adolescente, Klára tocaba la flauta en una banda de viento en Kuřim, y Eva fue una vez a escucharla al local social.",
        "fr": "Adolescente, Klára jouait de la flûte dans une fanfare à Kuřim, et Eva vint un jour l'écouter à la salle communale.",
    },
    "f069": {
        "ru": "После смерти Pavla Eva оставила в саду перголу, окрашенную в синий цвет, как он когда-то её покрасил.",
        "en": "After Pavel's death Eva left the pergola in the garden painted blue, as he had once painted it.",
        "es": "Tras la muerte de Pavel, Eva dejó la pérgola del jardín pintada de azul, como él la había pintado una vez.",
        "fr": "Après la mort de Pavel, Eva laissa la pergola du jardin peinte en bleu, comme il l'avait peinte autrefois.",
    },
    "f072": {
        "ru": "Матери Ludmila она помогала записывать семейные рецепты в синюю тетрадь в линейку.",
        "en": "She helped her mother Ludmila write down family recipes in a blue lined notebook.",
        "es": "Ayudaba a su madre Ludmila a anotar recetas familiares en un cuaderno azul de rayas.",
        "fr": "Elle aidait sa mère Ludmila à noter les recettes de famille dans un cahier bleu à lignes.",
    },
    "f074": {
        "ru": "Родословная, составленная в 2005 году, указывает, что прабабушка происходила из деревни Pavlov на Pálava.",
        "en": "A genealogy compiled in 2005 states that her great-grandmother came from the village of Pavlov in Pálava.",
        "es": "Un árbol genealógico elaborado en 2005 indica que su bisabuela procedía del pueblo de Pavlov, en Pálava.",
        "fr": "Un arbre généalogique établi en 2005 indique que son arrière-grand-mère venait du village de Pavlov, en Pálava.",
    },
    "f076": {
        "ru": "В 1979 году ученики подарили ей деревянное перо с выгравированной надписью «Спасибо, учительница».",
        "en": "In 1979 her students gave her a wooden pen engraved with the words Thank you, dear teacher.",
        "es": "En 1979 sus alumnos le regalaron una pluma de madera grabada con las palabras Gracias, profesora.",
        "fr": "En 1979, ses élèves lui offrirent un stylo en bois gravé des mots Merci, chère professeure.",
    },
    "f078": {
        "ru": "Список подарков к серебряной свадьбе в 1997 году включает набор фарфоровых чашек от бывших учеников.",
        "en": "The silver wedding gift list from 1997 includes a set of porcelain cups from former students.",
        "es": "La lista de regalos de bodas de plata de 1997 incluye un juego de tazas de porcelana de antiguos alumnos.",
        "fr": "La liste de cadeaux pour les noces d'argent de 1997 comprend un service de tasses en porcelaine offert par d'anciens élèves.",
    },
    "f080": {
        "ru": "Последней книгой, которую она дочитала, был роман о моравской деревне писательницы из Uherské Hradiště.",
        "en": "The last book she finished was a novel about a Moravian village by a writer from Uherské Hradiště.",
        "es": "El último libro que terminó fue una novela sobre un pueblo moravo de una escritora de Uherské Hradiště.",
        "fr": "Le dernier livre qu'elle termina était un roman sur un village morave d'une écrivaine d'Uherské Hradiště.",
    },
}

MEMORY_TITLE_TRANSLATIONS: dict[str, dict[str, str]] = {
    "f001": {
        "ru": "Детство у Popice",
        "en": "Childhood in Popice",
        "es": "Infancia en Popice",
        "fr": "Enfance à Popice",
    },
    "f002": {
        "ru": "Абрикосы в Mikulov",
        "en": "Apricots in Mikulov",
        "es": "Albaricoques en Mikulov",
        "fr": "Abricots à Mikulov",
    },
    "f004": {
        "ru": "Конкурс чтения",
        "en": "Reading contest",
        "es": "Concurso de lectura",
        "fr": "Concours de lecture",
    },
    "f010": {
        "ru": "Педагогический факультет",
        "en": "Faculty of education",
        "es": "Facultad de pedagogía",
        "fr": "Faculté de pédagogie",
    },
    "f013": {
        "ru": "Танцы с Pavlem",
        "en": "Dance evening with Pavel",
        "es": "Baile con Pavel",
        "fr": "Bal avec Pavel",
    },
    "f015": {
        "ru": "Свадьба в Brno",
        "en": "Wedding in Brno",
        "es": "Boda en Brno",
        "fr": "Mariage à Brno",
    },
    "f018": {
        "ru": "Рождение Tereza",
        "en": "Birth of Tereza",
        "es": "Nacimiento de Tereza",
        "fr": "Naissance de Tereza",
    },
    "f019": {
        "ru": "Рождение Martin",
        "en": "Birth of Martin",
        "es": "Nacimiento de Martin",
        "fr": "Naissance de Martin",
    },
    "f022": {
        "ru": "Рождение Klára",
        "en": "Birth of Klára",
        "es": "Nacimiento de Klára",
        "fr": "Naissance de Klára",
    },
    "f024": {
        "ru": "Учительница в Líšeň",
        "en": "Teacher in Líšeň",
        "es": "Profesora en Líšeň",
        "fr": "Enseignante à Líšeň",
    },
    "f029": {
        "ru": "Выход на пенсию",
        "en": "Retirement",
        "es": "Jubilación",
        "fr": "Retraite",
    },
    "f031": {
        "ru": "Первая гитара",
        "en": "First guitar",
        "es": "Primera guitarra",
        "fr": "Première guitare",
    },
    "f036": {
        "ru": "Книги в Vienna",
        "en": "Books in Vienna",
        "es": "Libros en Viena",
        "fr": "Livres à Vienne",
    },
    "f039": {
        "ru": "Поход по Pálava",
        "en": "Hike in Pálava",
        "es": "Excursión por Pálava",
        "fr": "Randonnée à Pálava",
    },
    "f041": {
        "ru": "Дом в Řečkovice",
        "en": "House in Řečkovice",
        "es": "Casa en Řečkovice",
        "fr": "Maison à Řečkovice",
    },
    "f046": {
        "ru": "Воскресный звонок",
        "en": "Sunday phone call",
        "es": "Llamada dominical",
        "fr": "Appel du dimanche",
    },
    "f049": {
        "ru": "Одуванчики с Klára",
        "en": "Dandelions with Klára",
        "es": "Dientes de león con Klára",
        "fr": "Pissenlits avec Klára",
    },
    "f051": {
        "ru": "Сердечный шум",
        "en": "Heart murmur",
        "es": "Soplo cardíaco",
        "fr": "Souffle cardiaque",
    },
    "f056": {
        "ru": "Последний день",
        "en": "Last day",
        "es": "Último día",
        "fr": "Dernier jour",
    },
    "f059": {
        "ru": "Взгляд в класс",
        "en": "Classroom look",
        "es": "Mirada al aula",
        "fr": "Regard en classe",
    },
    "f062": {
        "ru": "О книгах",
        "en": "About books",
        "es": "Sobre los libros",
        "fr": "Sur les livres",
    },
    "f064": {
        "ru": "Tereza — медсестра",
        "en": "Tereza the nurse",
        "es": "Tereza enfermera",
        "fr": "Tereza infirmière",
    },
    "f067": {
        "ru": "Klára и флейта",
        "en": "Klára's flute",
        "es": "Flauta de Klára",
        "fr": "Flûte de Klára",
    },
    "f069": {
        "ru": "Синяя пергола",
        "en": "Blue pergola",
        "es": "Pérgola azul",
        "fr": "Pergola bleue",
    },
    "f072": {
        "ru": "Рецепты матери",
        "en": "Mother's recipes",
        "es": "Recetas de la madre",
        "fr": "Recettes de mère",
    },
    "f076": {
        "ru": "Подарочное перо",
        "en": "Gift pen",
        "es": "Pluma de regalo",
        "fr": "Stylo offert",
    },
    "f080": {
        "ru": "Последняя книга",
        "en": "Last book",
        "es": "Último libro",
        "fr": "Dernier livre",
    },
}

PROFILE_TRANSLATIONS: dict[str, dict[str, str]] = {
    "ru": {
        "biography": (
            "Моравский учитель литературы, мать Tereza и Martin, бабушка Klára. "
            "Большую часть жизни провела в Brno и Řečkovice."
        ),
        "personality": "Тёплая, терпеливая, деловая; говорит спокойно и с уважением к фактам.",
        "catchphrases": (
            "Книга — более надёжный спутник.; Давайте скажем как есть.; Мне нужно это обдумать."
        ),
    },
    "en": {
        "biography": (
            "Moravian literature teacher, mother of Tereza and Martin, grandmother of Klára. "
            "She spent most of her life in Brno and Řečkovice."
        ),
        "personality": "Warm, patient, matter-of-fact; speaks calmly and with respect for facts.",
        "catchphrases": (
            "A book is a more reliable companion.; Let's tell it like it is.; I'll need to think that through."
        ),
    },
    "es": {
        "biography": (
            "Profesora de literatura morava, madre de Tereza y Martin, abuela de Klára. "
            "Pasó la mayor parte de su vida en Brno y Řečkovice."
        ),
        "personality": "Cálida, paciente, práctica; habla con calma y respeta los hechos.",
        "catchphrases": (
            "Un libro es un compañero más fiable.; Digámoslo con franqueza.; Déjame pensarlo."
        ),
    },
    "fr": {
        "biography": (
            "Enseignante de littérature morave, mère de Tereza et Martin, grand-mère de Klára. "
            "Elle a passé la plus grande partie de sa vie à Brno et à Řečkovice."
        ),
        "personality": "Chaleureuse, patiente, concrète; parle calmement et respecte les faits.",
        "catchphrases": (
            "Un livre est un compagnon plus fiable.; Disons les choses clairement.; Je dois y réfléchir."
        ),
    },
}

_EXPORT_FACT_IDS = frozenset(
    {
        "f001",
        "f002",
        "f004",
        "f006",
        "f010",
        "f011",
        "f013",
        "f015",
        "f016",
        "f018",
        "f019",
        "f022",
        "f024",
        "f025",
        "f028",
        "f029",
        "f031",
        "f034",
        "f036",
        "f038",
        "f039",
        "f041",
        "f042",
        "f046",
        "f048",
        "f049",
        "f051",
        "f053",
        "f056",
        "f057",
        "f059",
        "f061",
        "f062",
        "f064",
        "f066",
        "f067",
        "f069",
        "f072",
        "f074",
        "f076",
        "f078",
        "f080",
    }
)


def _czech_fact_text(fact_id: str) -> str:
    for fact in FAMILY_NOVAK_FACTS:
        if fact.fact_id == fact_id:
            return fact.text
    raise KeyError(f"Fact not found: {fact_id}")


def _czech_memory_title(fact_id: str) -> str | None:
    for fact in FAMILY_NOVAK_FACTS:
        if fact.fact_id == fact_id:
            return fact.memory_title
    raise KeyError(f"Fact not found: {fact_id}")


def get_fact_text(fact_id: str, locale: str) -> str:
    if locale == "cs":
        return _czech_fact_text(fact_id)
    if locale not in TRANSLATION_LANGS:
        raise ValueError(f"Unsupported locale: {locale}")
    return FACT_TRANSLATIONS[fact_id][locale]


def get_memory_title(fact_id: str, locale: str) -> str | None:
    if locale == "cs":
        return _czech_memory_title(fact_id)
    if locale not in TRANSLATION_LANGS:
        raise ValueError(f"Unsupported locale: {locale}")
    return MEMORY_TITLE_TRANSLATIONS.get(fact_id, {}).get(locale)


def validate_translation_coverage() -> None:
    if set(FACT_TRANSLATIONS) != _EXPORT_FACT_IDS:
        missing = _EXPORT_FACT_IDS - set(FACT_TRANSLATIONS)
        extra = set(FACT_TRANSLATIONS) - _EXPORT_FACT_IDS
        raise ValueError(f"FACT_TRANSLATIONS mismatch: missing={missing}, extra={extra}")

    for fact_id, translations in FACT_TRANSLATIONS.items():
        missing_langs = set(TRANSLATION_LANGS) - set(translations)
        if missing_langs:
            raise ValueError(f"Missing translations for {fact_id}: {missing_langs}")

    for fact_id in MEMORY_TITLE_TRANSLATIONS:
        if fact_id not in _EXPORT_FACT_IDS:
            raise ValueError(f"Unexpected memory title for {fact_id}")

    for fact_id, titles in MEMORY_TITLE_TRANSLATIONS.items():
        missing_langs = set(TRANSLATION_LANGS) - set(titles)
        if missing_langs:
            raise ValueError(f"Missing memory title translations for {fact_id}: {missing_langs}")

    for locale in TRANSLATION_LANGS:
        profile = PROFILE_TRANSLATIONS[locale]
        for field in ("biography", "personality", "catchphrases"):
            if not profile.get(field):
                raise ValueError(f"Missing profile field {field} for {locale}")


validate_translation_coverage()
