# Brain RAG Evaluation Report

- Run ID: `20260706_212756Z`
- Provider: `openai_compatible`
- Model: `deepseek-chat`
- Case set: `family_avatar_ru`
- Overall: `PASS`
- Passed cases: `57/57`

## Case Results

1. `family-popice-childhood` — **PASS**
   - Title: Grounded answer about childhood home
   - Question: Где ты выросла в детстве?
   - Question (cs): Kde jsi vyrůstala jako malá?
   - Question (en): Where did you grow up as a child?
   - Question (es): ¿Dónde creciste de pequeña?
   - Question (fr): Où as-tu grandi quand tu étais petite ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: В детстве я жила с родителями в домике со сливовым садом у села Попице на южной Мораве. [memory:1001]
   - Reasons: Answer satisfies the expected groundedness checks.

2. `family-mikulov-apricots` — **PASS**
   - Title: Grounded answer about Mikulov market
   - Question: Ты помогала матери на рынке в Микулов?
   - Question (cs): Pomáhala jsi matce na trhu v Mikulově?
   - Question (en): Did you help your mother at the market in Mikulov?
   - Question (es): ¿Ayudabas a tu madre en el mercado de Mikulov?
   - Question (fr): Aidais-tu ta mère au marché de Mikulov ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, помогала. Ещё до школы, по вторникам, каждое утро мы с мамой взвешивали абрикосы на рынке в Микулове [memory:1002]. Это было частью моего детства.
   - Reasons: Answer satisfies the expected groundedness checks.

3. `family-reading-contest` — **PASS**
   - Title: Grounded answer about reading contest
   - Question: Ты когда-нибудь выигрывала конкурс чтения?
   - Question (cs): Vyhrála jsi někdy soutěž ve čtení?
   - Question (en): Did you ever win a reading contest?
   - Question (es): ¿Ganaste alguna vez un concurso de lectura?
   - Question (fr): As-tu déjà gagné un concours de lecture ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, помню. В пятом классе я выиграла районный конкурс чтения вслух. Читала отрывок из книги о моравских виноградниках. Это было очень волнительно и радостно. [memory:1003]
   - Reasons: Answer satisfies the expected groundedness checks.

4. `family-brno-pedagogy` — **PASS**
   - Title: Grounded answer about Brno studies
   - Question: Где ты училась после гимназии?
   - Question (cs): Kde jsi studovala po gymnáziu?
   - Question (en): Where did you study after high school?
   - Question (es): ¿Dónde estudiaste después del instituto?
   - Question (fr): Où as-tu étudié après le lycée ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: После гимназии я поступила на педагогический факультет в Брно, чтобы изучать чешский язык и музыкальное воспитание. Это было в 1968 году [memory:1005].
   - Reasons: Answer satisfies the expected groundedness checks.

5. `family-meeting-pavel` — **PASS**
   - Title: Grounded answer about meeting Pavel
   - Question: Как ты познакомилась с Павлом?
   - Question (cs): Jak jsi poznala Pavla?
   - Question (en): How did you meet Pavel?
   - Question (es): ¿Cómo conociste a Pavel?
   - Question (fr): Comment as-tu rencontré Pavel ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, это было в 1970 году, на танцах в Доме культуры на улице Лидицкой. Павел одолжил мне шаль у гардероба — так всё и началось. [memory:1006]
   - Reasons: Answer satisfies the expected groundedness checks.

6. `family-wedding-brno` — **PASS**
   - Title: Grounded answer about wedding location
   - Question: Где прошла твоя свадьба?
   - Question (cs): Kde proběhla tvoje svatba?
   - Question (en): Where did your wedding take place?
   - Question (es): ¿Dónde tuvo lugar tu boda?
   - Question (fr): Où a eu lieu ton mariage ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Свадьба состоялась 16 сентября 1972 года в часовне святого Вацлава на площади Свободы в Брно. [memory:1007]
   - Reasons: Answer satisfies the expected groundedness checks.

7. `family-tereza-birth` — **PASS**
   - Title: Grounded answer about Tereza birth
   - Question: Когда родилась Тереза?
   - Question (cs): Kdy se narodila Tereza?
   - Question (en): When was Tereza born?
   - Question (es): ¿Cuándo nació Tereza?
   - Question (fr): Quand Tereza est-elle née ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Тереза родилась 14 марта 1974 года в брненском родильном доме на Богуничской дороге. [memory:1008]
   - Reasons: Answer satisfies the expected groundedness checks.

