import { useEffect } from 'react';
import { navigate, type CzechLegalPage as LegalPageKind } from '../lib/router';
import CzechLegalFooter from './CzechLegalFooter';

const todoClass = 'mt-4 rounded-md border border-amber-300/35 bg-amber-200/10 p-4 text-sm leading-6 text-amber-50/90';
const sectionClass = 'border-t border-white/10 py-8';
const tableClass = 'mt-4 w-full min-w-[760px] border-collapse text-left text-sm leading-6';

function OperatorTodo() {
  return (
    <div className={todoClass} role="note">
      <strong>Údaj musí provozovatel doplnit před zveřejněním:</strong> právní jméno nebo název správce, IČO
      (je-li přiděleno), sídlo či adresa a funkční kontakt pro žádosti o ochranu osobních údajů. Projekt tyto
      údaje neobsahuje, proto zde nejsou domyšlené.
    </div>
  );
}

function PrivacyContent() {
  return (
    <>
      <section className="pb-8">
        <p className="text-sm text-cyan">Účinnost od 22. září 2026</p>
        <h1 className="mt-3 font-serif text-4xl leading-tight sm:text-5xl">Zásady ochrany osobních údajů</h1>
        <p className="mt-5 max-w-[72ch] leading-7 text-fg/70">
          Tyto zásady vysvětlují, jak Eternal World zpracovává osobní údaje při provozu webu, uživatelského
          účtu, rodinných památníků, biografického asistenta a konverzace s digitálním avatarem.
        </p>
        <OperatorTodo />
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">1. Jaké údaje služba zpracovává</h2>
        <ul className="mt-4 grid gap-3 leading-7 text-fg/70">
          <li>Účet a přístup: jméno, e-mail, bezpečně odvozený otisk hesla, jazykové nastavení a údaje relace.</li>
          <li>Obsah památníku: jména, životopisné texty, vzpomínky, příspěvky, fotografie, zvuk, video a jejich popisy.</li>
          <li>Komunikace se službou: dotazy v chatu, odpovědi biografickému asistentovi, návrhy vzpomínek a historie schvalování.</li>
          <li>Odvozená technická data: číselné reprezentace textu pro vyhledávání, stav indexace a metadata potřebná k provozu.</li>
          <li>Provozní a bezpečnostní údaje: čas požadavku, cesta, identifikátor požadavku, stav operace a související diagnostika.</li>
        </ul>
        <p className="mt-4 text-sm leading-6 text-fg/55">
          Obsah může podle rozhodnutí uživatele zahrnovat citlivé rodinné informace. Uživatel má vkládat jen data,
          která je oprávněn zpřístupnit. Fotografie nebo hlas nejsou v této službě deklarovány jako biometrická
          identifikace; případné budoucí použití k jedinečné identifikaci by vyžadovalo nové posouzení a informace.
        </p>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">2. Účely a právní základy</h2>
        <div className="mt-4 overflow-x-auto">
          <table className={tableClass}>
            <thead><tr className="border-b border-white/15 text-fg"><th className="p-3">Účel</th><th className="p-3">Typický právní základ</th><th className="p-3">Rozsah</th></tr></thead>
            <tbody className="text-fg/65">
              <tr className="border-b border-white/10"><td className="p-3">Zřízení účtu a poskytování funkcí služby</td><td className="p-3">Plnění smlouvy nebo kroky před jejím uzavřením</td><td className="p-3">Účet, památníky, obsah a komunikace vyžádaná uživatelem</td></tr>
              <tr className="border-b border-white/10"><td className="p-3">Zabezpečení, prevence zneužití a diagnostika</td><td className="p-3">Oprávněný zájem na bezpečném a spolehlivém provozu</td><td className="p-3">Relace, omezené provozní logy a chybové údaje</td></tr>
              <tr><td className="p-3">Volitelné funkční uložení v prohlížeči</td><td className="p-3">Předchozí souhlas uživatele zařízení</td><td className="p-3">Jazyk, rozepsané texty a veřejná PWA cache</td></tr>
            </tbody>
          </table>
        </div>
        <div className={todoClass}>
          Provozovatel musí před zveřejněním potvrdit právní základy pro svůj konkrétní obchodní model, pravidla pro
          údaje zemřelých a případné zpracování zvláštních kategorií osobních údajů obsažených v uživatelském obsahu.
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">3. Umělá inteligence a vyhledávání ve vzpomínkách</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Vybrané dotazy a relevantní části schváleného obsahu mohou být odeslány nakonfigurovanému poskytovateli
          jazykového modelu, aby vytvořil odpověď, otázku nebo překlad. Pro sémantické vyhledávání služba vytváří
          číselné reprezentace textu a ukládá je do vyhledávací databáze. Aplikace podle aktuální implementace
          nepoužívá tyto funkce k rozhodování s právními nebo obdobně významnými účinky.
        </p>
        <div className={todoClass}>
          Provozovatel musí doplnit právní název každého produkčního AI a překladového poskytovatele, účel a rozsah
          předávaných dat, místo zpracování, dobu uchování a případné záruky předání mimo EHP. Konfigurace podporuje
          různé poskytovatele, takže přesný příjemce nelze pravdivě určit jen z veřejného rozhraní.
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">4. Komu mohou být údaje zpřístupněny</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Údaje mohou být zpřístupněny členům konkrétního památníku podle přidělené role, poskytovatelům hostingu,
          databází a doručování webu, nakonfigurovaným AI a překladovým službám a osobám zajišťujícím nezbytnou
          technickou podporu. Přístup má být omezen na nezbytný rozsah.
        </p>
        <div className={todoClass}>
          Před zveřejněním doplňte úplný seznam skutečných zpracovatelů a dalších příjemců včetně Cloudflare, hostingu
          a AI služeb, pokud jsou v produkci aktivní. U každého uveďte právní název, zemi a roli. Doplňte také, zda
          dochází k předání mimo EHP a jaké záruky se používají.
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">5. Doba uchování</h2>
        <ul className="mt-4 grid gap-3 leading-7 text-fg/70">
          <li>Přihlašovací cookie trvá do ukončení relace prohlížeče; serverová relace může při aktivitě trvat nejvýše 14 dní od posledního obnovení.</li>
          <li>Rozepsané texty jsou uloženy jen v dané relaci prohlížeče a po odvolání funkčního souhlasu se odstraní.</li>
          <li>Záznam přijetí funkčního ukládání platí nejvýše 12 měsíců, záznam odmítnutí nejvýše 6 měsíců.</li>
          <li>Účet, památníky, média, konverzace, odvozené indexy, zálohy a provozní logy se řídí retenčním plánem provozovatele.</li>
        </ul>
        <div className={todoClass}>
          Retenční plán pro účet, obsah, média, historii chatu, AI vstupy a výstupy, logy, databázové zálohy a požadavky
          na výmaz není v projektu úplně definován. Provozovatel musí před zveřejněním doplnit konkrétní lhůty a proces výmazu.
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">6. Vaše práva</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Za podmínek GDPR můžete požadovat přístup, opravu, výmaz, omezení zpracování a přenositelnost údajů, vznést
          námitku proti zpracování založenému na oprávněném zájmu a kdykoli odvolat souhlas do budoucna. Souhlas s
          funkčním ukládáním změníte přes odkaz „Nastavení cookies“ v patičce.
        </p>
        <p className="mt-4 leading-7 text-fg/70">
          Žádost odešlete na <strong>[DOPLNIT KONTAKT PRO OCHRANU OSOBNÍCH ÚDAJŮ]</strong>. Máte také právo podat
          stížnost u <a href="https://uoou.gov.cz" rel="noopener noreferrer" target="_blank">Úřadu pro ochranu osobních údajů</a>.
        </p>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">7. Zabezpečení a změny zásad</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Implementace používá šifrovaný přenos, hesla ukládá ve formě bezpečného otisku, přihlašovací cookie chrání
          před čtením JavaScriptem a přístup k památníkům řídí rolemi. Žádné opatření však nemůže zaručit absolutní
          bezpečnost. Při významné změně účelů nebo technologií musí být zásady aktualizovány a tam, kde je to nutné,
          bude vyžádán nový souhlas.
        </p>
      </section>
    </>
  );
}

