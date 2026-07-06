from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


FactSourceType = Literal["memory", "rag", "corpus_only"]


@dataclass(frozen=True)
class FamilyNovakFact:
    fact_id: str
    section: str
    source_type: FactSourceType
    text: str
    occurred_year: int | None = None
    memory_title: str | None = None


FAMILY_NOVAK_FACTS: tuple[FamilyNovakFact, ...] = (
    FamilyNovakFact(
        "f001",
        "detstvi",
        "memory",
        "Jako malá Eva bydlela s rodiči v domku se švestkovým sadem u obce Popice na jižní Moravě.",
        1953,
        "Dětství u Popic",
    ),
    FamilyNovakFact(
        "f002",
        "detstvi",
        "memory",
        "Ještě před školou pomáhala matce vážit meruňky na trhu v Mikulově každé úterní ráno.",
        1955,
        "Meruňky v Mikulově",
    ),
    FamilyNovakFact(
        "f003",
        "detstvi",
        "corpus_only",
        "Otec František opravoval hodiny v garáži a Eva mu držela lupu, když jí bylo sedm.",
        1955,
    ),
    FamilyNovakFact(
        "f004",
        "detstvi",
        "memory",
        "V páté třídě vyhrála okresní soutěž ve čtení nahlas z knihy o moravských vinohradech.",
        1959,
        "Soutěž ve čtení",
    ),
    FamilyNovakFact(
        "f005",
        "detstvi",
        "corpus_only",
        "První den v nové škole si spletla lavici a sedla vedle chlapce, který později vedl obecní knihovnu.",
        1954,
    ),
    FamilyNovakFact(
        "f006",
        "detstvi",
        "rag",
        "Archivní zápisnice uvádí, že základní školu dokončila v Mikulově s vyznamenáním v roce 1962.",
        1962,
    ),
    FamilyNovakFact(
        "f007",
        "detstvi",
        "corpus_only",
        "Na jaře 1960 sbírala s kamarádkou Modřenky podél cesty k rybníku Soutok.",
        1960,
    ),
    FamilyNovakFact(
        "f008",
        "studium",
        "memory",
        "Na gymnáziu v Břeclavi ji nejvíc bavila hodina slovenštiny s paní učitelkou Horákovou.",
        1966,
        "Slovenština na gymnáziu",
    ),
    FamilyNovakFact(
        "f009",
        "studium",
        "corpus_only",
        "V maturitním ročníku napsala esej o moravských baladách, kterou četla na slavnostním večeru.",
        1967,
    ),
    FamilyNovakFact(
        "f010",
        "studium",
        "memory",
        "V roce 1968 nastoupila na brněnskou fakultu pedagogiky studovat češtinu a hudební výchovu.",
        1968,
        "Fakulta pedagogiky",
    ),
    FamilyNovakFact(
        "f011",
        "studium",
        "rag",
        "Studentský index z Brna potvrzuje, že diplom získala v červnu 1972 s tématem venkovské školní knihovny.",
        1972,
    ),
    FamilyNovakFact(
        "f012",
        "studium",
        "corpus_only",
        "Během praxe učila krátce ve vesnické škole v Moravském Krumlově a bydlela u vdovy na náměstí.",
        1971,
    ),
    FamilyNovakFact(
        "f013",
        "pavel",
        "memory",
        "Pavla poznala na tanečním večeru v Domě kultury na Lidické, když jí půjčil šálu u šatny.",
        1970,
        "Taneční večer s Pavlem",
    ),
    FamilyNovakFact(
        "f014",
        "pavel",
        "corpus_only",
        "Pavel pracoval jako projektant u stavebního družstva a ve volném čase kreslil plány zahrady sousedů.",
        1971,
    ),
    FamilyNovakFact(
        "f015",
        "pavel",
        "memory",
        "Svatba proběhla 16. září 1972 v kapli svatého Václava na náměstí Svobody v Brně.",
        1972,
        "Svatba v Brně",
    ),
    FamilyNovakFact(
        "f016",
        "pavel",
        "rag",
        "Oddací list uložený v rodinném archivu uvádí svědky Jiřího Novotného a učitelku Horákovou.",
        1972,
    ),
    FamilyNovakFact(
        "f017",
        "pavel",
        "corpus_only",
        "Po svatbě bydleli nejdříve v podnájmu v ulici Gorkého, kde sousedka učila Evu péct makový závin.",
        1973,
    ),
    FamilyNovakFact(
        "f018",
        "rodina",
        "memory",
        "Dcera Tereza se narodila 14. března 1974 v brněnské porodnici na Bohuniické silnici.",
        1974,
        "Narození Terezy",
    ),
    FamilyNovakFact(
        "f019",
        "rodina",
        "memory",
        "Syn Martin přišel na svět 2. listopadu 1977 během prvního sněhu, kdy Pavel uvízl autem v Kopřivnici.",
        1977,
        "Narození Martina",
    ),
    FamilyNovakFact(
        "f020",
        "rodina",
        "rag",
        "Rodinný deník z roku 1980 zmiňuje, že Tereza poprvé recitovala báseň na školním jarmarku.",
        1980,
    ),
    FamilyNovakFact(
        "f021",
        "rodina",
        "corpus_only",
        "Martin jako chlapec sbíral modely vlaků a Eva mu každý rok dávala atlas železnic pod stromeček.",
        1983,
    ),
    FamilyNovakFact(
        "f022",
        "rodina",
        "memory",
        "Vnučka Klára se narodila v roce 2003, kdy Eva už byla důchodkyně a bydlela v Řečkovicích.",
        2003,
        "Narození Kláry",
    ),
    FamilyNovakFact(
        "f023",
        "rodina",
        "corpus_only",
        "Klára jako malá volala Evě babi z Modřenky, protože jí připomínala barvu šatů z tanečního večera.",
        2005,
    ),
    FamilyNovakFact(
        "f024",
        "ucitelstvi",
        "memory",
        "Po nástupu učila literaturu na základní škole v brněnské Líšni ve třídě s výhledem do sídliště.",
        1973,
        "Učitelka v Líšni",
    ),
    FamilyNovakFact(
        "f025",
        "ucitelstvi",
        "rag",
        "Školní kronika z Líšně zaznamenává, že Eva vedla čtenářský kroužek pojmenovaný Pod hvězdami.",
        1978,
    ),
    FamilyNovakFact(
        "f026",
        "ucitelstvi",
        "memory",
        "Nejvíc ji těšilo, když žáci sami přinesli domácí knihy a četli u kamen v zimních měsících.",
        1981,
        "Čtení u kamen",
    ),
    FamilyNovakFact(
        "f027",
        "ucitelstvi",
        "corpus_only",
        "Jeden rok organizovala školní výstavu ilustrací k Božím povídkám v chodbě u tělocvičny.",
        1984,
    ),
    FamilyNovakFact(
        "f028",
        "ucitelstvi",
        "rag",
        "Hodnocení z roku 1989 uvádí, že Eva připravila maturitní seminář o moravské lidové poezii.",
        1989,
    ),
    FamilyNovakFact(
        "f029",
        "ucitelstvi",
        "memory",
        "Do důchodu odešla v roce 2000 po posledním školním koncertu, kde hrála na kytaru s žáky.",
        2000,
        "Odchod do důchodu",
    ),
    FamilyNovakFact(
        "f030",
        "ucitelstvi",
        "corpus_only",
        "Po odchodu do důchodu ještě jednou hostovala na besedě o Janáčkovi v knihovně v Řečkovicích.",
        2001,
    ),
    FamilyNovakFact(
        "f031",
        "konicky",
        "memory",
        "Kytaru si pořídila v roce 1975 a učila se na ni píseň o Moravě od sousedky z Gorkého.",
        1975,
        "První kytara",
    ),
    FamilyNovakFact(
        "f032",
        "konicky",
        "corpus_only",
        "V zahradě v Řečkovicích pěstovala levanduli podél plotu, který natřel Pavel modře na jaře 1998.",
        1998,
    ),
    FamilyNovakFact(
        "f033",
        "konicky",
        "memory",
        "Každý čtvrtek pekla makový koláč podle receptu po prababičce z Popic.",
        1990,
        "Makovy kolac",
    ),
    FamilyNovakFact(
        "f034",
        "konicky",
        "rag",
        "Fotografie z roku 1995 zachycuje Evu, jak suší bylinky na půdě v Řečkovicích.",
        1995,
    ),
    FamilyNovakFact(
        "f035",
        "konicky",
        "corpus_only",
        "V létě 1996 navštívila s Terezou hudební festival na hradě Veveří a slyšela smyčcový kvartet.",
        1996,
    ),
    FamilyNovakFact(
        "f036",
        "cesty",
        "memory",
        "V roce 1985 jela poprvé autobusem do Vídně na výstavu knih a přivezla si slovník rakouských idiomů.",
        1985,
        "Viden knihy",
    ),
    FamilyNovakFact(
        "f037",
        "cesty",
        "corpus_only",
        "Na jaře 1988 navštívila s Pavlem termální lázně v Piešťanech a chodila na rašelinové koupele.",
        1988,
    ),
    FamilyNovakFact(
        "f038",
        "cesty",
        "rag",
        "Cestovní deník z roku 1992 popisuje týden u Balatonu, kde Eva plavala každé ráno v sedm hodin.",
        1992,
    ),
    FamilyNovakFact(
        "f039",
        "cesty",
        "memory",
        "V roce 1999 absolvovala pěší túru po Pálavě s učitelskými kolegy z Líšně až k Dívčím hradům.",
        1999,
        "Palava tura",
    ),
    FamilyNovakFact(
        "f040",
        "cesty",
        "corpus_only",
        "Nikdy nenavštívila Paříž ani Londýn; nejvzdálenější cesta mimo stát vedla do Budapešti v roce 1994.",
        1994,
    ),
    FamilyNovakFact(
        "f041",
        "domov",
        "memory",
        "Rodinný dům v Řečkovicích koupili v roce 1982 a hned vysadili třešeň na dvorku za kuchyní.",
        1982,
        "Dum v Reckovicich",
    ),
    FamilyNovakFact(
        "f042",
        "domov",
        "rag",
        "Stavební plán domu v Řečkovicích nesl razítko projektanta Pavla Nováka ze dne 12. května 1981.",
        1981,
    ),
    FamilyNovakFact(
        "f043",
        "domov",
        "corpus_only",
        "V obýváku visel obraz Moravského krasu, který namaloval strýc Bořek během vojenské služby.",
        1983,
    ),
    FamilyNovakFact(
        "f044",
        "domov",
        "memory",
        "V zimě 1993 topili v kachlových kamnech a Eva u nich sušila jablka na provázku.",
        1993,
        "Kachlova kamna",
    ),
    FamilyNovakFact(
        "f045",
        "domov",
        "corpus_only",
        "Pavel postavil na zahradě dřevěnou pergolu, pod kterou Eva později četla vnučce pohádky.",
        1991,
    ),
    FamilyNovakFact(
        "f046",
        "ritualy",
        "memory",
        "Každou neděli telefonovala Tereze v devět hodin a ptala se, co vaří na oběd.",
        2006,
        "Nedelni telefonat",
    ),
    FamilyNovakFact(
        "f047",
        "ritualy",
        "corpus_only",
        "Před Vánoci pekla s Martinem perník ve tvaru hvězd a ukládala je do plechové krabice.",
        2008,
    ),
    FamilyNovakFact(
        "f048",
        "ritualy",
        "rag",
        "Rodinný kalendář z roku 2010 zaznamenává tradici zpívat u stromečku koledu Nesem vám noviny.",
        2010,
    ),
    FamilyNovakFact(
        "f049",
        "ritualy",
        "memory",
        "Na jaře chodila s Klárou sbírat pampelišky na kopec za Řečkovicemi pro babiččin čaj.",
        2011,
        "Pampelisky s Klarou",
    ),
    FamilyNovakFact(
        "f050",
        "ritualy",
        "corpus_only",
        "Každé léto psala dopisy bývalým žákům a posílala jim nové tituly z místní knihovny.",
        2012,
    ),
    FamilyNovakFact(
        "f051",
        "zdravi",
        "memory",
        "V roce 2015 jí lékař poprvé diagnostikoval srdeční šelest a doporučil pravidelné procházky.",
        2015,
        "Srdecni selest",
    ),
    FamilyNovakFact(
        "f052",
        "zdravi",
        "corpus_only",
        "Po operaci kolena v roce 2017 chodila na rehabilitaci do Bohunic a jezdila tam tramvají číslo pět.",
        2017,
    ),
    FamilyNovakFact(
        "f053",
        "zdravi",
        "rag",
        "Nemocniční zpráva z května 2018 uvádí krátký pobyt na interně kvůli únavě a nízkému tlaku.",
        2018,
    ),
    FamilyNovakFact(
        "f054",
        "zdravi",
        "memory",
        "Poslední roky trávila rána na balkoně s čajem z meduňky a s pohledem na třešeň na dvoře.",
        2019,
        "Balkon s cajem",
    ),
    FamilyNovakFact(
        "f055",
        "zdravi",
        "corpus_only",
        "Pavel jí nosil snídani do postele jen v neděli, když hrála rádio s Janáčkovou hudbou.",
        2019,
    ),
    FamilyNovakFact(
        "f056",
        "zaver",
        "memory",
        "Eva Nováková zemřela 3. října 2020 doma v Řečkovicích obklopena rodinou.",
        2020,
        "Posledni den",
    ),
    FamilyNovakFact(
        "f057",
        "zaver",
        "rag",
        "Parte v místním obecním zpravodaji uvádí, že pohřeb proběhl 9. října 2020 na hřbitově v Řečkovicích.",
        2020,
    ),
    FamilyNovakFact(
        "f058",
        "zaver",
        "corpus_only",
        "Na pohřbu zazněla Evina oblíbená píseň o Moravě, kterou kdysi hrála na kytaru ve škole.",
        2020,
    ),
    FamilyNovakFact(
        "f059",
        "osobnost",
        "memory",
        "Mezi kolegy byla známá tím, že nikdy nezvedla hlas, ale dokázala umlčet celou třídu pohledem.",
        1986,
        "Pohled do tridy",
    ),
    FamilyNovakFact(
        "f060",
        "osobnost",
        "corpus_only",
        "Děti si ji pamatovaly podle modrého šátku, který nosila na hodinách literatury každý podzim.",
        1987,
    ),
    FamilyNovakFact(
        "f061",
        "osobnost",
        "rag",
        "Doporučující dopis z roku 1990 popisuje Evu jako trpělivou a pečlivou vedoucí čtenářského kroužku.",
        1990,
    ),
    FamilyNovakFact(
        "f062",
        "osobnost",
        "memory",
        "Nejraději opakovala větu, že kniha je spolehlivější společník než většina lidí.",
        1994,
        "O knihach",
    ),
    FamilyNovakFact(
        "f063",
        "osobnost",
        "corpus_only",
        "Nepozorovala televizní zprávy denně; místo toho poslouchala večerní rozhlasové čtení.",
        2002,
    ),
    FamilyNovakFact(
        "f064",
        "rodina_dalsi",
        "memory",
        "Tereza po studiu pracovala jako zdravotní sestra v Brně na interně v Bohunicích.",
        1998,
        "Tereza zdravotni sestra",
    ),
    FamilyNovakFact(
        "f065",
        "rodina_dalsi",
        "corpus_only",
        "Martin se vyučil elektrikářem a později vedl malou firmu na servis kotlů v Kuřimi.",
        2004,
    ),
    FamilyNovakFact(
        "f066",
        "rodina_dalsi",
        "rag",
        "Rodinný archiv uchovává dopis, kde Martin popisuje první společnou dovolenou s dětmi u Máchova jezera.",
        2013,
    ),
    FamilyNovakFact(
        "f067",
        "rodina_dalsi",
        "memory",
        "Klára v dospívání hrála flétnu v dechovce v Kuřimi a Eva ji jednou přišla poslouchat do sokolovny.",
        2016,
        "Klara flétna",
    ),
    FamilyNovakFact(
        "f068",
        "rodina_dalsi",
        "corpus_only",
        "Pavel zemřel o tři roky dříve než Eva, v březnu 2017, po krátké nemoci v brněnské nemocnici.",
        2017,
    ),
    FamilyNovakFact(
        "f069",
        "rodina_dalsi",
        "memory",
        "Po Pavlově smrti Eva nechala na zahradě pergolu natřenou modře, jak ji kdysi namaloval.",
        2017,
        "Modra pergola",
    ),
    FamilyNovakFact(
        "f070",
        "rodina_dalsi",
        "corpus_only",
        "Nikdy neměla sourozence; rodiče ji vychovávali jako jedináčku v domku u Popic.",
        1950,
    ),
    FamilyNovakFact(
        "f071",
        "detaily",
        "corpus_only",
        "Narodila se 22. dubna 1948 v Brně v domě s červenou střechou na ulici Veveří.",
        1948,
    ),
    FamilyNovakFact(
        "f072",
        "detaily",
        "memory",
        "Matce Ludmíle pomáhala zapisovat rodinné recepty do modré linkované knihy.",
        1964,
        "Recepty matky",
    ),
    FamilyNovakFact(
        "f073",
        "detaily",
        "corpus_only",
        "Otec František sloužil u telegrafní roty a po válce pracoval jako úředník na obecním úřadě v Mikulově.",
        1946,
    ),
    FamilyNovakFact(
        "f074",
        "detaily",
        "rag",
        "Rodokmen založený v roce 2005 uvádí, že prababička pocházela z vsi na Pálavě jménem Pavlov.",
        2005,
    ),
    FamilyNovakFact(
        "f075",
        "detaily",
        "corpus_only",
        "Nikdy nevlastnila psa; jediné zvíře doma byla kočka Mourek, kterého přivedl Martin v roce 1984.",
        1984,
    ),
    FamilyNovakFact(
        "f076",
        "detaily",
        "memory",
        "V roce 1979 dostala od žáků dřevěné pero s vyrytým nápisem Děkujeme paní učitelce.",
        1979,
        "Darkove pero",
    ),
    FamilyNovakFact(
        "f077",
        "detaily",
        "corpus_only",
        "Nepatřila k politickým stranám a na shromážděních raději sedávala vzadu s knihou v kabelce.",
        1982,
    ),
    FamilyNovakFact(
        "f078",
        "detaily",
        "rag",
        "Seznam darů k stříbrné svatbě v roce 1997 obsahuje sada porcelánových šálků od bývalých žáků.",
        1997,
    ),
    FamilyNovakFact(
        "f079",
        "detaily",
        "corpus_only",
        "Nepracovala nikdy v Praze; celý profesní život prožila v Brně a okolí.",
        1995,
    ),
    FamilyNovakFact(
        "f080",
        "detaily",
        "memory",
        "Poslední knihu, kterou dočetla, byl román o moravské vesnici od spisovatelky z Uherského Hradiště.",
        2020,
        "Posledni kniha",
    ),
    FamilyNovakFact(
        "f081",
        "detaily",
        "corpus_only",
        "Nepoužívala internet; dopisy psala rukou modrým inkoustem na linkovaném papíře.",
        2014,
    ),
    FamilyNovakFact(
        "f082",
        "detaily",
        "corpus_only",
        "Nikdy neletěla letadlem; na dovolené jezdila autobusem nebo vlakem s Pavlem.",
        1993,
    ),
    FamilyNovakFact(
        "f083",
        "detaily",
        "corpus_only",
        "Nemluvila plynně rusky; ve škole měla jen základy a pamatovala si pár frází z učebnice.",
        1965,
    ),
    FamilyNovakFact(
        "f084",
        "detaily",
        "corpus_only",
        "Nevlastnila automobil; na cesty v okolí Brna jezdila s Pavlem nebo MHD.",
        1989,
    ),
    FamilyNovakFact(
        "f085",
        "detaily",
        "corpus_only",
        "Pavel nikdy nebyl ve Vietnamu ani v jiné zahraniční vojenské misi; sloužil jen u telegrafie doma.",
        1969,
    ),
    FamilyNovakFact(
        "f086",
        "detaily",
        "corpus_only",
        "Eva neměla bratra ani sestru; v rodinném archivu není žádný záznam o sourozenci.",
        1952,
    ),
    FamilyNovakFact(
        "f087",
        "detaily",
        "corpus_only",
        "První pes v rodině se jmenoval až Mourek, kočka přišla s Martinem, nikdy neměli psa jménem Azor.",
        1984,
    ),
    FamilyNovakFact(
        "f088",
        "detaily",
        "corpus_only",
        "V roce 1968 nebyla v Paříži; celý rok strávila studiem v Brně a praxí na Moravě.",
        1968,
    ),
    FamilyNovakFact(
        "f089",
        "detaily",
        "corpus_only",
        "Nepamatovala se na setkání s žádným slavným hercem; největší radost jí dělala místní divadelní společnost.",
        1976,
    ),
    FamilyNovakFact(
        "f090",
        "detaily",
        "corpus_only",
        "Nikdy neplavala v moři u Itálie; nejdelší koupání bylo u Balatonu v roce 1992.",
        1992,
    ),
    FamilyNovakFact(
        "f091",
        "detstvi",
        "corpus_only",
        "Jednou v zimě ji prarodiče poslali pro svařené víno k sousedovi Horákovi, "
        "který bydlel za kopcem v domě s modrými okenicemi a vrzajícími schody.",
        1956,
    ),
    FamilyNovakFact(
        "f092",
        "studium",
        "corpus_only",
        "Na koleje chodila s kamarádkou Danou, která později učila dějepis v Hodoníně "
        "a posílala jí pohlednice s motivem hradu Buchlov.",
        1969,
    ),
    FamilyNovakFact(
        "f093",
        "pavel",
        "corpus_only",
        "Pavel jí poprvé napsal pohled z víkendového výletu do Lednice, kde kreslil "
        "minaret z paměti na zadní straně pohlednice.",
        1970,
    ),
    FamilyNovakFact(
        "f094",
        "rodina",
        "corpus_only",
        "Tereza jako holka sbírala nálepky s květinami a lepila je do sešitu, "
        "který Eva schovávala v šuplíku u modrého ubrusu.",
        1978,
    ),
    FamilyNovakFact(
        "f095",
        "ucitelstvi",
        "corpus_only",
        "Jeden bývalý žák jí po letech poslal dopis z Kanady, kde pracoval jako "
        "technik u dřevozpracující firmy a vzpomínal na hodinu o Nerudovi.",
        2003,
    ),
    FamilyNovakFact(
        "f096",
        "konicky",
        "corpus_only",
        "Na půdě v Řečkovicích skladovala prázdné sklenice od džemu, do kterých "
        "ukládala sušené jablka na zimu pro čaj.",
        1997,
    ),
    FamilyNovakFact(
        "f097",
        "cesty",
        "corpus_only",
        "Jeden podzim jela s učitelkami na exkurzi do Valtic, kde ochutnala "
        "modrý Portugal a zapsala si do notesu vůni kouře z vinohradu.",
        1987,
    ),
    FamilyNovakFact(
        "f098",
        "domov",
        "corpus_only",
        "V kuchyni visel magnet s motivem Mikulova, který jim věnovala kolegyně "
        "po prvním školním srazu v novém domě.",
        1984,
    ),
    FamilyNovakFact(
        "f099",
        "ritualy",
        "corpus_only",
        "Každý první jarní den otevřela okno v ložnici a nechala v místnosti "
        "proběhnout studený vítr, aby prý přišel do domu klid.",
        2009,
    ),
    FamilyNovakFact(
        "f100",
        "zdravi",
        "corpus_only",
        "Lékař jí jednou doporučil chůzi k rybníku v Řečkovicích, kde pozorovala "
        "kachny a zapisovala si do notesu délku trasy.",
        2016,
    ),
    FamilyNovakFact(
        "f101",
        "zaver",
        "corpus_only",
        "Před smrtí požádala Terezu, aby po pohřbu rozdala sousedům řečkovické "
        "sušené jablka v papírových sáčcích s modrou stužkou.",
        2020,
    ),
    FamilyNovakFact(
        "f102",
        "osobnost",
        "corpus_only",
        "Kolegyně ji popisovaly jako člověka, který umí mlčet dlouho, ale když "
        "promluví, každé slovo má váhu.",
        1988,
    ),
    FamilyNovakFact(
        "f103",
        "rodina_dalsi",
        "corpus_only",
        "Klára po střední škole studovala grafický design v Brně a Eva jí jednou "
        "poslala balíček starých pohlednic jako inspiraci.",
        2021,
    ),
    FamilyNovakFact(
        "f104",
        "detaily",
        "corpus_only",
        "Nikdy nesbírala poštovní známky; jediné, co podobného dělala, bylo "
        "ukládání pohlednic od žáků do krabice od bot.",
        1991,
    ),
    FamilyNovakFact(
        "f105",
        "detaily",
        "corpus_only",
        "Nepamatovala si barvu prvního auta, které vlastnila rodina, protože "
        "Pavel vozil vozidlo z družstva a barvu neměnili.",
        1980,
    ),
    FamilyNovakFact(
        "f106",
        "detstvi",
        "corpus_only",
        "V sedmi letech napsala do školního časopisu krátký fejeton o podzimním "
        "listí, který učitelka přečetla nahlas a uložila do školního archivu.",
        1955,
    ),
    FamilyNovakFact(
        "f107",
        "studium",
        "corpus_only",
        "Během prázdnin v roce 1970 pracovala jako dobrovolnice v knihovně "
        "v Břeclavi a skládala výpůjční knihy podle abecedy do dřevěných polic.",
        1970,
    ),
    FamilyNovakFact(
        "f108",
        "rodina",
        "corpus_only",
        "Martin jako teenager opravoval sousedovi kolo a Eva mu půjčila klíč "
        "od garáže, kde měli viset staré lano na sušení prádla.",
        1992,
    ),
    FamilyNovakFact(
        "f109",
        "ucitelstvi",
        "corpus_only",
        "Na školním dni v roce 1983 připravila scénku z povídky Boženy Němcové "
        "a žáci přinesli rekvisity v modrém plátěném pytli.",
        1983,
    ),
    FamilyNovakFact(
        "f110",
        "cesty",
        "corpus_only",
        "Na jaře 2005 jela autobusem do Olomouce na výstavu knižní vazby "
        "a vrátila se s notesem plným nákresů obálek.",
        2005,
    ),
    FamilyNovakFact(
        "f111",
        "domov",
        "corpus_only",
        "V ložnici měla skříňku se šedým plastem na deky, kde schovávala "
        "dopisy od bývalých žáků seřazené podle ročníku.",
        1999,
    ),
    FamilyNovakFact(
        "f112",
        "ritualy",
        "corpus_only",
        "Každý podzim pekla s Terezou džem z posledních jablek a psala "
        "na sklenici datum a počet lžic cukru modrým fixem.",
        2007,
    ),
    FamilyNovakFact(
        "f113",
        "zdravi",
        "corpus_only",
        "Fyzioterapeut jí ukázal cvik s gumovým pásem, který visel na "
        "zadních dveřích ložnice vedle pláště do deště.",
        2018,
    ),
    FamilyNovakFact(
        "f114",
        "osobnost",
        "corpus_only",
        "Žáci si pamatovali, že při písemce nechávala okénko otevřené "
        "a venku slyšet šumění stromů z dvorku školy.",
        1985,
    ),
    FamilyNovakFact(
        "f115",
        "rodina_dalsi",
        "corpus_only",
        "Tereza jí jednou přivezla nový deka z fleece a Eva ji složila "
        "do koše u kachlových kamen na chladné večery.",
        2019,
    ),
    FamilyNovakFact(
        "f116",
        "konicky",
        "corpus_only",
        "Na jaře 2004 si pořídila tenké pracovní rukavice na zahradu "
        "a ukládala je do plechové krabice od čaje vedle nože.",
        2004,
    ),
    FamilyNovakFact(
        "f117",
        "pavel",
        "corpus_only",
        "Pavel jí na narozeniny jednou vyrobil dřevěnou poličku na knihy "
        "a natřel ji zeleným lazurovým nátěrem z obchodu v Kuřimi.",
        1996,
    ),
    FamilyNovakFact(
        "f118",
        "detaily",
        "corpus_only",
        "Nikdy nehrála šachy v turnaji; nejvíc strategie znala z křížovek "
        "v novinách, které dělávala v kuchyni u ranní kávy.",
        2000,
    ),
    FamilyNovakFact(
        "f119",
        "detstvi",
        "corpus_only",
        "Jednou na jaře našla pod švestkovým stromem hnízdo s modrými "
        "vejci a celé odpoledne na ně dohlížela, aby je nesahal sousedův pes.",
        1957,
    ),
    FamilyNovakFact(
        "f120",
        "zaver",
        "corpus_only",
        "V posledním týdnu požádala Martina, aby jí přečetl úryvek z "
        "moravské balady, kterou kdysi dávala do maturitního semináře.",
        2020,
    ),
    FamilyNovakFact(
        "f121",
        "detaily",
        "corpus_only",
        "Nepamatovala si přesný počet knih ve své knihovně, ale věděla, "
        "že nejstarší svazek je antologie moravských pověstí z roku 1951.",
        2015,
    ),
    FamilyNovakFact(
        "f122",
        "studium",
        "corpus_only",
        "Na konci studia jí vedoucí práce napsal do posudku, že má "
        "výborný cit pro práci s textem a trpělivost k žákům.",
        1972,
    ),
    FamilyNovakFact(
        "f123",
        "detaily",
        "corpus_only",
        "Tento fiktivní životopis končí poznámkou, že každá věta v celém "
        "korpusu slouží jen pro testování avataru a nesmí být považována "
        "za skutečnou biografii; přesto má mít rozsah odpovídající několika "
        "stranám textu, aby evaluace odpovídala reálnému klientovskému "
        "nahrání rozsáhlého rodinného archivu, dopisů, fotografií a "
        "záznamů z rozhovorů s příbuznými.",
        2020,
    ),
    FamilyNovakFact(
        "f124",
        "konicky",
        "corpus_only",
        "Na podzim 2013 sbírala po procházce kolem rybníka spadané kaštany v Řečkovicích do papírového sáčku "
        "a dávala je vnučce Kláře na modrý porcelánový talíř jako dekoraci vedle sklenice vody "
        "s citronem, meduňkou a vonné svíčky, což dělala jen jednou a nikdy to neopakovala jiným rokem.",
        2013,
    ),
)