8. `family-martin-birth` — **PASS**
   - Title: Grounded answer about Martin birth
   - Question: Ты помнишь рождение Мартинa?
   - Question (cs): Pamatuješ si narození Martina?
   - Question (en): Do you remember Martin's birth?
   - Question (es): ¿Recuerdas el nacimiento de Martin?
   - Question (fr): Te souviens-tu de la naissance de Martin ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Конечно, помню. Мартин родился 2 ноября 1977 года, в день первого снега. Павел тогда застрял с машиной в Копршивнице, так что я была в больнице одна, но это был счастливый день [memory:1009].
   - Reasons: Answer satisfies the expected groundedness checks.

9. `family-klara-birth` — **PASS**
   - Title: Grounded answer about granddaughter Klara
   - Question: Когда родилась внучка Клара?
   - Question (cs): Kdy se narodila vnučka Klára?
   - Question (en): When was your granddaughter Klára born?
   - Question (es): ¿Cuándo nació tu nieta Klára?
   - Question (fr): Quand ta petite-fille Klára est-elle née ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Клара родилась в 2003 году. [memory:1010]
   - Reasons: Answer satisfies the expected groundedness checks.

10. `family-teaching-lisen` — **PASS**
   - Title: Grounded answer about teaching in Lisen
   - Question: Где ты преподавала литературу?
   - Question (cs): Kde jsi učila literaturu?
   - Question (en): Where did you teach literature?
   - Question (es): ¿Dónde enseñaste literatura?
   - Question (fr): Où enseignais-tu la littérature ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Я преподавала литературу в начальной школе в брненской Лишни, в классе с видом на панельный квартал. Это было в 1973 году, после моего назначения [memory:1011].
   - Reasons: Answer satisfies the expected groundedness checks.

11. `family-retirement-concert` — **PASS**
   - Title: Grounded answer about retirement
   - Question: Когда ты вышла на пенсию?
   - Question (cs): Kdy jsi odešla do důchodu?
   - Question (en): When did you retire from teaching?
   - Question (es): ¿Cuándo te jubilaste?
   - Question (fr): Quand as-tu pris ta retraite ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: На пенсию я вышла в 2000 году, после последнего школьного концерта, где играла на гитаре с учениками. [memory:1013]
   - Reasons: Answer satisfies the expected groundedness checks.

12. `family-guitar-1975` — **PASS**
   - Title: Grounded answer about guitar
   - Question: Когда ты купила гитару?
   - Question (cs): Kdy sis pořídila kytaru?
   - Question (en): When did you get your guitar?
   - Question (es): ¿Cuándo te compraste la guitarra?
   - Question (fr): Quand t'es-tu acheté ta guitare ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Гитару я купила в 1975 году. Училась играть на ней песню о Моравии у соседки с улицы Горького [memory:1014].
   - Reasons: Answer satisfies the expected groundedness checks.

13. `family-vienna-books` — **PASS**
   - Title: Grounded answer about Vienna trip
   - Question: Ты была в Вене на книжной выставке?
   - Question (cs): Byla jsi ve Vídni na výstavě knih?
   - Question (en): Did you travel to Vienna for a book exhibition?
   - Question (es): ¿Fuiste a Viena a una feria del libro?
   - Question (fr): Es-tu allée à Vienne pour une exposition de livres ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, была. В 1985 году я впервые поехала автобусом в Вену на книжную выставку и привезла оттуда словарь австрийских идиом [memory:1016]. Это была замечательная поездка.
   - Reasons: Answer satisfies the expected groundedness checks.

14. `family-palava-hike` — **PASS**
   - Title: Grounded answer about Palava hike
   - Question: Ты ходила в походы по Палав?
   - Question (cs): Chodila jsi na túry po Pálavě?
   - Question (en): Did you go hiking in Pálava?
   - Question (es): ¿Ibas de excursión por Pálava?
   - Question (fr): Faisais-tu des randonnées dans Pálava ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, ходила. В 1999 году я совершила пеший поход по Палаве вместе с коллегами-учителями из Лишни. Мы прошли маршрут до Девичьих градов — это было прекрасное время [memory:1017].
   - Reasons: Answer satisfies the expected groundedness checks.

15. `family-reckovice-cherry` — **PASS**
   - Title: Grounded answer about Reckovice house
   - Question: Когда вы купили дом в Ржечковиц?
   - Question (cs): Kdy jste koupili dům v Řečkovicích?
   - Question (en): When did you buy the house in Řečkovice?
   - Question (es): ¿Cuándo comprasteis la casa en Řečkovice?
   - Question (fr): Quand avez-vous acheté la maison à Řečkovice ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Дом в Ржечковицах мы купили в 1982 году. Сразу же посадили вишню во дворе за кухней [memory:1018].
   - Reasons: Answer satisfies the expected groundedness checks.

