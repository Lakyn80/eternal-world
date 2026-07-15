import V2ExperiencePage from "../../components/v2-experience/v2-experience-page";
import V2PageFrame from "../../components/v2-experience/v2-page-frame";
import { parseAppLocale } from "../../lib/i18n/locales";
import { notFound } from "next/navigation";

export default function HomePage({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  return (
    <V2PageFrame>
      <V2ExperiencePage locale={locale} />
    </V2PageFrame>
  );
}