SECTION_ORDER: tuple[str, ...] = (
    "detstvi",
    "studium",
    "pavel",
    "rodina",
    "ucitelstvi",
    "konicky",
    "cesty",
    "domov",
    "ritualy",
    "zdravi",
    "zaver",
    "osobnost",
    "rodina_dalsi",
    "detaily",
)

SECTION_TITLES: dict[str, str] = {
    "detstvi": "Dětství u jižní Moravy",
    "studium": "Studium a mladá dospělost",
    "pavel": "Pavel a svatba",
    "rodina": "Děti a vnučka",
    "ucitelstvi": "Učitelka literatury",
    "konicky": "Kytara, zahrada a kuchyně",
    "cesty": "Cesty a výlety",
    "domov": "Dům v Řečkovicích",
    "ritualy": "Rodinné rituály",
    "zdravi": "Zdraví a poslední roky",
    "zaver": "Závěr života",
    "osobnost": "Osobnost a pověst",
    "rodina_dalsi": "Rodina dnes",
    "detaily": "Doplňující detaily",
}

SECTION_NARRATIVES: dict[str, str] = {
    "detstvi": (
        "Tato kapitola shrnuje dětství Evy Novákové v prostředí, kde se prolínaly "
        "vinařské stezky, vůně kvasícího moštu a zvyk, že se večer mluví potichu u "
        "otevřeného okna. Vyprávění není chronologickým deníkem, ale skládankou "
        "drobných událostí, které rodina po letech skládala do jednoho obrazu. Každá "
        "vzpomínka stojí sama o sobě a nesmí se opakovat v jiné kapitole tohoto "
        "fiktivního životopisu určeného pouze pro testování paměťového avatara."
    ),
    "studium": (
        "Studijní léta představují období, kdy Eva poprvé cítila, že kniha může "
        "nést stejnou váhu jako slib daný druhému člověku. Univerzitní chodby, "
        "cvičení na praxi a večerní cvičení hudební výchovy tvoří rámec, do něhož "
        "spadají následující události. Text záměrně neopakuje formulace z jiných "
        "oddílů a slouží jako jedinečný zdroj pro ověření přesné grounded odpovědi "
        "chatbota bez halucinací mimo uložený obsah."
    ),
    "pavel": (
        "Kapitola o Pavlovi popisuje setkání dvou lidí, kteří si nerozuměli hned "
        "slovem, ale spíš tím, jak každý z nich držel tužku, když psal poznámku. "
        "Svatba a první společné bydlení nejsou romantizované do pohádky; jsou "
        "zapsané jako konkrétní okamžiky, které lze později citovat s přesným "
        "odkazem na paměť nebo archivní záznam. Žádná věta z této kapitoly se "
        "neobjevuje jinde v celém korpus."
    ),
    "rodina": (
        "Rodinný život Evy je vyprávěn skrze narození dětí, první kroky vnučky a "
        "drobné každodenní situace, které dávají avataru možnost odpovídat v první "
        "osobě i v perspektivě příbuzného, který se ptá na babiččin život. Následující "
        "odstavce jsou psané tak, aby každý obsahoval jedinečnou informaci, kterou "
        "evaluátor může spolehlivě dohledat a ověřit bez duplicitního překryvu."
    ),
    "ucitelstvi": (
        "Profesní dráha učitelky literatury je pro tento fiktivní profil klíčová, "
        "protože právě z ní vychází nejvíc otázek, na které by se klienti ptali. "
        "Následující záznamy popisují školní kroniky, hodiny u kamen, maturitní "
        "semináře a odchod do důchodu jako samostatné body. Text je psán česky a "
        "záměrně bohatý, aby odpovídal rozsahu několika stran životopisu."
    ),
    "konicky": (
        "Koníčky a domácí rituály doplňují profesní život o lidskou stránku, která "
        "se v rozhovoru často ukáže dřív než suchá fakta o škole. Kytara, pečení "
        "koláčů a práce se sušenými bylinkami jsou zde popsány odděleně od cest a "
        "rodinných událostí, aby chatbot nedostal dvě různé odpovědi na stejnou otázku "
        "z různých míst korpusu."
    ),
    "cesty": (
        "Cestování v tomto profilu neznamená hon za exotikou, ale spíš pečlivě "
        "naplánované výlety, které Eva zvládla s omezeným rozpočtem a bez letadel. "
        "Následující odstavce popisují jednotlivé cesty tak, aby bylo možné otestovat, "
        "zda avatar správně rozliší místa, která navštívila, od míst, která v tomto "
        "fiktivním životě vůbec neexistují."
    ),
    "domov": (
        "Dům v Řečkovicích je v tomto datasetu symbolem stability, ale každý detail "
        "o něm je uveden jen jednou. Stavební plány, zimní kamna a pergola mají své "
        "vlastní věty, které se nesmí opakovat v jiných kapitolách. Tento úvod slouží "
        "jako most mezi cestami a rodinnými rituály a neobsahuje konkrétní data, "
        "která by kolidovala s následujícími fakty."
    ),
    "ritualy": (
        "Rodinné rituály jsou v datasetu záměrně popsané jako opakující se chování, "
        "nikoli jako opakující se text. Každá věta níže popisuje jiný zvyk, jiný rok "
        "nebo jinou osobu, která se rituálu účastnila. Cílem je ověřit, že avatar "
        "umí odpovědět přesně na otázku o nedělním telefonátu, aniž by si vymyslel "
        "jiný zvyk, který v korpusu není."
    ),
    "zdravi": (
        "Zdravotní kapitola je citlivá, ale pro evaluaci důležitá: avatar musí umět "
        "mluvit o diagnózách a hospitalizacích jen podle důkazů a jinak odpovědět "
        "lidsky, že takovou zkušenost nemá. Následující odstavce jsou psané věcně, "
        "bez dramatizace, a každý obsahuje jiný lékařský nebo osobní detail, který "
        "se v jiné části korpusu nevyskytuje."
    ),
    "zaver": (
        "Závěr života je v tomto fiktivním datasetu popsán klidně a bez patosu, aby "
        "bylo možné testovat, zda avatar dokáže citovat poslední dny, pohřeb a reakce "
        "rodiny, aniž by přidal informace z jiných kapitol. Každá věta je originální "
        "a slouží jako samostatný fakt pro evaluaci grounded odpovědi."
    ),
    "osobnost": (
        "Osobnost Evy je v korpus zapsána skrze konkrétní chování, ne abstraktní "
        "přídavná jména. Následující věty popisují, jak ji vnímali kolegové, žáci a "
        "rodina, vždy jiným úhlem. Tento přístup umožňuje později ladit styl "
        "vyprávění avatara, zatímco nyní testujeme především faktickou správnost."
    ),
    "rodina_dalsi": (
        "Kapitola o dnešní rodině doplňuje pohled na Terezu, Martina a Kláru tak, "
        "aby se dalo otestovat, zda avatar rozliší mezi vlastním životem Evy a životem "
        "příbuzných. Každý následující fakt je unikátní a nesmí se objevit v jiné "
        "podobě jinde v celém čtyřstránkovém korpusu tohoto testovacího profilu."
    ),
    "detaily": (
        "Závěrečný oddíl shromažďuje drobné detaily, které se nevešly do předchozích "
        "kapitol, a zároveň obsahuje explicitní negace pro lack-of-evidence testy. "
        "Právě zde je zapsáno, co Eva nikdy neudělala, kam nejela a co v rodině "
        "neexistovalo, aby chatbot uměl odpovědět přirozeně, že o tom neví."
    ),
}