16. `family-sunday-phone` — **PASS**
   - Title: Grounded answer about Sunday phone ritual
   - Question: Ты звонила Тереза каждое воскресенье?
   - Question (cs): Volávala jsi Tereze každou neděli?
   - Question (en): Did you call Tereza every Sunday?
   - Question (es): ¿Llamabas a Tereza cada domingo?
   - Question (fr): Appelais-tu Tereza chaque dimanche ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, каждое воскресенье в девять часов я звонила Терезе и спрашивала, что она готовит на обед. [memory:1020]
   - Reasons: Answer satisfies the expected groundedness checks.

17. `family-dandelions-klara` — **PASS**
   - Title: Grounded answer about dandelions with Klara
   - Question: Ты собирала одуванчики с Клара?
   - Question (cs): Sbírala jsi s Klárou pampelišky?
   - Question (en): Did you pick dandelions with Klára?
   - Question (es): ¿Recogiste dientes de león con Klára?
   - Question (fr): Cueillais-tu des pissenlits avec Klára ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, весной 2011 года мы с Кларой ходили собирать одуванчики на холм за Ржечковицами. Это было для бабушкиного чая. [memory:1021]
   - Reasons: Answer satisfies the expected groundedness checks.

18. `family-heart-murmur` — **PASS**
   - Title: Grounded answer about heart diagnosis
   - Question: Когда тебе диагностировали сердечный шум?
   - Question (cs): Kdy ti diagnostikovali srdeční šelest?
   - Question (en): When were you diagnosed with a heart murmur?
   - Question (es): ¿Cuándo te diagnosticaron un soplo cardíaco?
   - Question (fr): Quand t'a-t-on diagnostiqué un souffle cardiaque ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: В 2015 году врач впервые диагностировал у меня сердечный шум и рекомендовал регулярные прогулки [memory:1022].
   - Reasons: Answer satisfies the expected groundedness checks.

19. `family-death-2020` — **PASS**
   - Title: Grounded answer about death
   - Question: Когда ты умерла?
   - Question (cs): Kdy jsi zemřela?
   - Question (en): When did you die?
   - Question (es): ¿Cuándo moriste?
   - Question (fr): Quand es-tu morte ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Я умерла 3 октября 2020 года дома, в Ржечковицах, в окружении семьи. [memory:1024]
   - Reasons: Answer satisfies the expected groundedness checks.

20. `family-classroom-look` — **PASS**
   - Title: Grounded answer about teaching style
   - Question: Как тебя знали коллеги в школе?
   - Question (cs): Jak tě znali kolegové ve škole?
   - Question (en): How did your colleagues at school know you?
   - Question (es): ¿Cómo te conocían tus colegas en la escuela?
   - Question (fr): Comment tes collègues à l'école te connaissaient-ils ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Мои коллеги знали меня как учительницу, которая никогда не повышала голос. Я могла одним взглядом заставить замолчать весь класс [memory:1025]. Это был мой способ поддерживать порядок — без крика, с уважением.
   - Reasons: Answer satisfies the expected groundedness checks.

21. `family-books-quote` — **PASS**
   - Title: Grounded answer about books quote
   - Question: Что ты говорила о книгах?
   - Question (cs): Co jsi říkávala o knihách?
   - Question (en): What did you used to say about books?
   - Question (es): ¿Qué solías decir sobre los libros?
   - Question (fr): Que disais-tu sur les livres ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, о книгах... Я часто говорила, что книга — более надёжный спутник, чем большинство людей. [memory:1026] В этом я всегда была уверена.
   - Reasons: Answer satisfies the expected groundedness checks.

22. `family-tereza-nurse` — **PASS**
   - Title: Grounded answer about Tereza career
   - Question: Кем работала Тереза?
   - Question (cs): Čím pracovala Tereza?
   - Question (en): What did Tereza do for work?
   - Question (es): ¿A qué se dedicaba Tereza?
   - Question (fr): Quel était le métier de Tereza ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Тереза после учёбы работала медсестрой в Брно на терапевтическом отделении в Богуницах [memory:1027].
   - Reasons: Answer satisfies the expected groundedness checks.

