import MarketingHome from "../../components/marketing-home";
import { parseAppLocale } from "../../lib/i18n/locales";
import { notFound } from "next/navigation";

export default function HomePage({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  return <MarketingHome locale={locale} />;
}