function CookiesContent() {
  return (
    <>
      <section className="pb-8">
        <p className="text-sm text-cyan">Účinnost od 22. září 2026</p>
        <h1 className="mt-3 font-serif text-4xl leading-tight sm:text-5xl">Cookies a podobná úložiště</h1>
        <p className="mt-5 max-w-[72ch] leading-7 text-fg/70">
          Tento přehled vychází z aktuální implementace Eternal World. Pojem „cookies“ zde zahrnuje také
          <code className="mx-1 text-fg/85">localStorage</code>, <code className="mx-1 text-fg/85">sessionStorage</code>
          a Cache Storage, protože i podobné technologie ukládají informace do zařízení.
        </p>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">Nezbytné</h2>
        <p className="mt-3 leading-7 text-fg/65">Tyto položky zajišťují přihlášení a uchování vaší volby. Nelze je vypnout v nastavení služby.</p>
        <div className="mt-4 overflow-x-auto">
          <table className={tableClass}>
            <thead><tr className="border-b border-white/15"><th className="p-3">Identifikátor</th><th className="p-3">Účel a obsah</th><th className="p-3">Poskytovatel</th><th className="p-3">Doba</th></tr></thead>
            <tbody className="text-fg/65">
              <tr className="border-b border-white/10"><td className="p-3 font-mono text-xs">eternal_world_session</td><td className="p-3">Náhodný identifikátor přihlášené relace; cookie je HttpOnly, SameSite=Lax a v produkci Secure.</td><td className="p-3">Eternal World, první strana</td><td className="p-3">Do zavření relace prohlížeče; serverový záznam má posuvnou lhůtu 14 dní.</td></tr>
              <tr><td className="p-3 font-mono text-xs">eternal-world.cookie-consent</td><td className="p-3">Verze, čas, konec platnosti a povolené kategorie. Slouží k doložení a respektování volby.</td><td className="p-3">Eternal World, localStorage</td><td className="p-3">Přijetí nejvýše 12 měsíců; odmítnutí nejvýše 6 měsíců.</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">Funkční, pouze po souhlasu</h2>
        <p className="mt-3 leading-7 text-fg/65">Ve výchozím stavu jsou vypnuté. Odvolání souhlasu odstraní níže uvedená data z prohlížeče.</p>
        <div className="mt-4 overflow-x-auto">
          <table className={tableClass}>
            <thead><tr className="border-b border-white/15"><th className="p-3">Identifikátor</th><th className="p-3">Účel</th><th className="p-3">Poskytovatel</th><th className="p-3">Doba</th></tr></thead>
            <tbody className="text-fg/65">
              <tr className="border-b border-white/10"><td className="p-3 font-mono text-xs">eternal-world.ui.lang</td><td className="p-3">Zapamatování zvoleného jazyka rozhraní.</td><td className="p-3">Eternal World, localStorage</td><td className="p-3">Do změny, odvolání souhlasu nebo smazání dat prohlížeče.</td></tr>
              <tr className="border-b border-white/10"><td className="p-3 font-mono text-xs">eternal_world:chat_draft:*</td><td className="p-3">Rozepsaná, dosud neodeslaná zpráva pro konkrétní památník.</td><td className="p-3">Eternal World, sessionStorage</td><td className="p-3">Po dobu relace dané karty nebo do odeslání, vymazání či odvolání.</td></tr>
              <tr className="border-b border-white/10"><td className="p-3 font-mono text-xs">eternal_world:biographer_draft:*</td><td className="p-3">Rozepsaná odpověď ke konkrétní biografické otázce.</td><td className="p-3">Eternal World, sessionStorage</td><td className="p-3">Po dobu relace dané karty nebo do odeslání, vymazání či odvolání.</td></tr>
              <tr><td className="p-3 font-mono text-xs">eternal-world-shell-*</td><td className="p-3">Veřejné soubory aplikace pro instalaci a omezený offline režim; nikdy API odpovědi ani soukromý obsah.</td><td className="p-3">Eternal World, Service Worker / Cache Storage</td><td className="p-3">Do nové verze aplikace, odvolání souhlasu nebo smazání dat prohlížeče.</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">Co se nepoužívá</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Aktuální frontend neinicializuje Google Analytics, Google Tag Manager, Meta Pixel, reklamní cookies,
          behaviorální profilování ani fingerprinting. Proto zde nejsou zobrazeny prázdné analytické nebo marketingové kategorie.
        </p>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">Externí požadavky bez deklarovaného ukládání cookies</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Veřejná stránka načítá písma z domén Google Fonts. Prohlížeč při tom předává běžné síťové údaje, například
          IP adresu a informace v HTTP požadavku. V kódu aplikace toto načtení nenastavuje analytickou ani marketingovou
          cookie. Produkční doména může být doručována přes Cloudflare, jehož konkrétní bezpečnostní nastavení může
          ovlivnit další technické zpracování.
        </p>
        <div className={todoClass}>
          Provozovatel musí ověřit aktuální produkční konfiguraci Cloudflare a Google Fonts, doplnit právní názvy,
          země, právní základy a případné předávání mimo EHP. Pokud infrastruktura vkládá další identifikátor, musí být
          před spuštěním doplněn do tohoto přehledu a správně zařazen.
        </div>
      </section>

      <section className={sectionClass}>
        <h2 className="font-serif text-3xl">Jak volbu změnit</h2>
        <p className="mt-4 leading-7 text-fg/70">
          Odkaz „Nastavení cookies“ je dostupný v české patičce. Odmítnutí ponechá nezbytné položky aktivní, odstraní
          funkční položky a odregistruje veřejnou offline cache. Data můžete odstranit také v nastavení prohlížeče;
          potom se žádost o volbu zobrazí znovu.
        </p>
      </section>
    </>
  );
}