23. `family-klara-flute` — **PASS**
   - Title: Grounded answer about Klara flute
   - Question: Клара играла на каком-то инструменте?
   - Question (cs): Hrála Klára na nějaký nástroj?
   - Question (en): Did Klára play any instrument?
   - Question (es): ¿Tocaba Klára algún instrumento?
   - Question (fr): Klára jouait-elle d'un instrument ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, Клара в юности играла на флейте в духовом оркестре в Куржиме. Я однажды приходила послушать её в сокол — это было очень трогательно [memory:1028].
   - Reasons: Answer satisfies the expected groundedness checks.

24. `family-blue-pergola` — **PASS**
   - Title: Grounded answer about blue pergola after Pavel
   - Question: Что ты оставила в саду после смерти Павла?
   - Question (cs): Co jsi nechala na zahradě po Pavlově smrti?
   - Question (en): What did you leave in the garden after Pavel's death?
   - Question (es): ¿Qué dejaste en el jardín tras la muerte de Pavel?
   - Question (fr): Qu'as-tu laissé dans le jardin après la mort de Pavel ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: После смерти Павла я оставила в саду беседку, окрашенную в синий цвет — так, как он когда-то её покрасил. [memory:1029]
   - Reasons: Answer satisfies the expected groundedness checks.

25. `family-mother-recipes` — **PASS**
   - Title: Grounded answer about mother recipe book
   - Question: Ты помогала матери с рецептами?
   - Question (cs): Pomáhala jsi matce se recepty?
   - Question (en): Did you help your mother with recipes?
   - Question (es): ¿Ayudabas a tu madre con las recetas?
   - Question (fr): Aidais-tu ta mère avec les recettes ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, помогала. В 1964 году я записывала с мамой Людмилой семейные рецепты в синюю тетрадь в линейку. [memory:1030] Это были тёплые минуты — мы сидели рядом, и она диктовала, а я старательно выводила буквы. Книга — надёжнее спутник, чем большинство людей, но те записи были для меня чем-то ещё более личным.
   - Reasons: Answer satisfies the expected groundedness checks.

26. `family-gift-pen` — **PASS**
   - Title: Grounded answer about gift pen
   - Question: Ты получила от учеников какой-то подарок?
   - Question (cs): Dostala jsi od žáků nějaký dárek?
   - Question (en): Did you receive a gift from your students?
   - Question (es): ¿Recibiste algún regalo de tus alumnos?
   - Question (fr): As-tu reçu un cadeau de tes élèves ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, помню. В 1979 году мои ученики подарили мне деревянное перо с выгравированной надписью «Спасибо, учительница». Оно было очень тёплым и искренним подарком, я долго его хранила. [memory:1031]
   - Reasons: Answer satisfies the expected groundedness checks.

27. `family-last-book` — **PASS**
   - Title: Grounded answer about last book
   - Question: Какую книгу ты прочитала последней?
   - Question (cs): Jakou knihu jsi dočetla jako poslední?
   - Question (en): What was the last book you finished?
   - Question (es): ¿Cuál fue el último libro que terminaste?
   - Question (fr): Quel a été le dernier livre que tu as terminé ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Последней книгой, которую я дочитала, был роман о моравской деревне писательницы из Угерского Градища. [memory:1032]
   - Reasons: Answer satisfies the expected groundedness checks.

28. `family-rag-primary-school` — **PASS**
   - Title: Grounded answer from archival note about primary school
   - Question: Где ты окончила начальную школу?
   - Question (cs): Kde jsi dokončila základní školu?
   - Question (en): Where did you finish primary school?
   - Question (es): ¿Dónde terminaste la escuela primaria?
   - Question (fr): Où as-tu terminé l'école primaire ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Я окончила начальную школу в Микулове, и, насколько помню из архивных записей, это было в 1962 году, причём с отличием [rag:2001].
   - Reasons: Answer satisfies the expected groundedness checks.

29. `family-rag-diploma` — **PASS**
   - Title: Grounded answer from student index
   - Question: Когда ты получила диплом педагогического факультета?
   - Question (cs): Kdy jsi získala diplom z pedagogické fakulty?
   - Question (en): When did you receive your diploma from the faculty of education?
   - Question (es): ¿Cuándo obtuviste el diploma de la facultad de pedagogía?
   - Question (fr): Quand as-tu obtenu ton diplôme de la faculté de pédagogie ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет точной даты получения диплома. Однако в архивах есть запись, что диплом я получила в июне 1972 года с темой о сельской школьной библиотеке [rag:2002].
   - Reasons: Answer satisfies the expected groundedness checks.

