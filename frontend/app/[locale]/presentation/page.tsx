import { notFound } from "next/navigation";

import PresentationPage from "../../../components/presentation-page";
import { parseAppLocale } from "../../../lib/i18n/locales";

export default function PresentationRoute({ params }: { params: { locale: string } }) {
  const locale = parseAppLocale(params.locale);
  if (locale === null) {
    notFound();
  }
  return <PresentationPage locale={locale} />;
}