export default function CzechLegalPage({ kind }: { kind: LegalPageKind }) {
  useEffect(() => {
    const previousLang = document.documentElement.lang;
    const previousTitle = document.title;
    document.title = kind === 'privacy' ? 'Ochrana osobních údajů | Eternal World' : 'Cookies | Eternal World';
    document.documentElement.lang = 'cs';
    window.scrollTo({ top: 0 });
    return () => {
      document.title = previousTitle;
      document.documentElement.lang = previousLang;
    };
  }, [kind]);

  return (
    <div className="min-h-screen bg-ink text-fg font-sans">
      <header className="border-b border-white/10 px-5 py-4 sm:px-8">
        <div className="mx-auto flex max-w-[1100px] items-center justify-between gap-4">
          <button className="font-semibold text-fg" onClick={() => navigate('/')} type="button">Eternal World</button>
          <button className="text-sm text-fg/65 hover:text-fg" onClick={() => navigate('/')} type="button">Zpět na hlavní stránku</button>
        </div>
      </header>
      <main className="mx-auto max-w-[980px] px-5 py-12 sm:px-8 sm:py-16">
        {kind === 'privacy' ? <PrivacyContent /> : <CookiesContent />}
      </main>
      <CzechLegalFooter compact />
    </div>
  );
}