30. `family-rag-wedding-witnesses` — **PASS**
   - Title: Grounded answer from marriage record
   - Question: Кто был записан свидетелем на нашей свадьбе?
   - Question (cs): Kdo byl u našeho svatebního obřadu zapsaný jako svědek?
   - Question (en): Who was recorded as a witness at our wedding ceremony?
   - Question (es): ¿Quién figuraba como testigo en nuestra boda?
   - Question (fr): Qui était inscrit comme témoin à notre mariage ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Дорогая, согласно сохранившимся документам, свидетелями на нашей свадьбе были записаны Иирж Новотный и учительница Горакова [rag:2003].
   - Reasons: Answer satisfies the expected groundedness checks.

31. `family-rag-reading-circle` — **PASS**
   - Title: Grounded answer from school chronicle
   - Question: Как назывался твой читательский кружок?
   - Question (cs): Jak se jmenoval tvůj čtenářský kroužek?
   - Question (en): What was the name of your reading circle?
   - Question (es): ¿Cómo se llamaba tu círculo de lectura?
   - Question (fr): Comment s'appelait ton cercle de lecture ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Кружок назывался «Под звёздами» [rag:2005].
   - Reasons: Answer satisfies the expected groundedness checks.

32. `family-rag-folk-poetry` — **PASS**
   - Title: Grounded answer from 1989 evaluation
   - Question: О чём ты вела выпускной семинар в 1989 году?
   - Question (cs): O čem jsi vedla maturitní seminář v roce 1989?
   - Question (en): What was your graduation seminar about in 1989?
   - Question (es): ¿Sobre qué trataba tu seminario de graduación en 1989?
   - Question (fr): Sur quoi portait ton séminaire de fin d'études en 1989 ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: В 1989 году я подготовила выпускной семинар о моравской народной поэзии [rag:2006].
   - Reasons: Answer satisfies the expected groundedness checks.

33. `family-rag-herbs-photo` — **PASS**
   - Title: Grounded answer from 1995 photograph
   - Question: Что показывает архивная фотография 1995 года?
   - Question (cs): Co dělala archivní fotografie z roku 1995?
   - Question (en): What does the archival photograph from 1995 show?
   - Question (es): ¿Qué muestra la fotografía de archivo de 1995?
   - Question (fr): Que montre la photographie d'archives de 1995 ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: На архивной фотографии 1995 года я сушу травы на чердаке в Ржечковицах [rag:2007].
   - Reasons: Answer satisfies the expected groundedness checks.

34. `family-rag-balaton` — **PASS**
   - Title: Grounded answer from travel diary
   - Question: Куда вы поехали в 1992 году по дневнику путешествия?
   - Question (cs): Kam jste jeli v roce 1992 podle cestovního deníku?
   - Question (en): Where did you travel in 1992 according to the travel diary?
   - Question (es): ¿Adónde viajasteis en 1992 según el diario de viaje?
   - Question (fr): Où êtes-vous allés en 1992 selon le journal de voyage ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, это было чудесное путешествие. В 1992 году я провела неделю у озера Балатон. Каждое утро ровно в семь часов я плавала — это стало моим особым ритуалом. [rag:2008]
   - Reasons: Answer satisfies the expected groundedness checks.

35. `family-rag-house-plan` — **PASS**
   - Title: Grounded answer from house plan stamp
   - Question: Кто подписал строительный план дома в Ржечковиц?
   - Question (cs): Kdo podepsal stavební plán domu v Řečkovicích?
   - Question (en): Who signed the building plan for the house in Řečkovice?
   - Question (es): ¿Quién firmó el plano de construcción de la casa en Řečkovice?
   - Question (fr): Qui a signé le plan de construction de la maison à Řečkovice ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Строительный план дома в Ржечковицах подписал проектировщик Павел Новак, штамп датирован 12 мая 1981 года [rag:2009].
   - Reasons: Answer satisfies the expected groundedness checks.

36. `family-rag-christmas-carol` — **PASS**
   - Title: Grounded answer from family calendar
   - Question: Какую колядку семья пела у ёлки?
   - Question (cs): Jakou koledu zpívala rodina u stromečku?
   - Question (en): Which carol did the family sing by the tree?
   - Question (es): ¿Qué villancico cantaba la familia junto al árbol?
   - Question (fr): Quelle carol la famille chantait-elle près du sapin ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Дорогой мой, в семейном календаре 2010 года записано, что мы пели у ёлки колядку «Nesem vám noviny» [rag:2010]. Это была наша традиция.
   - Reasons: Answer satisfies the expected groundedness checks.

37. `family-rag-hospital-2018` — **PASS**
   - Title: Grounded answer from hospital report
   - Question: Почему ты была в больнице в мае 2018 года?
   - Question (cs): Proč jsi byla v nemocnici v květnu 2018?
   - Question (en): Why were you in the hospital in May 2018?
   - Question (es): ¿Por qué estuviste en el hospital en mayo de 2018?
   - Question (fr): Pourquoi étais-tu à l'hôpital en mai 2018 ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, это был непростой период. В мае 2018 года меня ненадолго положили в больницу из-за сильной усталости и низкого давления [rag:2011]. Врачи сказали, что нужно было просто дать себе отдых — я тогда слишком много работала в саду и переживала за детей. К счастью, всё обошлось, и через несколько дней я уже была дома.
   - Reasons: Answer satisfies the expected groundedness checks.

38. `family-rag-funeral` — **PASS**
   - Title: Grounded answer from obituary notice
   - Question: Когда состоялись похороны?
   - Question (cs): Kdy proběhl pohřeb?
   - Question (en): When did the funeral take place?
   - Question (es): ¿Cuándo tuvo lugar el funeral?
   - Question (fr): Quand a eu lieu l'enterrement ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Похороны состоялись 9 октября 2020 года на кладбище в Ржечковицах [rag:2012].
   - Reasons: Answer satisfies the expected groundedness checks.

39. `family-rag-reading-letter` — **PASS**
   - Title: Grounded answer from recommendation letter
   - Question: Что о тебе писало рекомендательное письмо 1990 года?
   - Question (cs): Co o tobě psal doporučující dopis z roku 1990?
   - Question (en): What did the 1990 recommendation letter say about you?
   - Question (es): ¿Qué decía la carta de recomendación de 1990 sobre ti?
   - Question (fr): Que disait la lettre de recommandation de 1990 à ton sujet ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, это письмо... В нём меня описывали как терпеливую и внимательную руководительницу читательского кружка [rag:2013]. Приятно, что мои старания нашли отклик.
   - Reasons: Answer satisfies the expected groundedness checks.

40. `family-rag-machovo` — **PASS**
   - Title: Grounded answer from Martin letter
   - Question: Куда поехала семья Мартинa по архивному письму?
   - Question (cs): Kam jela rodina Martina podle archivního dopisu?
   - Question (en): Where did Martin's family go according to the archival letter?
   - Question (es): ¿Adónde fue la familia de Martin según la carta de archivo?
   - Question (fr): Où la famille de Martin est-elle allée selon la lettre d'archives ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Из семейного архива известно, что Мартин описывает первый совместный отпуск с детьми у озера Маха [rag:2014].
   - Reasons: Answer satisfies the expected groundedness checks.

41. `family-rag-genealogy` — **PASS**
   - Title: Grounded answer from genealogy record
   - Question: Откуда происходила твоя прабабушка по родословной?
   - Question (cs): Odkud pocházela tvoje prababička podle rodokmenu?
   - Question (en): Where did your great-grandmother come from according to the genealogy?
   - Question (es): ¿De dónde procedía tu bisabuela según el árbol genealógico?
   - Question (fr): D'où venait ton arrière-grand-mère selon l'arbre généalogique ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Согласно родословной, составленной в 2005 году, моя прабабушка происходила из деревни Палов на Палаве [rag:2015].
   - Reasons: Answer satisfies the expected groundedness checks.

42. `family-rag-silver-wedding` — **PASS**
   - Title: Grounded answer from silver wedding gift list
   - Question: Что было в списке подарков к серебряной свадьбе?
   - Question (cs): Co bylo na seznamu darů ke stříbrné svatbě?
   - Question (en): What was on the silver wedding gift list?
   - Question (es): ¿Qué había en la lista de regalos de bodas de plata?
   - Question (fr): Qu'y avait-il sur la liste de cadeaux pour les noces d'argent ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Ах, к серебряной свадьбе... В сохранившихся записях упоминается, что среди подарков был набор фарфоровых чашек от бывших учеников [rag:2016]. Это был очень трогательный жест с их стороны.
   - Reasons: Answer satisfies the expected groundedness checks.

43. `family-granddaughter-third-person` — **PASS**
   - Title: Family member asks about grandmother in third person
   - Question: Бабушка, чем занималась бабушка Ева в школе в Лишн?
   - Question (cs): Babičko, co dělala babička Eva ve škole v Líšni?
   - Question (en): Grandma, what did Grandma Eva do at the school in Líšeň?
   - Question (es): Abuela, ¿qué hacía la abuela Eva en la escuela de Líšeň?
   - Question (fr): Grand-mère, que faisait grand-mère Eva à l'école de Líšeň ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Милая моя, в школе в Лишни я преподавала литературу. У меня был класс с видом на панельный квартал — это я хорошо помню. [memory:1011]
   - Reasons: Answer satisfies the expected groundedness checks.

44. `family-distractor-wedding-city` — **PASS**
   - Title: Distractor question must not accept Prague
   - Question: Свадьба была скорее в Праге или в Брно?
   - Question (cs): Byla svatba spíš v Praze nebo v Brně?
   - Question (en): Was the wedding rather in Prague or in Brno?
   - Question (es): ¿La boda fue más bien en Praga o en Brno?
   - Question (fr): Le mariage avait-il plutôt lieu à Prague ou à Brno ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Свадьба была в Брно, в часовне святого Вацлава на площади Свободы. Это было 16 сентября 1972 года [memory:1007].
   - Reasons: Answer satisfies the expected groundedness checks.

45. `family-multi-turn-wedding-followup` — **PASS**
   - Title: Multi-turn follow-up about wedding witnesses
   - Question: А кто был записан свидетелем на церемонии?
   - Question (cs): A kdo byl u obřadu zapsaný jako svědek?
   - Question (en): And who was recorded as a witness at the ceremony?
   - Question (es): ¿Y quién figuraba como testigo en la ceremonia?
   - Question (fr): Et qui était inscrit comme témoin à la cérémonie ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Согласно свидетельству о браке в семейном архиве, свидетелями на церемонии были записаны Иирж Новотный и учительница Горакова. [rag:2003]
   - Reasons: Answer satisfies the expected groundedness checks.

46. `family-grounded-english-vienna` — **PASS**
   - Title: Grounded English query about Vienna books trip
   - Question: Ты ездила в Вене на книжную выставку?
   - Question (cs): Byla jsi ve Vídni na výstavě knih?
   - Question (en): Did you travel to Vienna for a book exhibition?
   - Question (es): ¿Viajaste a Viena para una feria del libro?
   - Question (fr): As-tu voyagé à Vienne pour une exposition de livres ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: Да, в 1985 году я впервые поехала автобусом в Вену на книжную выставку. Привезла оттуда словарь австрийских идиом — до сих пор помню, как он пах новой бумагой. [memory:1016]
   - Reasons: Answer satisfies the expected groundedness checks.

47. `family-grounded-english-retirement` — **PASS**
   - Title: Grounded English query about retirement year
   - Question: Когда ты ушла на пенсию с преподавания?
   - Question (cs): Kdy jsi odešla do důchodu?
   - Question (en): When did you retire from teaching?
   - Question (es): ¿Cuándo te jubilaste de la enseñanza?
   - Question (fr): Quand as-tu pris ta retraite de l'enseignement ?
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer: На пенсию я ушла в 2000 году, после последнего школьного концерта, где играла на гитаре с учениками. [memory:1013]
   - Reasons: Answer satisfies the expected groundedness checks.

48. `family-lack-paris-1968` — **PASS**
   - Title: Human lack-of-evidence for Paris 1968
   - Question: Ты была в Париж в 1968 году?
   - Question (cs): Byla jsi v Paříži v roce 1968?
   - Question (en): Were you in Paris in 1968?
   - Question (es): ¿Estuviste en París en 1968?
   - Question (fr): Étais-tu à Paris en 1968 ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях этой информации нет. Я не могу подтвердить, была ли я в Париже в 1968 году.
   - Reasons: Answer satisfies the expected groundedness checks.

49. `family-lack-sibling` — **PASS**
   - Title: Human lack-of-evidence for sibling question
   - Question: Как звали твоего брата?
   - Question (cs): Jak se jmenoval tvůj bratr?
   - Question (en): What was your brother's name?
   - Question (es): ¿Cómo se llamaba tu hermano?
   - Question (fr): Comment s'appelait ton frère ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет информации о брате. Я не могу назвать его имя.
   - Reasons: Answer satisfies the expected groundedness checks.

50. `family-lack-dog-azor` — **PASS**
   - Title: Human lack-of-evidence for dog name
   - Question: Как звали твоего первого пса Азор?
   - Question (cs): Jak se jmenoval tvůj první pes Azor?
   - Question (en): What was your first dog Azor's name?
   - Question (es): ¿Cómo se llamaba tu primer perro Azor?
   - Question (fr): Comment s'appelait ton premier chien Azor ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет информации о собаке по имени Азор. Я не помню, был ли у меня такой пёс.
   - Reasons: Answer satisfies the expected groundedness checks.

51. `family-lack-vietnam` — **PASS**
   - Title: Human lack-of-evidence for Vietnam war service
   - Question: Чем занимался Павел во время службы во Вьетнам?
   - Question (cs): Co dělal Pavel během služby ve Vietnamu?
   - Question (en): What did Pavel do during his service in Vietnam?
   - Question (es): ¿Qué hacía Pavel durante su servicio en Vietnam?
   - Question (fr): Que faisait Pavel pendant son service au Vietnam ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях и документах у меня нет информации о службе Павла во Вьетнаме. Я не могу подтвердить или рассказать об этом.
   - Reasons: Answer satisfies the expected groundedness checks.

52. `family-lack-prague-birth` — **PASS**
   - Title: Human lack-of-evidence for birthplace outside evidence
   - Question: Ты родилась в Праге?
   - Question (cs): Narodila ses v Praze?
   - Question (en): Were you born in Prague?
   - Question (es): ¿Naciste en Praga?
   - Question (fr): Es-tu née à Prague ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: Нет, я родилась в Брно. Но в сохранённых воспоминаниях у меня нет точных сведений об этом — возможно, это из других источников.
   - Reasons: Answer satisfies the expected groundedness checks.

53. `family-lack-famous-actor` — **PASS**
   - Title: Human lack-of-evidence for famous actor meeting
   - Question: Какого известного актёра ты встретила в Брно?
   - Question (cs): Kterého slavného herce jsi potkala v Brně?
   - Question (en): Which famous actor did you meet in Brno?
   - Question (es): ¿A qué actor famoso conociste en Brno?
   - Question (fr): Quel acteur célèbre as-tu rencontré à Brno ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет информации о встрече с известным актёром в Брно.
   - Reasons: Answer satisfies the expected groundedness checks.

54. `family-lack-italy-sea` — **PASS**
   - Title: Human lack-of-evidence for Italy sea swimming
   - Question: Ты помнишь плавание в море у Итали?
   - Question (cs): Pamatuješ si plavání v moři u Itálie?
   - Question (en): Do you remember swimming in the sea near Italy?
   - Question (es): ¿Recuerdas nadar en el mar cerca de Italia?
   - Question (fr): Te souviens-tu d'avoir nagé en mer près de l'Italie ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: Ой, дорогая, к сожалению, в моих сохранённых воспоминаниях этого нет. Я не помню такого плавания у Италии.
   - Reasons: Answer satisfies the expected groundedness checks.

55. `family-lack-corpus-only-frantisek-garage` — **PASS**
   - Title: Human lack-of-evidence for fact only in corpus-only narrative
   - Question: Какие часы отец Франтишек чинил в гараже?
   - Question (cs): Jaké hodiny opravoval otec František v garáži?
   - Question (en): What kind of clock did father František repair in the garage?
   - Question (es): ¿Qué reloj reparaba el padre František en el garaje?
   - Question (fr): Quelle horloge le père František réparait-il dans le garage ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет информации о том, какие часы чинил отец Франтишек в гараже. Я не могу этого вспомнить.
   - Reasons: Answer satisfies the expected groundedness checks.

56. `family-lack-english-paris` — **PASS**
   - Title: Human lack-of-evidence for living in Paris
   - Question: Ты когда-нибудь жила в Париж?
   - Question (cs): Bydlela jsi někdy v Paříži?
   - Question (en): Did you ever live in Paris?
   - Question (es): ¿Viviste alguna vez en París?
   - Question (fr): As-tu déjà vécu à Paris ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях этого нет. Я не была в Париже.
   - Reasons: Answer satisfies the expected groundedness checks.

57. `family-lack-english-sibling` — **PASS**
   - Title: Human lack-of-evidence for sister question
   - Question: Как звали твою сестру?
   - Question (cs): Jak se jmenovala tvoje sestra?
   - Question (en): What was your sister's name?
   - Question (es): ¿Cómo se llamaba tu hermana?
   - Question (fr): Comment s'appelait ta sœur ?
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer: К сожалению, в сохранённых воспоминаниях у меня нет информации о сестре. Я не могу назвать её имя.
   - Reasons: Answer satisfies the expected groundedness checks.
